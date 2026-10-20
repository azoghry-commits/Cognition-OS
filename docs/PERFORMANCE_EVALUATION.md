# Performance evaluation

## V4.1 target protocol — not yet run

Compare A: host without the plugin, B: model-selected skills, C: B plus supported deterministic hooks, and D: C plus selective deep advisory. Include simple coding tasks as negative controls, along with architecture, debugging, database incidents, security review, strategic decisions, multi-step implementation, documentation, and mathematics. Measure original deliverable quality, requirement coverage, regressions, activation relevance, unnecessary activation, false-positive warnings, calls/tokens/latency, and recovery when observable.

A host without hook support cannot receive a full C/D result; report partial support and the actual configuration. Manual script invocation is not evidence of hook delivery. V4.1 experiment status: `NOT_RUN`. See the [concept review](CONCEPT_V4_1.md) and [migration plan](V4_1_MIGRATION_PLAN.md).

## Baseline 3.1 measurement and plan

No baseline-versus-plugin native performance gain is claimed. Deterministic helper timing can be measured using `python scripts/benchmark.py` and is recorded separately in evidence/benchmark.json. Those measurements exclude model calls, skill activation, token use and user-task quality.

Native protocol: use examples A-E plus all 50 cognitive cases, fixed host/model/settings, equivalent input context, randomized order and repeated runs. Compare baseline, QUICK, STANDARD and DEEP. Record task quality using blinded method/evidence rubrics, activation precision/recall, chosen frameworks, tool/model calls, input/output tokens where exposed, elapsed time, correctness, traceability and user completion. Report missing instrumentation as NOT_VERIFIED rather than zero. Preserve raw transcripts and failures.

Current host comparison status: NOT_VERIFIED until actual runs are collected. Source targets (<30 minutes synthesis, <50 ms simulation, graph density and >90% confidence) are unvalidated product assertions. Registry coverage and metadata size are inspectable engineering metrics, not evidence of improved cognition.

