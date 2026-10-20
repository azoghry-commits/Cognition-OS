"""Capture reproducible local QA evidence without invoking paid model inference."""
import io
import json
import platform
import shutil
import subprocess
import sys
import unittest
from datetime import datetime,timezone
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1];sys.path.insert(0,str(ROOT))
from scripts.validate_package import validate

def main():
    suite=unittest.defaultTestLoader.discover(str(ROOT/'tests'))
    stream=io.StringIO();result=unittest.TextTestRunner(stream=stream,verbosity=2).run(suite)
    report={'timestamp':datetime.now(timezone.utc).isoformat(),'python':platform.python_version(),'tests_run':result.testsRun,'passed':result.testsRun-len(result.failures)-len(result.errors)-len(result.skipped),'failures':len(result.failures),'errors':len(result.errors),'skipped':[{'test':test.id(),'reason':reason} for test,reason in result.skipped],'test_output':stream.getvalue()}
    try:report['package_validation']=validate()
    except Exception as error:report['package_validation']={'status':'FAILED','error':str(error)}
    validator=Path.home()/'.codex/skills/.system/skill-creator/scripts/quick_validate.py'
    report['skill_validator']=[]
    if validator.exists():
        for p in sorted((ROOT/'skills').iterdir()):
            probe=subprocess.run([sys.executable,str(validator),str(p)],capture_output=True,text=True,timeout=20)
            report['skill_validator'].append({'skill':p.name,'returncode':probe.returncode,'output':probe.stdout.strip(),'stderr':probe.stderr.strip()})
    claude=shutil.which('claude')
    report['claude_validation']=[]
    if claude:
        for target in ['.claude-plugin/plugin.json','.claude-plugin/marketplace.json']:
            p=subprocess.run([claude,'plugin','validate',str(ROOT/target)],capture_output=True,text=True,encoding='utf-8',errors='replace',timeout=30)
            report['claude_validation'].append({'target':target,'returncode':p.returncode,'output':p.stdout,'stderr':p.stderr})
    (ROOT/'docs/evidence/checks.json').write_text(json.dumps(report,indent=2),encoding='utf-8')
    print(json.dumps({k:v for k,v in report.items() if k not in ['test_output']},indent=2))
    return 0 if result.wasSuccessful() and report['package_validation'].get('status')=='TESTED' and all(p['returncode']==0 for p in report['skill_validator']+report['claude_validation']) else 1

if __name__=='__main__':sys.exit(main())
