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
