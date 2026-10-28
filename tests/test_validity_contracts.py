import contextlib
import io
import json
import subprocess
import sys
import tempfile
import unittest
import zipfile
from pathlib import Path

import jsonschema
from cognition.validity import check_memory
from scripts import package_release
from tests.test_validity import NOW, context, record

ROOT = Path(__file__).resolve().parents[1]


class ValidityContractTests(unittest.TestCase):
    def test_metadata_and_results_match_published_schemas(self):
        for name, instance in [('applicability', record()['applicability']),
                                ('memory-check-result', check_memory(record(), context(), now=NOW)),
                                ('memory-check-result', check_memory({}, {}, now=NOW))]:
            schema = json.loads((ROOT / 'schemas' / (name + '.schema.json')).read_text())
            jsonschema.Draft202012Validator(schema, format_checker=jsonschema.FormatChecker()).validate(instance)
        schema = json.loads((ROOT / 'schemas/applicability.schema.json').read_text())
        for operator, expected in [('shell', 'echo bad'), ('lt', '1.2'), ('in', []), ('equals', {})]:
            saved = record()['applicability']
            saved['conditions'][0].update(operator=operator, expected=expected)
            with self.subTest(operator=operator), self.assertRaises(jsonschema.ValidationError):
                jsonschema.validate(saved, schema)

    def test_extracted_package_runs_check_impact_and_snapshot(self):
        with contextlib.redirect_stdout(io.StringIO()):
            package_release.package()
        archive = ROOT / 'dist' / f'cognition-os-{package_release.VERSION}.zip'
        with tempfile.TemporaryDirectory(prefix='validity package ') as folder:
            with zipfile.ZipFile(archive) as packed:
                packed.extractall(folder)
            target = Path(folder)
            (target / 'proof.txt').write_text('evidence')
            script = target / 'scripts/cognition.py'
            payloads = [('memory-check', {'record': record(), 'context': context(), 'now': NOW}),
                        ('decision-impact', {'nodes': [{'id': 'a', 'kind': 'decision', 'depends_on': []}], 'changes': ['a']}),
                        ('evidence-snapshot', {'workspace': folder, 'paths': {'proof': 'proof.txt'}, 'now': NOW})]
            for action, payload in payloads:
                output = subprocess.run([sys.executable, '-I', str(script), action], input=json.dumps(payload),
                                        capture_output=True, text=True, cwd=folder)
                self.assertEqual(output.returncode, 0, output.stderr)
                result = json.loads(output.stdout)
                if action == 'memory-check':
                    self.assertEqual(result['status'], 'applicable')
                elif action == 'decision-impact':
                    self.assertEqual(result['decisions'][0]['status'], 'needs_review')
                else:
                    self.assertTrue(result['complete'])
                    self.assertEqual(len(result['evidence']['proof']['fingerprint']), 64)
