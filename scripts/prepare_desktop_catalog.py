"""Authorized one-time personal catalog setup for ChatGPT Desktop local discovery."""
import json
import zipfile
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]

def prepare():
    version=json.loads((ROOT/'plugin.json').read_text())['version']
    source=Path.home()/'.codex/plugins/local-sources/cognition-os'
    catalog=Path.home()/'.agents/plugins/marketplace.json'
    if source.exists() or catalog.exists():raise FileExistsError('Existing personal source/catalog requires a reviewed merge; nothing overwritten')
    with zipfile.ZipFile(ROOT/f'dist/cognition-os-{version}.zip') as z:
        for item in z.infolist():
            p=(source/item.filename).resolve()
            if not p.is_relative_to(source.resolve()) or ':' in item.filename or '\\' in item.filename:raise ValueError('Unsafe archive member')
        z.extractall(source)
    data={'name':'cognition-os-local','interface':{'displayName':'Cognition OS local'},'plugins':[{'name':'cognition-os','source':{'source':'local','path':'./.codex/plugins/local-sources/cognition-os'},'policy':{'installation':'AVAILABLE','authentication':'ON_INSTALL'},'category':'Productivity'}]}
    catalog.parent.mkdir(parents=True,exist_ok=True)
    with catalog.open('x',encoding='utf-8') as stream:json.dump(data,stream,indent=2)
    record={'target':'ChatGPT Desktop on Windows','user_authorization':'Yes, install in Codex only','catalog':str(catalog),'source':str(source),'marketplace_name':data['name'],'version':version,'desktop_activation':'UNVERIFIED; requires native fresh-chat observation'}
    (ROOT/'docs/evidence/desktop-catalog.json').write_text(json.dumps(record,indent=2),encoding='utf-8')
    print(json.dumps(record,indent=2))

if __name__=='__main__':prepare()
