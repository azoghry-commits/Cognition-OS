"""Behavioral expectations for read-only context validity checks."""
import copy
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from cognition import validity
from cognition.memory import CaseStore

NOW = '2026-10-23T12:00:00+00:00'


def record():
    return {'title': 'Single writer storage', 'classification': 'approved_knowledge',
            'applicability': {'schema_version': '1.0', 'scope': {'component': 'storage'},
                              'conditions': [{'id': 'writers', 'fact': 'writers', 'operator': 'equals',
                                              'expected': 1, 'max_age_seconds': 60}],
                              'evidence_refs': [{'id': 'architecture', 'fingerprint': 'a' * 64}]}}


def context():
    return {'scope': {'component': 'storage'},
            'facts': {'writers': {'value': 1, 'source': 'runtime inventory', 'observed_at': NOW}},
            'evidence': {'architecture': {'fingerprint': 'a' * 64, 'source': 'architecture.md',
                                          'observed_at': NOW}}}


class ValidityTests(unittest.TestCase):
    def test_all_required_conditions_must_match_without_mutating_input(self):
        saved, facts = record(), context()
        before = copy.deepcopy((saved, facts))
        result = validity.check_memory(saved, facts, now=NOW)
        self.assertEqual(result['status'], 'applicable')
        self.assertEqual((saved, facts), before)

    def test_missing_legacy_and_changed_evidence_have_distinct_results(self):
        self.assertEqual(validity.check_memory({'title': 'legacy'}, {}, now=NOW)['status'], 'unknown')
        for change, expected in [('missing', 'unknown'), ('changed', 'needs_review'),
                                 ('contradiction', 'contradicted'), ('scope', 'contradicted')]:
            facts = context()
            if change == 'missing':
                facts['facts'].clear()
            elif change == 'changed':
                facts['evidence']['architecture']['fingerprint'] = 'b' * 64
            elif change == 'scope':
                facts['scope']['component'] = 'frontend'
            else:
                facts['facts']['writers']['value'] = 2
                facts['evidence'].clear()
            with self.subTest(change=change):
                self.assertEqual(validity.check_memory(record(), facts, now=NOW)['status'], expected)

    def test_freshness_boundary_future_timestamp_and_wrong_type(self):
        for value, observed, expected in [(1, '2026-10-23T11:59:00Z', 'applicable'),
                                           (1, '2026-10-23T11:58:59Z', 'unknown'),
                                           (1, '2026-10-23T12:00:01Z', 'unknown'),
                                           (True, NOW, 'unknown'), ('1', NOW, 'unknown')]:
            facts = context()
            facts['facts']['writers'].update(value=value, observed_at=observed)
            with self.subTest(value=value, observed=observed):
                self.assertEqual(validity.check_memory(record(), facts, now=NOW)['status'], expected)

    def test_review_date_does_not_silently_invalidate_decision(self):
        saved = record()
        saved['applicability']['review_after'] = NOW
        result = validity.check_memory(saved, context(), now=NOW)
        self.assertEqual(result['status'], 'needs_review')
        self.assertTrue(any(item['reason'] == 'review_due' for item in result['checks']))

    def test_unrepresentable_observed_utc_dates_remain_unknown(self):
        for observed in ['0001-01-01T00:00:00+01:00', '9999-12-31T23:59:59-01:00']:
            facts = context()
            facts['facts']['writers']['observed_at'] = observed
            with self.subTest(observed=observed):
                self.assertEqual(validity.check_memory(record(), facts, now=NOW)['status'], 'unknown')

    def test_precedence_preserves_each_condition_result(self):
        saved = record()
        saved['applicability']['review_after'] = NOW
        facts = context()
        facts['facts']['writers']['value'] = 4
        facts['evidence'].clear()
        result = validity.check_memory(saved, facts, now=NOW)
        self.assertEqual(result['status'], 'contradicted')
        self.assertTrue({'unknown', 'needs_review', 'contradicted'} <= {c['status'] for c in result['checks']})

    def test_optional_mismatch_is_visible_but_does_not_block(self):
        saved, facts = record(), context()
        saved['applicability']['conditions'][0]['required'] = False
        facts['facts']['writers']['value'] = 2
        result = validity.check_memory(saved, facts, now=NOW)
        self.assertEqual(result['status'], 'applicable')
        self.assertTrue(any(c['status'] == 'contradicted' and not c['required'] for c in result['checks']))

    def test_allowlisted_comparisons_and_unusable_facts(self):
        for op, expected, value, wanted in [('in', [1, 2], 2, 'applicable'),
                                           ('gte', 2, 2, 'applicable'), ('lt', 2, 2, 'contradicted'),
                                           ('lte', 2, 2, 'applicable'), ('gt', 2, 3, 'applicable'),
                                           ('equals', 'v1', 'v1', 'applicable'),
                                           ('equals', None, None, 'unknown')]:
            saved, facts = record(), context()
            saved['applicability']['conditions'][0].update(operator=op, expected=expected)
            facts['facts']['writers']['value'] = value
            with self.subTest(op=op, expected=expected):
                self.assertEqual(validity.check_memory(saved, facts, now=NOW)['status'], wanted)
        for key, value in [('source', ''), ('observed_at', 'not a date'), ('value', float('inf'))]:
            facts = context()
            facts['facts']['writers'][key] = value
            with self.subTest(key=key):
                self.assertEqual(validity.check_memory(record(), facts, now=NOW)['status'], 'unknown')

    def test_invalid_contracts_are_rejected(self):
        mutations = [lambda a: a.update(schema_version='2.0'),
                     lambda a: a.update(conditions=[]),
                     lambda a: a['conditions'][0].update(operator='shell'),
                     lambda a: a['conditions'][0].update(max_age_seconds=-1),
                     lambda a: a['conditions'][0].update(required='yes'),
                     lambda a: a['conditions'].append(a['conditions'][0].copy()),
                     lambda a: a.update(extra='unsupported'),
                     lambda a: a.update(review_after='2026-10-23'),
                     lambda a: a['conditions'][0].update(expected=float('nan'))]
        for mutate in mutations:
            saved = record()
            mutate(saved['applicability'])
            with self.subTest(saved=saved), self.assertRaises(ValueError):
                validity.check_memory(saved, context(), now=NOW)

    def test_oversized_legacy_record_cannot_bypass_input_limit(self):
        with self.assertRaises(ValueError):
            validity.check_memory({'title': 'x' * 1000001}, {}, now=NOW)

    def test_store_check_enforces_project_scope_and_preserves_legacy(self):
        with tempfile.TemporaryDirectory() as folder:
            store = CaseStore(folder)
            saved = record()
            saved['applicability']['scope']['project_id'] = store.project_id
            store.save('decision', saved, authorized=True)
            store.save('legacy', {'title': 'Old', 'classification': 'hypothesis'}, authorized=True)
            before = {p.name: p.read_bytes() for p in store.path('decision').parent.glob('*.json')}
            self.assertEqual(store.check('decision', context(), now=NOW)['status'], 'applicable')
            facts = context()
            facts['scope']['project_id'] = 'forged'
            self.assertEqual(store.check('decision', facts, now=NOW)['status'], 'applicable')
            self.assertEqual(store.check('legacy', {}, now=NOW)['status'], 'unknown')
            self.assertEqual(before, {p.name: p.read_bytes() for p in store.path('decision').parent.glob('*.json')})
            saved['applicability']['schema_version'] = '9'
            with self.assertRaises(ValueError):
                store.save('invalid', saved, authorized=True)
            self.assertFalse(store.path('invalid').exists())

    def test_cli_success_and_invalid_input_exit_codes(self):
        script = Path(__file__).resolve().parents[1] / 'scripts/cognition.py'
        for payload, code, status in [({'record': record(), 'context': context(), 'now': NOW}, 0, 'applicable'),
                                      ({'record': record(), 'context': {}, 'now': 'invalid'}, 2, 'FAILED')]:
            result = subprocess.run([sys.executable, str(script), 'memory-check'], input=json.dumps(payload),
                                    text=True, capture_output=True)
            self.assertEqual(result.returncode, code, result.stderr)
            self.assertEqual(json.loads(result.stdout if code == 0 else result.stderr)['status'], status)

    def test_retrieval_validity_is_opt_in_and_filter_requires_context(self):
        with tempfile.TemporaryDirectory() as folder:
            store = CaseStore(folder)
            store.save('current', record(), authorized=True)
            store.save('old', {'title': 'Old', 'classification': 'hypothesis'}, authorized=True)
            self.assertNotIn('validity', store.list()[0])
            rows = store.list(context=context(), now=NOW)
            self.assertEqual([row['validity']['status'] for row in rows], ['applicable', 'unknown'])
            self.assertEqual([row['id'] for row in store.list(context=context(), status='applicable', now=NOW)], ['current'])
            with self.assertRaises(ValueError):
                store.list(status='applicable')
