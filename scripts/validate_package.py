"""Validate full JSON schemas when dev dependency exists, references and shared assets."""
import json
import re
import sys
import importlib.metadata
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT));sys.path.insert(0,str(ROOT/'.dev-deps'))
from cognition import engine as e

def validate():
    import jsonschema
    schemas={p.stem:json.loads(p.read_text(encoding='utf-8')) for p in (ROOT/'schemas').glob('*.json')}
    for schema in schemas.values():jsonschema.Draft202012Validator.check_schema(schema)
    for p in (ROOT/'schemas/framework-output').glob('*.json'):jsonschema.Draft202012Validator.check_schema(json.loads(p.read_text()))
    manifest=e.read_json(ROOT/'plugin.json')
    jsonschema.validate(manifest,e.read_json(ROOT/'schemas/vendor/plugin.schema.json'))
    assert e.read_json(ROOT/'.claude-plugin/plugin.json')['name']==manifest['name']
    assert e.read_json(ROOT/'.codex-plugin/plugin.json')['version']==manifest['version']
    for path in ['onboardingSkill']:
        value=manifest['extensions']['com.openai'][path];assert value.startswith('./') and (ROOT/value).is_file()
    for path in ['logo','composerIcon']:
        assert (ROOT/manifest['extensions']['com.openai']['interface'][path]).is_file()
    catalog=e.registry()
    for entry in catalog:jsonschema.validate(e.framework(entry['id']),schemas['framework.schema'])
    for agent in e.read_json(ROOT/'cognitive-core/agents/registry.json')['agents']:jsonschema.validate(agent,schemas['agent.schema'])
    skill_paths=list((ROOT/'skills').glob('*/SKILL.md'))
    for p in skill_paths:
        text=p.read_text(encoding='utf-8')
        assert text.startswith('---\nname: '+p.parent.name+'\n')
        description=re.search(r'^description: (.+)$',text,re.M);assert description and len(description[1])<400
        for link in re.findall(r'\]\(([^)]+)\)',text):
            if not link.startswith(('https:','http:','#')):assert (p.parent/link).resolve().is_file(),f'Missing {p}: {link}'
        assert (p.parent/'../../cognitive-core/frameworks/definitions/FW-11.json').resolve().is_file()
    core_code='\n'.join(p.read_text() for p in (ROOT/'cognition').glob('*.py'))
    assert not re.search(r'\b(eval|exec|subprocess|requests|urllib)\b',core_code)
    assert not (ROOT/'mcp.json').exists() and not (ROOT/'hooks').exists()
    required=['SOURCE_ANALYSIS','REQUIREMENTS_TRACEABILITY','PLATFORM_COMPATIBILITY','ARCHITECTURE','ARCHITECTURE_DECISIONS','MENTAL_MODEL_REGISTRY','AGENT_REGISTRY','SKILL_SPECIFICATIONS','ORCHESTRATION_DESIGN','DATA_CONTRACTS','MATHEMATICAL_VALIDATION','DECISION_PROVENANCE','MEMORY_ARCHITECTURE','MCP_DECISION','SECURITY_MODEL','PERFORMANCE_EVALUATION','TEST_PLAN','INSTALLATION_CLAUDE','INSTALLATION_CODEX','USER_GUIDE','TROUBLESHOOTING','RELEASE_CHECKLIST']
    for n in required:assert (ROOT/f'docs/{n}.md').is_file(),n
    return {'status':'TESTED','full_schema_validator':importlib.metadata.version('jsonschema'),'frameworks':len(catalog),'logical_agents':52,'skills':len(skill_paths),'required_documents':len(required),'note':'Structural validation; native semantic behavior is a separate gate.'}

if __name__=='__main__':print(json.dumps(validate(),indent=2))
