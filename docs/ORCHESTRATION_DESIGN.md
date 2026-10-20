# Orchestration design

**Delta V4.1 yang belum diimplementasikan:** governor menilai relevansi, risiko, kompleksitas, kecukupan bukti, izin, budget dan duplikasi; menyediakan tujuh kebijakan internal termasuk `PASS_THROUGH`; mengembalikan advisory ringkas ke host. AG-51 mengoordinasikan analisis terpilih, sementara host tetap pemilik tugas. Mode dan default di bawah adalah baseline 3.1. Lihat [kajian konsep](CONCEPT_V4_1.md) dan [rencana migrasi](V4_1_MIGRATION_PLAN.md).

AG-51 collects objective and only decision-relevant missing context, reviewing domain/type/criticality/complexity/reversibility/evidence/stakeholders/exposure/risks/time/output/tools/budget. The Python planner is a disclosed keyword heuristic with explicit framework selection precedence. Host judgment can revise it. AUTO is an efficient default heuristic, not a trained autonomous classifier.

Limits are canonical in cognitive-core/orchestration/policy.json. Each step carries required inputs, expected outputs, predecessor IDs, logical specialist ID and status PLANNED. No analytical task is executed by planning. check-workflow accepts host-created artifacts, enforces predecessor order and blocks on absent or invalid artifacts. Semantically compatible fields must be mapped by the host; equal names are insufficient.

Actual specialist handoff includes objective, source IDs, assumptions, relevant payload, selected method, unresolved questions, constraints and remaining allowance. Dependent tasks are sequential. Independent optimistic/critical reviewers may be delegated with observed native tools and authorization; returned execution IDs are recorded. The static plan conservatively says SEQUENTIAL_HOST_ROLES. It neither dispatches agents nor fabricates parallel records.

Conditional steps run only when stated evidence/constraints hold. Stop at sufficient answer, missing essential tool/evidence, exhausted allowance, unresolved user judgment or negligible marginal value. Estimated context allowances are not measured token accounting; the host must stop using actual usage when instrumentation exists. Debates have at most two rebuttals; further work requires new decision value and user scope.

AG-52 checks method, evidence, contradictions and risk policy and can reject. Native response uses Minto format with a clear conditional or insufficient-evidence outcome. Source five-phase workflow is preserved without forcing every problem through every model.

