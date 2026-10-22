import hashlib
import json
import os
import shlex
import subprocess
import sys
import tempfile
import tomllib
import unittest
import zipfile
from pathlib import Path
from cognition.engine import ROOT
from cognition import __version__
from scripts.package_release import runtime_files,archive

class PackagingTests(unittest.TestCase):
    def test_project_metadata_versions_and_lockfile_are_synchronized(self):
        project = tomllib.loads((ROOT / 'pyproject.toml').read_text(encoding='utf-8'))
        plugin = json.loads((ROOT / 'plugin.json').read_text(encoding='utf-8'))
        self.assertEqual(project['project']['version'], plugin['version'])
        self.assertEqual(__version__, plugin['version'])
        self.assertEqual(project['project']['requires-python'], '>=3.10')
        self.assertTrue((ROOT / 'uv.lock').is_file())

    def test_hybrid_tools_and_hook_run_from_extracted_archive(self):
        files=runtime_files()
        with tempfile.TemporaryDirectory(prefix='cognition package ') as folder:
            target=Path(folder); archive_path=target/'candidate.zip'
            archive(archive_path,[(p.relative_to(ROOT).as_posix(),p.read_bytes()) for p in files])
            with zipfile.ZipFile(archive_path) as z:z.extractall(target/'installed')
            installed=target/'installed'
            result=subprocess.run([sys.executable,str(installed/'scripts/cognition.py'),'assess'],
                input=json.dumps({'objective':'Rename a label','task_type':'simple_edit'}),cwd=target,capture_output=True,text=True)
            self.assertEqual(result.returncode,0,result.stderr)
            self.assertEqual(json.loads(result.stdout)['policy'],'PASS_THROUGH')
            capability=subprocess.run([sys.executable,str(installed/'scripts/cognition.py'),'capability-plan'],
                input=json.dumps({'profile':{'capability_tier':'unknown','context_tokens':4096,'tools':{}},
                                  'task':{'objective':'Review a change','task_type':'artifact_review','complexity':'medium','risk':'normal'}}),
                cwd=target,capture_output=True,text=True)
            self.assertEqual(capability.returncode,0,capability.stderr)
            self.assertEqual(json.loads(capability.stdout)['resolved_tier'],'constrained')
            path=target/'.cognition/artifacts/one.json';path.parent.mkdir(parents=True);path.write_text('{bad')
            payload={'cwd':str(target),'hook_event_name':'PostToolUse','tool_name':'Write','tool_input':{'file_path':str(path)}}
            hook=subprocess.run([sys.executable,str(installed/'scripts/check_artifact.py')],
                input=json.dumps(payload),cwd=target,capture_output=True,text=True)
            self.assertEqual(hook.returncode,0,hook.stderr)
            output=json.loads(hook.stdout)
            self.assertIn('additionalContext',output['hookSpecificOutput'])
            self.assertNotIn('decision',output)
            for host in ['codex','claude']:
                config=json.loads((installed/f'hooks/{host}/hooks.json').read_text())
                self.assertIn('PostToolUse',config['hooks'])
                command=config['hooks']['PostToolUse'][0]['hooks'][0]['command']
                environment=os.environ.copy();environment['PLUGIN_ROOT' if host=='codex' else 'CLAUDE_PLUGIN_ROOT']=str(installed)
                if os.name=='nt':
                    # A command string is parsed by cmd; passing it as a quoted list
                    # argument would use Python's argv escaping rather than cmd syntax.
                    command_args=command
                else:
                    command_args=shlex.split(command);command_args[0]=sys.executable
                configured=subprocess.run(command_args,input=json.dumps(payload),cwd=target,
                    capture_output=True,text=True,env=environment,shell=os.name=='nt')
                self.assertEqual(configured.returncode,0,configured.stderr)
                self.assertIn('hookSpecificOutput',json.loads(configured.stdout))

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

    def test_cross_host_adapters_are_packaged(self):
        names=[p.relative_to(ROOT).as_posix() for p in runtime_files()]
        for platform in ['antigravity','github-copilot','vscode','generic','opencode','commandcode','openclaw','hermes']:
            self.assertIn(f'adapters/{platform}/README.md',names)
        self.assertIn('openclaw.plugin.json',names)
        self.assertIn('docs/CROSS_HOST_COMPATIBILITY.md',names)
        self.assertIn('docs/SELF_IMPROVEMENT.md',names)
        self.assertIn('docs/CAPABILITY_AMPLIFICATION.md',names)
        self.assertIn('cognition/capability.py',names)
    def test_retired_sources_are_not_required_or_packaged(self):
        names=[p.relative_to(ROOT).as_posix() for p in runtime_files()]
        self.assertFalse((ROOT/'Cognition Os Master Blueprint.md').exists())
        self.assertFalse((ROOT/'Cognition_OS_Strategic_Intelligence.pdf').exists())
        self.assertNotIn('Cognition Os Master Blueprint.md',names)
        self.assertNotIn('Cognition_OS_Strategic_Intelligence.pdf',names)
    def test_cli_failure_is_structured_nonzero(self):
        p=subprocess.run([sys.executable,str(ROOT/'scripts/cognition.py'),'compute'],input=json.dumps({'operation':'__import__','inputs':{}}),capture_output=True,text=True)
        self.assertEqual(p.returncode,2)
        self.assertEqual(json.loads(p.stderr)['status'],'FAILED')
