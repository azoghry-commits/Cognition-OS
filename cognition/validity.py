"""Bounded, read-only applicability checks using explicit observed facts."""
import json
import math
import hashlib
from collections import deque
from datetime import datetime, timezone
from pathlib import Path, PureWindowsPath
from typing import Any

DEFAULT_MAX_AGE_SECONDS = 86400
MAX_CONDITIONS = 128
MAX_CONTEXT_ITEMS = 512
MAX_INPUT_BYTES = 1000000
PRIORITY = {'applicable': 0, 'unknown': 1, 'needs_review': 2, 'contradicted': 3}


def _timestamp(value):
    if not isinstance(value, str):
        raise ValueError('Timestamp must be an ISO datetime with timezone')
    try:
        result = datetime.fromisoformat(value.replace('Z', '+00:00'))
    except ValueError as error:
        raise ValueError('Invalid timestamp') from error
    if result.tzinfo is None:
        raise ValueError('Timestamp requires timezone')
    try:
        return result.astimezone(timezone.utc)
    except OverflowError as error:
        raise ValueError('Timestamp is outside the UTC datetime range') from error


def _bounded(value):
    try:
        encoded = json.dumps(value, ensure_ascii=False, allow_nan=False)
    except (TypeError, ValueError, RecursionError) as error:
        raise ValueError('Expected bounded finite JSON') from error
    if len(encoded.encode('utf-8')) > MAX_INPUT_BYTES:
        raise ValueError('Input exceeds 1 MB')


def _object(value, allowed, required=()):
    if not isinstance(value, dict) or set(value) - set(allowed) or set(required) - set(value):
        raise ValueError('Invalid object fields')


def _text(value):
    if not isinstance(value, str) or not value.strip() or len(value) > 1024:
        raise ValueError('Expected nonempty text up to 1024 characters')


def _scalar_kind(value):
    if type(value) is bool:
        return 'boolean'
    if type(value) in (int, float):
        try:
            return 'number' if math.isfinite(value) else None
        except OverflowError:
            return None
    if isinstance(value, str):
        return 'string'
    return None


def _age_limit(value):
    if type(value) is not int or not 0 <= value <= 31536000:
        raise ValueError('max_age_seconds must be an integer from 0 to 31536000')


def validate_applicability(applicability):
    """Validate v1 metadata before storage or evaluation; no runtime dependencies."""
    _bounded(applicability)
    _object(applicability, ['schema_version', 'scope', 'conditions', 'evidence_refs', 'review_after',
                            'supersedes', 'limitations'], ['schema_version', 'conditions'])
    if applicability['schema_version'] != '1.0':
        raise ValueError('Unsupported applicability schema version')
    scope = applicability.get('scope', {})
    _object(scope, ['project_id', 'component', 'task_type'])
    for value in scope.values():
        _text(value)
    conditions = applicability['conditions']
    if not isinstance(conditions, list) or not 1 <= len(conditions) <= MAX_CONDITIONS:
        raise ValueError('Expected 1 to 128 conditions')
    ids = set()
    for condition in conditions:
        _object(condition, ['id', 'fact', 'operator', 'expected', 'required', 'max_age_seconds'],
                ['id', 'fact', 'operator', 'expected'])
        for key in ('id', 'fact'):
            _text(condition[key])
        if condition['id'] in ids:
            raise ValueError('Duplicate condition ID')
        ids.add(condition['id'])
        op = condition['operator']
        if op not in ('equals', 'in', 'lt', 'lte', 'gt', 'gte'):
            raise ValueError('Unsupported comparison operator')
        expected = condition['expected']
        if op == 'in':
            if not isinstance(expected, list) or not 1 <= len(expected) <= 128:
                raise ValueError('Membership requires 1 to 128 scalar choices')
            if any(_scalar_kind(item) is None for item in expected):
                raise ValueError('Membership choices must be finite scalars')
        elif op != 'equals' and _scalar_kind(expected) != 'number':
            raise ValueError('Ordering requires a finite number')
        elif expected is not None and _scalar_kind(expected) is None:
            raise ValueError('Expected finite scalar or null')
        if type(condition.get('required', True)) is not bool:
            raise ValueError('required must be boolean')
        _age_limit(condition.get('max_age_seconds', DEFAULT_MAX_AGE_SECONDS))
    evidence = applicability.get('evidence_refs', [])
    if not isinstance(evidence, list) or len(evidence) > 128:
        raise ValueError('Expected at most 128 evidence references')
    evidence_ids = set()
    for ref in evidence:
        _object(ref, ['id', 'fingerprint', 'max_age_seconds'], ['id', 'fingerprint'])
        _text(ref['id'])
        fingerprint = ref['fingerprint']
        if not isinstance(fingerprint, str) or len(fingerprint) != 64 or any(c not in '0123456789abcdef' for c in fingerprint):
            raise ValueError('Expected lowercase SHA-256 fingerprint')
        if ref['id'] in evidence_ids:
            raise ValueError('Duplicate evidence ID')
        evidence_ids.add(ref['id'])
        _age_limit(ref.get('max_age_seconds', DEFAULT_MAX_AGE_SECONDS))
    if 'review_after' in applicability:
        _timestamp(applicability['review_after'])
    if 'supersedes' in applicability:
        _text(applicability['supersedes'])
    if 'limitations' in applicability:
        limitations = applicability['limitations']
        if not isinstance(limitations, list) or len(limitations) > 128:
            raise ValueError('Expected at most 128 limitations')
        for limitation in limitations:
            _text(limitation)


def _observed(item, now, max_age):
    if not isinstance(item, dict):
        return 'missing_observation'
    if not isinstance(item.get('source'), str) or not item['source'].strip():
        return 'missing_source'
    try:
        observed = _timestamp(item.get('observed_at'))
    except ValueError:
        return 'invalid_observed_at'
    age = (now - observed).total_seconds()
    if age < 0:
        return 'future_observation'
    if age > max_age:
        return 'stale_observation'
    return None


def check_memory(record, context, now=None):
    """Return derived status without writing, running tools, or endorsing truth."""
    instant = _timestamp(now) if now is not None else datetime.now(timezone.utc)
    if not isinstance(record, dict) or not isinstance(context, dict):
        raise ValueError('Record and context must be objects')
    _bounded(record)
    # Unusable observed values remain unknown; metadata itself must be finite.
    try:
        context_bytes = json.dumps(context).encode('utf-8')
    except (TypeError, ValueError, RecursionError) as error:
        raise ValueError('Context must contain JSON values') from error
    if len(context_bytes) > MAX_INPUT_BYTES:
        raise ValueError('Context exceeds size limit')
    _object(context, ['scope', 'facts', 'evidence'])
    scope = context.get('scope', {})
    _object(scope, ['project_id', 'component', 'task_type'])
    facts, evidence = context.get('facts', {}), context.get('evidence', {})
    if any(not isinstance(items, dict) or len(items) > MAX_CONTEXT_ITEMS for items in (facts, evidence)):
        raise ValueError('Expected bounded fact and evidence objects')
    result: dict[str, Any] = {'schema_version': '1.0', 'status': 'unknown', 'checked_at': instant.isoformat(),
              'checks': [], 'limitations': [], 'truth_verified': False}
    if 'applicability' not in record:
        result['checks'] = [{'id': 'metadata', 'status': 'unknown', 'reason': 'legacy_without_applicability',
                             'required': True}]
        return result
    metadata = record['applicability']
    validate_applicability(metadata)
    checks = result['checks']

    def add(identifier, status, reason, required=True):
        checks.append({'id': identifier, 'status': status, 'reason': reason, 'required': required})

    for key, expected in metadata.get('scope', {}).items():
        actual = scope.get(key)
        state = 'unknown' if not isinstance(actual, str) else 'applicable' if actual == expected else 'contradicted'
        add('scope:' + key, state, 'scope_' + ('missing' if state == 'unknown' else 'matches' if state == 'applicable' else 'mismatch'))
    for condition in metadata['conditions']:
        observed = facts.get(condition['fact'])
        reason = _observed(observed, instant, condition.get('max_age_seconds', DEFAULT_MAX_AGE_SECONDS))
        required = condition.get('required', True)
        identifier = 'condition:' + condition['id']
        if reason:
            add(identifier, 'unknown', reason, required)
            continue
        actual, expected, op = observed.get('value'), condition['expected'], condition['operator']
        actual_kind = _scalar_kind(actual)
        choices = expected if op == 'in' else [expected]
        if actual_kind is None or not any(_scalar_kind(choice) == actual_kind for choice in choices):
            add(identifier, 'unknown', 'unusable_or_mismatched_type', required)
            continue
        if op in ('equals', 'in'):
            matched = any(_scalar_kind(choice) == actual_kind and actual == choice for choice in choices)
        elif op == 'lt':
            matched = actual < expected
        elif op == 'lte':
            matched = actual <= expected
        elif op == 'gt':
            matched = actual > expected
        else:
            matched = actual >= expected
        add(identifier, 'applicable' if matched else 'contradicted', 'matches' if matched else 'mismatch', required)
    for ref in metadata.get('evidence_refs', []):
        observed = evidence.get(ref['id'])
        reason = _observed(observed, instant, ref.get('max_age_seconds', DEFAULT_MAX_AGE_SECONDS))
        actual = observed.get('fingerprint') if isinstance(observed, dict) else None
        if not reason and (not isinstance(actual, str) or len(actual) != 64 or any(c not in '0123456789abcdef' for c in actual)):
            reason = 'unusable_fingerprint'
        changed = actual != ref['fingerprint']
        add('evidence:' + ref['id'], 'unknown' if reason else 'needs_review' if changed else 'applicable',
            reason or ('fingerprint_changed' if changed else 'fingerprint_matches'))
    if 'review_after' in metadata and instant >= _timestamp(metadata['review_after']):
        add('review_after', 'needs_review', 'review_due')
    required_checks = [check['status'] for check in checks if check['required']]
    result['status'] = max(required_checks, key=lambda state: PRIORITY[state]) if required_checks else 'unknown'
    result['limitations'] = list(metadata.get('limitations', []))
    return result


def decision_impact(nodes, changes, max_results=1000):
    """Propagate explicit changes and missing references through a bounded DAG."""
    _bounded({'nodes': nodes, 'changes': changes})
    if not isinstance(nodes, list) or len(nodes) > 1000:
        raise ValueError('Expected at most 1000 nodes')
    if not isinstance(changes, list) or len(changes) > 1000:
        raise ValueError('Expected at most 1000 changes')
    if type(max_results) is not int or not 1 <= max_results <= 1000:
        raise ValueError('max_results must be from 1 to 1000')
    graph = {}
    edges = 0
    for node in nodes:
        _object(node, ['id', 'kind', 'depends_on'], ['id', 'kind', 'depends_on'])
        _text(node['id'])
        if node['id'] in graph or node['kind'] not in ('evidence', 'assumption', 'decision'):
            raise ValueError('Duplicate node or invalid kind')
        deps = node['depends_on']
        if not isinstance(deps, list) or len(deps) > 1000:
            raise ValueError('Invalid dependencies')
        for dep in deps:
            _text(dep)
        if len(set(deps)) != len(deps):
            raise ValueError('Duplicate dependency')
        edges += len(deps)
        if edges > 4096:
            raise ValueError('Graph exceeds 4096 edges')
        graph[node['id']] = node
    for change in changes:
        _text(change)
    changed = set(changes)
    referenced = {dep for node in nodes for dep in node['depends_on']}
    missing = referenced - set(graph)
    unmapped = changed - (set(graph) | referenced)
    children: dict[str, list[str]] = {key: [] for key in set(graph) | missing}
    indegrees = {}
    causes = {key: ({key} if key in changed else set()) for key in children}
    gaps = {key: ({key} if key in missing else set()) for key in children}
    for key, node in graph.items():
        indegrees[key] = sum(dep in graph for dep in node['depends_on'])
        for dep in node['depends_on']:
            children[dep].append(key)
            if dep in missing:
                causes[key].update(causes[dep])
                gaps[key].add(dep)
    queue = deque(sorted(key for key in graph if indegrees[key] == 0))
    visited = 0
    while queue:
        key = queue.popleft()
        visited += 1
        for child in children[key]:
            causes[child].update(causes[key])
            gaps[child].update(gaps[key])
            indegrees[child] -= 1
            if indegrees[child] == 0:
                queue.append(child)
    if visited != len(graph):
        raise ValueError('Dependency graph contains a cycle')
    decisions = []
    for key in sorted(graph):
        if graph[key]['kind'] == 'decision' and (causes[key] or gaps[key]):
            decisions.append({'id': key, 'status': 'needs_review' if causes[key] else 'unknown',
                              'causes': sorted(causes[key] | gaps[key])})
    omitted = max(0, len(decisions) - max_results)
    return {'schema_version': '1.0', 'decisions': decisions[:max_results],
            'missing_references': sorted(missing), 'unmapped_changes': sorted(unmapped),
            'omitted_decisions': omitted, 'complete': not (missing or unmapped or omitted)}


def snapshot_evidence(workspace, paths, now=None):
    """Hash regular local evidence files; never execute or follow linked paths."""
    _bounded(paths)
    if not isinstance(paths, dict) or len(paths) > 128:
        raise ValueError('Expected up to 128 named relative evidence paths')
    root_path = Path(workspace).absolute()
    # Ancestor aliases of the workspace are resolved once; children must be lexical.
    root = root_path.resolve(strict=True)
    if not root.is_dir():
        raise ValueError('Workspace must be a directory')
    instant = _timestamp(now) if now is not None else datetime.now(timezone.utc)
    evidence: dict[str, Any] = {}
    unavailable = []
    total_bytes = 0
    for identifier, relative in paths.items():
        _text(identifier)
        _text(relative)
        windows = PureWindowsPath(relative)
        path = Path(relative)
        if path.is_absolute() or windows.drive or windows.root or ':' in relative or '..' in windows.parts or '..' in path.parts:
            raise ValueError('Evidence path must remain relative to workspace')
        target = root / path
        for part in (target, *target.parents):
            if part == root:
                break
            if part.is_symlink() or (hasattr(part, 'is_junction') and part.is_junction()):
                raise ValueError('Linked evidence paths are forbidden')
        if not target.resolve().is_relative_to(root):
            raise ValueError('Evidence escapes workspace')
        reason = None
        raw = b''
        try:
            if not target.is_file():
                reason = 'not_regular_file'
            else:
                with target.open('rb') as stream:
                    before = target.stat()
                    raw = stream.read(MAX_INPUT_BYTES + 1)
                    after = target.stat()
                total_bytes += len(raw)
                if len(raw) > MAX_INPUT_BYTES:
                    reason = 'oversized'
                elif (before.st_size, before.st_mtime_ns, before.st_ino) != (after.st_size, after.st_mtime_ns, after.st_ino):
                    reason = 'changed_during_read'
        except OSError:
            reason = 'unreadable'
        if total_bytes > 16000000:
            reason = 'total_read_budget_exhausted'
        if reason:
            unavailable.append({'id': identifier, 'reason': reason})
        else:
            evidence[identifier] = {'fingerprint': hashlib.sha256(raw).hexdigest(),
                                    'source': path.as_posix(), 'observed_at': instant.isoformat()}
        if total_bytes > 16000000:
            break
    omitted = sorted(set(paths) - set(evidence) - {item['id'] for item in unavailable})
    return {'schema_version': '1.0', 'evidence': evidence, 'unavailable': unavailable,
            'omitted_ids': omitted, 'complete': not (unavailable or omitted)}
