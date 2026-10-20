# Architecture decisions

## V4.1 direction

On 2026-10-20, the V4.1 prompt was accepted as the next conceptual direction. The target is an augmentation layer for host agents, with one core, two adapters, three assistance paths, and a selective governor. Target design status is `SOURCE_DERIVED` / `PROPOSED`; implementation decisions, host support, and releases require their own evidence. See the [concept review](CONCEPT_V4_1.md) and [migration plan](V4_1_MIGRATION_PLAN.md).

ADR-02 retains one catalog; the target skill count and names follow actual needs. ADR-05 means MCP/hooks were optional for the baseline; V4.1 proposes selective deterministic hooks on supporting hosts. The table's no-hook/no-daemon statement refers to package 0.1.0. This concept review alone did not advance package or schema versions.

## Baseline 3.1 decisions

| Decision | Rationale | Classification | Consequence |
|---|---|---|---|
| ADR-01 root portable manifest + Claude manifest + optional Codex fallback | Current official packaging formats | EXTERNALLY_VERIFIED | Root com.openai replaces fallback OpenAI settings, never merged |
| ADR-02 one catalog, eleven skills | Preserve 50 models with progressive disclosure | ENGINEERING_ADAPTATION | Definitions loaded only when relevant |
| ADR-03 host reasoning + pure Python helper | Native UX, no separate credentials/backend | ENGINEERING_ADAPTATION | Semantic quality depends on host and must be behavior-tested |
| ADR-04 two reusable Claude wrappers | Native delegation without 52 always-visible agents | ENGINEERING_ADAPTATION | Logical role IDs stay stable; no runtime concurrency claim |
| ADR-05 no required MCP/hooks | Existing host file/code tools suffice | ENGINEERING_ADAPTATION | No installation-time executable or daemon |
| ADR-06 explicit finite math inputs/distributions | Source formulas and examples conflict | CONFLICTING -> ENGINEERING_ADAPTATION | Reject rather than silently clamp or invent |
| ADR-07 plain project JSON, explicit consent | Local-first optional memory | ENGINEERING_ADAPTATION | No encryption claim; project relocation needs reviewed migration |
| ADR-08 version 0.1.0, readiness gated | Spec 3.1 is not evidence of mature software | ENGINEERING_ADAPTATION | Host behavior, benchmarks and licensing remain gates |
| ADR-09 no public licensing assertion | Source ownership terms are unspecified | UNVERIFIED | No LICENSE grant fabricated; publication blocked pending owner decision |

Changes to trusted instructions follow Observe -> Evaluate -> Propose -> Test -> Approve -> Version -> Deploy. Each accepted change must include rationale, before/after, regression evidence, approval record and rollback. This is governed engineering, not model retraining.

