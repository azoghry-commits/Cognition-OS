"""Bounded read-only host inventory probes; stores only this plugin's records."""
import json
import subprocess
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]

def run(command,name,timeout=45):
    try:
        result=subprocess.run(command,cwd=ROOT,capture_output=True,text=True,encoding='utf-8',errors='replace',timeout=timeout,shell=False)
        data={'command':command,'returncode':result.returncode,'stdout':result.stdout,'stderr':result.stderr}
    except subprocess.TimeoutExpired:
        data={'command':command,'status':'TIMEOUT','seconds':timeout}
    (ROOT/f'docs/evidence/{name}.json').write_text(json.dumps(data,indent=2),encoding='utf-8')
    print(json.dumps(data,indent=2))

if __name__=='__main__':
    import shutil
    run([shutil.which('claude') or 'claude','--plugin-dir',str(ROOT),'plugin','details','cognition-os'],'claude-discovery')
    codex=shutil.which('codex.cmd') or shutil.which('codex.exe')
    if codex:
        try:
            result=subprocess.run([codex,'plugin','list','--available','--json'],cwd=ROOT,capture_output=True,text=True,encoding='utf-8',errors='replace',timeout=45)
            raw=json.loads(result.stdout)
            def relevant(value):
                if isinstance(value,list):return [r for x in value if (r:=relevant(x)) is not None]
                if isinstance(value,dict):
                    if value.get('name')=='cognition-os' or value.get('name')=='cognition-os-local':return value
                    found={k:r for k,v in value.items() if isinstance(v,(list,dict)) and (r:=relevant(v))}
                    return found or None
                return None
            data={'returncode':result.returncode,'plugin_records':relevant(raw),'scope':'read-only inventory, not install/activation test'}
        except (subprocess.TimeoutExpired,json.JSONDecodeError) as error:data={'status':'UNVERIFIED','error':type(error).__name__}
        (ROOT/'docs/evidence/codex-discovery.json').write_text(json.dumps(data,indent=2),encoding='utf-8');print(json.dumps(data,indent=2))
