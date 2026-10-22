# Development log

## 2026-10-22 — measured scaffolding and repository governance

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
