# Development log

## 2026-10-24 — native context validity evaluation

- Completed 20 pairs with gpt-5.6-luna, low reasoning, after human label approval. Candidate exact decisions 20/20 versus baseline 18/20; all 20 helper executions verified from fixture-bound command/output evidence.
- Product acceptance failed: median paired latency overhead 59.1% against maximum 20%. Capability verdict IMPROVED_NOT_SIGNIFICANT (delta 0.0667, p=0.5). Token usage increased; no efficiency or production-readiness claim.
- Added collection/audit harness, 13 regression tests and inspectable raw evidence. Lightweight review exposed echoed-command false positives; command parsing, complete result matching and input-hash binding now reject them. Regraded existing logs without additional inference or runtime tuning.
- Final local gate: 151 tests run, 1 skipped (Windows symlink permission), runtime coverage 85%; Ruff, mypy, structural package validation and all four package builds passed. Offline regrade from archived raw logs reproduced the published summary; archive checksum, auditor and frozen runtime verified. Linux CI was not run in this turn.
- See [native evaluation report](NATIVE_CONTEXT_VALIDITY_EVALUATION.md). P4 measurement is complete; acceptance and release promotion remain unmet. Next optimize on development cases and use a new held-out confirmation set.

## 2026-10-23 â€” context validity MVP

- Managed worktree `context-validity`, branch `feat/context-validity`, base `6d1edfa`. Original checkout and unrelated dirty files preserved. Bounded-storage dependency reviewed and committed separately as `d386dd8`.
- Implemented P1â€“P3: applicability v1 metadata, typed/fresh observed facts, evidence fingerprints, read-only stored-case checks and optional retrieval filtering; bounded dependency impact and workspace evidence snapshots; CLI, schemas, example, skill/generator guidance and documentation.
- Red/green evidence: reproduced old storage failures, absent validity/impact APIs and retrieval filter, then timestamp UTC overflow identified by a fresh reviewer. Added a failing regression and fixed the timestamp conversion. No other concrete defect was identified in that review.
- Final local gate: 138 tests run, 1 skipped (Windows symlink creation unavailable), runtime coverage 85% against current 80% floor; Ruff and mypy passed; 50 framework/52 role/12 skill structural schema validation and all release archives passed. Extracted-package commands run with isolated Python in a path containing spaces.
- Full rebuild/package succeeded in a disposable repository copy; authored skill and schemas survived generation with platform newlines normalized. pip-audit found no known dependency vulnerabilities; unpublished local cognition-os package could not be audited against PyPI. Cache-deserialization warnings were emitted by the audit client.
- P4 native paired task evaluation is NOT_RUN; cross-host behavior, automatic selection, task improvement and production readiness are not established. Thresholds and collection protocol are predeclared in CONTEXT_VALIDITY.md. Package version remains 0.5.0 for local development; no release or installation performed. Future failure-regression, experiment-selection and sensitivity work remains separate backlog.

## 2026-10-22 â€” measured scaffolding and repository governance

- Analyzed feasibility using the Cognition OS orchestrator and FW-49. Offline advisory selection is feasible; automatic deployment and real-model capability claims remain gated.
- Found existing paired evaluation and manual capability profiles. Existing test scores are synthetic, not measurements of current host ability.
- Found unrelated storage changes in the working tree; preserve them outside this change set.
- Started a consistent installation guide structure and documented branch, version, PR and release responsibilities.
- GitHub connector resolves the public repository and reports push/admin permission. Local GitHub CLI authentication returned HTTP 401. Remote metadata and release mutations need a working authorized interface; never record them as completed from prepared files alone.

Validation results and actual remote links are appended after execution.

- Feature commit c84e889: clean source passed 109 tests on Windows locally; PR #1 opened. Linux CI passed; Windows CI revealed existing short-path alias handling in artifact validation. Fixed lexical/canonical workspace handling and added an alias regression test, preserving child-link exclusion.
- Baseline main 2213cda: clean source passed 104 local tests; schema validation passed with jsonschema 4.26.0 supplied through the development dependency path. Native hooks and semantic quality remain unverified.

## Verified remote outcome

- [PR #1](https://github.com/azoghry-commits/Cognition-OS/pull/1): feat/measured-scaffolding into main; implementation and guides remain reviewable on the feature branch.
- Commit adb0a00036331aab0ce0dbcdb4d38e455fcd5e42: [Windows/Linux CI run](https://github.com/azoghry-commits/Cognition-OS/actions/runs/39679309784) completed successfully after the alias fix.
- [Engineering prerelease v0.5.0](https://github.com/azoghry-commits/Cognition-OS/releases/tag/v0.5.0): published from main 2213cdaa52c9455095d44454ebbdffdefab46f9d, four ZIP assets plus SHA256SUMS.json. Server-reported asset digests match the clean package checksums. Release notes disclose native acceptance gaps and the Windows alias issue fixed in PR #1.
- Repository About description and five topics updated and read back successfully.
- [Issue #2](https://github.com/azoghry-commits/Cognition-OS/issues/2) tracks real host collection, held-out scoring and policy activation gates for the next feature cycle.
- Local uncommitted storage files remain outside this work. No host installation, paid provider inference, automatic policy activation or main-branch merge was performed.
