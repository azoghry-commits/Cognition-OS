"""Explicit, bounded project storage. No automatic writes or cross-project retrieval."""
import hashlib
import json
import re
from datetime import datetime,timezone
from pathlib import Path

class CaseStore:
    def __init__(self,workspace):
        self.root=Path(workspace).resolve(strict=True)
        if not self.root.is_dir(): raise ValueError('Workspace directory required')
        self.project_id=hashlib.sha256(str(self.root).casefold().encode()).hexdigest()[:24]
    def path(self,case_id):
        if not isinstance(case_id,str) or not re.fullmatch(r'[a-z0-9][a-z0-9-]{0,63}',case_id): raise ValueError('Invalid case id')
        if case_id.upper() in {'CON','PRN','AUX','NUL',*(f'COM{i}' for i in range(1,10)),*(f'LPT{i}' for i in range(1,10))}: raise ValueError('Reserved device name')
        base=self.root/'.cognition'/'cases'
        target=base/(case_id+'.json')
        if not target.resolve().is_relative_to(self.root): raise ValueError('Storage path escapes project')
        # Reject symlinks and Windows junctions, including ancestors.
        for p in [self.root/'.cognition',base,target]:
            if p.is_symlink() or (hasattr(p,'is_junction') and p.is_junction()): raise ValueError('Linked storage paths are forbidden')
        return target
    def save(self,case_id,record,authorized=False,sensitive=False,sensitive_authorized=False):
        if authorized is not True: raise ValueError('Explicit persistence authorization required')
        if sensitive and sensitive_authorized is not True: raise ValueError('Explicit sensitive-data authorization required')
        if not isinstance(record,dict) or not record.get('title') or not record.get('classification'): raise ValueError('Case title and knowledge classification required')
        if record['classification'] not in ['approved_knowledge','hypothesis','observed_outcome','user_preference']: raise ValueError('Invalid knowledge classification')
        encoded=json.dumps(record,ensure_ascii=False,allow_nan=False)
        if len(encoded.encode())>1000000: raise ValueError('Case exceeds 1 MB limit')
        p=self.path(case_id);p.parent.mkdir(parents=True,exist_ok=True)
        # Exclusive create prevents accidental overwrite. Versions receive new IDs.
        data={'schema_version':'1.0','version':1,'project_id':self.project_id,'created_at':datetime.now(timezone.utc).isoformat(),'sensitive':bool(sensitive),'record':record}
        with p.open('x',encoding='utf-8') as stream: json.dump(data,stream,ensure_ascii=False,indent=2)
        return {'id':case_id,'path':str(p),'project_id':self.project_id}
    def get(self,case_id):
        data=json.loads(self.path(case_id).read_text(encoding='utf-8'))
        if data.get('project_id')!=self.project_id: raise ValueError('Cross-project case rejected')
        return data
    def list(self,query=''):
        p=self.path('probe').parent
        if not p.exists():return []
        result=[]
        for f in sorted(p.glob('*.json')):
            data=self.get(f.stem)
            if query.casefold() in data['record']['title'].casefold(): result.append({'id':f.stem,'title':data['record']['title'],'classification':data['record']['classification']})
        return result
    def delete(self,case_id,authorized=False):
        if authorized is not True: raise ValueError('Explicit deletion authorization required')
        self.get(case_id);self.path(case_id).unlink()
        return {'deleted':case_id}
