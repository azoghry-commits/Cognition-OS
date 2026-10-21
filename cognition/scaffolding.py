"""Offline advisory selection from one frozen, paired strategy comparison."""

from .capability import _bounded, evaluate_capability

STRATEGIES = {"conservative", "bounded", "sparse"}


def select_scaffolding(baseline, candidate, strategy, evidence_id):
    """Consume scored evidence; never run models or attest evidence authenticity."""
    _bounded(locals(), "scaffolding comparison")
    if strategy not in STRATEGIES - {"conservative"}:
        raise ValueError("Challenger strategy must be bounded or sparse")
    if not isinstance(evidence_id, str) or not evidence_id.strip():
        raise ValueError("A workload-scoped evidence reference is required")
    for records in (baseline, candidate):
        if not isinstance(records, list) or not records:
            raise ValueError("Scored cases are required")
        if any(not isinstance(row, dict) or "critical_error" not in row for row in records):
            raise ValueError("Every case requires an explicit critical_error result")
    evaluation = evaluate_capability(baseline, candidate)
    # A pre-existing baseline critical error cannot make an unsafe challenger acceptable.
    safe = not any(row["critical_error"] for row in candidate)
    accepted = safe and evaluation["verdict"] == "SIGNIFICANT_IMPROVEMENT"
    return {
        "status": "ADVISORY_ONLY",
        "recommended_strategy": strategy if accepted else "conservative",
        "evidence_id": evidence_id,
        "candidate_has_no_critical_errors": safe,
        "evaluation": evaluation,
        "limitations": [
            "Scores and evidence provenance are supplied, not independently verified.",
            "Synthetic fixtures do not measure real model capability.",
            "Requires held-out cases, independent scoring and cost/latency review before activation.",
            "No host settings, capability tier or permissions are changed.",
        ],
    }
