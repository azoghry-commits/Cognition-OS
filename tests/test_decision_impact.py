import hashlib
import tempfile
import unittest
from pathlib import Path

from cognition import validity


class ImpactTests(unittest.TestCase):
    def test_transitive_impact_leaves_unrelated_decisions_alone(self):
        nodes = [{'id': 'file', 'kind': 'evidence', 'depends_on': []},
                 {'id': 'assumption', 'kind': 'assumption', 'depends_on': ['file']},
                 {'id': 'choice', 'kind': 'decision', 'depends_on': ['assumption']},
                 {'id': 'other', 'kind': 'decision', 'depends_on': []}]
        result = validity.decision_impact(nodes, ['file'])
        self.assertEqual(result['decisions'], [{'id': 'choice', 'status': 'needs_review', 'causes': ['file']}])
        self.assertTrue(result['complete'])

    def test_missing_reference_propagates_unknown_and_change_takes_precedence(self):
        nodes = [{'id': 'choice', 'kind': 'decision', 'depends_on': ['missing']},
                 {'id': 'downstream', 'kind': 'decision', 'depends_on': ['choice']}]
        result = validity.decision_impact(nodes, [])
        self.assertEqual(result['missing_references'], ['missing'])
        self.assertEqual([d['status'] for d in result['decisions']], ['unknown', 'unknown'])
        self.assertFalse(result['complete'])
        result = validity.decision_impact(nodes, ['missing'])
        self.assertEqual([d['status'] for d in result['decisions']], ['needs_review', 'needs_review'])
        self.assertFalse(result['complete'])

    def test_cycles_duplicates_oversized_graph_and_unknown_changes_are_explicit(self):
        for nodes in [[{'id': 'a', 'kind': 'decision', 'depends_on': ['a']}],
                      [{'id': 'a', 'kind': 'decision', 'depends_on': ['b']},
                       {'id': 'b', 'kind': 'assumption', 'depends_on': ['a']}],
                      [{'id': 'a', 'kind': 'decision', 'depends_on': []}] * 2,
                      [{'id': str(i), 'kind': 'decision', 'depends_on': []} for i in range(1001)]]:
            with self.subTest(nodes=len(nodes)), self.assertRaises(ValueError):
                validity.decision_impact(nodes, [])
        result = validity.decision_impact([], ['unregistered'])
        self.assertEqual(result['unmapped_changes'], ['unregistered'])
        self.assertFalse(result['complete'])

    def test_result_limit_is_deterministic_and_reports_incomplete(self):
        nodes = [{'id': 'file', 'kind': 'evidence', 'depends_on': []}]
        nodes += [{'id': str(i), 'kind': 'decision', 'depends_on': ['file']} for i in range(3)]
        result = validity.decision_impact(nodes, ['file'], max_results=1)
        self.assertEqual(len(result['decisions']), 1)
        self.assertEqual(result['omitted_decisions'], 2)
        self.assertFalse(result['complete'])

    def test_iterative_graph_handles_deep_dependency_chain(self):
        nodes = [{'id': '0', 'kind': 'evidence', 'depends_on': []}]
        nodes += [{'id': str(i), 'kind': 'decision', 'depends_on': [str(i - 1)]} for i in range(1, 1000)]
        result = validity.decision_impact(nodes, ['0'], max_results=1000)
        self.assertEqual(len(result['decisions']), 999)
        self.assertTrue(result['complete'])

    def test_evidence_snapshot_is_bounded_read_only_and_confined(self):
        with tempfile.TemporaryDirectory() as folder, tempfile.TemporaryDirectory() as outside:
            root = Path(folder)
            (root / 'proof.md').write_bytes(b'confirmed evidence')
            before = (root / 'proof.md').read_bytes()
            result = validity.snapshot_evidence(folder, {'proof': 'proof.md', 'absent': 'missing.md'},
                                                now='2026-10-23T12:00:00Z')
            self.assertEqual(result['evidence']['proof']['fingerprint'], hashlib.sha256(before).hexdigest())
            self.assertEqual(result['unavailable'][0]['id'], 'absent')
            self.assertEqual((root / 'proof.md').read_bytes(), before)
            (root / 'large').write_bytes(b'x' * 1000001)
            self.assertEqual(validity.snapshot_evidence(folder, {'x': 'large'})['unavailable'][0]['reason'], 'oversized')
            for path in ['../outside', str(Path(outside) / 'proof'), 'C:relative', 'proof.md:stream']:
                with self.subTest(path=path), self.assertRaises(ValueError):
                    validity.snapshot_evidence(folder, {'proof': path})
            try:
                (root / 'linked').symlink_to(root / 'proof.md')
            except OSError:
                self.skipTest('Symlink creation unavailable')
            with self.assertRaises(ValueError):
                validity.snapshot_evidence(folder, {'proof': 'linked'})
