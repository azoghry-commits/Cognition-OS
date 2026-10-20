# Architecture decisions

## Arah V4.1

Pada 2026-10-20, prompt V4.1 diterima sebagai arah konsep berikutnya. Identitas target adalah augmentation layer untuk agen host, dengan satu core, dual adapter, tiga jalur bantuan dan governor selektif. Status desain target `SOURCE_DERIVED` / `PROPOSED`; keputusan implementasi, dukungan host, dan rilis harus memiliki evidence sendiri. Detail: [kajian konsep](CONCEPT_V4_1.md), [rencana migrasi](V4_1_MIGRATION_PLAN.md).

ADR-02 tetap mempertahankan satu katalog; jumlah/nama skill target mengikuti kebutuhan. ADR-05 berarti MCP/hook tidak wajib bagi baseline; V4.1 mengusulkan hook deterministik selektif pada host yang mendukung. Pernyataan tidak ada hook/daemon pada tabel merujuk paket 0.1.0. Versi paket dan schema tidak dinaikkan oleh kajian ini.

## Keputusan baseline 3.1

| Decision | Rationale | Classification | Consequence |
|---|---|---|---|
| ADR-01 root portable manifest + Claude manifest + optional Codex fallback | Current official packaging formats | EXTERNALLY_VERIFIED | Root com.openai replaces fallback OpenAI settings, never merged |
| ADR-02 one catalog, eleven skills | Preserve 50 models with progressive disclosure | ENGINEERING_ADAPTATION | Definitions loaded only when relevant |
| ADR-03 host reasoning + pure Python helper | Native UX, no separate credentials/backend | ENGINEERING_ADAPTATION | Semantic quality depends on host and must be behavior-tested |
| ADR-04 two reusable Claude wrappers | Native delegation without 52 always-visible agents | ENGINEERING_ADAPTATION | Logical role IDs stay stable; no runtime concurrency claim |
| ADR-05 no required MCP/hooks | Existing host file/code tools suffice | ENGINEERING_ADAPTATION | No installation-time executable or daemon |
| ADR-06 explicit finite math inputs/distributions | Source formulas and examples conflict | CONFLICTING -> ENGINEERING_ADAPTATION | Reject rather than silently clamp or invent |
| ADR-07 plain project JSON, explicit consent | Local-first optional memory | ENGINEERING_ADAPTATION | No encryption claim; project relocation needs reviewed migration |
| ADR-08 version 0.1.0, readiness gated | Spec 3.1 is not evidence of mature software | ENGINEERING_ADAPTATION | Host behavior, benchmarks and licensing remain gates |
| ADR-09 no public licensing assertion | Source ownership terms are unspecified | UNVERIFIED | No LICENSE grant fabricated; publication blocked pending owner decision |

Changes to trusted instructions follow Observe -> Evaluate -> Propose -> Test -> Approve -> Version -> Deploy. Each accepted change must include rationale, before/after, regression evidence, approval record and rollback. This is governed engineering, not model retraining.

