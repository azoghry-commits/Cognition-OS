import hashlib
import json
import subprocess
import sys
import tempfile
import unittest
import zipfile
from pathlib import Path
from cognition.engine import ROOT
from scripts.package_release import runtime_files,archive

class PackagingTests(unittest.TestCase):
    def test_runtime_archive_is_portable_and_excludes_sources_secrets(self):
        files=runtime_files()
        names=[p.relative_to(ROOT).as_posix() for p in files]
        self.assertIn('plugin.json',names)
        self.assertNotIn('Cognition Os Master Blueprint.md',names)
        self.assertNotIn('docs/evidence/implementation-request.txt',names)
        self.assertTrue(all('.dev-deps' not in n and '__pycache__' not in n and not n.endswith('.pdf') for n in names))
        with tempfile.TemporaryDirectory() as folder:
            target=Path(folder);zpath=target/'candidate.zip'
            items=[(p.relative_to(ROOT).as_posix(),p.read_bytes()) for p in files]
            archive(zpath,items)
            before=hashlib.sha256(zpath.read_bytes()).hexdigest()
            archive(zpath,items)
            self.assertEqual(before,hashlib.sha256(zpath.read_bytes()).hexdigest())
            with zipfile.ZipFile(zpath) as z:
                self.assertIsNone(z.testzip());z.extractall(target/'installed')
            installed=target/'installed'
            result=subprocess.run([sys.executable,str(installed/'scripts/cognition.py'),'compute','--input',str(installed/'references/examples/ev.json')],cwd=target,capture_output=True,text=True)
            self.assertEqual(result.returncode,0,result.stderr)
            self.assertAlmostEqual(json.loads(result.stdout)['net_ev'],.655)
            definition=subprocess.run([sys.executable,str(installed/'scripts/cognition.py'),'framework'],cwd=target,input=json.dumps({'id':'Kepner-Tregoe'}),capture_output=True,text=True)
            self.assertEqual(definition.returncode,0,definition.stderr)
            self.assertEqual(json.loads(definition.stdout)['id'],'FW-11')
    def test_supplied_source_hashes_preserved(self):
        manifest=json.loads((ROOT/'docs/evidence/sources.json').read_text())
        for filename,record in manifest.items():
            with self.subTest(source=filename):self.assertEqual(hashlib.sha256((ROOT/filename).read_bytes()).hexdigest(),record['sha256'])
    def test_cli_failure_is_structured_nonzero(self):
        p=subprocess.run([sys.executable,str(ROOT/'scripts/cognition.py'),'compute'],input=json.dumps({'operation':'__import__','inputs':{}}),capture_output=True,text=True)
        self.assertEqual(p.returncode,2)
        self.assertEqual(json.loads(p.stderr)['status'],'FAILED')
