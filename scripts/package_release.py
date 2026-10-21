"""Deterministic local artifacts; no publication, install or personal config writes."""
import hashlib
import json
import sys
import zipfile
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
VERSION=json.loads((ROOT/'plugin.json').read_text())['version']
RUNTIME_DIRS=['skills','cognitive-core','cognition','schemas','references','templates','assets','agents','adapters','hooks']
SCRIPTS=['scripts/cognition.py','scripts/check_artifact.py']
RUNTIME_FILES=['plugin.json','openclaw.plugin.json','.claude-plugin/plugin.json','.codex-plugin/plugin.json','README.md','CHANGELOG.md']

def runtime_files():
    files=[ROOT/f for f in RUNTIME_FILES+SCRIPTS]
    for folder in RUNTIME_DIRS:
        files.extend(p for p in (ROOT/folder).rglob('*') if p.is_file() and '__pycache__' not in p.parts and p.suffix!='.pyc')
    # Ship human guides, excluding rendered sources, raw implementation prompt and test transcripts.
    files.extend((ROOT/'docs').glob('*.md'))
    return sorted(set(files),key=lambda p:p.relative_to(ROOT).as_posix())

def archive(path,items):
    with zipfile.ZipFile(path,'w',compression=zipfile.ZIP_DEFLATED,compresslevel=9) as z:
        for name,data in sorted(items):
            info=zipfile.ZipInfo(name,date_time=(2026,10,20,0,0,0));info.compress_type=zipfile.ZIP_DEFLATED;info.external_attr=0o644<<16
            z.writestr(info,data)

def package():
    dist=ROOT/'dist';dist.mkdir(exist_ok=True)
    files=runtime_files();items=[(p.relative_to(ROOT).as_posix(),p.read_bytes()) for p in files]
    integrity={name:hashlib.sha256(data).hexdigest() for name,data in items}
    items.append(('PACKAGE_CONTENTS.json',(json.dumps({'version':VERSION,'files':integrity},indent=2)+'\n').encode()))
    plugin=dist/f'cognition-os-{VERSION}.zip';archive(plugin,items)
    market_items=[('plugins/cognition-os/'+name,data) for name,data in items]
    market_items += [('.agents/plugins/marketplace.json',json.dumps({'name':'cognition-os-local','interface':{'displayName':'Cognition OS local'},'plugins':[{'name':'cognition-os','source':{'source':'local','path':'./plugins/cognition-os'},'policy':{'installation':'AVAILABLE','authentication':'ON_INSTALL'},'category':'Productivity'}]},indent=2).encode()),('.claude-plugin/marketplace.json',json.dumps({'name':'cognition-os-local','owner':{'name':'Cognition OS project'},'metadata':{'description':'Cognition OS private local catalog'},'plugins':[{'name':'cognition-os','source':'./plugins/cognition-os','version':VERSION}]},indent=2).encode())]
    marketplace=dist/f'cognition-os-marketplace-{VERSION}.zip';archive(marketplace,market_items)
    antigravity_items=[(name,data) for name,data in items if name!='plugin.json']
    antigravity_manifest=(json.dumps({'name':'cognition-os','version':VERSION,
        'description':'Cognition OS portable skills, orchestration and governed improvement.'},indent=2)+'\n').encode()
    antigravity_items.append(('plugin.json',antigravity_manifest))
    antigravity=dist/f'cognition-os-antigravity-{VERSION}.zip';archive(antigravity,antigravity_items)
    qa_files=[]
    for directory in ['tests','scripts']:
        qa_files.extend(p for p in (ROOT/directory).rglob('*') if p.is_file() and '__pycache__' not in p.parts and p.suffix!='.pyc')
    qa_files.extend(p for p in (ROOT/'docs/evidence').glob('*.json'))
    qa=dist/f'cognition-os-qa-{VERSION}.zip'
    archive(qa,[(p.relative_to(ROOT).as_posix(),p.read_bytes()) for p in qa_files])
    result={p.name:{'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'bytes':p.stat().st_size} for p in [plugin,marketplace,antigravity,qa]}
    (dist/'SHA256SUMS.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    # Reopen archives; hash every runtime member and reject unwanted data.
    with zipfile.ZipFile(plugin) as z:
        assert z.testzip() is None
        for name,digest in integrity.items():assert hashlib.sha256(z.read(name)).hexdigest()==digest
        assert not any(n.endswith('.pdf') or '.env' in n or '.dev-deps' in n or '__pycache__' in n for n in z.namelist())
    print(json.dumps(result,indent=2));return result

if __name__=='__main__':package()
