import json
import tempfile
import unittest
from pathlib import Path

from scripts import eval_integrity
from scripts import prepare_context_review


def write_json(path, value):
    path.write_text(json.dumps(value), encoding='utf-8')


class ContextReviewTests(unittest.TestCase):
    def suite(self, root):
        cases = {'cases': []}
        labels = {'human_reviewed': False, 'labels': []}
        for index in range(20):
            case_id = f'HE-{index + 1:02d}'
            cases['cases'].append({'case_id': case_id, 'split': 'held_out',
                                   'input': {'record': {'title': case_id}, 'context': {}}})
            labels['labels'].append({'case_id': case_id, 'status': 'unknown',
                                     'reuse_allowed': False, 'review_required': True,
                                     'negative_control': index < 10})
        protocol = {'suite_status': 'UNCONSUMED', 'model': 'gpt-5.6-luna',
                    'reasoning_effort': 'low',
                    'thresholds': dict(prepare_context_review.ACCEPTANCE_THRESHOLDS)}
        for name, value in [('cases.json', cases), ('labels.provisional.json', labels),
                            ('protocol.json', protocol)]:
            write_json(root / name, value)
        return cases, labels, protocol

    def test_request_binds_cases_labels_and_protocol_without_approving(self):
        with tempfile.TemporaryDirectory() as folder:
            cases, labels, protocol = self.suite(Path(folder))
            request = prepare_context_review.prepare(folder)
        self.assertEqual(request['status'], 'PENDING_INDEPENDENT_REVIEW')
        self.assertFalse(request['approved'])
        self.assertEqual(request['counts'], {'cases': 20, 'negative_controls': 10})
        self.assertEqual({key: request[key] for key in ('hash_scheme', 'cases_sha256',
                                                        'labels_sha256', 'protocol_sha256')},
                         eval_integrity.review_fingerprints(cases, labels, protocol))

    def test_protocol_change_invalidates_bound_approval(self):
        with tempfile.TemporaryDirectory() as folder:
            cases, labels, protocol = self.suite(Path(folder))
            certificate = {'approved': True,
                           **eval_integrity.review_fingerprints(cases, labels, protocol)}
            self.assertTrue(eval_integrity.has_bound_approval(cases, labels, certificate, protocol))
            protocol['reasoning_effort'] = 'medium'
            self.assertFalse(eval_integrity.has_bound_approval(cases, labels, certificate, protocol))

    def test_rejects_consumed_suite_and_threshold_drift(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            self.suite(root)
            protocol = json.loads((root / 'protocol.json').read_text(encoding='utf-8'))
            protocol['suite_status'] = 'CONSUMED'
            write_json(root / 'protocol.json', protocol)
            with self.assertRaisesRegex(ValueError, 'UNCONSUMED'):
                prepare_context_review.prepare(root)
            protocol['suite_status'] = 'UNCONSUMED'
            protocol['thresholds']['minimum_precision'] = 0.5
            write_json(root / 'protocol.json', protocol)
            with self.assertRaisesRegex(ValueError, 'thresholds'):
                prepare_context_review.prepare(root)


if __name__ == '__main__':
    unittest.main()
