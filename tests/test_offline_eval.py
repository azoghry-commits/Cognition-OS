import hashlib
import json
import tempfile
import subprocess
import sys
import unittest
import zipfile
from pathlib import Path
from unittest.mock import patch

from scripts import audit_context_host as audit

ROOT = Path(__file__).resolve().parents[1]
ARCHIVE = ROOT / 'docs/evidence/context-validity-native-v2-2026-10-24.zip'
COHORT = 'heldout-batched-v2-corrected-20261024'


class OfflineAuditTests(unittest.TestCase):
    def test_printed_helper_text_is_not_execution_evidence(self):
        payload = {'record': {'title': 'Legacy'}, 'context': {}, 'now': '2026-10-23T12:00:00Z'}
        encoded = (json.dumps(payload, indent=2, allow_nan=False) + '\n').encode()
        fake = {'evaluation_input': payload, 'input_sha256': hashlib.sha256(encoded).hexdigest(),
                'commands': [{'exit_code': 0,
                              'command': 'Write-Output "; python .agents/scripts/cognition.py memory-check --input input.json"',
                              'aggregated_output': '{"schema_version":"1.0","status":"unknown",'
                                                   '"checks":[],"truth_verified":false}'}]}
        self.assertEqual(audit._captured_evidence(fake),
                         {'helper_executed': False, 'workspace_read_observed': False})

    def test_cli_fingerprints_do_not_grant_or_rewrite_historical_approval(self):
        suite = ROOT / 'tests/native-evals/context-validity-v2'
        before = (suite / 'human-review.json').read_bytes()
        run = subprocess.run([sys.executable, str(ROOT / 'scripts/audit_context_host.py'),
                              'fingerprints', '--fixtures', str(suite)], capture_output=True, text=True)
        self.assertEqual(run.returncode, 0, run.stderr)
        self.assertEqual(set(json.loads(run.stdout)), {'hash_scheme', 'cases_sha256', 'labels_sha256'})
        self.assertEqual((suite / 'human-review.json').read_bytes(), before)

    def verify(self, path=ARCHIVE):
        return audit.audit_archive(path, hashlib.sha256(path.read_bytes()).hexdigest(), COHORT)

    def variant(self, change):
        folder = tempfile.TemporaryDirectory()
        self.addCleanup(folder.cleanup)
        path = Path(folder.name) / 'changed.zip'
        with zipfile.ZipFile(ARCHIVE) as source:
            entries = {row.filename: source.read(row) for row in source.infolist()}
        change(entries)
        with zipfile.ZipFile(path, 'w', zipfile.ZIP_DEFLATED) as output:
            for name, raw in entries.items():
                output.writestr(name, raw)
        return path

    def test_real_v2_archive_replays_offline_without_promoting_legacy_approval(self):
        with (patch('subprocess.run', side_effect=AssertionError('No external commands during audit')),
              patch('scripts.evaluate_context_host.check_memory',
                    side_effect=AssertionError('No current checker during audit'))):
            result = self.verify()
        self.assertEqual(result['status'], 'VERIFIED')
        self.assertTrue(result['summary_matches_recorded'])
        self.assertEqual(result['summary']['paired_cases'], 20)
        self.assertEqual(result['summary']['candidate']['helper_executions'], 20)
        self.assertTrue(result['summary']['acceptance_passed'])
        self.assertEqual(result['approval_binding'], 'LEGACY_UNBOUND')
        self.assertFalse(result['new_collection_approved'])
        self.assertFalse(result['local_checker_matches_frozen'])
        self.assertRegex(result['frozen_checker_sha256'], r'^[0-9a-f]{64}$')

    def test_external_checksum_is_required_to_match(self):
        with self.assertRaisesRegex(ValueError, 'checksum'):
            audit.audit_archive(ARCHIVE, '0' * 64, COHORT)

    def test_changed_frozen_input_is_rejected_even_with_new_archive_checksum(self):
        name = COHORT + '/suite-frozen/cases.json'
        path = self.variant(lambda entries: entries.__setitem__(name, entries[name] + b' '))
        with self.assertRaisesRegex(ValueError, 'Frozen'):
            self.verify(path)

    def test_missing_raw_events_are_rejected(self):
        name = COHORT + '/CV2-11-candidate/events.jsonl'
        path = self.variant(lambda entries: entries.pop(name))
        with self.assertRaisesRegex(ValueError, 'Missing'):
            self.verify(path)

    def test_response_must_match_collected_record(self):
        name = COHORT + '/CV2-11-candidate/response.json'
        path = self.variant(lambda entries: entries.__setitem__(name, b'{"case_id":"forged"}'))
        with self.assertRaisesRegex(ValueError, 'Response'):
            self.verify(path)

    def test_scored_response_must_match_final_raw_agent_message(self):
        name = COHORT + '/CV2-11-candidate/events.jsonl'
        def forge_final_message(entries):
            events = [json.loads(line) for line in entries[name].splitlines() if line.strip()]
            messages = [event for event in events
                        if event.get('type') == 'item.completed'
                        and event.get('item', {}).get('type') == 'agent_message']
            forged = json.loads(messages[-1]['item']['text'])
            forged.update(status='applicable', reuse_allowed=True, review_required=False)
            messages[-1]['item']['text'] = json.dumps(forged)
            entries[name] = ('\n'.join(json.dumps(event) for event in events) + '\n').encode()
        with self.assertRaisesRegex(ValueError, 'Final agent response'):
            self.verify(self.variant(forge_final_message))

    def test_duplicate_runs_and_incomplete_events_are_rejected(self):
        def duplicate(entries):
            name = COHORT + '/collected-runs.json'
            runs = json.loads(entries[name])
            runs['baseline'].append(runs['baseline'][0])
            entries[name] = json.dumps(runs).encode()
        with self.assertRaisesRegex(ValueError, 'unique'):
            self.verify(self.variant(duplicate))
        def incomplete(entries):
            name = COHORT + '/CV2-11-candidate/events.jsonl'
            entries[name] = b'\n'.join(line for line in entries[name].splitlines()
                                          if b'turn.completed' not in line)
        with self.assertRaisesRegex(ValueError, 'Trace|complete'):
            self.verify(self.variant(incomplete))

    def test_unsafe_names_and_oversized_archives_are_rejected(self):
        path = self.variant(lambda entries: entries.__setitem__('../escape', b'untrusted'))
        with self.assertRaisesRegex(ValueError, 'Unsafe'):
            self.verify(path)
        with patch.object(audit, 'MAX_TOTAL_BYTES', 1):
            with self.assertRaisesRegex(ValueError, 'size'):
                self.verify()
