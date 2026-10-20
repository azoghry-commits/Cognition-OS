# Release acceptance checklist

**Kandidat aktif:** rebuild V4.1 / paket 0.2.0. Daftar 18 acceptance criteria dengan status/evidence ada pada [REBUILD_STATUS_V4_1.md](REBUILD_STATUS_V4_1.md). Suite terbaru: 85 tests, 83 passed, 2 symlink skips; routing rules 16/16. Native model selection, hook trust/delivery, semantic fidelity dan benchmark host A/B/C/D belum lulus. Checklist baseline berikut dipertahankan sebagai riwayat; perbandingan mode QUICK/STANDARD/DEEP bukan pengganti eksperimen A/B/C/D V4.1.

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

