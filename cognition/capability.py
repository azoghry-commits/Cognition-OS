"""Tier-adaptive capability amplification and paired evaluation."""

import json
import math

from .orchestration import plan_execution
from .log import debug


TIERS = {"constrained", "balanced", "advanced", "unknown"}
COMPLEXITIES = {"low", "medium", "high", "unknown"}
RISKS = {"normal", "high", "critical", "unknown"}
TOOL_NAMES = {"retrieval", "calculator", "code_execution", "deterministic_validation", "delegation"}


def _bounded(value, label):
    try:
        encoded = json.dumps(value, ensure_ascii=True, allow_nan=False)
    except (TypeError, ValueError) as error:
        raise ValueError(f"Invalid {label}: {error}") from error
    if len(encoded) > 262144:
        raise ValueError(f"{label} exceeds 256 KiB")


def _profile(profile):
    _bounded(profile, "capability profile")
    if not isinstance(profile, dict):
        raise ValueError("Capability profile must be an object")
    tier = profile.get("capability_tier")
    if tier not in TIERS:
        raise ValueError("Unknown capability tier")
    context_tokens = profile.get("context_tokens")
    if isinstance(context_tokens, bool) or not isinstance(context_tokens, int) or context_tokens < 256:
        raise ValueError("context_tokens must be an integer of at least 256")
    tools = profile.get("tools", {})
    if not isinstance(tools, dict) or any(name not in TOOL_NAMES or not isinstance(enabled, bool)
                                          for name, enabled in tools.items()):
        raise ValueError("Invalid capability tools")
    capacity = profile.get("parallel_capacity", 1)
    if isinstance(capacity, bool) or not isinstance(capacity, int) or not 1 <= capacity <= 16:
        raise ValueError("parallel_capacity must be between 1 and 16")
    return tier, context_tokens, {name: tools.get(name, False) for name in TOOL_NAMES}, capacity


def _task(task):
    _bounded(task, "task context")
    if not isinstance(task, dict) or not isinstance(task.get("objective"), str) or not task["objective"].strip():
        raise ValueError("Task objective is required")
    if task.get("complexity", "unknown") not in COMPLEXITIES:
        raise ValueError("Unknown task complexity")
    if task.get("risk", "unknown") not in RISKS:
        raise ValueError("Unknown task risk")


def capability_plan(profile, task):
    """Build a host-executed workflow from observed capability, never a model-name guess."""
    tier, context_tokens, tools, capacity = _profile(profile)
    _task(task)
    resolved_tier = "constrained" if tier == "unknown" else tier
    if resolved_tier == "constrained":
        steps = [
            {"step_id": "frame_contract", "depends_on": []},
            {"step_id": "prepare_evidence_packet", "depends_on": ["frame_contract"]},
            {"step_id": "execute_one_method", "depends_on": ["prepare_evidence_packet"]},
            {"step_id": "check_output", "depends_on": ["execute_one_method"]},
            {"step_id": "finalize", "depends_on": ["check_output"]},
        ]
        scaffolding = ["explicit input/output contract", "one method per step", "small evidence packets",
                       "worked pattern when available", "mandatory completion checklist"]
        concurrency = 1
    elif resolved_tier == "balanced":
        steps = [
            {"step_id": "frame_contract", "depends_on": []},
            {"step_id": "ground_evidence", "depends_on": ["frame_contract"]},
            {"step_id": "apply_methods", "depends_on": ["frame_contract"]},
            {"step_id": "synthesize", "depends_on": ["ground_evidence", "apply_methods"]},
            {"step_id": "check_output", "depends_on": ["synthesize"]},
        ]
        scaffolding = ["structured task contract", "bounded framework selection", "claim-to-evidence links",
                       "deterministic checks where available", "explicit unresolved questions"]
        concurrency = min(capacity, 2)
    else:
        steps = [
            {"step_id": "frame_contract", "depends_on": []},
            {"step_id": "primary_analysis", "depends_on": ["frame_contract"]},
            {"step_id": "adversarial_analysis", "depends_on": ["frame_contract"]},
            {"step_id": "ground_evidence", "depends_on": ["frame_contract"]},
            {"step_id": "synthesize", "depends_on": ["primary_analysis", "adversarial_analysis", "ground_evidence"]},
            {"step_id": "check_output", "depends_on": ["synthesize"]},
        ]
        scaffolding = ["sparse task contract", "independent challenge", "claim-to-evidence links",
                       "deterministic verification", "stop when marginal value is exhausted"]
        concurrency = min(capacity, 3)
    host_parallel = tools["delegation"] and concurrency > 1
    schedule = plan_execution(steps, strategy="AUTO", host_parallel=host_parallel, max_concurrency=concurrency)
    verification = "DETERMINISTIC" if tools["deterministic_validation"] else "STRUCTURED_SELF_CHECK"
    limitations = []
    if tier == "unknown":
        limitations.append("Unknown tier uses the constrained profile until observed task evidence supports promotion.")
    if not tools["deterministic_validation"]:
        limitations.append("Deterministic validation is unavailable; self-checks do not prove correctness.")
    if task.get("risk") in {"high", "critical"} and verification != "DETERMINISTIC":
        limitations.append("High-risk output requires an external or host-supported verification gate.")
    debug("capability.plan", resolved_tier=resolved_tier)
    return {
        "status": "PLANNED",
        "capability_tier": tier,
        "resolved_tier": resolved_tier,
        "context_packet_limit": max(256, min(context_tokens // 4, 12000)),
        "scaffolding": scaffolding,
        "verification": verification,
        "schedule": schedule,
        "promotion_policy": "Change tier only from repeated observed task results, never from model branding alone.",
        "limitations": limitations,
    }


def _cases(records, label):
    if not isinstance(records, list) or not records:
        raise ValueError(f"{label} cases are required")
    output = {}
    for record in records:
        if not isinstance(record, dict) or not isinstance(record.get("case_id"), str) or not record["case_id"]:
            raise ValueError(f"Invalid {label} case")
        if record["case_id"] in output:
            raise ValueError(f"Duplicate {label} case id")
        score = record.get("score")
        if isinstance(score, bool) or not isinstance(score, (int, float)) or not math.isfinite(score) or not 0 <= score <= 1:
            raise ValueError(f"Invalid {label} score")
        critical_error = record.get("critical_error", False)
        if not isinstance(critical_error, bool):
            raise ValueError(f"Invalid {label} critical_error")
        output[record["case_id"]] = {"score": float(score), "critical_error": critical_error}
    return output


def _sign_test(wins, losses):
    trials = wins + losses
    if not trials:
        return 1.0
    tail = sum(math.comb(trials, index) for index in range(min(wins, losses) + 1)) / (2 ** trials)
    return min(1.0, 2 * tail)


def evaluate_capability(baseline, candidate, minimum_pairs=20, minimum_effect=0.10, alpha=0.05):
    """Evaluate paired cases and reserve significant claims for an explicit statistical gate."""
    _bounded({"baseline": baseline, "candidate": candidate}, "capability evaluation")
    if isinstance(minimum_pairs, bool) or not isinstance(minimum_pairs, int) or not 5 <= minimum_pairs <= 10000:
        raise ValueError("minimum_pairs must be between 5 and 10000")
    for value, name in [(minimum_effect, "minimum_effect"), (alpha, "alpha")]:
        if isinstance(value, bool) or not isinstance(value, (int, float)) or not math.isfinite(value):
            raise ValueError(f"Invalid {name}")
    if not 0 < minimum_effect <= 1 or not 0 < alpha < 1:
        raise ValueError("Invalid evaluation thresholds")
    before = _cases(baseline, "baseline")
    after = _cases(candidate, "candidate")
    if set(before) != set(after):
        raise ValueError("Baseline and candidate case ids must match exactly")
    deltas = [after[case_id]["score"] - before[case_id]["score"] for case_id in sorted(before)]
    wins = sum(delta > 0 for delta in deltas)
    losses = sum(delta < 0 for delta in deltas)
    ties = len(deltas) - wins - losses
    mean_delta = sum(deltas) / len(deltas)
    critical_regressions = [case_id for case_id in sorted(before)
                            if after[case_id]["critical_error"] and not before[case_id]["critical_error"]]
    p_value = _sign_test(wins, losses)
    gates = {
        "enough_pairs": len(deltas) >= minimum_pairs,
        "minimum_effect_met": mean_delta >= minimum_effect,
        "statistical_gate_met": p_value <= alpha,
        "no_new_critical_errors": not critical_regressions,
    }
    if all(gates.values()):
        verdict = "SIGNIFICANT_IMPROVEMENT"
    elif mean_delta < 0 or critical_regressions:
        verdict = "REGRESSION"
    elif mean_delta > 0:
        verdict = "IMPROVED_NOT_SIGNIFICANT"
    else:
        verdict = "NO_MEASURABLE_GAIN"
    return {
        "status": "EVALUATED",
        "verdict": verdict,
        "paired_cases": len(deltas),
        "mean_score_delta": mean_delta,
        "wins": wins,
        "losses": losses,
        "ties": ties,
        "sign_test_p_value": p_value,
        "critical_regressions": critical_regressions,
        "thresholds": {"minimum_pairs": minimum_pairs, "minimum_effect": minimum_effect, "alpha": alpha},
        "gates": gates,
        "limitations": ["This evaluates the supplied paired cases only; representativeness, judge quality, latency, and cost need separate evidence."],
    }
