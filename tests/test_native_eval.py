import json
import hashlib
import tempfile
import unittest
from pathlib import Path

from scripts import evaluate_context_host as host

EVAL_INPUT = {'record': {'title': 'Legacy'}, 'context': {}, 'now': '2026-10-23T12:00:00Z'}
HELPER_RESULT = {'schema_version': '1.0', 'status': 'unknown', 'checked_at': '2026-10-23T12:00:00+00:00',
                 'checks': [{'id': 'metadata', 'status': 'unknown', 'reason': 'legacy_without_applicability',
                             'required': True}], 'limitations': [], 'truth_verified': False}


class HostEvalTests(unittest.TestCase):
    def test_evaluation_command_pins_efficient_model_and_avoids_app_catalog(self):
        command = host.host_command('codex', 'workspace', 'schema.json', 'response.json')
        self.assertEqual(command[command.index('--model') + 1], 'gpt-5.6-luna')
        disabled = [command[i + 1] for i, value in enumerate(command[:-1]) if value == '--disable']
        self.assertTrue({'apps', 'plugins', 'memories', 'multi_agent'} <= set(disabled))
        self.assertIn('--approve-for-me', command)
        self.assertNotIn('--dangerously-bypass-approvals-and-sandbox', command)

    def test_grading_uses_real_output_not_claimed_self_score(self):
        label = {'status': 'unknown', 'reuse_allowed': False, 'review_required': True}
        good = {'case_id': 'CV-01', **label, 'reason': 'Missing observation'}
        self.assertEqual(host.grade_response('CV-01', good, label)['score'], 1.0)
        bad = {**good, 'status': 'applicable', 'reuse_allowed': True, 'review_required': False, 'score': 1.0}
        self.assertEqual(host.grade_response('CV-01', bad, label)['score'], 0.0)
        self.assertEqual(host.grade_response('wrong', good, label)['score'], 0.0)
        self.assertEqual(host.grade_response('CV-01', {'status': 'unknown'}, label)['score'], 0.0)

    def test_trace_parser_preserves_calls_and_observed_usage(self):
        events = '\n'.join(json.dumps(item) for item in [
            {'type': 'thread.started', 'thread_id': 'observed-thread'},
            {'type': 'item.completed', 'item': {'type': 'command_execution', 'id': 'tool-1',
                                               'command': 'python .agents/scripts/cognition.py memory-check --input input.json',
                                               'exit_code': 0, 'aggregated_output': json.dumps(HELPER_RESULT)}},
            {'type': 'turn.completed', 'usage': {'input_tokens': 40, 'output_tokens': 10}}])
        result = host.parse_trace(events, evaluation_input=EVAL_INPUT)
        self.assertEqual(result['thread_id'], 'observed-thread')
        self.assertEqual(result['usage']['input_tokens'], 40)
        self.assertEqual(result['commands'][0]['id'], 'tool-1')
        self.assertTrue(result['helper_executed'])
        self.assertIsNone(host.parse_trace('')['usage'])
        self.assertFalse(host.parse_trace(json.dumps({'type': 'turn.failed', 'error': {'message': 'unsupported'}}))['completed'])

    def test_fabricated_output_after_helper_is_rejected(self):
        event = {'type': 'item.completed', 'item': {'type': 'command_execution', 'exit_code': 0,
                 'command': 'python .agents/scripts/cognition.py memory-check --input input.json; echo fabricated',
                 'aggregated_output': json.dumps(HELPER_RESULT)}}
        self.assertFalse(host.parse_trace(json.dumps(event), evaluation_input=EVAL_INPUT)['helper_executed'])

    def test_filename_echo_is_not_an_observed_read(self):
        event = {'type': 'item.completed', 'item': {'type': 'command_execution', 'exit_code': 0,
                 'command': 'echo input.json', 'aggregated_output': json.dumps(EVAL_INPUT)}}
        self.assertFalse(host.parse_trace(json.dumps(event), evaluation_input=EVAL_INPUT)['workspace_read_observed'])

    def test_successful_read_is_bound_to_fixture_content(self):
        event = {'type': 'item.completed', 'item': {'type': 'command_execution', 'exit_code': 0,
                 'command': 'Get-Content -Raw input.json', 'aggregated_output': json.dumps(EVAL_INPUT)}}
        self.assertTrue(host.parse_trace(json.dumps(event), evaluation_input=EVAL_INPUT)['workspace_read_observed'])
        other = {**EVAL_INPUT, 'record': {'title': 'Different'}}
        self.assertFalse(host.parse_trace(json.dumps(event), evaluation_input=other)['workspace_read_observed'])

    def test_run_evidence_requires_matching_input_hash(self):
        raw = (json.dumps(EVAL_INPUT, indent=2) + '\n').encode()
        run = {'evaluation_input': EVAL_INPUT, 'input_sha256': hashlib.sha256(raw).hexdigest(),
               'commands': [{'command': 'python .agents/scripts/cognition.py memory-check --input input.json',
                             'exit_code': 0, 'aggregated_output': json.dumps(HELPER_RESULT)}]}
        self.assertTrue(host.bound_run_evidence(run)['helper_executed'])
        run['input_sha256'] = hashlib.sha256(raw.replace(b'\n', b'\r\n')).hexdigest()
        self.assertTrue(host.bound_run_evidence(run)['helper_executed'])
        run['input_sha256'] = '0' * 64
        self.assertFalse(host.bound_run_evidence(run)['helper_executed'])

    def test_echoed_helper_name_is_not_execution_evidence(self):
        event = {'type': 'item.completed', 'item': {'type': 'command_execution', 'exit_code': 0,
                 'command': 'echo memory-check', 'aggregated_output': 'memory-check'}}
        self.assertFalse(host.parse_trace(json.dumps(event))['helper_executed'])

    def test_declined_workspace_read_cannot_pass_execution_gate(self):
        label = {'case_id': 'CV-01', 'status': 'unknown', 'reuse_allowed': False,
                 'review_required': True, 'negative_control': False}
        run = {'case_id': 'CV-01', 'returncode': 0, 'completed': True, 'seconds': 1,
               'response': {**label, 'reason': 'Missing evidence'}, 'critical_error': False,
               'helper_executed': True, 'commands': [{'command': 'Get-Content input.json',
                                                      'status': 'declined', 'exit_code': None}]}
        result = host.summarize([run], [run], [label], human_reviewed=True)
        self.assertFalse(result['gates']['workspace_reads_observed'])

    def test_invalid_response_counts_as_execution_error(self):
        label = {'case_id': 'CV-01', 'status': 'unknown', 'reuse_allowed': False,
                 'review_required': True, 'negative_control': False}
        run = {'case_id': 'CV-01', 'returncode': 0, 'completed': True, 'seconds': 1,
               'response': None, 'critical_error': False, 'helper_executed': True}
        result = host.summarize([run], [run], [label], human_reviewed=True)
        self.assertEqual(result['candidate']['execution_errors'], 1)

    def test_frozen_manifest_detects_tampered_fixture(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            fixture = root / 'cases.json'
            fixture.write_text('{"cases": []}')
            manifest = host.freeze_inputs([fixture], source_sha='abc')
            host.verify_frozen(manifest)
            fixture.write_text('{"cases": [1]}')
            with self.assertRaises(ValueError):
                host.verify_frozen(manifest)

    def test_summary_does_not_pass_acceptance_without_human_labels(self):
        label = {'case_id': 'CV-01', 'status': 'applicable', 'reuse_allowed': True,
                 'review_required': False, 'negative_control': True}
        run = {'case_id': 'CV-01', 'returncode': 0, 'response': {'case_id': 'CV-01', **label, 'reason': 'Conditions match'},
               'seconds': 1.0, 'completed': True, 'critical_error': False, 'helper_executed': True}
        result = host.summarize([run], [run], [label], human_reviewed=False)
        self.assertEqual(result['candidate']['false_positive_rate'], 0.0)
        self.assertEqual(result['candidate']['precision'], None)
        self.assertFalse(result['acceptance_passed'])
        self.assertFalse(result['gates']['human_labels_reviewed'])
        self.assertFalse(result['gates']['enough_pairs'])

    def test_completed_answer_without_helper_is_not_native_candidate_acceptance(self):
        labels = [{'case_id': f'CV-{i:02d}', 'status': 'unknown' if i < 10 else 'applicable',
                   'reuse_allowed': i >= 10, 'review_required': i < 10, 'negative_control': i >= 10}
                  for i in range(20)]
        baseline = [{'case_id': label['case_id'], 'returncode': 0, 'completed': True,
                     'response': {**label, 'reason': 'Observed result'}, 'seconds': 1,
                     'helper_executed': False, 'critical_error': False} for label in labels]
        result = host.summarize(baseline, baseline, labels, human_reviewed=True)
        self.assertFalse(result['acceptance_passed'])
        self.assertFalse(result['gates']['candidate_helper_observed'])
