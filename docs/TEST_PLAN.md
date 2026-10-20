# Test plan

Run `python -m unittest discover -s tests -v`, `python scripts/validate_package.py`, `python scripts/benchmark.py`, and `python scripts/package_release.py` from the repository root. Optional full-schema QA: install jsonschema into project-local .dev-deps and run the validator with that path on sys.path; runtime stays dependency-free.

Tests cover independent numerical expectations, boundary probabilities, impossible evidence, zero effort, units, scale direction, cash-flow discounting, explicit simulation distributions/seeds, conservation, DAG and slack; all 50 registry identities and method-specific contracts; all modes and explicit selections; workflow blocking; evidence/provenance and jury rejection; persistence boundaries and archive allowlists.

tests/cognitive-evals/cases.json contains 50 framework behavioral test prompts and method rubrics. references/examples/host-evals.json covers A-E. Static resource/contract tests do not mark those behavioral cases passed. Each actual host run must preserve prompt, selected skill, loaded references, tool IDs/results, response, rubric and observed verdict. Native discovery, semantic fidelity, adversarial prompt handling, permissions, optional calculator fallback and comparative performance are separate gates.

Use Claude's native validator for manifest and local discovery inventory where available. Use a repo-scoped Codex marketplace and inspect its installed plugin skills in a fresh chat. Never report current conversation capability as proof of a newly installed package. Record unsupported/unavailable tooling without fabricating a pass.

