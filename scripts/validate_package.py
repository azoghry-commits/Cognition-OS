"""Validate full JSON schemas when dev dependency exists, references and shared assets."""
import json
import re
import sys
import importlib.metadata
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT));sys.path.insert(0,str(ROOT/'.dev-deps'))
from cognition import engine as e


def validate_release_metadata():
    """Keep active package metadata and release instructions on one version/command contract."""
    manifest = e.read_json(ROOT/'plugin.json')
    version = manifest['version']
    pyproject = (ROOT/'pyproject.toml').read_text(encoding='utf-8')
    project = re.search(r'^\[project\]\s*(.*?)(?=^\[|\Z)', pyproject, re.M | re.S)
    project_version = re.search(r'^version\s*=\s*["\']([^"\']+)["\']', project[1], re.M) if project else None
    assert project_version and project_version[1] == version, 'pyproject version differs from plugin.json'
    for path in (ROOT/'.codex-plugin/plugin.json', ROOT/'.claude-plugin/plugin.json'):
        assert e.read_json(path)['version'] == version, f'{path} version differs from plugin.json'

    release_checklist = (ROOT/'docs/RELEASE_CHECKLIST.md').read_text(encoding='utf-8')
    assert f'**Active candidate:** package {version}' in release_checklist, 'release checklist candidate is stale'

    test_plan = (ROOT/'docs/TEST_PLAN.md').read_text(encoding='utf-8')
    required_commands = (
        'uv sync --locked --extra dev',
        'uv run --locked --extra dev python scripts/verify.py',
        'pytest --collect-only',
        'coverage run -m pytest',
        'coverage report --fail-under=80',
    )
    for command in required_commands:
        assert command in test_plan, f'test plan is missing canonical command: {command}'
    assert 'coverage run -m unittest' not in test_plan, 'test plan still uses the superseded coverage runner'
    return version

def validate():
    import jsonschema
    schemas={p.stem:json.loads(p.read_text(encoding='utf-8')) for p in (ROOT/'schemas').glob('*.json')}
    for schema in schemas.values():jsonschema.Draft202012Validator.check_schema(schema)
    for p in (ROOT/'schemas/framework-output').glob('*.json'):jsonschema.Draft202012Validator.check_schema(json.loads(p.read_text()))
    package_version=validate_release_metadata()
    manifest=e.read_json(ROOT/'plugin.json')
    jsonschema.validate(manifest,e.read_json(ROOT/'schemas/vendor/plugin.schema.json'))
    assert e.read_json(ROOT/'.claude-plugin/plugin.json')['name']==manifest['name']
    codex_manifest=e.read_json(ROOT/'.codex-plugin/plugin.json')
    assert codex_manifest['version']==manifest['version']
    assert codex_manifest['hooks']=='./hooks/codex/hooks.json'
    assert codex_manifest['extensions']['com.openai']['onboardingSkill']=='./skills/setup/SKILL.md'
    for path in ['onboardingSkill','hooks']:
        value=manifest['extensions']['com.openai'][path];assert value.startswith('./') and (ROOT/value).is_file()
    for path in ['logo','composerIcon']:
        assert (ROOT/manifest['extensions']['com.openai']['interface'][path]).is_file()
    catalog=e.registry()
    for entry in catalog:
        model=e.framework(entry['id'])
        jsonschema.validate(model,schemas['framework.schema'])
        jsonschema.Draft202012Validator.check_schema(model['input_schema'])
        assert (ROOT/model['output_schema']).is_file()
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
    assert not (ROOT/'mcp.json').exists()
    for platform in ['codex','claude']:
        config=e.read_json(ROOT/f'hooks/{platform}/hooks.json')
        assert set(config['hooks'])=={'PostToolUse'}
        handlers=config['hooks']['PostToolUse']
        assert len(handlers)==1 and handlers[0]['matcher']=='Write|Edit|apply_patch'
        assert handlers[0]['hooks'][0]['type']=='command'
        assert handlers[0]['hooks'][0]['timeout']==3
    assert manifest['extensions']['com.openai']['hooks']=='./hooks/codex/hooks.json'
    assert (ROOT/'scripts/check_artifact.py').is_file()
    required=['SOURCE_ANALYSIS','REQUIREMENTS_TRACEABILITY','PLATFORM_COMPATIBILITY','CROSS_HOST_COMPATIBILITY','SELF_IMPROVEMENT','CAPABILITY_AMPLIFICATION','TOKEN_EFFICIENCY','MODEL_COMPATIBILITY','ARCHITECTURE','ARCHITECTURE_DECISIONS','MENTAL_MODEL_REGISTRY','AGENT_REGISTRY','SKILL_SPECIFICATIONS','ORCHESTRATION_DESIGN','DATA_CONTRACTS','MATHEMATICAL_VALIDATION','DECISION_PROVENANCE','MEMORY_ARCHITECTURE','MCP_DECISION','SECURITY_MODEL','PERFORMANCE_EVALUATION','TEST_PLAN','INSTALLATION_CLAUDE','INSTALLATION_CODEX','INSTALLATION_OPENCODE','INSTALLATION_COMMANDCODE','INSTALLATION_OPENCLAW','INSTALLATION_HERMES','USER_GUIDE','TROUBLESHOOTING','RELEASE_CHECKLIST','DEVELOPMENT_ROADMAP']
    for n in required:assert (ROOT/f'docs/{n}.md').is_file(),n
    for platform in ['antigravity','github-copilot','vscode','generic','opencode','commandcode','openclaw','hermes']:
        assert (ROOT/f'adapters/{platform}/README.md').is_file(),platform
    assert e.read_json(ROOT/'openclaw.plugin.json')['skills']==['skills']
    return {'status':'TESTED','package_version':package_version,'full_schema_validator':importlib.metadata.version('jsonschema'),'frameworks':len(catalog),'logical_agents':52,'skills':len(skill_paths),'required_documents':len(required),'note':'Structural validation; native semantic behavior is a separate gate.'}

if __name__=='__main__':print(json.dumps(validate(),indent=2))
