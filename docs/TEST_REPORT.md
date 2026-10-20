# Observed verification report

Evidence timestamp: 2026-10-20T03:03:24.009458+00:00. Python 3.13.15. Package 0.1.0 / specification 3.1.

| Check | Observed result | Evidence |
|---|---|---|
| Automated suite | 56 executed: 55 passed, 0 failures, 0 errors, 1 skipped | evidence/checks.json includes raw test output |
| Full JSON Schema | Portable manifest matches downloaded Agent Plugins schema; framework/agent contracts and schema syntax validated with jsonschema 4.26.0 | scripts/validate_package.py; evidence/checks.json |
| Skills | All eleven entrypoints passed bundled skill-creator validation | evidence/checks.json |
| Source fidelity | 50 table identities preserved, category counts 8/8/7/8/6/5/6/2, logical IDs AG-01..52; original source SHA-256 unchanged | tests/test_contracts.py; tests/test_packaging.py; evidence/sources.json |
| Claude manifests | Plugin and marketplace separately accepted without warnings | evidence/checks.json |
| Claude native discovery | 11 skills and 2 agents found through --plugin-dir by Code 2.1.201 | evidence/claude-discovery.json |
| Portable runtime | Archive extracted to a temporary install, helper ran from an unrelated cwd, canonical KT reference loaded and EV verified | tests/test_packaging.py |
| Failure integrity | Invalid operation yields structured FAILED JSON and nonzero exit; missing evidence blocks workflow; jury rejects critical issues | unit and governance tests |
| Local simulation timing | Seven 10,000-sample helper runs; median 11.313 ms on recorded Windows/Python runtime | evidence/benchmark.json; excludes model/host latency |
| Codex read-only inventory | Command succeeded but returned no target plugin record | evidence/codex-discovery.json; discovery/installation remains UNVERIFIED |

The skipped test attempted to create a symbolic link; this Windows environment did not grant the required capability. Path traversal, project boundaries, copied cross-project records, unsafe case IDs, overwrite, deletion consent and case size were still tested. The skip is not counted as a pass. Junction rejection is implemented but not runtime-tested here.

Numerical references include independent Decimal EV, Bayes base-rate calculation, probability endpoints, impossible evidence, log-space updates, RICE factors/units, benefit/cost scale direction, discounted cash flows, explicit reproducible simulation distributions, quantile interpolation, sensitivity, Pareto, stock conservation and a diamond CPM graph. Seeded simulation agreement is evaluated against its sampling error, not asserted as a forecast.

Untested release gates: actual native skill activation and semantic responses in Claude/Codex; all 50 cognitive fidelity prompts; examples A-E host outputs; prompt-injection behavior and permission-denial fallbacks in real hosts; desktop installation/cache refresh; baseline/QUICK/STANDARD/DEEP quality/token/latency comparisons; source licensing/distribution approval. Claude native inventory's ~463 always-on tokens is its estimate, not measured usage. No paid model inference was run.

Versioned runtime/marketplace/QA artifacts are produced by scripts/package_release.py and include content hashes. Local packaging never publishes or installs. The runtime archive excludes source PDFs, raw source Markdown, raw implementation prompt, dev dependencies, test transcripts and global host data. The QA archive supplements this repository and runtime; source-audit reruns require the two original supplied files retained in the repository.

Overall: IMPLEMENTED / PARTIALLY_TESTED candidate. Production readiness is not declared. See PROJECT_STATUS.md for phase gates, limitations and concrete next actions.

Account scope: the user subsequently clarified ChatGPT Plus/Codex and Claude Free. Local Codex authentication was observed to use ChatGPT. Native validation now targets Codex within existing subscription allowance; paid Claude/API calls remain unauthorized and deferred. See ACCOUNT_SCOPE.md. This account clarification does not change the recorded test outcomes or prove installation.

## Subsequent Codex installation and subscription-backed attempt

After explicit Codex-only approval, native marketplace registration and plugin installation succeeded. Native list reports installed=true, enabled=true, version 0.1.0. The clean installed copy contains eleven skills, fifty framework definitions and fifty-two logical roles; source/development files are excluded. See evidence/codex-installation.json. The installed helper independently returned gross EV 1.455 and net EV 0.655 USD million.

The first native model smoke was attempted through verified ChatGPT authentication. It failed before analysis: the CLI-selected gpt-6.1-sol model was rejected for that account route, and the CLI reported an exceeded skills context budget. A localhost MCP transport error was also logged by the inherited CLI environment. No global model/permission/plugin settings were changed to bypass those errors. The incident model smoke was not attempted after this preflight failure. See evidence/codex-smoke-numerical.json and its JSONL events.

This supersedes the earlier no-target inventory observation for installation only. Desktop skill activation, semantic analysis, all fifty behavioral cases and comparative performance remain UNVERIFIED. No Claude or API-billed inference was used. The installation does not establish production readiness.
