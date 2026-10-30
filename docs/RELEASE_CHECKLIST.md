# Release acceptance checklist

**Active candidate:** package 0.5.0 engineering candidate toward 0.6.0. Use the [development roadmap](DEVELOPMENT_ROADMAP.md) for current execution order and the [test report](TEST_REPORT.md) for observed checks. [REBUILD_STATUS_V4_1.md](REBUILD_STATUS_V4_1.md) remains a historical 0.2.0 snapshot and does not describe the active package.

This package is an engineering candidate, not a production-certified release. Refer to TEST_REPORT.md for observed checks.

- [x] One shared source catalog; 50 source names/category memberships and 52 logical roles.
- [x] Native plugin manifests/adapters and focused skills; no separate application.
- [x] Dependency-free deterministic runtime; no required database, Docker, credential or network service.
- [x] Source audit, explicit corrections and traceability inventory.
- [x] Locked verifier covers audit, lint, typing, direct pytest discovery, runtime coverage, package validation, and deterministic archives.
- [x] Windows and Ubuntu CI run the quality gate; a fresh Dev Container separately runs locked installation, pytest, and the coverage floor.
- [x] Active plugin manifests and Python project metadata agree on package 0.5.0.
- [x] Context-validity evidence can be audited and replayed offline without executing archived code.
- [ ] Verify actual Claude activation/resource/tool behavior and semantic outputs across representative cases.
- [ ] Verify actual Codex desktop installation/activation/resource/tool behavior in a fresh chat.
- [ ] Run all 50 model behavioral fidelity cases on target hosts; static contracts do not fulfill this gate.
- [ ] Complete adversarial host evaluations and permission-denial/fallback tests.
- [ ] Collect independently reviewable held-out native quality, latency, token, and critical-error results under frozen thresholds.
- [ ] Accept OpenClaw natively or record its current unsupported state with bounded failure evidence.
- [ ] Owner confirms licensing/distribution terms and explicitly authorizes external publication.

Release policy: preserve versioned ZIP and SHA-256, verify archive inventory, smoke after install, keep rollback version and project cases outside cache. No public upload or marketplace publication is performed by the local packaging script. Upgrade regenerates adapters from canonical core and reruns checks; rollback restores a reviewed prior artifact with schema compatibility review. A passed deterministic test suite cannot close the behavioral or licensing gates.

