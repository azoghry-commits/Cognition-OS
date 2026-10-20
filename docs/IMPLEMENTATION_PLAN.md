# Cognition OS native plugin implementation

## Rencana aktif: V4.1

Acuan terbaru adalah [kajian konsep V4.1](CONCEPT_V4_1.md) dan [rencana migrasi Phase 0–8](V4_1_MIGRATION_PLAN.md). Urutan: audit delta sumber → verifikasi host → desain governor/kontrak/tiga jalur → prototype minimum dan satu hook yang didukung → kelengkapan core → deep advisory → uji dua adapter → evaluasi A/B/C/D → hardening.

Permintaan 2026-10-20 ditangani sebagai kajian konsep dan dokumentasi. Implementasi hybrid belum dimulai; paket tetap 0.1.0. Perbarui sumber generator sebelum regenerasi agar tidak menimpa arah V4.1 dengan baseline. Gate dan evidence harus dinilai per fase serta per host.

## Rencana historis: baseline 3.1

Specification: 3.1. Package version starts at 0.1.0, independently of specification version.

1. Audit all eight blueprint sections and visually inspect all 15 PDF pages. Preserve hashes, row-level source references, contradictions, and feature transformations.
2. Verify official portable, OpenAI, and Claude formats before generating manifests. Separate documented capabilities from observations on installed clients.
3. Extract AG-01..AG-50 directly from source tables. Map FW-01..FW-50 by numeric correspondence (engineering adaptation; FW-11 is explicitly illustrated). Preserve AG-51 and AG-52. Add framework-specific procedures and contracts.
4. Implement native skills with lazy resources, bounded orchestration, deterministic calculations, evidence validation, optional project-local case storage, and learning workflows. Host supplies analytical judgments; scripts never invent specialist findings.
5. Generate adapters, manifests, local marketplace packages, schemas, reference examples and documentation from canonical assets. No network server, API credentials, hooks or background processes are required.
6. Verify independent numerical references, negative inputs, orchestration dependencies and budgets, all 50 framework contracts, persistence boundaries, packaging, and actual host discovery where available.
7. Package reproducibly; retain a status record and report every unpassed gate. Do not publish or claim production readiness without native behavioral and comparative evaluation evidence.

Acceptance evidence is recorded in TEST_REPORT.md, PLATFORM_COMPATIBILITY.md and RELEASE_CHECKLIST.md. Contract validation alone does not certify cognitive reasoning quality.
