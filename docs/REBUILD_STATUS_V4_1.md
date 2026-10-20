# Status rebuild Cognition OS V4.1

Tanggal: 2026-10-20. Paket kandidat: **0.2.0**, spesifikasi: **4.1**. Status: `IMPLEMENTED` / `TESTED` lokal, acceptance native dan production readiness belum terpenuhi.

Permintaan pengguna: README berbahasa Inggris, proses Git, lalu pelaksanaan migrasi; kemudian diperjelas menjadi rebuild plugin menurut V4.1. README awal telah di-commit dan di-push sebagai `95122dc`; pembaruan README `67783e9` yang muncul selama pekerjaan dipertahankan. Dengan otorisasi Codex-only yang sudah tercatat, kandidat 0.2.0 dipasang melalui CLI native dan dilaporkan installed/enabled. Trust hook, credential, global memory, serta kasus pengguna tidak diubah. Adapter Claude tidak dipasang.

## Kemajuan fase

| Phase | Status | Bukti / batas |
|---|---|---|
| 0 Source audit | `TESTED` untuk identitas dan coverage; inspeksi manual selesai | Seluruh 1.362 baris A / delapan bagian, render baru dan review 15 halaman B, 50 model, 52 role, 24 feature groups. [Audit](SOURCE_TRANSFORMATION_V4_1.md) dan [JSON](evidence/v4-1-source-audit.json) |
| 1 Platform verification | `VERIFIED` dokumentasi; `PARTIALLY_SUPPORTED` runtime | Dokumentasi resmi dibuka ulang; versi CLI lokal diamati; dukungan tiap surface dan batas akun dipisahkan. [Verifikasi](PLATFORM_VERIFICATION_V4_1.md) |
| 2 Hybrid design | `IMPLEMENTED` / `TESTED` lokal | Governor tujuh policy, context/budget, tiga jalur, request/result, compatibility 3.1, failure policy. [Arsitektur](HYBRID_ARCHITECTURE.md) |
| 3 Minimal native prototype | `IMPLEMENTED` / `TESTED` lokal; native gate terbuka | Model-facing entrypoints dan core MECE/First Principles/5 Whys/Pre-Mortem; hook PostToolUse read-only; packaged execution dan payload fixtures diuji. Pemilihan model dan event native belum teramati |
| 4 Full core | `IMPLEMENTED` / `TESTED` struktur | Semua 50 definisi/kontrak diperbarui dari generator; source IDs dan kategori tetap. 52 role dipertahankan. Behavioral fidelity 50 model tetap `NOT_RUN_ON_HOST` |
| 5 Deep advisory | `IMPLEMENTED` / `TESTED` lokal | Bounded plan dan skill untuk advocate/challenger/jury, pengujian budget, prior-analysis sufficiency dan critical gaps. Tidak ada native dispatch atau model call buatan |
| 6 Dual integration | `PARTIALLY_SUPPORTED` / `PARTIALLY_TESTED` | Dua manifest/hook adapter, schema validation, Claude manifest validation dan extracted-package launcher checks. Codex 0.2.0 installed/enabled dan helper terpasang diuji. Claude native inference/instalasi tidak dijalankan sesuai account scope; native semantic acceptance masih terbuka |
| 7 Evaluation | `TESTED` untuk routing deterministik; benchmark host `NOT_RUN` | 16 authored routing cases lulus. A/B/C/D, task success, tokens dan latency host tetap null/belum diukur. [Hasil](evidence/v4-1-activation-evals.json) |
| 8 Hardening | `PARTIALLY_TESTED` | Uji bukti, malformed payload, path/scope, ukuran artifact, nonblocking failure, numerical references dan portable archives. Dua uji symlink dilewati OS. Native permission/trust, cache lintas event, semantic quality dan distribusi belum menutup gate |

Phase yang bergantung pada gate native dipersiapkan dan diuji lokal tanpa menyatakannya selesai. Tidak ada evidence 3.1 dipakai untuk meluluskan gate perilaku V4.1.

## Verifikasi lokal

Suite kandidat: **85 test, 83 passed, 0 failed/errors, 2 skipped**. Kedua skip terkait izin membuat symlink di Windows; pengujian traversal/path luar scope tetap dijalankan. Uji baru mencakup required check yang tidak tersedia, duplicate evidence/claim, inference tanpa link, ketidakcocokan record kalkulasi, budget habis, advisory terlalu besar, konten tak tepercaya serta noninterference pada batch edit yang tidak relevan.

Full JSON Schema validation: 50 framework input/output contracts, 52 role, 12 skill, manifest portabel dan kontrak V4.1. Kontrak artifact framework 3.1 sengaja tetap tersedia. Skrip/helper serta configured hook launcher diuji dari archive yang diekstrak pada path dengan spasi, terpisah dari repo sumber. Manifest Claude diuji tanpa inference atau instalasi akun.

Perintah yang dapat dijalankan ulang:

```powershell
python scripts/rebuild_plugin.py
python scripts/verify_rebuild.py
python -m unittest discover -s tests -v
python scripts/evaluate_activation.py
python scripts/validate_package.py
python scripts/package_release.py
```

Log verifikasi terstruktur terbaru ada di [v4-1-checks.json](evidence/v4-1-checks.json). Checksum paket lokal disimpan di `dist/SHA256SUMS.json`; artefak installable `dist/cognition-os-0.2.0.zip`, marketplace `dist/cognition-os-marketplace-0.2.0.zip`, dan QA `dist/cognition-os-qa-0.2.0.zip`. Paket raw source dan PDF tidak dimasukkan ke runtime archive. Build/packaging tidak memasang atau memercayai hook.

## Delapan belas acceptance criteria V4.1

| # | Kriteria prompt bagian 22 | Status kandidat / gate |
|---|---|---|
| 1 | Host-agent augmentation layer | Implemented sebagai skill/core; efek pada tugas native belum dibuktikan |
| 2 | Tiga activation paths sesuai dukungan | Implemented lokal; native invocation/event gate terbuka |
| 3 | Tidak mengklaim unsupported interception | Desain dan instruksi membatasi diri pada native skills dan event terverifikasi |
| 4 | Model-selected skills bekerja pada host | Metadata disiapkan; selection aktual `NOT_RUN_ON_HOST` |
| 5 | Checks lewat authorized hooks | Fixture/launcher lulus; trust dan native event delivery belum diuji |
| 6 | Deep advisory selektif | Rule/negative-control lulus; perilaku model belum dievaluasi |
| 7 | 50 model terpelihara | Source identity, kategori, metode dan kontrak diuji |
| 8 | 52 spesialis logis terpelihara | Stable AG IDs diuji; tidak berarti 52 proses |
| 9 | Host tetap pemilik tugas | Kontrak/skill secara eksplisit mempertahankan otoritas host; perlu observasi native |
| 10 | Deliverable pengguna tidak diganti laporan plugin | Instruksi internal output diselaraskan; native output evaluation terbuka |
| 11 | Tanpa aplikasi mandiri wajib | Tidak ada aplikasi/server tambahan dibangun |
| 12 | Tanpa Docker/database server wajib | Runtime helper lokal dan resources; memory opsional |
| 13 | Verifikasi matematika | Referensi independen dan negative input suite lulus |
| 14 | Security/permission boundaries | Path/scope/bukti diuji; symlink dan native permission/trust belum sepenuhnya diuji |
| 15 | Quality improvement terukur | `NOT_RUN` untuk host A/B/C/D; tidak ada klaim peningkatan |
| 16 | Overhead/unnecessary activation dikontrol | Lazy resources, bounded checks, 16 rule cases; token/latency/activation host belum diukur |
| 17 | Adapter diuji terpisah | Struktur dan configured launcher terpisah diuji; acceptance native masing-masing masih terbuka |
| 18 | Install/update/rollback | Update Codex 0.2.0 dan hash/helper terpasang diverifikasi; backup rollback 0.1.0 disimpan. Restore backup dan desktop activation belum diuji |

## Batas dan langkah validasi berikutnya

Kandidat 0.2.0 sudah menggantikan versi aktif Codex melalui `codex plugin add cognition-os@cognition-os-local --json`; versi 0.1.0 disimpan dalam backup rollback lokal. Lihat [bukti instalasi](evidence/v4-1-codex-installation.json). Buka chat baru atau refresh/restart aplikasi agar memuat paket terbaru, lalu tinjau trust hook melalui UI host; instalasi tidak membuktikan trust/event delivery. Uji task natural dan negative control, catat selected skill/resource, tools, deliverable dan gap. Jalankan benchmark A/B/C/D hanya dalam account/budget scope yang diotorisasi. CLI smoke baseline sebelumnya gagal sebelum analisis akibat model/context preflight; kegagalan tersebut tidak disamarkan sebagai keberhasilan kandidat baru. Tidak ada fallback ke API billing atau inference Claude.

Hook hanya structural advisory dan tidak menggantikan sandbox OS. Pemeriksaan link/junction adalah pre-check, bukan jaminan melawan malicious filesystem race. Deduplikasi content hash masih sebatas satu event; caching lintas proses dan efektivitasnya adalah gate optimasi terpisah. Klaim production-ready memerlukan seluruh gate yang relevan beserta bukti hasil host.
