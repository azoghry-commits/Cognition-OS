# Release acceptance checklist

**Active candidate:** V4.1 rebuild / package 0.2.0. The 18 acceptance criteria and their status/evidence are in [REBUILD_STATUS_V4_1.md](REBUILD_STATUS_V4_1.md). At the time of this record, the suite had 85 tests: 83 passed and two symlink tests skipped; routing rules passed 16/16. Native model selection, hook trust/delivery, semantic fidelity, and host A/B/C/D benchmarks remained open. The following baseline checklist is retained as history; QUICK/STANDARD/DEEP mode comparisons do not replace the V4.1 A/B/C/D experiment.

This package is an engineering candidate, not a production-certified release. Refer to TEST_REPORT.md for observed checks.

- [x] One shared source catalog; 50 source names/category memberships and 52 logical roles.
- [x] Native plugin manifests/adapters and focused skills; no separate application.
- [x] Dependency-free deterministic runtime; no required database, Docker, credential or network service.
- [x] Source audit, explicit corrections and traceability inventory.
- [x] Local numerical, contract, storage and archive checks recorded in TEST_REPORT; one Windows symlink test explicitly skipped.
- [ ] Verify actual Claude activation/resource/tool behavior and semantic outputs across representative cases.
- [ ] Verify actual Codex desktop installation/activation/resource/tool behavior in a fresh chat.
- [ ] Run all 50 model behavioral fidelity cases on target hosts; static contracts do not fulfill this gate.
- [ ] Complete adversarial host evaluations and permission-denial/fallback tests.
- [ ] Collect baseline/QUICK/STANDARD/DEEP native quality, latency and instrumented token comparisons.
- [ ] Owner confirms licensing/distribution terms and explicitly authorizes external publication.

Release policy: preserve versioned ZIP and SHA-256, verify archive inventory, smoke after install, keep rollback version and project cases outside cache. No public upload or marketplace publication is performed by the local packaging script. Upgrade regenerates adapters from canonical core and reruns checks; rollback restores a reviewed prior artifact with schema compatibility review. A passed deterministic test suite cannot close the behavioral or licensing gates.

