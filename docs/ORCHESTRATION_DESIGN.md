# Orchestration design

**Implementation update:** the V4.1 governor and deep plan are in `cognition/augmentation.py`; [hybrid architecture](HYBRID_ARCHITECTURE.md) explains the new policies, budgets, and contracts. The planner modes below remain only for the compatibility `plan` action. Host model selection still needs native evidence.

**V4.1 design delta:** the governor assesses relevance, risk, complexity, evidence sufficiency, permissions, budget, and duplication; it offers seven internal policies including `PASS_THROUGH` and returns concise advice to the host. AG-51 coordinates selected analysis while the host remains the task owner. The modes and defaults below describe baseline 3.1. See the [concept review](CONCEPT_V4_1.md) and [migration plan](V4_1_MIGRATION_PLAN.md).

AG-51 collects objective and only decision-relevant missing context, reviewing domain/type/criticality/complexity/reversibility/evidence/stakeholders/exposure/risks/time/output/tools/budget. The Python planner is a disclosed keyword heuristic with explicit framework selection precedence. Host judgment can revise it. AUTO is an efficient default heuristic, not a trained autonomous classifier.

Limits are canonical in cognitive-core/orchestration/policy.json. Each step carries required inputs, expected outputs, predecessor IDs, logical specialist ID and status PLANNED. No analytical task is executed by planning. check-workflow accepts host-created artifacts, enforces predecessor order and blocks on absent or invalid artifacts. Semantically compatible fields must be mapped by the host; equal names are insufficient.

Actual specialist handoff includes objective, source IDs, assumptions, relevant payload, selected method, unresolved questions, constraints and remaining allowance. `analysis-plan` validates the dependency DAG and emits execution waves. Dependent tasks remain ordered; independent steps in one wave may be delegated concurrently when the host exposes native delegation and the authorized concurrency allowance permits it. Otherwise the scheduler returns a sequential fallback. Returned execution IDs are recorded by the host. Planning never dispatches agents or fabricates parallel records.

Conditional steps run only when stated evidence/constraints hold. Stop at sufficient answer, missing essential tool/evidence, exhausted allowance, unresolved user judgment or negligible marginal value. Estimated context allowances are not measured token accounting; the host must stop using actual usage when instrumentation exists. Debates have at most two rebuttals; further work requires new decision value and user scope.

AG-52 checks method, evidence, contradictions and risk policy and can reject. Native response uses Minto format with a clear conditional or insufficient-evidence outcome. Source five-phase workflow is preserved without forcing every problem through every model.

