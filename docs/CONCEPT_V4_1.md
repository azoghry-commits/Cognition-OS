# Cognition OS V4.1 concept review

**Historical note:** this document records the understanding before the rebuild was authorized. Candidate 0.2.0 implementation and phase status are in [REBUILD_STATUS_V4_1.md](REBUILD_STATUS_V4_1.md); implemented contracts and the governor are described in [HYBRID_ARCHITECTURE.md](HYBRID_ARCHITECTURE.md).

Date: 2026-10-20. Concept review status: prompt reading and checkout comparison complete. The V4.1 architecture was `SOURCE_DERIVED` / `PROPOSED` at this point; hybrid implementation had not yet started.

Full reference: [Master Implementation Prompt V4.1](evidence/master-implementation-prompt-v4.1.txt), preserved byte-for-byte at 36,889 bytes with SHA-256 `2bea071346bc243cdf6bac965c86d27b7f515278fae0c72817dc462ee5d6b99b`. Metadata: [concept-v4.1.json](evidence/concept-v4.1.json).

The original request was to understand the conceptual change and perform Git work. This review established a direction and recorded gaps while runtime package 0.1.0 retained 3.1 contracts. A specification number does not automatically become a package release number.

## Fundamental change

Cognition OS becomes a **Hybrid Agent Cognitive Augmentation Layer**. Its primary consumers are models and agents carrying out human instructions. The user still requests an outcome from Claude or Codex; the host selects relevant cognitive assistance, receives structured findings, and completes the original deliverable.

The repository was already a plugin without a separate app. The 3.1→4.1 shift therefore concerns capability selection, governance, advisory contracts, event-driven validation, and task-outcome evaluation. Existing catalog and helper assets can be reused after a suitability audit.

| Dimension | Baseline 3.1 checkout | V4.1 direction |
|---|---|---|
| Task owner | Host already supplies reasoning and permissions; skills guide analysis sessions | Host owns execution and deliverables; plugin supplies internal assistance |
| Activation | Guides emphasize manual invocation; orchestrator defaults to STANDARD | Model selection is primary; simple tasks may pass through |
| Routing | Keyword planner selects a framework sequence, including a generic fallback | Added value, risk, complexity, evidence, duplication, host capability, and budget determine assistance |
| Depth | AUTO/QUICK/STANDARD/DEEP/EXECUTIVE/CUSTOM/LEARN workflow modes | Seven internal policies; no user mode selection required |
| Validation | Helpers run explicitly; no hook | Narrow deterministic hooks only on verified events |
| Deep advisory | Orchestration and review are available in a workflow | Dormant until analytical stakes justify overhead |
| Output | Orchestrator requests frame, artifact, ledger, verdict, and recommendation | Concise findings return to the host; the user's requested format governs delivery |
| Success measure | Contracts, catalog counts, local helpers, and a mode-evaluation plan | Measured task outcomes against baseline and actual overhead |

## Target architecture and control boundaries

This diagram is a prompt-derived design, not evidence of implementation or runtime interception.

```mermaid
flowchart TD
    U[User instruction and deliverable] --> H[Claude / Codex: host task owner]
    H --> X[Task execution with host tools and permissions]
    H -. when relevant .-> G[Hybrid Activation Governor]
    G --> A[A: Model-selected assistance]
    G --> B[B: Deterministic validation on verified events]
    G --> C[C: Conditional deep advisory]
    A --> K[One canonical Cognitive Core]
    B --> K
    C --> K
    K --> R[Findings, evidence, calculations, limitations]
    R --> H
    X --> D[Original deliverable]
    H --> D
    G -. PASS_THROUGH .-> X
```

One core serves the Claude and Codex adapters. Canonical locations remain `cognitive-core/frameworks/` and `cognitive-core/agents/`; example names `mental-models/` and `specialists/` in the prompt do not require a rename or duplicate copy. AG-51 coordinates selected core analysis without taking over the host. AG-52 evaluates findings and may reject support for a recommendation. An analytical verdict does not authorize the plugin to block host tools. Enforcement requires a supported, authorized host mechanism.

## Three assistance paths

| Path | Trigger and work | Limits and acceptance evidence |
|---|---|---|
| A — primary | Host selects relevant skills and loads necessary definitions | No loading all 50 definitions, forced full intake, or duplicated host analysis. Installation does not prove invocation; evaluate actual selection |
| B — secondary | A native event invokes a local format/schema or artifact check | Verify event name, payload, permission, feedback, blocking capability, timeout, and failure separately by host. No LLM call on every event |
| C — conditional | Complexity, risk, conflicting evidence, or failed earlier analysis | Complementary frameworks, bounded iterations, real calculations, concise findings, stop on low marginal value. Answer length is not a trigger |

Paths may be combined with an explicit reason for each addition. Do not assume hidden chain-of-thought access, capture of every work stage, universal events, or uniform hooks across Claude Code, Chat, Desktop, Cowork, and Codex CLI/Desktop. Native subagents are an implementation choice when supported, authorized, and useful. Fifty-two specialists denote logical analytical specializations, not 52 model processes, automatic parallelism, or specially trained models.

## Hybrid Activation Governor

The governor considers only observable context: objective, task type, risk, complexity, evidence sufficiency, artifacts, available host tools/capabilities, permissions, execution limits, remaining context, and prior analysis.

| Policy | Intended behavior |
|---|---|
| `PASS_THROUGH` | No extra assistance beyond unavoidable discovery overhead |
| `LIGHT_AUGMENTATION` | One narrow, relevant capability |
| `STANDARD_AUGMENTATION` | Short sequence of complementary frameworks |
| `DETERMINISTIC_VALIDATION` | Tool/hook with bounded inputs and scope |
| `DEEP_ADVISORY` | Fuller analysis where the question justifies cost |
| `CRITICAL_REVIEW` | Stronger evidence/artifact review for consequential tasks |
| `DEGRADED` | Use available capabilities when an optional component is missing |

These are internal policies, not a required user menu. There is no one-to-one mapping from old modes. The governor must explain its choice without inventing optimization scores, risk probabilities, or token estimates as measured values. Budgets include framework invocations, subagents, debate rounds, tool calls, compute time, and context. On exhaustion, return partial results and material gaps; do not issue a safe verdict merely because calculations stopped. Security enforcement must never fail open through `DEGRADED`.

## Transformation of source capabilities

This table maps every V4.1-required capability group to repository assets and target roles. A full repeat audit of source A/B, each formula, and every contract remained a Phase 0 gate at the time of this review. The [earlier audit](SOURCE_ANALYSIS.md) remains a 3.1 record; this concept review did not reinspect the 15-page PDF.

| Source capability | Baseline assets | V4.1 target transformation |
|---|---|---|
| 50 mental models / eight categories | `cognitive-core/frameworks/registry.json`, `definitions/`, `schemas/framework-output/` | Lazy-loaded knowledge/skills; audit each model's preconditions, triggers, input/output, method, evidence, limitations, compatibility, references, and validation |
| 52 logical specialists | `cognitive-core/agents/registry.json`, two `agents/` wrappers | Host roles, skills, deterministic helpers, or native subagents as needed; stable AG-01..52 |
| Framework Stack Builder | `skills/framework-composer/`, `cognition/engine.py` | Complementary routing for host task gaps; no automatic long workflow |
| Problem Ingestion | `skills/cognition-orchestrator/` | Normalize observed context; ask only for blocking prerequisites |
| Thinking Canvas | `templates/issue-tree.md`, Markdown/Mermaid/JSON | Optional supporting artifact in host work when useful; no mandatory app |
| Adversarial Debate | `skills/adversarial-review/`, `references/REVIEW.md`, AG-52 | Bounded advocate/challenger/jury advisory; retain disagreement when evidence is weak |
| Scenario Simulation | `cognition/mathematics.py`, `references/CALCULATIONS.md` | Local tool with explicit inputs, distributions, and seed; separate simulation evidence class |
| Logic Guardrails | `cognition/engine.py`, evidence schema, `references/REVIEW.md` | Deterministic checks for objective rules, qualitative review for semantics; possible narrow hook |
| Mathematical Validation | `cognition/mathematics.py`, `tests/test_mathematics.py` | Actual calculations with independent references, units, and assumptions |
| Reasoning Knowledge Graph | `schemas/provenance.schema.json`, `docs/DECISION_PROVENANCE.md` | Observable artifact/evidence/decision lineage without hidden thought access |
| Institutional Memory | `cognition/memory.py`, `references/MEMORY.md` | Authorized local/host-native reuse with provenance and versions; no mandatory database server |
| Executive Synthesis | `skills/executive-synthesis/`, `templates/executive-brief.md` | Match host/user format; executive form when relevant |
| Human Mastery Track | `skills/cognitive-mastery/`, `cognitive-core/mastery/` | Separate opt-in human learning, never automatic model training |

Shared orchestration, guardrails, and mathematics appear in several groups without creating duplicate catalogs. This review did not remove any capability.

## Advisory contracts and evidence classification

The target request includes, when available: request ID, host ID, agent role, task summary, requested capabilities, evidence references, constraints, risk, tools, budget, and authorization scope. The target response includes status, findings, supporting evidence, issues, computed results, recommendations, confidence limitations, unresolved questions, and optional follow-up checks.

At the time of this review these conceptual fields were not executable schemas. Existing `schemas/agent-envelope.schema.json` required `envelope_version: "3.1"` and centered on specialist artifacts. V4.1 request/result contracts and compatibility rules were required before changing schema versions; simply changing a constant or relabeling an old payload would not suffice.

V4.1 evidence classes are `VERIFIED_FACT`, `SOURCE_SUPPORTED`, `CALCULATED_RESULT`, `SIMULATED_RESULT`, `ASSUMPTION`, `INFERENCE`, `HYPOTHESIS`, and `UNKNOWN`. Baseline 3.1 used `USER_ASSUMPTION` and `MODEL_INFERENCE`. Migration must explicitly map the latter to `ASSUMPTION` / `INFERENCE` while retaining origin and actor in provenance; the old strict schema does not accept new enum values. No fabricated confidence score is allowed. Schema-valid, source-supported, calculated, hypothetical, and tested claims must remain distinguishable. Advisory output excludes long debate transcripts and hidden chain-of-thought.

## Checkout gaps identified at the review

| ID | Repository evidence at review | Gap and next action |
|---|---|---|
| G01 | `skills/cognition-orchestrator/SKILL.md`: STANDARD default and four-stage intake | Add selection without manual invocation, `PASS_THROUGH`, and proportional intake |
| G02 | `cognition/engine.py:plan`: four-framework fallback, old `MODES` and limits | Add relevance/risk/duplication/budget governor; honor explicit user choices |
| G03 | Orchestrator skill requires frame/artifact/ledger/verdict report | Separate internal advice from host deliverable; do not require a Cognition OS report for a simple code edit |
| G04 | `schemas/agent-envelope.schema.json`: 3.1 and old evidence enum | Add target request/result and compatibility strategy without forced replacement of old data |
| G05 | No `hooks/` / `mcp.json`; `scripts/validate_package.py` asserts absence | Verify host capabilities and adjust validator for a selected hook; MCP stays optional |
| G06 | `docs/PERFORMANCE_EVALUATION.md`: baseline vs QUICK/STANDARD/DEEP | Add A/B/C/D experiment, negative controls, and original-deliverable metrics |
| G07 | `scripts/build_docs.py`, `build_plugin.py`, `build_catalog.py` generate baseline | Align generators before regeneration so manual edits to generated files survive |
| G08 | `docs/PROJECT_STATUS.md`: desktop activation/native behavior unverified | Discovery/install does not prove invocation; run real host evaluations within authorized account scope |

This concept review did not reverify host/API/hook availability online. The [earlier compatibility matrix](PLATFORM_COMPATIBILITY.md) is baseline evidence with its own scope, not certification of current V4.1 capabilities. `cognition_assess_task` and other MCP tool names in the prompt remained proposals, not available APIs.

## Success measures and fallback

| Required experiment | Configuration |
|---|---|
| A | Host without Cognition OS |
| B | Host with model-selected skills |
| C | B plus genuinely supported deterministic hooks |
| D | C plus deep advisory only when justified |

Use simple coding, complex architecture, debugging, database incidents, security review, strategic decisions, multi-step implementation, documentation, and mathematics. Include negative controls where the plugin should stay passive. If a host lacks hooks, report C/D unavailable or partial with reasons; manual script calls are not native-hook evidence.

Measure correctness/task success, regressions, requirement coverage, framework-selection relevance, unnecessary activation, false-positive warnings, tool/model calls, token overhead, latency, artifact/evidence quality, and recovery. Missing instrumentation is `UNKNOWN`/unmeasured, not zero. Helper timing and passing schemas do not prove better host outcomes.

When a skill is unavailable, the host continues native reasoning if sufficient. Advisory hook failure is diagnosed and degraded according to policy. Failed security enforcement follows verified host permission behavior. When deep advisory or MCP is unavailable, use supported local paths and disclose material limitations; do not invent calculations.

## Coverage of every prompt section

| V4.1 section | Interpretation / mapped work |
|---|---|
| 0 | Identity, one core, dual adapters, noninterference, task outcomes |
| 1 | Audit A/B and transform every capability; retain old audit and schedule delta audit |
| 2 | Host-owned architecture and target diagram above |
| 3 | Three paths A/B/C with distinct priority and boundaries |
| 4 | Seven internal governor policies, relevance, pass-through |
| 5 | Preserve 50/52 catalog; minimum effective execution |
| 6 | New advisory request/result and 3.1 envelope compatibility |
| 7 | Help at relevant stages through observable boundaries, without universal interception |
| 8 | Adaptive software-engineering workflow; examples are not mandatory sequence |
| 9 | Guardrails, evidence classes, enum migration |
| 10 | Bounded advocate/challenger/jury deep advisory |
| 11 | Officially verify Claude adapter events and surfaces |
| 12 | Verify Codex adapter and Windows desktop separately |
| 13 | Optional MCP; named tool list is a proposal |
| 14 | Framework/delegation/debate/tool/time/context budgets and early stop |
| 15 | QA of real deliverables; schema or scores do not prove correctness |
| 16 | Preserve user objective, permissions, scope, and output format |
| 17 | Explicit fallback; distinguish advisory from security enforcement |
| 18 | Opt-in memory; Observe → Evaluate → Propose → Test → Approve → Version; optional mastery |
| 19 | Conceptual directory structure; one core, actual host support governs files |
| 20 | A/B/C/D evaluation with negative controls and measured overhead |
| 21 | Phase 0–8 roadmap in the [migration plan](V4_1_MIGRATION_PLAN.md) |
| 22 | Eighteen release criteria become evidence gates, not presumed passes |
| 23 | Distinguish source/proposal/implementation/verification/test/support/blocker states |
| 24 | Map deliverable packages A–G in the migration plan |
| 25 | This review and plan now use English; technical identifiers remain stable |
| 26 | Record implementation sequence as subsequent work within the original review scope |

The next steps at the time of this review were the source delta audit and host-capability verification, followed by a minimum governor and contracts. The [migration plan](V4_1_MIGRATION_PLAN.md) records reviewable order and gates before runtime changes; subsequent implementation status is tracked separately.
