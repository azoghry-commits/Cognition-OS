# Cognition OS development roadmap

Status date: 2026-10-27  
Current package: 0.5.0 engineering candidate  
Target milestone: 0.6.0 evidence-ready candidate

This document is the active development plan after the V4.1 implementation. It converts the remaining repository, host, security, and release gaps into reviewable work. Historical implementation plans remain useful design records, but they do not define the current execution order.

## Product objective

Cognition OS should provide portable cognitive assistance that agent hosts can discover, select, and apply without weakening the host's ownership of tools, permissions, or the requested deliverable. Version 0.6.0 should be supported by reproducible repository checks and observed host evidence. Package structure, installation, or authored evaluation cases alone do not establish a task-quality improvement.

## Current baseline

- The shared core contains 50 mental models, 52 logical specialist definitions, and 12 host-facing skills.
- The locked repository verifier runs dependency audit, lint, typing, pytest with coverage, schema/package validation, and deterministic archive construction.
- Codex, Claude, OpenCode, Antigravity/Gemini, OpenClaw, and portable adapters have separate acceptance boundaries.
- Main-branch CI is cross-platform, but direct `pytest` discovery must remain an explicit gate because external buyers and contributors may invoke the console entry point rather than `python -m pytest`.
- Native installation and skill inventory are engineering evidence. Semantic selection and task-quality improvement require fresh-session positive and negative controls.
- Licensing and external distribution remain owner decisions.

## Delivery order

| Order | Work package | Required evidence | Completion gate |
| --- | --- | --- | --- |
| P0.1 | Reliable direct test discovery | Fresh locked environment; direct collection; full suite and coverage | `pytest --collect-only -q`, `python -m pytest`, and the repository verifier pass on Windows and Ubuntu |
| P0.2 | Credential remediation | Secret-free record of rotation and client reconnection | Replacement is atomic, configuration parses, the old credential is absent and rejected, and the new credential works |
| P0.3 | Context-validity change review | Focused source-and-test changes rebased on current main | Conflicts and open review findings are resolved; Windows, Ubuntu, and package regressions pass |
| P1.1 | Held-out host evaluation | Versioned cases, deterministic rubrics, run IDs, host/model fingerprints, hashes, tokens, latency, and critical-error results | Development and held-out sets are separated; independent semantic review can reproduce the verdict |
| P1.2 | Native host acceptance | Fresh-session explicit, implicit, and negative controls per supported host | Evidence states observed selection, resources, tools, output, limitations, and failures without transferring results between hosts |
| P1.3 | OpenClaw runtime recovery | Native setup and smoke transcript | Isolated-session mismatch is removed and a bounded native smoke succeeds |
| P1.4 | Documentation and release hygiene | Current status, test report, checklist, changelog, version inventory, and license decision | No active guide reports obsolete package/test/skill counts; release gates agree with observed evidence |
| P2.1 | Dependency maintenance | One dependency family per focused PR with full CI | Supported upgrades merge without weakening locked reproducibility |
| Continuous | Mineable maintenance history | Small source-plus-test commits over sustained time | Each behavior change has the proof needed to understand and replay it; history is never fabricated for scoring |

## Planned pull requests

### PR A — make test discovery runner-independent

Problem: an editable install exposed `scripts/cognition.py` as a top-level `cognition` candidate, while test support imports expected `tests` to be importable as a package. The `python -m pytest` path passed, but the direct `pytest` console path failed during collection.

Scope:

- Package only the runtime `cognition` module with setuptools.
- Mark `tests` as a repository test package.
- Run direct collection before the measured coverage suite in local verification and CI.
- Preserve the packaged `scripts/cognition.py` host helper and its archive tests.

Acceptance:

```powershell
uv sync --locked --extra dev
uv run --locked --extra dev pytest --collect-only -q
uv run --locked --extra dev python -m pytest -q
uv run --locked --extra dev coverage run -m pytest -q
uv run --locked --extra dev coverage report --fail-under=80
uv run --locked --extra dev python scripts/verify.py
```

### PR B — land context validity in reviewable slices

Rebase the context-validity work on current main and resolve the platform-specific evaluator finding. Prefer three focused slices when that reduces review risk:

1. context validity, persistence limits, and logging with their behavior tests;
2. generator, CI, and development-container reproducibility;
3. offline evaluator, evidence audit, and evaluation-integrity checks.

Each slice must retain current generator behavior and native-host documentation. Successful replay proves reproducibility; it does not authorize new data collection or attest semantic quality.

### PR C — implement held-out host evidence

Implement the collector and rubric required by issue 2. Use local or subscription-backed host execution already authorized by the user. Do not silently use paid API inference. Freeze thresholds before scoring the held-out set, require explicit critical-error results, and retain conservative scaffolding whenever a gate fails.

### PR D — close host and release gates

Run native acceptance per host, repair OpenClaw, refresh status documents, and record the owner's licensing decision. Release 0.6.0 only after evidence links and rollback artifacts are complete.

## Evidence rules

- Keep `UNKNOWN` for missing host, model, permission, latency, token, or semantic evidence.
- Distinguish discovery, installation, selection, execution, output quality, and comparative gain.
- Record negative controls; a plugin that activates on irrelevant work fails selective-routing acceptance.
- Store no credential values, personal configuration contents, or private prompts in repository evidence.
- Do not add runtime services, health endpoints, or dependencies solely to improve an external score. Architecture changes require a product or reliability need.
- Rescan external quality services only after their underlying repository signals are fixed. Treat the resulting score as external evidence, not a promised outcome.

## 0.6.0 exit criteria

- Direct and module-based pytest discovery work from a fresh locked clone on Windows and Ubuntu.
- The full repository verifier and package archive checks pass at the release commit.
- Context-validity work is merged without unresolved review threads or conflicts.
- At least Codex Desktop and OpenCode have fresh explicit, implicit, and negative-control evidence.
- Held-out evaluation artifacts include provenance, frozen thresholds, critical-error results, and an independently reviewable verdict.
- OpenClaw is either natively accepted or explicitly listed as unsupported with current failure evidence.
- Active documentation agrees on package version, skill inventory, test command, evidence boundary, and remaining gates.
- A license and distribution decision is recorded before public publication or funding-oriented redistribution.

## Work tracking

Update this document only when priority, scope, evidence, or a completion gate changes. Record detailed results in the relevant test, platform, or release report and link them here. A checked repository task does not close its native-host or comparative-quality counterpart.
