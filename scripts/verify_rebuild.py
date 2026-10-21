"""Record local candidate checks without installing plugins or invoking a model."""
import contextlib
import hashlib
import io
import json
import shutil
import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from package_release import runtime_files
from validate_package import validate


def snapshot():
    return {p.relative_to(ROOT).as_posix(): hashlib.sha256(p.read_bytes()).hexdigest()
            for p in runtime_files()}


def run():
    before = snapshot()
    rebuild = subprocess.run([sys.executable, str(ROOT/'scripts/rebuild_plugin.py')],
                             cwd=ROOT, capture_output=True, text=True)
    reproducible = before == snapshot()
    structural = validate()
    activation = subprocess.run([sys.executable, str(ROOT/'scripts/evaluate_activation.py')],
                                cwd=ROOT, capture_output=True, text=True)
    activation_record = json.loads((ROOT/'docs/evidence/v4-1-activation-evals.json').read_text())
    transcript = io.StringIO()
    with contextlib.redirect_stdout(transcript), contextlib.redirect_stderr(transcript):
        suite = unittest.defaultTestLoader.discover(str(ROOT/'tests'))
        result = unittest.TextTestRunner(stream=transcript, verbosity=2).run(suite)
    claude_path = shutil.which('claude')
    claude = subprocess.run([claude_path, 'plugin', 'validate', '.claude-plugin/plugin.json'],
                            cwd=ROOT, capture_output=True, text=True) if claude_path else None
    sources = json.loads((ROOT/'docs/evidence/sources.json').read_text())
    retired_sources = {
        record['path']: {'absent': not (ROOT/record['path']).exists(),
                         'last_recorded_sha256': record['last_recorded_sha256']}
        for record in sources['removed_files']
    }
    package_version = json.loads((ROOT/'plugin.json').read_text())['version']
    checks = {
        'specification_version': '4.1', 'package_version': package_version,
        'scope': 'Local structural, deterministic and extracted-package execution checks only.',
        'rebuild': {'exit_code': rebuild.returncode, 'runtime_files_unchanged_after_regeneration': reproducible,
                    'runtime_file_count': len(before)},
        'structural_validation': structural,
        'activation_rules': {'exit_code': activation.returncode, 'cases': activation_record['rule_cases'],
                             'passed': activation_record['rule_cases_passed'], 'native_selection': 'NOT_RUN_ON_HOST'},
        'unit_tests': {'run': result.testsRun, 'passed': result.testsRun-len(result.skipped)-len(result.failures)-len(result.errors),
                       'failures': len(result.failures), 'errors': len(result.errors),
                       'skipped': [{'test': str(test), 'reason': reason} for test, reason in result.skipped],
                       'transcript': transcript.getvalue()},
        'claude_manifest_validation': {'exit_code': claude.returncode if claude else None,
                                       'output': (claude.stdout+claude.stderr) if claude else 'Claude CLI unavailable',
                                       'scope': 'Local manifest validation; no installation or inference.'},
        'retired_sources': retired_sources,
        'native_host_acceptance': 'NOT_RUN', 'host_ABCD_benchmark': 'NOT_RUN',
        'host_installation_changed_by_verification': False,
    }
    passed = (rebuild.returncode == 0 and reproducible and activation.returncode == 0
              and result.wasSuccessful() and claude is not None and claude.returncode == 0
              and all(record['absent'] for record in retired_sources.values()))
    checks['local_checks_passed'] = passed
    (ROOT/'docs/evidence/v4-1-checks.json').write_text(json.dumps(checks, indent=2)+'\n', encoding='utf-8')
    print(json.dumps({key: value for key, value in checks.items() if key not in ['unit_tests', 'claude_manifest_validation']}, indent=2))
    print(f'Tests: {result.testsRun}; failures: {len(result.failures)}; errors: {len(result.errors)}; skips: {len(result.skipped)}')
    return passed


if __name__ == '__main__':
    sys.exit(0 if run() else 1)
