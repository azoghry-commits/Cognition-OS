import json
import sys
import tempfile
import types
import unittest
from pathlib import Path
from unittest.mock import patch


SCRIPTS = Path(__file__).resolve().parents[1] / "scripts"
sys.path.insert(0, str(SCRIPTS))

import build_catalog  # noqa: E402
import build_docs  # noqa: E402


class BuildCatalogTests(unittest.TestCase):
    def test_methods_define_all_fifty_frameworks(self):
        rows = [line.split("|") for line in build_catalog.METHODS.strip().splitlines()]
        identifiers = [int(row[0]) for row in rows]

        self.assertEqual(identifiers, list(range(1, 51)))
        for identifier, required, outputs, method in rows:
            with self.subTest(identifier=identifier):
                self.assertTrue(required)
                self.assertTrue(outputs)
                self.assertGreaterEqual(len(method.split(";")), 3)

    def test_write_creates_parent_and_serializes_json(self):
        with tempfile.TemporaryDirectory() as directory:
            with patch.object(build_catalog, "ROOT", Path(directory)):
                build_catalog.write("nested/catalog.json", {"version": build_catalog.VERSION})

            output = Path(directory) / "nested" / "catalog.json"
            self.assertEqual(json.loads(output.read_text(encoding="utf-8")), {"version": "0.5.0"})
            self.assertTrue(output.read_text(encoding="utf-8").endswith("\n"))


class BuildDocsTests(unittest.TestCase):
    def test_current_version_routes_to_hybrid_builder(self):
        calls = []
        fake_module = types.ModuleType("build_hybrid")
        fake_module.build = lambda: calls.append("build")

        with patch.dict(sys.modules, {"build_hybrid": fake_module}):
            build_docs.build()

        self.assertEqual(calls, ["build"])


if __name__ == "__main__":
    unittest.main()
