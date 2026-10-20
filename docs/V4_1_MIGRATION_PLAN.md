# Rencana migrasi Cognition OS V4.1

**Pelaksanaan rebuild:** rencana ini kini dijalankan atas instruksi pengguna. Kemajuan, evidence dan gate yang masih terbuka dicatat di [REBUILD_STATUS_V4_1.md](REBUILD_STATUS_V4_1.md). Teks cakupan kajian di bagian akhir dipertahankan sebagai konteks awal, bukan pembatas otorisasi rebuild terbaru.

Tanggal: 2026-10-20. Status: `PROPOSED`. Arah konsep berasal dari [prompt V4.1](evidence/master-implementation-prompt-v4.1.txt); analisis checkout ada pada [kajian konsep](CONCEPT_V4_1.md). Rencana ini belum merupakan catatan implementasi atau hasil evaluasi V4.1.

## Prinsip pelaksanaan

Pertahankan satu core, 50 model dalam delapan kategori, dan AG-01..52. Gunakan aset baseline 0.1.0 yang lolos audit. Selesaikan deliverable asli melalui host dengan bantuan minimum yang bermanfaat. Model-selected menjadi jalur utama, deterministic validation selektif menjadi jalur kedua, deep advisory bersifat kondisional. MCP, penyimpanan kasus, dan learning tetap opsional.

Sumber generator harus diperbarui sebelum regenerasi. `scripts/build_docs.py` dapat menimpa panduan lama; `scripts/build_plugin.py` dapat menimpa metadata dan skill; `scripts/build_catalog.py` memuat kontrak baseline. Simpan dokumen konsep dan prompt sebagai sumber tetap yang tidak dihasilkan generator. Jangan menjalankan ulang seluruh generator baseline hanya untuk menyegarkan dokumentasi V4.1.

## Tahapan dan gate

| Phase | Pekerjaan konkret | Deliverable / area | Gate sebelum lanjut |
|---|---|---|---|
| 0 — Source audit delta | Cocokkan blueprint lengkap dan seluruh 15 halaman PDF dengan V4.1; inventaris kemampuan, metodologi, spesialis, formula, kontrak, dependency, bukti, asumsi aplikasi, keamanan, konflik dan gap | Pembaruan `docs/SOURCE_ANALYSIS.md`, traceability dan transformation matrix berlocator | Semua fitur terpetakan; source-derived dibedakan dari adaptasi dan proposal; hash sumber tetap dapat diverifikasi |
| 1 — Platform verification | Periksa dokumentasi resmi dan runtime yang tersedia per surface Claude/Codex; catat versi, event, payload, feedback/block, izin/trust, instalasi script dan fallback | `docs/PLATFORM_COMPATIBILITY.md`, adapter notes dan evidence per host | Tidak ada API/event/manifest field hasil asumsi; unsupported dan untested dinyatakan jelas; pengujian mengikuti `ACCOUNT_SCOPE.md` |
| 2 — Hybrid design | Definisikan governor tujuh kebijakan, contract request/result, output host, budget dan dedup; rancang kompatibilitas 3.1 dan enum bukti | Policy/core, schemas target, orchestration, keputusan arsitektur dan generator | Negative control menghasilkan pass-through; format/tujuan host utuh; budget tidak menyamarkan gap keamanan |
| 3 — Minimal prototype | Migrasikan routing, MECE, First Principles, 5 Whys, Pre-Mortem dan artifact validation; satu hook aman pada host yang mendukung | Generator, skills, helper/core, schema, adapter/hook terpilih | Tugas biasa dapat memilih bantuan tanpa menyebut Cognition OS; ada bukti native invocation. Hook disertai uji payload, timeout, feedback, duplikasi, path dan failure; jika tak didukung catat gate terbuka |
| 4 — Full core | Audit/selaraskan definisi dan kontrak 50 model serta 52 spesialis; trigger/precondition, limitation, compatibility dan reference tiap framework | Satu registry/definitions kanonis, schema, evaluasi metode | ID/kategori/metodologi sumber terjaga, kontrak lengkap, semantic fidelity diuji terpisah dari validasi struktur |
| 5 — Deep advisory | Tambah seleksi multi-framework, kalkulasi, advocate/challenger/jury dan penghentian yang eksplisit | Workflow terbatas, advisory result, test/evals | Tetap dormant pada tugas sederhana; disagreement/evidence gap dipertahankan; tidak ada delegasi rekursif tanpa batas |
| 6 — Dual integration | Uji adapter Claude dan Codex secara terpisah pada surface yang tersedia; matriks fallback tanpa MCP/hook/script | Adapter/package, instalasi, update, rollback, transcript native | Hasil satu host tidak dipakai sebagai hasil host lain; installed/discovered/selected/executed dibedakan |
| 7 — Evaluation | Jalankan A baseline, B skills, C skills+hooks, D full hybrid; randomisasi urutan dan repeated runs dengan model/settings sebanding | Eval cases/rubric, raw results, instrumentation dan performance report | Task outcomes, unnecessary activation, warning false positives, tokens/calls/latency dan recovery terukur; data hilang tidak dikarang |
| 8 — Hardening | Periksa permission boundaries, prompt injection, path handling, secrets, paket portabel, update/rollback dan dokumentasi release | Validation/operational package dan checklist rilis | Seluruh acceptance criteria punya bukti atau blocker eksplisit; production-ready hanya setelah gate terpenuhi |

Urutan fase mengikuti V4.1. Audit delta tidak menghapus evidence 3.1. Prototype boleh menggunakan helper/core yang sudah ada, tetapi status reused bukan bukti perilaku hybrid. Tidak ada tenggat atau klaim peningkatan numerik sebelum pengukuran.

## Keputusan implementasi yang perlu ditetapkan melalui bukti

1. Verifikasi invocation model melalui tugas natural dan negative control; manual invocation dipakai untuk diagnosis bila pemilihan gagal.
2. Pilih satu event dan validator yang payload serta umpan baliknya memadai. Rekomendasi awal: pemeriksaan schema artifact pada path dalam scope setelah edit, jika host menyediakan event yang sesuai. Ini proposal, bukan nama event lintas platform.
3. Pisahkan advisory failure dari enforcement failure. Tentukan timeout, batas file/ukuran, content hash, cache bounded dan invalidasinya; hasil cache tidak memperluas izin.
4. Tambah request/result schema tanpa mengubah artifact/case lama secara diam-diam. Pemetaan `USER_ASSUMPTION` → `ASSUMPTION` dan `MODEL_INFERENCE` → `INFERENCE` harus mempertahankan asal pada provenance.
5. Ganti asumsi validator paket yang selalu melarang `hooks/` dengan pemeriksaan konfigurasi hook yang memang dipilih. Jangan menambah MCP hanya untuk memenuhi contoh struktur repo.
6. Hilangkan laporan analisis wajib dari jalur bantuan ringan. Format host/pengguna menentukan output; temuan internal cukup ringkas dan dapat ditelusuri.
7. Catat konsumsi budget aktual bila host mengeksposnya. Batas numerik awal adalah konfigurasi eksperimen yang perlu dikalibrasi, bukan hasil optimasi ilmiah.

## Pemetaan paket deliverable V4.1

| Paket wajib | Hasil yang harus tersedia |
|---|---|
| A — Source Intelligence | Audit lengkap, capability inventory, transformation matrix berlocator dan klasifikasi sumber/adaptasi/proposal |
| B — Hybrid Architecture | Tiga jalur, governor, contracts, budget, guardrails, izin dan fallback |
| C — Unified Core | 50 model, 52 spesialis, perhitungan/validasi dan schema bersama |
| D — Claude Adapter | Package/skills native, dukungan agent/hook/MCP yang terverifikasi sesuai kebutuhan, installation evidence |
| E — Codex Adapter | Package/skills native, dukungan hook/delegasi sesuai runtime, installation evidence khusus Codex |
| F — Validation | Uji functional, activation, deep advisory, hook, security, compatibility dan benchmark A/B/C/D |
| G — Operational | Setup, konfigurasi, troubleshooting, update, rollback dan release evidence |

## Kriteria review hasil migrasi

Delapan belas kriteria rilis pada bagian 22 prompt harus dicatat satu per satu dengan locator bukti. Minimal buktikan host tetap pemilik tugas, seluruh katalog terjaga, pilihan skill aktual, hook yang diotorisasi, deep advisory selektif, kalkulasi benar, batas izin, dan evaluasi manfaat versus overhead. Ketiadaan MCP atau aplikasi terpisah tidak menghalangi baseline. Hook yang belum tersedia tidak boleh diberi status `TESTED`.

Cakupan kajian saat ini selesai pada penyimpanan prompt, pemahaman konsep, gap repo dan rencana ini. Runtime, host configuration, credentials, dan benchmark V4.1 belum dimigrasikan.
