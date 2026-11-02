"""Prepare a content-bound review request for a fresh context-validity suite."""
import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from scripts.eval_integrity import read_json_bytes, review_fingerprints
from scripts.evaluate_context_host import (ACCEPTANCE_THRESHOLDS, validate_protocol,
                                           validate_suite, write_json)


def prepare(fixtures):
    fixtures = Path(fixtures)
    cases_document = read_json_bytes((fixtures / 'cases.json').read_bytes())
    labels_document = read_json_bytes((fixtures / 'labels.provisional.json').read_bytes())
    protocol_document = read_json_bytes((fixtures / 'protocol.json').read_bytes())
    cases = cases_document.get('cases')
    labels = labels_document.get('labels')
    if not isinstance(cases, list) or not isinstance(labels, list):
        raise ValueError('Expected cases and labels arrays')
    validate_suite(cases, labels)
    if len(cases) < ACCEPTANCE_THRESHOLDS['minimum_paired_cases']:
        raise ValueError('Fresh confirmation requires at least 20 paired cases')
    if any(case.get('split') != 'held_out' for case in cases):
        raise ValueError('Every confirmation case must use split=held_out')
    negative_controls = sum(label.get('negative_control') is True for label in labels)
    if negative_controls < ACCEPTANCE_THRESHOLDS['minimum_negative_controls']:
        raise ValueError('Fresh confirmation requires at least 10 negative controls')
    if labels_document.get('human_reviewed') is not False:
        raise ValueError('Provisional labels must declare human_reviewed=false')
    validate_protocol(protocol_document)
    fingerprints = review_fingerprints(cases_document, labels_document, protocol_document)
    return {
        'schema_version': '1.0',
        'status': 'PENDING_INDEPENDENT_REVIEW',
        'approved': False,
        **fingerprints,
        'counts': {'cases': len(cases), 'negative_controls': negative_controls},
        'review_scope': ['cases.json', 'labels.provisional.json', 'protocol.json'],
        'approval_instruction': (
            'After independent semantic review, copy these fingerprints into human-review.json '
            'with approved=true and reviewer evidence. Do not alter reviewed inputs afterward.'
        ),
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--fixtures', type=Path, required=True)
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    output = args.output or args.fixtures / 'review-request.json'
    request = prepare(args.fixtures)
    write_json(output, request)
    print(json.dumps(request, sort_keys=True))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
