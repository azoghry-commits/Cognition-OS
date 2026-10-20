"""Summarize observed QA; never promotes unrun native evaluations."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]

def finalize():
    checks=json.loads((ROOT/'docs/evidence/checks.json').read_text())
    bench=json.loads((ROOT/'docs/evidence/benchmark.json').read_text())
    report=f'''# Observed verification report

Evidence timestamp: {checks['timestamp']}. Python {checks['python']}. Package 0.1.0 / specification 3.1.

| Check | Observed result | Evidence |
|---|---|---|
| Automated suite | {checks['tests_run']} executed: {checks['passed']} passed, {checks['failures']} failures, {checks['errors']} errors, {len(checks['skipped'])} skipped | evidence/checks.json includes raw test output |
| Full JSON Schema | Portable manifest matches downloaded Agent Plugins schema; framework/agent contracts and schema syntax validated with jsonschema 4.26.0 | scripts/validate_package.py; evidence/checks.json |
| Skills | All eleven entrypoints passed bundled skill-creator validation | evidence/checks.json |
| Source fidelity | 50 table identities preserved, category counts 8/8/7/8/6/5/6/2, logical IDs AG-01..52; original source SHA-256 unchanged | tests/test_contracts.py; tests/test_packaging.py; evidence/sources.json |
| Claude manifests | Plugin and marketplace separately accepted without warnings | evidence/checks.json |
| Claude native discovery | 11 skills and 2 agents found through --plugin-dir by Code 2.1.201 | evidence/claude-discovery.json |
| Portable runtime | Archive extracted to a temporary install, helper ran from an unrelated cwd, canonical KT reference loaded and EV verified | tests/test_packaging.py |
| Failure integrity | Invalid operation yields structured FAILED JSON and nonzero exit; missing evidence blocks workflow; jury rejects critical issues | unit and governance tests |
| Local simulation timing | Seven 10,000-sample helper runs; median {bench['median_ms']:.3f} ms on recorded Windows/Python runtime | evidence/benchmark.json; excludes model/host latency |
| Codex read-only inventory | Command succeeded but returned no target plugin record | evidence/codex-discovery.json; discovery/installation remains UNVERIFIED |

The skipped test attempted to create a symbolic link; this Windows environment did not grant the required capability. Path traversal, project boundaries, copied cross-project records, unsafe case IDs, overwrite, deletion consent and case size were still tested. The skip is not counted as a pass. Junction rejection is implemented but not runtime-tested here.

Numerical references include independent Decimal EV, Bayes base-rate calculation, probability endpoints, impossible evidence, log-space updates, RICE factors/units, benefit/cost scale direction, discounted cash flows, explicit reproducible simulation distributions, quantile interpolation, sensitivity, Pareto, stock conservation and a diamond CPM graph. Seeded simulation agreement is evaluated against its sampling error, not asserted as a forecast.

Untested release gates: actual native skill activation and semantic responses in Claude/Codex; all 50 cognitive fidelity prompts; examples A-E host outputs; prompt-injection behavior and permission-denial fallbacks in real hosts; desktop installation/cache refresh; baseline/QUICK/STANDARD/DEEP quality/token/latency comparisons; source licensing/distribution approval. Claude native inventory's ~463 always-on tokens is its estimate, not measured usage. No paid model inference was run.

Versioned runtime/marketplace/QA artifacts are produced by scripts/package_release.py and include content hashes. Local packaging never publishes or installs. The runtime archive excludes source PDFs, raw source Markdown, raw implementation prompt, dev dependencies, test transcripts and global host data. The QA archive supplements this repository and runtime; source-audit reruns require the two original supplied files retained in the repository.

Overall: IMPLEMENTED / PARTIALLY_TESTED candidate. Production readiness is not declared. See PROJECT_STATUS.md for phase gates, limitations and concrete next actions.

Account scope: the user subsequently clarified ChatGPT Plus/Codex and Claude Free. Local Codex authentication was observed to use ChatGPT. Native validation now targets Codex within existing subscription allowance; paid Claude/API calls remain unauthorized and deferred. See ACCOUNT_SCOPE.md. This account clarification does not change the recorded test outcomes or prove installation.
'''
    (ROOT/'docs/TEST_REPORT.md').write_text(report,encoding='utf-8')
    installation=ROOT/'docs/evidence/codex-installation.json'
    if installation.exists():
        observed=json.loads(installation.read_text())
        if observed.get('plugin_setting',{}).get('enabled') is True:
            latest='''\n## Subsequent Codex installation and subscription-backed attempt
\nAfter explicit Codex-only approval, native marketplace registration and plugin installation succeeded. Native list reports installed=true, enabled=true, version 0.1.0. The clean installed copy contains eleven skills, fifty framework definitions and fifty-two logical roles; source/development files are excluded. See evidence/codex-installation.json. The installed helper independently returned gross EV 1.455 and net EV 0.655 USD million.
\nThe first native model smoke was attempted through verified ChatGPT authentication. It failed before analysis: the CLI-selected gpt-6.1-sol model was rejected for that account route, and the CLI reported an exceeded skills context budget. A localhost MCP transport error was also logged by the inherited CLI environment. No global model/permission/plugin settings were changed to bypass those errors. The incident model smoke was not attempted after this preflight failure. See evidence/codex-smoke-numerical.json and its JSONL events.
\nThis supersedes the earlier no-target inventory observation for installation only. Desktop skill activation, semantic analysis, all fifty behavioral cases and comparative performance remain UNVERIFIED. No Claude or API-billed inference was used. The installation does not establish production readiness.\n'''
            with (ROOT/'docs/TEST_REPORT.md').open('a',encoding='utf-8') as stream:stream.write(latest)
    p=ROOT/'docs/RELEASE_CHECKLIST.md'
    text=p.read_text(encoding='utf-8').replace('- [ ] Record numerical, contract, security and package validation outcomes in TEST_REPORT.','- [x] Local numerical, contract, storage and archive checks recorded in TEST_REPORT; one Windows symlink test explicitly skipped.')
    p.write_text(text,encoding='utf-8')
    print(f"Report updated: {checks['passed']} passed, {len(checks['skipped'])} skipped; native gates unchanged.")

if __name__=='__main__':finalize()
