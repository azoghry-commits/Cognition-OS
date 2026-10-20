"""Stage the allowlisted runtime archive before native user-level installation."""
import json
import zipfile
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]

def prepare():
    version=json.loads((ROOT/'plugin.json').read_text())['version']
    archive=ROOT/f'dist/cognition-os-marketplace-{version}.zip'
    destination=ROOT/'local-marketplace'
    if destination.exists():raise FileExistsError('Staging directory exists; review it before replacing an installed source.')
    with zipfile.ZipFile(archive) as z:
        for item in z.infolist():
            target=(destination/item.filename).resolve()
            if not target.is_relative_to(destination.resolve()) or ':' in item.filename or '\\' in item.filename:
                raise ValueError('Unsafe archive entry')
        z.extractall(destination)
    manifest=ROOT/'.agents/plugins/marketplace.json'
    data=json.loads(manifest.read_text())
    entry=next(p for p in data['plugins'] if p['name']=='cognition-os')
    entry['source']={'source':'local','path':'./local-marketplace/plugins/cognition-os'}
    manifest.write_text(json.dumps(data,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'staged':str(destination),'plugin_path':entry['source']['path'],'version':version},indent=2))

if __name__=='__main__':prepare()
