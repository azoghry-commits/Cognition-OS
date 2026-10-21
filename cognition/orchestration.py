"""Build deterministic execution waves for host-run analytical work."""

from collections import deque


STRATEGIES = {"AUTO", "SEQUENTIAL", "PARALLEL", "HYBRID"}


def _validate_steps(steps):
    if not isinstance(steps, list) or not steps:
        raise ValueError("At least one analysis step is required")
    if len(steps) > 50:
        raise ValueError("Analysis plan exceeds 50 steps")
    identifiers = []
    for step in steps:
        if not isinstance(step, dict) or not isinstance(step.get("step_id"), str) or not step["step_id"]:
            raise ValueError("Every step requires a nonempty step_id")
        if not isinstance(step.get("depends_on", []), list):
            raise ValueError("depends_on must be an array")
        identifiers.append(step["step_id"])
    if len(identifiers) != len(set(identifiers)):
        raise ValueError("Duplicate analysis step")
    known = set(identifiers)
    for step in steps:
        if step["step_id"] in step.get("depends_on", []):
            raise ValueError("A step cannot depend on itself")
        if any(dependency not in known for dependency in step.get("depends_on", [])):
            raise ValueError("Unknown analysis dependency")
    return identifiers


def _topological_waves(steps):
    identifiers = _validate_steps(steps)
    position = {identifier: index for index, identifier in enumerate(identifiers)}
    indegree = {identifier: 0 for identifier in identifiers}
    children = {identifier: [] for identifier in identifiers}
    for step in steps:
        for dependency in step.get("depends_on", []):
            indegree[step["step_id"]] += 1
            children[dependency].append(step["step_id"])
    ready = deque(identifier for identifier in identifiers if indegree[identifier] == 0)
    waves = []
    completed = 0
    while ready:
        wave = sorted(list(ready), key=position.get)
        ready.clear()
        waves.append(wave)
        completed += len(wave)
        next_ready = []
        for identifier in wave:
            for child in children[identifier]:
                indegree[child] -= 1
                if indegree[child] == 0:
                    next_ready.append(child)
        ready.extend(sorted(next_ready, key=position.get))
    if completed != len(identifiers):
        raise ValueError("Cyclic analysis dependency")
    return waves


def plan_execution(steps, strategy="AUTO", host_parallel=False, max_concurrency=1):
    """Return dependency-safe execution waves without dispatching any work."""
    if strategy not in STRATEGIES:
        raise ValueError("Unknown execution strategy")
    if isinstance(max_concurrency, bool) or not isinstance(max_concurrency, int) or not 1 <= max_concurrency <= 16:
        raise ValueError("max_concurrency must be an integer from 1 to 16")
    dependency_waves = _topological_waves(steps)
    has_independent_work = any(len(wave) > 1 for wave in dependency_waves)
    parallel_available = bool(host_parallel and max_concurrency > 1)
    requested_parallel = strategy in {"AUTO", "PARALLEL", "HYBRID"}
    parallel_enabled = requested_parallel and parallel_available and has_independent_work
    limitations = []
    if strategy == "PARALLEL" and not parallel_available:
        limitations.append("Parallel execution requested but the host capability or concurrency allowance is unavailable; use sequential fallback.")

    if strategy == "SEQUENTIAL" or not parallel_enabled:
        waves = [[identifier] for wave in dependency_waves for identifier in wave]
        resolved = "SEQUENTIAL"
    else:
        waves = []
        for dependency_wave in dependency_waves:
            for start in range(0, len(dependency_wave), max_concurrency):
                waves.append(dependency_wave[start:start + max_concurrency])
        resolved = "PARALLEL" if len(dependency_waves) == 1 else "HYBRID"

    step_index = {step["step_id"]: step for step in steps}
    return {
        "status": "PLANNED",
        "requested_strategy": strategy,
        "resolved_strategy": resolved,
        "host_parallel": bool(host_parallel),
        "max_concurrency": max_concurrency,
        "waves": [
            {
                "wave": index + 1,
                "execution": "PARALLEL" if len(identifiers) > 1 else "SEQUENTIAL",
                "steps": [step_index[identifier] for identifier in identifiers],
            }
            for index, identifiers in enumerate(waves)
        ],
        "limitations": limitations,
        "dispatch_policy": "The host may dispatch steps in the same wave concurrently. Start the next wave only after every dependency result is available and validated.",
        "native_dispatch_performed": False,
    }
