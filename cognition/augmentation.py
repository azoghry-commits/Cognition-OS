"""Host-independent V4.1 routing and advisory contracts. No model calls or dispatch."""
import copy
import json
from . import engine as e


def object_schema(required, properties):
    return {'type': 'object', 'required': required, 'properties': properties, 'additionalProperties': False}


TEXT = {'type': 'string', 'minLength': 1}
STRINGS = {'type': 'array', 'items': TEXT, 'maxItems': 100}
FRAMEWORK = {'type': 'string', 'pattern': r'^FW-(0[1-9]|[1-4][0-9]|50)$'}
FRAMEWORKS = {'type': 'array', 'items': FRAMEWORK, 'maxItems': 50, 'uniqueItems': True}
CLAIM_TYPES = ['VERIFIED_FACT', 'SOURCE_SUPPORTED', 'CALCULATED_RESULT', 'SIMULATED_RESULT',
               'ASSUMPTION', 'INFERENCE', 'HYPOTHESIS', 'UNKNOWN']
BUDGET = object_schema([], {name: {'type': 'integer', 'minimum': 0} for name in
                           ['framework_invocations', 'subagent_calls', 'debate_rounds', 'tool_calls', 'computation_ms', 'context_tokens']})
CONTEXT = object_schema(['objective', 'task_type'], {
    'objective': TEXT,
    'task_type': {'enum': ['simple_edit', 'translation', 'formatting', 'arithmetic', 'debugging',
                          'architecture', 'strategic_decision', 'artifact_review', 'documentation',
                          'implementation', 'learning', 'other']},
    'risk': {'enum': ['normal', 'high', 'critical', 'unknown']},
    'complexity': {'enum': ['low', 'medium', 'high', 'unknown']},
    'evidence_sufficiency': {'enum': ['sufficient', 'partial', 'missing', 'contradictory', 'unknown']},
    'capabilities': object_schema([], {k: {'type': 'boolean'} for k in ['skills', 'deterministic_validation', 'deep_advisory']}),
    'augmentation_relevant': {'type': 'boolean'}, 'analysis_sufficient': {'type': 'boolean'},
    'required_validation': {'type': 'boolean'}, 'deep_requested': {'type': 'boolean'},
    'requested_frameworks': FRAMEWORKS, 'completed_frameworks': FRAMEWORKS,
    'budget': BUDGET, 'constraints': STRINGS, 'relevant_artifacts': STRINGS})
REQUEST = object_schema(['specification_version', 'request_id', 'host_id', 'agent_role', 'task_context',
                         'capability', 'evidence_references', 'constraints', 'authorization_scope'], {
    'specification_version': {'const': '4.1'}, 'request_id': TEXT, 'host_id': TEXT, 'agent_role': TEXT,
    'task_context': CONTEXT, 'capability': TEXT, 'evidence_references': STRINGS,
    'constraints': STRINGS, 'authorization_scope': STRINGS})
CLAIM = object_schema(['id', 'text', 'classification', 'evidence_ids'], {
    'id': TEXT, 'text': TEXT, 'classification': {'enum': CLAIM_TYPES}, 'evidence_ids': STRINGS})
RESULT = object_schema(['specification_version', 'artifact_type', 'request_id', 'status', 'findings',
                        'supporting_evidence', 'issues', 'computed_results', 'recommendations',
                        'confidence_limitations', 'unresolved_questions', 'follow_up_checks', 'provenance'], {
    'specification_version': {'const': '4.1'}, 'artifact_type': {'const': 'advisory_result'},
    'request_id': TEXT, 'status': {'enum': ['COMPLETED', 'PARTIAL', 'BLOCKED', 'FAILED']},
    'findings': {'type': 'array', 'items': CLAIM, 'maxItems': 50},
    'supporting_evidence': {'type': 'array', 'items': e.read_json(e.ROOT/'schemas/evidence.schema.json'), 'maxItems': 100},
    'issues': STRINGS, 'computed_results': {'type': 'array', 'items': object_schema(
        ['operation', 'inputs', 'method', 'result', 'unit', 'evidence_ids'],
        {'operation': TEXT, 'inputs': {'type': 'object'}, 'method': TEXT, 'result': {}, 'unit': TEXT, 'evidence_ids': STRINGS}), 'maxItems': 50},
    'recommendations': STRINGS, 'confidence_limitations': STRINGS, 'unresolved_questions': STRINGS,
    'follow_up_checks': STRINGS, 'provenance': {'type': 'array', 'items': object_schema(
        ['claim_id', 'origin_classification', 'agent_id', 'trace_id'],
        {'claim_id': TEXT, 'origin_classification': TEXT, 'agent_id': TEXT, 'trace_id': TEXT}), 'maxItems': 50}})
SCHEMAS = {'task-context': CONTEXT, 'cognitive-request': REQUEST, 'advisory-result': RESULT}


def check(value, schema):
    # Reject nonfinite/oversized data before bounded schema traversal; no default=str coercion.
    if len(json.dumps(value, allow_nan=False, ensure_ascii=True)) > 262144:
        raise ValueError('Advisory input exceeds 256 KiB serialized limit')
    errors = e.validate_schema(value, schema)
    if errors:
        raise ValueError('; '.join(errors[:12]))


def assess(context):
    """A disclosed policy suggestion from host-supplied context, never executed reasoning."""
    check(context, CONTEXT)
    policy = e.read_json(e.ROOT/'cognitive-core/augmentation/policy.json')
    budget = policy['default_budget'] | context.get('budget', {})
    caps = context.get('capabilities', {})
    requested = context.get('requested_frameworks', [])
    response = {'specification_version': '4.1', 'status': 'PLANNED', 'policy': 'PASS_THROUGH',
                'paths': [], 'frameworks': [], 'requested_frameworks': requested.copy(), 'budget': budget,
                'subagent_calls': 0, 'requires_host_execution': True,
                'reason': '', 'limitations': [], 'deliverable_policy': 'Preserve the original user objective, constraints and output format.',
                'routing_method': 'Explicit host context and configurable rules; no learned classifier or numerical confidence.'}

    if context.get('required_validation') and not caps.get('deterministic_validation'):
        response.update(status='BLOCKED', policy='DEGRADED', reason='Required validation is unavailable.')
        response['limitations'].append('A required check cannot silently fail open; host policy remains authoritative.')
        return response
    validation = bool(caps.get('deterministic_validation') and
                      (context.get('required_validation') or context['task_type'] == 'artifact_review' or context.get('relevant_artifacts')))
    if context.get('augmentation_relevant') is False or context.get('analysis_sufficient'):
        if not context.get('required_validation'):
            response['reason'] = 'Host reports no incremental analytical value.'
            return response
    task = context['task_type']
    relevant = bool(requested or task in policy['routes'] or context.get('deep_requested') or validation)
    if not relevant:
        response['reason'] = 'No narrowly justified capability; continue the host task.'
        return response
    if not budget['tool_calls'] or not budget['computation_ms'] or budget['context_tokens'] < policy['minimum_context_allowance']:
        response.update(status='BLOCKED', policy='DEGRADED', reason='Remaining execution allowance is insufficient.')
        response['limitations'].append('Return partial work and material gaps; budget exhaustion is not verification.')
        return response
    frames = requested.copy() if requested else policy['routes'].get(task, []).copy()
    if context.get('analysis_sufficient') or context.get('augmentation_relevant') is False:
        frames = []
    # IDs are schema validated, so the rule-based default does not need to load the registry.
    frames = [f for f in frames if f not in context.get('completed_frameworks', [])]
    if not caps.get('skills'):
        frames = []
    if frames and len(frames) > budget['framework_invocations']:
        response.update(status='BLOCKED', policy='DEGRADED', reason='Framework selection exceeds the remaining allowance.')
        response['limitations'].append('Selection was not silently truncated; host must narrow scope or authorize a larger allowance.')
        return response
    if frames:
        response['paths'].append('MODEL_SELECTED')
        response['frameworks'] = frames
    if validation:
        response['paths'].append('DETERMINISTIC')
    deep_justified = bool(context.get('deep_requested') or context.get('complexity') == 'high' or
                          context.get('risk') in ['high', 'critical'] or context.get('evidence_sufficiency') == 'contradictory')
    if frames and deep_justified and caps.get('deep_advisory') and budget['debate_rounds'] > 0:
        response['paths'].append('DEEP_ADVISORY')
    elif deep_justified:
        response['limitations'].append('Deep advisory unavailable or outside allowance; critical gaps remain visible.')
    if not response['paths']:
        response['policy'] = 'DEGRADED' if not caps.get('skills') else 'PASS_THROUGH'
    elif context.get('risk') == 'critical':
        response['policy'] = 'CRITICAL_REVIEW'
    elif 'DEEP_ADVISORY' in response['paths']:
        response['policy'] = 'DEEP_ADVISORY'
    elif frames:
        response['policy'] = 'LIGHT_AUGMENTATION' if len(frames) == 1 else 'STANDARD_AUGMENTATION'
    else:
        response['policy'] = 'DETERMINISTIC_VALIDATION'
    response['reason'] = 'Use only capabilities justified by the supplied task context; host may revise this suggestion.'
    return response


def deep_plan(context):
    routing = assess(context)
    steps = []
    if routing['status'] == 'PLANNED' and 'DEEP_ADVISORY' in routing['paths']:
        steps = [{'logical_role': 'AG-51', 'task': 'Define one analytical question and material evidence gaps.'},
                 *[{'logical_role': 'AG-'+f[3:], 'framework_id': f, 'task': 'Apply the canonical methodology to supplied evidence.'}
                   for f in routing['frameworks']],
                 {'logical_role': 'AG-51', 'perspective': 'Constructive Advocate', 'task': 'Present the strongest supported option using existing findings; no additional framework run is implied.'},
                 {'logical_role': 'AG-49', 'perspective': 'Critical Challenger', 'task': 'Challenge major assumptions and failure conditions using existing findings; retain contrary evidence.'},
                 {'logical_role': 'AG-52', 'task': 'Evaluate advocate and challenger findings; retain disagreement and insufficient evidence.'}]
    return routing | {'steps': steps, 'max_rebuttal_rounds': routing['budget']['debate_rounds'] if steps else 0,
                      'stop_when': ['question answered', 'missing essential evidence', 'budget exhausted', 'no incremental value'],
                      'execution': 'PLANNED_SEQUENTIAL_HOST_ROLES; no native dispatch has occurred'}


def review_advisory(request, result):
    try:
        check(request, REQUEST); check(result, RESULT)
        if request['request_id'] != result['request_id']:
            raise ValueError('Request identity mismatch')
        evidence = result['supporting_evidence']
        evidence_schema = e.read_json(e.ROOT/'schemas/evidence.schema.json')
        for record in evidence:
            check(record, evidence_schema)
        allowed = set(request['evidence_references'])
        if any(record['id'] not in allowed for record in evidence):
            raise ValueError('Evidence outside request references; update the host request explicitly')
        if len({record['id'] for record in evidence}) != len(evidence):
            raise ValueError('Duplicate evidence identifiers')
        claim_ids = [finding['id'] for finding in result['findings']]
        if len(set(claim_ids)) != len(claim_ids):
            raise ValueError('Duplicate finding identifiers')
        for computation in result['computed_results']:
            refs = computation['evidence_ids']
            records = [record for record in evidence if record['id'] in refs]
            if not refs or len(records) != len(set(refs)) or not any(
                    record['kind'] in ['calculation', 'simulation'] and
                    record.get('inputs') == computation['inputs'] and record.get('method') == computation['method'] and
                    record.get('result') == computation['result'] for record in records):
                raise ValueError('Computed result does not match a linked calculation record')
        if any(item['claim_id'] not in claim_ids for item in result['provenance']):
            raise ValueError('Provenance refers to an absent finding')
        for finding in result['findings']:
            kind = finding['classification']
            refs = finding['evidence_ids']
            if kind in ['ASSUMPTION', 'HYPOTHESIS', 'UNKNOWN'] and not refs:
                continue
            if kind == 'CALCULATED_RESULT' and not any(record['id'] in refs and record['kind'] == 'calculation' for record in evidence):
                raise ValueError('Calculated claim requires calculation evidence')
            if kind == 'SIMULATED_RESULT':
                matches = [record for record in evidence if record['id'] in refs]
                if not matches or not all(record.get('kind') == 'simulation' and
                        isinstance(record.get('inputs'), dict) and 'seed' in record['inputs'] for record in matches):
                    raise ValueError('Simulation claim needs simulation evidence with reproducibility inputs')
            legacy = copy.deepcopy(finding)
            legacy['classification'] = {'ASSUMPTION': 'USER_ASSUMPTION', 'INFERENCE': 'MODEL_INFERENCE'}.get(kind, kind)
            if e.audit_evidence([legacy], evidence)['gaps']:
                raise ValueError('Finding lacks the required evidence or verification record')
        if result['status'] == 'COMPLETED' and (result['unresolved_questions'] or any(f['classification'] == 'UNKNOWN' for f in result['findings'])):
            raise ValueError('Unresolved questions or UNKNOWN findings require PARTIAL status')
        return {'status': 'STRUCTURALLY_VALID', 'semantic_status': 'Host review required; structure and link checks do not prove truth.'}
    except (ValueError, TypeError, KeyError, OverflowError, RecursionError) as error:
        return {'status': 'BLOCKED', 'issues': [str(error)], 'semantic_status': 'Not verified'}


def normalize_legacy(envelope, request_id):
    check(envelope, e.read_json(e.ROOT/'schemas/agent-envelope.schema.json'))
    check(request_id, TEXT)
    findings = copy.deepcopy(envelope['claims'])
    for finding in findings:
        finding.pop('material', None)
        finding['classification'] = {'USER_ASSUMPTION': 'ASSUMPTION', 'MODEL_INFERENCE': 'INFERENCE'}.get(finding['classification'], finding['classification'])
    return {'specification_version': '4.1', 'artifact_type': 'advisory_result', 'request_id': request_id,
            'status': envelope['status'], 'findings': findings, 'supporting_evidence': [], 'issues': envelope['gaps'].copy(),
            'computed_results': [], 'recommendations': [], 'confidence_limitations': ['Legacy conversion preserves assertions; evidence must be supplied and reviewed.'],
            'unresolved_questions': envelope['gaps'].copy(), 'follow_up_checks': [],
            'provenance': [{'claim_id': c['id'], 'origin_classification': c['classification'],
                            'agent_id': envelope['agent_id'], 'trace_id': envelope['trace_id']} for c in envelope['claims']]}
