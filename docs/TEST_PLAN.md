# Test plan

Run the reproducible quality gate from the repository root:

```powershell
uv sync --locked --extra dev
uv run --locked --extra dev ruff check cognition scripts tests
uv run --locked --extra dev coverage run -m unittest discover -s tests -q
uv run --locked --extra dev coverage report --fail-under=70
uv run --locked --extra dev coverage xml
uv run --locked --extra dev python scripts/validate_package.py
uv run --locked --extra dev python scripts/package_release.py
```

Coverage measures the `cognition` runtime package. Build, validation, and packaging scripts remain separate executable smoke gates. The default runtime stays dependency-free; `jsonschema`, Coverage.py, and Ruff are development extras locked in `uv.lock`.

Tests cover independent numerical expectations, boundary probabilities, impossible evidence, zero effort, units, scale direction, cash-flow discounting, explicit simulation distributions/seeds, conservation, DAG and slack; all 50 registry identities and method-specific contracts; all modes and explicit selections; workflow blocking; evidence/provenance and jury rejection; persistence boundaries and archive allowlists.

tests/cognitive-evals/cases.json contains 50 framework behavioral test prompts and method rubrics. references/examples/host-evals.json covers A-E. Static resource/contract tests do not mark those behavioral cases passed. Each actual host run must preserve prompt, selected skill, loaded references, tool IDs/results, response, rubric and observed verdict. Native discovery, semantic fidelity, adversarial prompt handling, permissions, optional calculator fallback and comparative performance are separate gates.

Use Claude's native validator for manifest and local discovery inventory where available. Use a repo-scoped Codex marketplace and inspect its installed plugin skills in a fresh chat. Never report current conversation capability as proof of a newly installed package. Record unsupported/unavailable tooling without fabricating a pass.

