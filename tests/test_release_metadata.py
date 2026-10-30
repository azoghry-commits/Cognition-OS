import json
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from scripts import validate_package


class ReleaseMetadataTests(unittest.TestCase):
    def test_active_version_and_test_commands_share_one_contract(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            (root/'.codex-plugin').mkdir()
            (root/'.claude-plugin').mkdir()
            for path in ('plugin.json', '.codex-plugin/plugin.json', '.claude-plugin/plugin.json'):
                (root/path).write_text(json.dumps({'version': '0.5.0'}), encoding='utf-8')
            (root/'pyproject.toml').write_text('[project]\nversion = "0.5.0"\n', encoding='utf-8')
            (root/'docs').mkdir()
            (root/'docs/RELEASE_CHECKLIST.md').write_text(
                '**Active candidate:** package 0.5.0 engineering candidate toward 0.6.0.\n',
                encoding='utf-8',
            )
            (root/'docs/TEST_PLAN.md').write_text(
                '\n'.join((
                    'uv sync --locked --extra dev',
                    'uv run --locked --extra dev python scripts/verify.py',
                    'pytest --collect-only',
                    'coverage run -m pytest',
                    'coverage report --fail-under=80',
                )),
                encoding='utf-8',
            )
            with patch.object(validate_package, 'ROOT', root):
                self.assertEqual(validate_package.validate_release_metadata(), '0.5.0')

    def test_stale_release_candidate_is_rejected(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            (root/'.codex-plugin').mkdir()
            (root/'.claude-plugin').mkdir()
            for path in ('plugin.json', '.codex-plugin/plugin.json', '.claude-plugin/plugin.json'):
                (root/path).write_text(json.dumps({'version': '0.5.0'}), encoding='utf-8')
            (root/'pyproject.toml').write_text('[project]\nversion = "0.5.0"\n', encoding='utf-8')
            (root/'docs').mkdir()
            (root/'docs/RELEASE_CHECKLIST.md').write_text(
                '**Active candidate:** package 0.2.0.\n', encoding='utf-8'
            )
            (root/'docs/TEST_PLAN.md').write_text(
                'uv sync --locked --extra dev\n'
                'uv run --locked --extra dev python scripts/verify.py\n'
                'pytest --collect-only\ncoverage run -m pytest\ncoverage report --fail-under=80\n',
                encoding='utf-8',
            )
            with patch.object(validate_package, 'ROOT', root):
                with self.assertRaisesRegex(AssertionError, 'release checklist candidate is stale'):
                    validate_package.validate_release_metadata()
