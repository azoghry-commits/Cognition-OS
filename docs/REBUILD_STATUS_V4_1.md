# Cognition OS V4.1 rebuild status

Date: 2026-10-20. Candidate package: **0.2.0**; specification: **4.1**. Status: locally `IMPLEMENTED` / `TESTED`; native acceptance and production readiness remain open.

The user requested an English README, Git work, then migration, and subsequently clarified that the plugin should be rebuilt for V4.1. The initial README was committed and pushed as `95122dc`; a concurrent README update at `67783e9` was preserved. Under recorded Codex-only authorization, candidate 0.2.0 was installed through the native CLI and reported installed/enabled. Hook trust, credentials, global memory, and user cases were not changed. The Claude adapter was not installed.

## Phase progress

| Phase | Status | Evidence / boundary |
|---|---|---|
| 0 Source audit | `TESTED` for identity and coverage; manual inspection complete | All 1,362 lines / eight sections of A, fresh rendering and review of all 15 pages of B, 50 models, 52 roles, 24 feature groups. [Audit](SOURCE_TRANSFORMATION_V4_1.md) and [JSON](evidence/v4-1-source-audit.json) |
| 1 Platform verification | Documentation `VERIFIED`; runtime `PARTIALLY_SUPPORTED` | Official documentation reviewed; local CLI versions observed; surface support and account limits separated. [Verification](PLATFORM_VERIFICATION_V4_1.md) |
| 2 Hybrid design | Locally `IMPLEMENTED` / `TESTED` | Seven-policy governor, context/budget, three paths, request/result, 3.1 compatibility, failure policy. [Architecture](HYBRID_ARCHITECTURE.md) |
| 3 Minimal native prototype | Locally `IMPLEMENTED` / `TESTED`; native gate open | Model-facing entrypoints and MECE/First Principles/5 Whys/Pre-Mortem core; read-only PostToolUse hook; packaged execution and payload fixtures tested. Model selection and native event delivery not observed |
| 4 Full core | Structurally `IMPLEMENTED` / `TESTED` | All 50 definitions/contracts regenerated; source IDs and categories retained, along with 52 roles. Behavioral fidelity of the 50 models remains `NOT_RUN_ON_HOST` |
| 5 Deep advisory | Locally `IMPLEMENTED` / `TESTED` | Bounded plan and advocate/challenger/jury skill; budget, prior-analysis sufficiency, and critical-gap tests. No fabricated native dispatch or model calls |
| 6 Dual integration | `PARTIALLY_SUPPORTED` / `PARTIALLY_TESTED` | Two adapter manifests/hooks, schema validation, Claude manifest validation, and extracted-package launcher checks. Codex 0.2.0 installed/enabled and its installed helper tested. Claude native inference/installation deferred under account scope; native semantic acceptance open |
| 7 Evaluation | Deterministic routing `TESTED`; host benchmark `NOT_RUN` | All 16 authored routing cases passed. A/B/C/D task success, host tokens, and latency remain null/unmeasured. [Results](evidence/v4-1-activation-evals.json) |
| 8 Hardening | `PARTIALLY_TESTED` | Evidence, malformed payload, path/scope, artifact size, nonblocking failure, numerical references, and portable archives tested. Two symlink tests skipped by OS. Native permissions/trust, cross-event caching, semantic quality, and distribution gates remain open |

Phases depending on native gates were prepared and tested locally without being declared complete. No 3.1 evidence is used to pass V4.1 behavioral gates.

## Local verification

Candidate suite at this status snapshot: **85 tests, 83 passed, 0 failed/errors, 2 skipped**. Both skips involved Windows symlink-creation permissions; traversal and out-of-scope path tests still ran. New tests covered unavailable required checks, duplicate evidence/claims, unsupported inference links, inconsistent calculation records, exhausted budgets, oversized advisory output, untrusted content, and noninterference with unrelated batch edits.

Full JSON Schema validation covered 50 framework input/output contracts, 52 roles, 12 skills, the portable manifest, and V4.1 contracts. Framework artifact contract 3.1 intentionally remains available. Scripts/helpers and configured hook launchers were tested from extracted archives at paths containing spaces, separately from the source repository. The Claude manifest was validated without inference or account installation.

Reproducible commands:

```powershell
python scripts/rebuild_plugin.py
python scripts/verify_rebuild.py
python -m unittest discover -s tests -v
python scripts/evaluate_activation.py
python scripts/validate_package.py
python scripts/package_release.py
```

The latest structured verification log is [v4-1-checks.json](evidence/v4-1-checks.json). Local package checksums are in `dist/SHA256SUMS.json`; installable artifacts are `dist/cognition-os-0.2.0.zip`, `dist/cognition-os-marketplace-0.2.0.zip`, and `dist/cognition-os-qa-0.2.0.zip`. Raw source files and the PDF are excluded from runtime archives. Building/packaging does not install or trust hooks.

## Eighteen V4.1 acceptance criteria

| # | Prompt section 22 criterion | Candidate status / gate |
|---|---|---|
| 1 | Host-agent augmentation layer | Implemented as skills/core; effect on native tasks unproven |
| 2 | Three supported activation paths | Implemented locally; native invocation/event gate open |
| 3 | No unsupported interception claim | Design/instructions limit operation to native skills and verified events |
| 4 | Model-selected skills work on host | Metadata ready; actual selection `NOT_RUN_ON_HOST` |
| 5 | Checks through authorized hooks | Fixtures/launcher pass; trust and native event delivery untested |
| 6 | Selective deep advisory | Rules/negative control pass; model behavior not evaluated |
| 7 | Preserve 50 models | Source identity, categories, methods, and contracts tested |
| 8 | Preserve 52 logical specialists | Stable AG IDs tested; does not imply 52 processes |
| 9 | Host owns the task | Contracts/skills explicitly preserve host authority; native observation needed |
| 10 | Do not replace user deliverable with plugin report | Internal output instructions aligned; native output evaluation open |
| 11 | No required standalone app | No additional app/server built |
| 12 | No required Docker/database server | Local runtime helper/resources; memory optional |
| 13 | Verify mathematics | Independent references and negative-input suite pass |
| 14 | Security/permission boundaries | Path/scope/evidence tested; symlink and native permission/trust not fully tested |
| 15 | Measurable quality improvement | Host A/B/C/D `NOT_RUN`; no improvement claim |
| 16 | Control overhead/unnecessary activation | Lazy resources, bounded checks, 16 rule cases; host tokens/latency/activation unmeasured |
| 17 | Test adapters separately | Separate structure and configured launchers tested; each native acceptance remains open |
| 18 | Install/update/rollback | Codex 0.2.0 update and installed hashes/helper verified; 0.1.0 rollback backup retained. Backup restore and desktop activation untested |

## Boundaries and next validation steps

Candidate 0.2.0 replaced the active Codex version via `codex plugin add cognition-os@cognition-os-local --json`; version 0.1.0 is retained in a local rollback backup. See [installation evidence](evidence/v4-1-codex-installation.json). Open a new chat or refresh/restart the app to load the latest package, then review hook trust in the host UI; installation does not prove trust or event delivery. Test a natural task and a negative control, recording selected skills/resources, tools, deliverables, and gaps. Run A/B/C/D benchmarks only within authorized account/budget scope. Earlier baseline CLI smoke failed before analysis due to model/context preflight; that failure is not represented as candidate success. No fallback to API billing or Claude inference was used.

The hook provides structural advice only and does not replace an OS sandbox. Link/junction checks are prechecks, not a guarantee against malicious filesystem races. Content-hash deduplication is limited to one event; cross-process caching and its effectiveness are a separate optimization gate. A production-ready claim requires evidence for every relevant gate.
