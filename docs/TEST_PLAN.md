# Test plan

Run the reproducible quality gate from the repository root:

```powershell
uv sync --locked --extra dev
uv run --locked --extra dev ruff check cognition scripts tests
uv run --locked --extra dev coverage run -m unittest discover -s tests -q
uv run --locked --extra dev coverage report --fail-under=80
uv run --locked --extra dev coverage xml
uv run --locked --extra dev python scripts/validate_package.py
uv run --locked --extra dev python scripts/package_release.py
```

Coverage measures the `cognition` runtime package. Build, validation, and packaging scripts remain separate executable smoke gates. The default runtime stays dependency-free; `jsonschema`, Coverage.py, and Ruff are development extras locked in `uv.lock`.

Also run `uv run --locked --extra dev mypy cognition`, matching CI. Context validity tests cover read-only case checks/retrieval, finite typed facts, freshness boundaries, evidence changes, bounded dependency graphs, workspace-confined evidence reads, schema checks and isolated CLI execution from extracted archives. See CONTEXT_VALIDITY.md for the separate native host evaluation protocol and predeclared acceptance thresholds. Symlink checks may skip where Windows denies creation; report the skip explicitly.

Tests cover independent numerical expectations, boundary probabilities, impossible evidence, zero effort, units, scale direction, cash-flow discounting, explicit simulation distributions/seeds, conservation, DAG and slack; all 50 registry identities and method-specific contracts; all modes and explicit selections; workflow blocking; evidence/provenance and jury rejection; persistence boundaries and archive allowlists.

tests/cognitive-evals/cases.json contains 50 framework behavioral test prompts and method rubrics. references/examples/host-evals.json covers A-E. Static resource/contract tests do not mark those behavioral cases passed. Each actual host run must preserve prompt, selected skill, loaded references, tool IDs/results, response, rubric and observed verdict. Native discovery, semantic fidelity, adversarial prompt handling, permissions, optional calculator fallback and comparative performance are separate gates.

Use Claude's native validator for manifest and local discovery inventory where available. Use a repo-scoped Codex marketplace and inspect its installed plugin skills in a fresh chat. Never report current conversation capability as proof of a newly installed package. Record unsupported/unavailable tooling without fabricating a pass.


## Explicit enforcement and generator scope

CI runs `uv run --locked --extra dev python -m unittest discover -s tests -q` in its named Run unit tests step, then collects coverage separately. A temporary failing-test branch was pushed and reverted; [enforcement evidence](DATAFACTOR_REASSESSMENT_2026-10-24.md) records actual red and green runs, plus a local coverage-wrapper exit1 probe.

Logging tests cover opt-in JSON stderr, root logger isolation, routing metadata, no task-content leakage and handler lifecycle. Generator tests use temporary projects rather than rewriting repository resources. Measure generators separately:

```powershell
uv run --locked --extra dev coverage run --data-file=.coverage.generators --source=scripts -m unittest discover -s tests -p "test_build*.py" -q
uv run --locked --extra dev coverage report --data-file=.coverage.generators --include="*/scripts/build_catalog.py,*/scripts/build_docs.py,*/scripts/build_hybrid.py" --fail-under=0
```

This informational generator report has no 80% claim; the ordinary runtime report still enforces 80%. The container-smoke CI job uses the Dev Container Dockerfile, a fresh checkout and the README locked install/test sequence.

Evaluation integrity tests are in test_native_eval.py and test_offline_eval.py. They do not call a native solver. See [offline auditing](OFFLINE_EVALUATION_AUDIT.md) for a reproducible regrade of the complete v2 archive and the distinction between historical approval and new collection authorization.
