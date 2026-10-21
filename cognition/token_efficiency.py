"""Deterministic context budgeting with quality-preserving escalation gates."""

PROFILES = {
    "LEAN": {"frameworks": 1, "references": 1, "rebuttal_rounds": 0, "context_fraction": 0.12},
    "BALANCED": {"frameworks": 4, "references": 3, "rebuttal_rounds": 1, "context_fraction": 0.25},
    "DEEP": {"frameworks": 8, "references": 6, "rebuttal_rounds": 2, "context_fraction": 0.45},
}


def token_plan(task, context_tokens=8000, requested="AUTO"):
    """Select the smallest safe context profile and disclose escalation reasons."""
    if not isinstance(task, dict) or not str(task.get("objective", "")).strip():
        raise ValueError("Task objective is required")
    if isinstance(context_tokens, bool) or not isinstance(context_tokens, int) or context_tokens < 512:
        raise ValueError("context_tokens must be an integer of at least 512")
    if requested not in {"AUTO", *PROFILES}:
        raise ValueError("Unknown token profile")
    complexity = task.get("complexity", "unknown")
    risk = task.get("risk", "unknown")
    uncertainty = task.get("uncertainty", "unknown")
    evidence_complete = task.get("evidence_complete", False)
    deterministic_check = task.get("deterministic_check", False)
    if complexity not in {"low", "medium", "high", "unknown"}:
        raise ValueError("Unknown task complexity")
    if risk not in {"normal", "high", "critical", "unknown"}:
        raise ValueError("Unknown task risk")
    if uncertainty not in {"low", "medium", "high", "unknown"}:
        raise ValueError("Unknown task uncertainty")
    if not isinstance(evidence_complete, bool) or not isinstance(deterministic_check, bool):
        raise ValueError("Quality flags must be booleans")

    minimum = "LEAN"
    reasons = []
    if complexity in {"medium", "unknown"} or uncertainty in {"medium", "unknown"} or not evidence_complete:
        minimum = "BALANCED"
        reasons.append("bounded analysis is required by complexity, uncertainty, or incomplete evidence")
    if complexity == "high" or risk in {"high", "critical"} or uncertainty == "high":
        minimum = "DEEP"
        reasons.append("deep analysis is required by high complexity, risk, or uncertainty")
    order = {"LEAN": 0, "BALANCED": 1, "DEEP": 2}
    selected = minimum if requested == "AUTO" else requested
    if order[selected] < order[minimum]:
        selected = minimum
        reasons.append(f"requested profile escalated to {minimum} by the quality floor")
    profile = PROFILES[selected]
    allowance = max(512, min(context_tokens, int(context_tokens * profile["context_fraction"])))
    checks = ["claim-to-evidence links", "explicit UNKNOWN gaps", "completion checklist"]
    if deterministic_check:
        checks.append("deterministic validation")
    if risk in {"high", "critical"}:
        checks.extend(["adversarial review", "human or external verification before consequential action"])
    return {
        "status": "PLANNED",
        "profile": selected,
        "minimum_safe_profile": minimum,
        "context_allowance": allowance,
        "max_frameworks": profile["frameworks"],
        "max_references": profile["references"],
        "max_rebuttal_rounds": profile["rebuttal_rounds"],
        "progressive_disclosure": [
            "load skill name and description for discovery",
            "load one matching SKILL.md after activation",
            "load only selected framework definitions and referenced evidence",
            "expand context only when a quality gate triggers",
        ],
        "quality_checks": checks,
        "escalation_triggers": [
            "material evidence conflict",
            "missing decision-critical input",
            "failed deterministic check",
            "new critical objection",
            "requested deliverable remains unsupported",
        ],
        "reasons": reasons,
        "claim_boundary": "The allowance is a deterministic context budget, not measured provider billing or proof of equal model quality.",
    }


def evaluate_efficiency(baseline_tokens, candidate_tokens, baseline_score, candidate_score,
                        maximum_quality_loss=0.02, minimum_token_reduction=0.20):
    """Gate token-efficiency claims using paired measured usage and quality scores."""
    for value, name in [(baseline_tokens, "baseline_tokens"), (candidate_tokens, "candidate_tokens")]:
        if isinstance(value, bool) or not isinstance(value, int) or value <= 0:
            raise ValueError(f"{name} must be a positive integer")
    for value, name in [(baseline_score, "baseline_score"), (candidate_score, "candidate_score")]:
        if isinstance(value, bool) or not isinstance(value, (int, float)) or not 0 <= value <= 1:
            raise ValueError(f"{name} must be between 0 and 1")
    reduction = 1 - candidate_tokens / baseline_tokens
    quality_delta = candidate_score - baseline_score
    gates = {
        "token_reduction_met": reduction >= minimum_token_reduction,
        "quality_floor_met": quality_delta >= -maximum_quality_loss,
    }
    return {
        "status": "EVALUATED",
        "verdict": "TOKEN_EFFICIENT_QUALITY_RETAINED" if all(gates.values()) else "GATE_NOT_MET",
        "token_reduction": reduction,
        "quality_delta": quality_delta,
        "gates": gates,
        "claim_boundary": "Valid only for the supplied paired measurement and judge rubric.",
    }
