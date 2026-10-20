"""Rebuild the native V4.1 package locally; no installation or publication side effects."""
import argparse
import hashlib
import json
from pathlib import Path
from build_catalog import build as catalog
from build_plugin import build as plugin
from build_docs import build as docs
from validate_package import validate
from package_release import package


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--package',action='store_true',help='Also create local deterministic ZIP archives')
    args=parser.parse_args()
    root=Path(__file__).resolve().parents[1]
    source_manifest=json.loads((root/'docs/evidence/sources.json').read_text(encoding='utf-8'))
    for name,record in source_manifest.items():
        if hashlib.sha256((root/name).read_bytes()).hexdigest()!=record['sha256']:
            raise ValueError('Source identity changed; complete a reviewed source audit before regeneration')
    catalog(); plugin(); docs()
    print(json.dumps(validate(),indent=2))
    if args.package:package()


if __name__=='__main__':main()
