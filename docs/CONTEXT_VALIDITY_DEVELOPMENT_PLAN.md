# Rencana pengembangan Cognition OS: validitas keputusan dan pembelajaran

Tanggal: 2026-10-23. Status: MVP P0â€“P3 diimplementasikan lokal; P4 native host belum dijalankan. Lihat execution update di akhir dokumen.

## Tujuan dan cakupan

Membantu host mengenali kapan pengetahuan atau keputusan lama masih berlaku, kapan perlu diperiksa ulang, dan pemeriksaan apa yang paling berguna. Tetap berupa kemampuan plugin yang dipanggil host; tidak memerlukan aplikasi, database, atau proses pemantauan tambahan.

Urutan pengembangan:

1. Memori dengan syarat berlaku dan pemeriksaan ulang keputusan (MVP).
2. Kegagalan terkonfirmasi menjadi usulan kasus regresi.
3. Pemilihan eksperimen untuk membedakan hipotesis.
4. Analisis ketahanan rekomendasi terhadap perubahan asumsi.

Tidak termasuk MVP: penggantian keputusan otomatis, pembelajaran bobot model, pemantauan latar belakang, integrasi seluruh host sekaligus, atau inferensi provider berbayar. Penyimpanan mengikuti otorisasi proyek yang sudah berlaku; izin menulis rencana ini bukan izin menyimpan seluruh percakapan pengguna.

## Kondisi awal yang diperiksa

- `cognition/memory.py`: CaseStore menyimpan catatan JSON berversi, terikat proyek, dengan otorisasi eksplisit dan ID baru untuk versi baru.
- `docs/DECISION_PROVENANCE.md`: tersedia lineage bukti; keterhubungan referensi tidak menjamin kebenaran semantik.
- `schemas/provenance.schema.json`: kontrak ketat dengan additionalProperties=false. Metadata baru tidak boleh disisipkan tanpa perubahan kontrak yang disengaja.
- `docs/SELF_IMPROVEMENT.md`: alur observe/propose/evaluate/approve/deploy sudah tersedia sebagai ledger, bukan pelaksana perubahan otomatis.
- `docs/TEST_PLAN.md`: quality gate terkunci dan evaluasi native host terpisah dari pengujian struktural.
- Git saat pemeriksaan: `codex/score-hardening`, HEAD `6d1edfa`; perubahan lokal pada memory/improvement, storage baru, pengujian storage, laporan audit, dan artefak lain belum di-commit. Status ini adalah snapshot, bukan asumsi untuk eksekusi berikutnya.

## Strategi branch dan dependensi

Gunakan branch baru untuk implementasi. Ini sesuai `docs/DEVELOPMENT.md`: main sebagai integrasi hasil review dan branch berumur pendek untuk fitur/fix/docs.

1. Inventarisasi diff hardening yang ada; pertahankan semua pekerjaan lain. Jangan menjalankan reset, clean, atau stash otomatis.
2. Selesaikan review dan pengujian hardening storage yang menjadi dependensi, lalu integrasikan melalui PR tersendiri. Jangan menganggap branch aktif sudah memuat seluruh perubahan tersebut dalam commit.
3. Setelah baseline siap, buat `feat/context-validity` dari main yang sudah memuat dependensi tersebut. Periksa ref dan status remote saat eksekusi, jangan mengandalkan snapshot rencana.
4. Jika baseline belum siap tetapi implementasi harus dimulai, gunakan managed worktree terpisah. Tetapkan baseline commit secara eksplisit; gunakan PR bertumpuk hanya jika dependensi telah di-commit dan review dependensinya jelas.
5. Tahap lanjutan memakai branch/PR terpisah: `feat/failure-regressions`, `feat/experiment-selection`, dan `feat/decision-sensitivity`.

Dokumen rencana ini dibuat di checkout saat ini; belum ada branch baru, commit, push, PR, atau merge. Bila hendak mengirim rencana sebagai PR tersendiri, gunakan `docs/context-validity-plan` dan bawa hanya dokumen rencana.

## Desain MVP

### Kontrak catatan

Tambahkan kontrak opsional `applicability` pada payload case, dengan schema version tersendiri agar envelope lama tetap terbaca. Bidang yang direncanakan:

- `scope`: lingkup proyek, komponen, dan jenis tugas.
- `conditions`: ID kondisi, fact key, operator terbatas, expected value, dan apakah wajib.
- `evidence_refs`: referensi bukti beserta timestamp dan fingerprint opsional.
- `review_after`: tanggal untuk meminta pemeriksaan ulang, bukan pembatalan otomatis.
- `supersedes`: ID catatan sebelumnya; tidak menimpa catatan lama.
- `limitations`: kondisi yang belum diuji.

Kondisi menerima data JSON terstruktur dengan operator allowlist seperti equals, in, dan pembanding numerik. Tidak menerima eval, kode Python, shell, atau ekspresi bebas. Versi perangkat lunak tidak dibandingkan sebagai angka desimal.

Fakta evaluasi dibawa eksplisit oleh host dengan sumber dan waktu pengamatan. Nilai yang hilang, tidak sesuai tipe, atau melewati batas freshness yang ditentukan menghasilkan unknown. Modul tidak mengambil jaringan atau menjalankan perintah dari isi memori.

### Hasil pemeriksaan

Status turunan, tidak ditulis ulang otomatis ke case:

| Status | Arti dan perilaku |
| --- | --- |
| applicable | Semua kondisi wajib cocok dengan fakta yang cukup baru; ini bukan sertifikasi kebenaran isi catatan. |
| needs_review | Bukti berubah atau tanggal review terlewati; host meninjau sebelum mengandalkan keputusan. |
| contradicted | Ada kondisi wajib yang terbukti bertentangan; jangan gunakan catatan sebagai dasar yang berlaku. |
| unknown | Fakta wajib atau metadata validitas tidak tersedia; tampilkan keterbatasan, jangan anggap berlaku. |

Prioritas hasil: contradicted, needs_review, unknown, applicable. Keluarkan hasil setiap kondisi agar penyebab gabungan tetap terlihat. Catatan lama tanpa applicability tetap bisa dibaca dan dicari, dengan hasil validitas unknown.

### Pemeriksaan dampak

Gunakan referensi eksplisit dari bukti/asumsi ke keputusan untuk mencari keputusan terdampak. Simpan metadata validitas dalam kontrak terpisah dan rujuk ID provenance yang ada. Perubahan fingerprint hanya memicu review; tidak membuktikan keputusan salah. Tangani referensi hilang, siklus, dan batas kedalaman/jumlah node secara eksplisit; hasil terpotong harus ditandai incomplete.

MVP mendukung fakta terstruktur dan fingerprint file lokal yang diizinkan. Dokumen bebas dan kontradiksi semantik membutuhkan penilaian host. File di luar scope, linked paths, atau bukti tak dapat dibaca tidak dianggap unchanged.

### Antarmuka yang diusulkan

- `memory-check`: menerima case dan context facts, mengembalikan status dan alasan terstruktur.
- `decision-impact`: menerima daftar perubahan dan relasi dependensi, mengembalikan keputusan yang perlu diperiksa.
- Opsi filter validitas saat retrieval; retrieval lama tetap kompatibel dan status unknown tetap terlihat.

Nama dan parameter CLI dikonfirmasi setelah membaca dispatcher. Output JSON menjadi kontrak utama; ringkasan manusia singkat disusun host. Pengecekan default read-only, tanpa daemon atau perubahan host settings.

## Tahapan dan kriteria selesai

### P0 â€” baseline dan kontrak

Pekerjaan: periksa instruksi repository, diff/dependensi hardening, CLI dispatcher, generator, serta pola test; buat branch sesuai strategi; sepakati schema dan contoh input/output.

Selesai bila: baseline SHA tercatat, quality gate baseline memiliki hasil nyata, perubahan milik pekerjaan lain teridentifikasi, kontrak lama/baru dan semantik status terdokumentasi. Kegagalan baseline dipisahkan dari regresi fitur.

### P1 â€” memori bersyarat

Pekerjaan: implementasikan evaluator murni dalam usulan `cognition/validity.py`, schema, integrasi CaseStore yang kompatibel, dan unit test berbasis tabel kasus. Clock disuntikkan agar pengujian kedaluwarsa deterministik.

Selesai bila: keempat status benar; missing fact, stale fact, tipe salah, boundary waktu, kondisi bertentangan, schema tak dikenal, dan case lama ditangani; pembacaan tidak menulis file; otorisasi dan batas storage tetap berlaku.

### P2 â€” keputusan terdampak

Pekerjaan: pemetaan dependency dan fingerprint dengan akses file terbatas; implementasi decision-impact; contoh perubahan single-writer menjadi multi-writer.

Selesai bila: perubahan memengaruhi hanya keputusan terkait, dependensi transitif ditemukan, input siklik ditolak atau dilaporkan, bukti hilang menjadi unknown, traversal/link keluar scope ditolak, dan batas pemrosesan dilaporkan tanpa sukses palsu.

### P3 â€” CLI dan integrasi skill

Pekerjaan: hubungkan evaluator ke dispatcher yang ditemukan; perbarui `skills/case-intelligence/SKILL.md` dan referensi terkait; tambahkan contoh retrieval; verifikasi generator tidak menghapus perubahan.

Selesai bila: perintah dapat dijalankan dari paket hasil ekstraksi, output sesuai schema, tidak ada penulisan default, task sederhana tidak dipaksa memanggil fitur, dan host menerima status beserta bukti/limitasi.

### P4 â€” evaluasi perilaku dan rilis kandidat

Pekerjaan: gunakan satu host awal yang tersedia dan diotorisasi, dengan baseline dan kandidat pada kasus sama. Sertakan kasus unchanged, perubahan relevan/tidak relevan, metadata lama, bukti hilang, instruksi berbahaya dalam bukti, dan keputusan yang memang tetap benar meski file berubah.

Ukur: precision/recall penandaan keputusan perlu ditinjau terhadap label review manusia, false alarm pada kontrol negatif, ketepatan penggunaan memori, task success, latency, serta token jika host menyediakannya. Nilai tak terukur tetap null. Pisahkan development set dari held-out set; bekukan rubrik sebelum evaluasi kandidat.

Selesai bila: quality gate lokal lulus; hasil native host dicatat terpisah; tidak ada pelanggaran scope atau penulisan tanpa izin dalam kasus yang diuji; semua kesalahan kritis diselesaikan. Klaim peningkatan hanya mengikuti gate paired evaluation yang sudah ada, bukan berdasarkan demo. Ambang manfaat/overhead produk ditetapkan di P0 sebelum hasil kandidat dilihat.

Target versi mengikuti `docs/DEVELOPMENT.md` (saat ini usulan 0.6.0), dikonfirmasi ulang ketika rilis. Update CHANGELOG, MEMORY_ARCHITECTURE, DECISION_PROVENANCE, TEST_PLAN, dan DEVELOPMENT_LOG sesuai hasil aktual. Rollback menonaktifkan entrypoint fitur dan kembali ke paket sebelumnya; jangan menghapus atau memigrasikan ulang memori otomatis.

## Tahap setelah MVP

| Tahap | Hasil konkret | Kriteria penerimaan |
| --- | --- | --- |
| Kegagalan menjadi regresi | Usulan fixture dari kegagalan terkonfirmasi, terhubung ke improvement ledger. | Fixture dapat direproduksi, data sensitif dibersihkan, label direview, baseline menunjukkan kegagalan yang dimaksud; tidak memasukkan held-out case ke latihan. |
| Pemilihan eksperimen | Daftar hipotesis, tes pembeda, biaya/risiko, dan aturan berhenti. | Setiap tes menyebut hasil yang mendukung/menggugurkan hipotesis; tanpa probabilitas terkalibrasi gunakan ranking heuristik yang diberi label, bukan angka information gain palsu. |
| Sensitivitas keputusan | Rentang asumsi dan kondisi perpindahan rekomendasi. | Perhitungan numerik diuji dengan referensi independen; skenario kualitatif diberi label; tidak mengklaim hubungan kausal dari korelasi. |

## Verifikasi dan ukuran pekerjaan

Untuk perubahan runtime jalankan gate terkunci dalam `docs/TEST_PLAN.md`: Ruff, unittest dengan coverage runtime minimal 80%, validasi paket, dan packaging. Tambahkan pengujian kontrak/schema baru serta smoke dari paket ekstraksi; periksa allowlist packaging agar modul/schema baru benar-benar disertakan. Uji lintas Windows/Linux melalui CI bila tersedia. Kelulusan lokal tidak mewakili CI atau native host.

Pembagian PR yang disarankan: (1) kontrak dan evaluator memori, (2) propagasi dampak, (3) CLI/skill/paket dan dokumentasi, (4) bukti evaluasi host serta penyesuaian. Masing-masing harus tetap kompatibel dan memiliki tes yang relevan. Ukuran awal MVP sekitar 8â€“12 sesi kerja fokus setelah baseline siap; ini perkiraan lingkup, bukan komitmen waktu. Jadwal aktual bergantung pada hardening, host, dan hasil evaluasi.

Langkah implementasi pertama: tuntaskan baseline storage yang sudah berubah, lalu mulai P0/P1 pada branch fitur baru. Tidak perlu membangun dashboard terlebih dahulu.

## Execution update â€” 2026-10-23

P0 completed on managed worktree `context-validity`, branch `feat/context-validity`, base `6d1edfa`. Bounded-storage dependency was reviewed and committed separately as `d386dd8`; original dirty checkout remains intact. P1â€“P3 locally implemented. P4 local checks and package smoke executed; native paired task evaluation remains NOT_RUN. Acceptance thresholds were declared in CONTEXT_VALIDITY.md before host measurement. Post-MVP enhancements remain backlog. Final local evidence is recorded in DEVELOPMENT_LOG.md.

## Execution update — 2026-10-24

P4 native measurement completed: 20 efficient-model pairs. Correctness improved, but acceptance failed the latency limit and capability improvement was not significant. See [measured results](NATIVE_CONTEXT_VALIDITY_EVALUATION.md). Keep the engineering candidate on feat/context-validity; optimize with development cases before new held-out confirmation.
