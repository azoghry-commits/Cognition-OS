# Measured scaffolding decision — 2026-10-22

Decision: GO for an offline, advisory selection prototype; HOLD for automatic host deployment and claims of improved model capability.

## Evidence and scope

The Cognition OS orchestrator policy and FW-49 Pre-Mortem & Red Teaming were applied to this proposal. Evidence: `cognition/capability.py` already implements explicit profiles, conservative unknown handling, and paired evaluation. `tests/test_capability.py` exercises statistical gates using synthetic scores. Neither establishes measured ability on real host tasks. Native benchmark results, judge agreement, and actual costs are UNKNOWN.

Alternatives: retain manually declared tiers (simple, weak calibration); infer tiers from branding (rejected: no task evidence); measure strategies on matched tasks (selected: auditable, workload-specific). Select the scaffolding strategy directly instead of assigning a universal intelligence tier.

## Pre-mortem

Assume the pilot fails after its first evaluation cycle (planning horizon, not a promised date).

| Failure mechanism | Early signal | Mitigation / stop condition |
| --- | --- | --- |
| Training examples leak into evaluation | Near-duplicate prompts or answers | Keep development and held-out cases separate; invalidate contaminated runs |
| Self-scoring rewards verbosity | Judge disagreement, high scores with failed executable checks | Deterministic rubric first; independent blinded review for semantic criteria; stop promotion if critical errors occur |
| One host result is reused elsewhere | Tool/context/model revision changes | Fingerprint model revision, host, tools, prompt, corpus and rubric; require re-evaluation after changes |
| More scaffolding consumes budget without improving quality | Higher latency/tokens with unchanged correctness | Report measured usage separately; require quality floor and operational budget before activation |
| Multiple candidates produce a lucky winner | Repeated tuning against the same test set | Development set chooses one challenger; fresh held-out set confirms it against baseline |

## Executable plan and acceptance gates

1. Integrate a dependency-free offline selector that compares exactly one preselected challenger with baseline using existing paired gates. Reject missing critical-error fields and mismatched cases. All recommendations remain advisory.
2. Add CLI and negative tests. Insufficient evidence, any candidate critical error, or failed significance gates retain conservative scaffolding. A negative verdict never upgrades the strategy.
3. Collect real runs externally through authorized host execution: case ID, run ID, task family, strategy, model revision, host/tool fingerprint, seed/settings, rubric version, raw output reference/hash, score, explicit critical-error flag, wall time and observed usage. Missing usage stays UNKNOWN. Do not start paid provider inference implicitly.
4. Compare baseline/conservative, bounded, and sparse strategies on development cases; freeze one challenger, thresholds and rubric before held-out confirmation. Use independent cases; repeated seeds on one case are not independent samples. The existing 20-pair gate is a prototype default, not a power analysis or proof of generality.
5. Promote only a workload-scoped policy after independent score review, quality-floor review and cost/latency acceptance. Re-evaluate on fingerprint change. Roll back to conservative on critical failure or drift.

Prototype completion proves deterministic selection behavior only. The host still owns permissions, verification and activation. Automatic collection, trusted provenance verification, calibrated quality thresholds and production deployment remain future work.
