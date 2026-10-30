# Test plan

Run the locked repository verifier from the repository root. It is the canonical local equivalent of the CI quality job:

```powershell
uv sync --locked --extra dev
uv run --locked --extra dev python scripts/verify.py
```

The verifier runs dependency audit, Ruff, mypy, direct `pytest --collect-only -q`, the measured `coverage run -m pytest` suite, `coverage report --fail-under=80`, structural package validation, and release archive construction. Direct collection remains explicit because contributors and repository buyers may invoke the pytest console entry point. Coverage measures the `cognition` runtime package. Build, validation, and packaging scripts remain separate executable smoke gates. The default runtime stays dependency-free; development tools are locked in `uv.lock`.

CI also builds `.devcontainer/Dockerfile` and runs the locked install, pytest suite, and 80 percent coverage gate inside that fresh container. Context validity tests cover read-only case checks/retrieval, finite typed facts, freshness boundaries, evidence changes, bounded dependency graphs, workspace-confined evidence reads, schema checks and isolated CLI execution from extracted archives. See CONTEXT_VALIDITY.md for the separate native host evaluation protocol and predeclared acceptance thresholds. Symlink checks may skip where Windows denies creation; report the skip explicitly.

Tests cover independent numerical expectations, boundary probabilities, impossible evidence, zero effort, units, scale direction, cash-flow discounting, explicit simulation distributions/seeds, conservation, DAG and slack; all 50 registry identities and method-specific contracts; all modes and explicit selections; workflow blocking; evidence/provenance and jury rejection; persistence boundaries and archive allowlists.

tests/cognitive-evals/cases.json contains 50 framework behavioral test prompts and method rubrics. references/examples/host-evals.json covers A-E. Static resource/contract tests do not mark those behavioral cases passed. Each actual host run must preserve prompt, selected skill, loaded references, tool IDs/results, response, rubric and observed verdict. Native discovery, semantic fidelity, adversarial prompt handling, permissions, optional calculator fallback and comparative performance are separate gates.

Use Claude's native validator for manifest and local discovery inventory where available. Use a repo-scoped Codex marketplace and inspect its installed plugin skills in a fresh chat. Never report current conversation capability as proof of a newly installed package. Record unsupported/unavailable tooling without fabricating a pass.

Evaluation-integrity tests are in `test_native_eval.py` and `test_offline_eval.py`. They do not call a native solver. See [offline auditing](OFFLINE_EVALUATION_AUDIT.md) for a reproducible regrade of the complete v2 archive and the distinction between historical approval and authorization for new collection.

