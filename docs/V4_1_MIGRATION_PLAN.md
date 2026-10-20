# V4.1 migration plan

**Execution update:** the rebuild was authorized and this plan is being executed. Progress, evidence, and open gates are recorded in [REBUILD_STATUS_V4_1.md](REBUILD_STATUS_V4_1.md). The historical review scope near the end records the initial context; it no longer limits rebuild authorization.

Date: 2026-10-20. Original plan status: `PROPOSED`. The concept comes from the [V4.1 prompt](evidence/master-implementation-prompt-v4.1.txt); checkout analysis is in the [concept review](CONCEPT_V4_1.md). This plan alone is neither an implementation record nor a V4.1 evaluation result.

## Target and constraints

Retain one core, 50 models in eight categories, and AG-01..52. Reuse audited 0.1.0 assets. Complete the original deliverable through the host with the minimum useful assistance. Model-selected skills are the primary path, selective deterministic validation is secondary, and deep advisory is conditional. MCP, case storage, and learning remain optional.

Update generator sources before regeneration. `scripts/build_docs.py` can overwrite older guides; `scripts/build_plugin.py` can overwrite metadata and skills; `scripts/build_catalog.py` contains baseline contracts. Keep the concept document and prompt as fixed, nongenerated sources. Do not rerun every baseline generator merely to refresh V4.1 documentation.

## Phase sequence and gates

| Phase | Concrete work | Deliverable / area | Gate before proceeding |
|---|---|---|---|
| 0 — Source delta audit | Compare the complete blueprint and all 15 PDF pages with V4.1; inventory capabilities, methods, specialists, formulas, contracts, dependencies, evidence, application assumptions, security, conflicts, and gaps | Updated `docs/SOURCE_ANALYSIS.md`, traceability, and locator-backed transformation matrix | Every feature mapped; source-derived material distinguished from adaptations/proposals; source hashes verifiable |
| 1 — Platform verification | Check official documentation and available runtime for each Claude/Codex surface; record versions, events, payloads, feedback/block behavior, permissions/trust, script installation, and fallback | `docs/PLATFORM_COMPATIBILITY.md`, adapter notes, host-specific evidence | No invented API/event/manifest fields; unsupported and untested states explicit; tests respect `ACCOUNT_SCOPE.md` |
| 2 — Hybrid design | Define seven-policy governor, request/result contracts, host output, budgets, and deduplication; design 3.1 compatibility and evidence enums | Policy/core, target schemas, orchestration, architecture decisions, generators | Negative control yields pass-through; host format/objective preserved; budgets do not hide security gaps |
| 3 — Minimal prototype | Migrate routing, MECE, First Principles, 5 Whys, Pre-Mortem, and artifact validation; add one safe hook on a supporting host | Generators, skills, helper/core, schemas, selected adapter/hook | Ordinary task can select assistance without naming Cognition OS; native invocation evidenced. Hook tests cover payload, timeout, feedback, duplicates, paths, and failures, or retain an explicit open gate |
| 4 — Full core | Audit/align definitions and contracts for 50 models and 52 specialists: triggers/preconditions, limitations, compatibility, and references | One canonical registry/definitions, schemas, method evaluations | Source IDs/categories/methods retained; contracts complete; semantic fidelity tested apart from structure |
| 5 — Deep advisory | Add multi-framework selection, calculations, advocate/challenger/jury, and explicit stopping | Bounded workflow, advisory result, tests/evaluations | Dormant for simple tasks; disagreement/evidence gaps retained; no unbounded recursive delegation |
| 6 — Dual integration | Test Claude and Codex adapters separately on available surfaces; create a fallback matrix without MCP/hooks/scripts | Adapters/packages, installation, update, rollback, native transcripts | One host's result is not transferred to another; installed/discovered/selected/executed states distinguished |
| 7 — Evaluation | Run A baseline, B skills, C skills+hooks, D full hybrid; randomize order and repeat runs with comparable models/settings | Cases/rubric, raw results, instrumentation, performance report | Task outcomes, unnecessary activation, false-positive warnings, tokens/calls/latency, and recovery measured; missing data not invented |
| 8 — Hardening | Review permission boundaries, prompt injection, paths, secrets, portable package, update/rollback, and release docs | Validated operational package and release checklist | Each acceptance criterion has evidence or an explicit blocker; production-ready only after gates pass |

Phase order follows V4.1. Delta auditing does not erase 3.1 evidence. A prototype may reuse existing helpers/core, but reuse is not proof of hybrid behavior. No deadline or numerical improvement claim precedes measurement.

## Implementation decisions requiring evidence

1. Verify model invocation with natural tasks and negative controls; use manual invocation to diagnose failed selection.
2. Choose one event and validator with adequate payload and feedback. Initial proposal: check artifact schemas on in-scope paths after edit if the host provides a suitable event. This is a proposal, not a universal cross-platform event name.
3. Separate advisory failure from enforcement failure. Define timeout, file/size bounds, content hash, bounded cache, and invalidation; cache results do not expand permission.
4. Add request/result schemas without silently changing old artifact/case records. Mapping `USER_ASSUMPTION` → `ASSUMPTION` and `MODEL_INFERENCE` → `INFERENCE` must retain provenance.
5. Replace the package validator's blanket rejection of `hooks/` with validation of the chosen hook configuration. Add MCP only if the implementation needs it.
6. Remove mandatory analysis reports from the light path. Host/user format determines output; internal findings can remain brief and traceable.
7. Record actual budget consumption where exposed by the host. Initial numeric limits are experiment configuration to calibrate, not scientifically optimized results.

## Required deliverables

| Package | Required result |
|---|---|
| A — Source Intelligence | Complete audit, capability inventory, locator-backed transformation matrix, and source/adaptation/proposal classification |
| B — Hybrid Architecture | Three paths, governor, contracts, budget, guardrails, permissions, and fallback |
| C — Cognitive Core | Canonical 50-model / 52-role registry, schemas, calculations, and evidence handling |
| D — Claude Adapter | Native package/skills, verified agent/hook/MCP support when needed, installation evidence |
| E — Codex Adapter | Portable package/skills, verified hook support when needed, installation evidence |
| F — Evaluation | A/B/C/D protocol, cases, raw results, overhead and outcome metrics |
| G — Release | Security review, reproducible package, update/rollback guidance, and acceptance status |

Track all 18 release criteria from prompt section 22 individually with evidence locators. At minimum, demonstrate host task ownership, catalog preservation, actual skill selection, authorized hooks, selective deep advisory, correct calculations, permission boundaries, and benefit versus overhead. Lack of MCP or a separate app does not block the baseline. An unavailable hook must never be marked `TESTED`.

The initial concept-review scope ended with preserving the prompt, understanding the concept, identifying repository gaps, and drafting this plan. At that time runtime, host configuration, credentials, and V4.1 benchmarks had not been migrated; later progress is recorded in the rebuild status.
