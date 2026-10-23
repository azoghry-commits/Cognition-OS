import json
import tempfile
import unittest
from pathlib import Path

from cognition.memory import CaseStore
from cognition.improvement import ImprovementStore
from cognition.storage import MAX_RECORD_BYTES


class StorageReadTests(unittest.TestCase):
    def test_stores_reject_oversized_nonfinite_and_nonobject_files(self):
        with tempfile.TemporaryDirectory() as folder:
            for store in (CaseStore(folder), ImprovementStore(folder)):
                path = store.path('bad')
                path.parent.mkdir(parents=True, exist_ok=True)
                for raw in (b' ' * (MAX_RECORD_BYTES + 1), b'[]',
                            json.dumps({'project_id': store.project_id, 'state': 'OBSERVED',
                                        'value': float('nan')}).encode()):
                    with self.subTest(store=type(store).__name__, size=len(raw)):
                        path.write_bytes(raw)
                        with self.assertRaises(ValueError):
                            store.get('bad')

    def test_case_limit_includes_pretty_printed_envelope(self):
        with tempfile.TemporaryDirectory() as folder:
            store = CaseStore(folder)
            record = {'title': 'Case', 'classification': 'hypothesis',
                      'items': [''] * 160000}
            self.assertLess(len(json.dumps(record).encode()), MAX_RECORD_BYTES)
            with self.assertRaises(ValueError):
                store.save('large', record, authorized=True)
            self.assertFalse(store.path('large').exists())

    def test_saved_unicode_case_roundtrips(self):
        with tempfile.TemporaryDirectory() as folder:
            store = CaseStore(folder)
            record = {'title': 'Bukti é', 'classification': 'hypothesis'}
            store.save('case', record, authorized=True)
            self.assertEqual(store.get('case')['record'], record)
