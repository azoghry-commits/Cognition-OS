"""Verify and replay native evaluation evidence without network or model execution."""
import argparse
import hashlib
import json
import math
import re
import stat
import sys
import zipfile
from pathlib import Path, PurePosixPath

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from scripts import evaluate_context_host as host
from scripts.eval_integrity import read_json_bytes, review_fingerprints, has_bound_approval

MAX_FILE_BYTES = 8 * 1024 * 1024
MAX_TOTAL_BYTES = 64 * 1024 * 1024
MAX_ARCHIVE_BYTES = 16 * 1024 * 1024


def _safe_name(name):
    parts = name.split('/')
    if (not name or name.startswith('/') or '\\' in name or ':' in name
            or any(part in ('.', '..') for part in parts)):
        raise ValueError('Unsafe archive path: ' + name)
    return name


def _sha(raw):
    return hashlib.sha256(raw).hexdigest()


def _frozen_member(path, prefix):
    normalized = path.replace('\\', '/')
    for name in ('cases.json', 'labels.provisional.json', 'human-review.json'):
        if normalized.endswith('/' + name):
            return prefix + 'suite-frozen/' + name
    if normalized.endswith('/scripts/evaluate_context_host.py'):
        return prefix + 'runner-frozen.py'
    if normalized.endswith('/docs/CONTEXT_VALIDITY.md'):
        return 'protocol/CONTEXT_VALIDITY.md'
    for directory in ('cognition', 'scripts', 'skills'):
        marker = '/' + directory + '/'
        if marker in normalized:
            return 'runtime/' + directory + '/' + normalized.rsplit(marker, 1)[1]
    raise ValueError('Unsupported frozen source path: ' + path)


def audit_archive(path, expected_sha256, cohort):
    path = Path(path)
    if path.stat().st_size > MAX_ARCHIVE_BYTES:
        raise ValueError('Archive size limit exceeded')
    if not re.fullmatch(r'[0-9a-f]{64}', expected_sha256) or _sha(path.read_bytes()) != expected_sha256:
        raise ValueError('Archive checksum does not match the trusted summary')
    if not cohort or '/' in cohort or '\\' in cohort:
        raise ValueError('Select one explicit cohort name')
    prefix = _safe_name(cohort) + '/'
    with zipfile.ZipFile(path) as archive:
        infos = archive.infolist()
        if len(infos) > 2000 or sum(row.file_size for row in infos) > MAX_TOTAL_BYTES:
            raise ValueError('Archive entry count or expanded size limit exceeded')
        names = set()
        for row in infos:
            _safe_name(row.filename)
            if row.filename in names:
                raise ValueError('Duplicate archive entry')
            names.add(row.filename)
            if row.file_size > MAX_FILE_BYTES or stat.S_ISLNK(row.external_attr >> 16):
                raise ValueError('Archive member size limit exceeded or linked member')
        if archive.testzip() is not None:
            raise ValueError('Archive CRC validation failed')

        def raw(name):
            if name not in names:
                raise ValueError('Missing archived evidence: ' + name)
            return archive.read(name)

        def document(name):
            return read_json_bytes(raw(name))

        manifest = document(prefix + 'frozen-manifest.json')
        frozen = manifest['files']
        frozen_names = set()
        for item in frozen:
            member = _frozen_member(item['path'], prefix)
            if member in frozen_names or _sha(raw(member)) != item['sha256']:
                raise ValueError('Frozen input mismatch or duplicate: ' + member)
            frozen_names.add(member)
        required = {prefix + 'suite-frozen/' + name for name in
                    ('cases.json', 'labels.provisional.json', 'human-review.json')}
        required |= {prefix + 'runner-frozen.py', 'runtime/cognition/validity.py'}
        if not required <= frozen_names:
            raise ValueError('Frozen manifest does not bind required audit inputs')
        # Never import/execute archived Python. Replay helper evidence only with a
        # local checker matching the frozen source, tolerating platform newlines.
        checker = raw('runtime/cognition/validity.py').replace(b'\r\n', b'\n')
        if checker != (ROOT / 'cognition/validity.py').read_bytes().replace(b'\r\n', b'\n'):
            raise ValueError('Local validity checker differs from archived source')

        cases_document = document(prefix + 'suite-frozen/cases.json')
        labels_document = document(prefix + 'suite-frozen/labels.provisional.json')
        review = document(prefix + 'suite-frozen/human-review.json')
        cases, labels = cases_document['cases'], labels_document['labels']
        host.validate_suite(cases, labels)
        expected = {row['case_id']: row['input'] for row in cases}
        runs = document(prefix + 'collected-runs.json')
        if set(runs) != {'baseline', 'candidate'}:
            raise ValueError('Expected baseline and candidate run groups')
        for arm, records in runs.items():
            identifiers = [row['case_id'] for row in records]
            if len(set(identifiers)) != len(identifiers) or set(identifiers) != set(expected):
                raise ValueError('Runs must be unique and complete for every case')
            for run in records:
                folder = prefix + _safe_name(run['case_id'] + '-' + arm) + '/'
                if run != document(folder + 'run.json') or run.get('arm') != arm:
                    raise ValueError('Collected run differs from original run record')
                payload_bytes = raw(folder + 'input.json')
                payload = read_json_bytes(payload_bytes)
                if not host._same_json(payload, expected[run['case_id']]) or _sha(payload_bytes) != run['input_sha256']:
                    raise ValueError('Run input differs from frozen case or recorded hash')
                response = document(folder + 'response.json')
                if not host._same_json(response, run['response']):
                    raise ValueError('Response differs from collected record')
                events = raw(folder + 'events.jsonl').decode('utf-8-sig')
                for line in events.splitlines():
                    if line.strip() and not isinstance(read_json_bytes(line.encode('utf-8')), dict):
                        raise ValueError('Expected JSON event objects')
                trace = host.parse_trace(events, evaluation_input=payload)
                for key in ('commands', 'usage', 'completed', 'errors', 'thread_id'):
                    if not host._same_json(trace[key], run[key]):
                        raise ValueError('Trace differs from collected run: ' + key)
                if type(run['returncode']) is not int or run['returncode'] != 0 or not trace['completed'] or trace['errors']:
                    raise ValueError('Execution is incomplete or failed')
                flags = ('critical_error', 'fixture_modified', 'prohibited_command_attempt')
                prohibited = any(any(token in item.get('command', '').casefold()
                                     for token in ('remove-item', 'rm -', 'unlink(', 'del input.json'))
                                 for item in trace['commands'])
                if (any(type(run.get(key)) is not bool for key in flags)
                        or run['prohibited_command_attempt'] != prohibited
                        or run['critical_error'] != (run['fixture_modified'] or prohibited)):
                    raise ValueError('Recorded critical-error flags disagree with evidence')
                seconds = run['seconds']
                if type(seconds) not in (int, float) or not math.isfinite(seconds) or seconds <= 0:
                    raise ValueError('Invalid recorded latency')
                usage = trace['usage']
                if (not isinstance(usage, dict) or any(type(usage.get(key)) is not int or usage[key] < 0
                        for key in ('input_tokens', 'cached_input_tokens', 'output_tokens'))
                        or usage['cached_input_tokens'] > usage['input_tokens']):
                    raise ValueError('Missing or invalid token evidence')
                run.update(trace, evaluation_input=payload)
                evidence = host.bound_run_evidence(run)
                if not evidence['workspace_read_observed'] or (arm == 'candidate' and not evidence['helper_executed']):
                    raise ValueError('Missing fixture-bound read/helper execution proof')

        bound = has_bound_approval(cases_document, labels_document, review)
        if 'hash_scheme' in review and not bound:
            raise ValueError('Approval fingerprints do not match the frozen suite')
        # Historical reports retain their original approval policy. An archived,
        # unbound certificate never authorizes future collection under the new gate.
        summary = host.summarize(runs['baseline'], runs['candidate'], labels,
                                 human_reviewed=review.get('approved') is True)
        if not host._same_json(summary, document(prefix + 'summary.json')):
            raise ValueError('Replayed summary differs from recorded results')
        return {'status': 'VERIFIED', 'archive_sha256': expected_sha256, 'cohort': cohort,
                'frozen_files_verified': len(frozen_names), 'summary_matches_recorded': True,
                'approval_binding': 'BOUND' if bound else 'LEGACY_UNBOUND',
                'new_collection_approved': bound, 'summary': summary,
                'auditor_sha256': _sha(Path(__file__).read_bytes()),
                'replay_sources_sha256': {name: _sha((ROOT / name).read_bytes()) for name in
                    ('scripts/audit_context_host.py', 'scripts/evaluate_context_host.py',
                     'scripts/eval_integrity.py', 'cognition/validity.py', 'cognition/capability.py')},
                'limitations': ['Integrity relative to the supplied trusted checksum; not signer authentication.',
                                'Replays structured rubric and observed tool traces, not reason-text semantics.',
                                'Historical fixture exposure and original evaluation limitations still apply.']}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest='command', required=True)
    fingerprints = commands.add_parser('fingerprints', help='Print hashes; never grant human approval')
    fingerprints.add_argument('--fixtures', type=Path, required=True)
    audit = commands.add_parser('audit', help='Verify an existing evidence bundle without inference')
    audit.add_argument('--summary', type=Path, required=True)
    audit.add_argument('--cohort', required=True)
    audit.add_argument('--output', type=Path)
    args = parser.parse_args()
    try:
        if args.command == 'fingerprints':
            cases = read_json_bytes((args.fixtures / 'cases.json').read_bytes())
            labels = read_json_bytes((args.fixtures / 'labels.provisional.json').read_bytes())
            result = review_fingerprints(cases, labels)
        else:
            if args.summary.stat().st_size > MAX_FILE_BYTES:
                raise ValueError('Summary size limit exceeded')
            published = read_json_bytes(args.summary.read_bytes())
            name = _safe_name(published['raw_evidence']['path'])
            if PurePosixPath(name).name != name:
                raise ValueError('Archive must be adjacent to its trusted summary')
            result = audit_archive(args.summary.parent / name, published['raw_evidence']['sha256'], args.cohort)
            for key, value in result['summary'].items():
                if key not in published or not host._same_json(value, published[key]):
                    raise ValueError('Published summary differs from replay: ' + key)
            if args.output:
                args.output.parent.mkdir(parents=True, exist_ok=True)
                with args.output.open('x', encoding='utf-8') as output:
                    output.write(json.dumps(result, indent=2, allow_nan=False) + '\n')
                result = {key: result[key] for key in ('status', 'cohort', 'summary_matches_recorded', 'approval_binding')}
        print(json.dumps(result, indent=2, allow_nan=False))
        return 0
    except (ValueError, KeyError, TypeError, OSError, zipfile.BadZipFile, UnicodeError,
            RecursionError, OverflowError) as error:
        print(json.dumps({'status': 'FAILED', 'error': str(error)}), file=sys.stderr)
        return 2


if __name__ == '__main__':
    raise SystemExit(main())
