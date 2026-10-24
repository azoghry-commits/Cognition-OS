import json
import math
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
import build_catalog


class CatalogSerializationTests(unittest.TestCase):
    def test_nonfinite_values_never_create_invalid_json_artifacts(self):
        for value in (math.nan, math.inf, -math.inf):
            with self.subTest(value=value), tempfile.TemporaryDirectory() as folder:
                with patch.object(build_catalog, 'ROOT', Path(folder)):
                    with self.assertRaises(ValueError):
                        build_catalog.write('catalog.json', {'value': value})
                self.assertFalse((Path(folder) / 'catalog.json').exists())

    def test_unicode_json_and_all_fifty_method_rows(self):
        rows = [row.split('|') for row in build_catalog.METHODS.strip().splitlines()]
        self.assertEqual([int(row[0]) for row in rows], list(range(1, 51)))
        with tempfile.TemporaryDirectory() as folder:
            with patch.object(build_catalog, 'ROOT', Path(folder)):
                build_catalog.write('nested/catalog.json', {'title':'Kondisi berubah', 'rows':rows})
            self.assertEqual(len(json.loads((Path(folder)/'nested/catalog.json').read_text(encoding='utf-8'))['rows']), 50)
