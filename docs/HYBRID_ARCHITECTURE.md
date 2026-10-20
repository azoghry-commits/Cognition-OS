# Arsitektur rebuild V4.1

Konsumen langsung plugin adalah model/agen Claude dan Codex. Host memilih kapabilitas, menerima advisory dan menyelesaikan deliverable asli. Paket kandidat 0.2.0 mengimplementasikan kontrak V4.1; artifact framework 3.1 tetap dapat dibaca melalui jalur kompatibilitas. Nomor paket terpisah dari spesifikasi.

## Tiga jalur dan governor

`cognition/augmentation.py:assess` menerima task-context yang telah dinormalisasi host: objective, task type, risiko, kompleksitas, bukti, artifact, kapabilitas, analisis terdahulu dan remaining budget. `cognitive-core/augmentation/policy.json` menyimpan tujuh kebijakan dan routing rules yang dapat ditinjau. Ini saran berbasis rule, bukan classifier terlatih atau runtime interceptor. Helper tidak melakukan reasoning model, native dispatch, atau perubahan file.

Path A memakai skill model-selected dengan lazy references. Path B adalah script deterministik pada PostToolUse yang relevan. Path C adalah deep-plan terbatas dengan role logis advocate/challenger/jury. Default delegasi native nol; host boleh mendelegasikan sesuai otorisasi dan dukungan aktual. Panjang jawaban bukan pemicu deep advisory. Tugas sederhana dan analisis yang cukup memakai PASS_THROUGH. Check wajib yang tidak tersedia menghasilkan BLOCKED, tidak disamarkan oleh degradasi advisory.

Budget memuat framework invocation, subagent call, debat, tools, waktu komputasi dan konteks. Angka default adalah allowance awal rekayasa, dapat diubah oleh konteks host dan belum dikalibrasi melalui benchmark. Helper tidak mengukur token host. Budget habis menghasilkan gap/incomplete outcome; tidak berarti aman, benar, atau selesai.

## Kontrak dan core

Kontrak request: `schemas/cognitive-request.schema.json`. Result: `schemas/advisory-result.schema.json`. Task context: `schemas/task-context.schema.json`. `review-advisory` mengecek struktur, identity, evidence scope, link dan record perhitungan; penilaian makna/kebenaran tetap pada host. Tidak ada confidence score buatan. Klaim INFERENCE harus punya dukungan; HYPOTHESIS, ASSUMPTION dan UNKNOWN eksplisit dapat belum memiliki evidence.

`normalize-legacy` menghasilkan objek baru dari envelope 3.1, mempertahankan origin classification, AG ID dan trace ID. Ia tidak menulis ulang kasus pengguna atau menciptakan bukti yang hilang. CALCULATED_RESULT dan SIMULATED_RESULT tidak otomatis tervalidasi hanya karena ada output JSON.

Seluruh 50 definisi di `cognitive-core/frameworks/definitions` memiliki preconditions, input schema, output schema path, trigger, metode, evidence requirements, limitations, relationships, validation criteria dan source references. Satu registry AG-01..52 merujuk core yang sama. Relasi framework yang kosong berarti belum ada rekomendasi pasangan eksplisit, bukan larangan kompatibilitas.

## Hook deterministik

Konfigurasi terpisah: `hooks/codex/hooks.json` dan `hooks/claude/hooks.json`. Keduanya hanya PostToolUse dengan matcher Write/Edit/apply_patch, timeout tiga detik, dan entrypoint `scripts/check_artifact.py`. Konfigurasi host memakai variabel root plugin sesuai dokumentasi masing-masing. Python harus tersedia pada environment eksekusi. Instalasi tidak memberi trust atau izin eksekusi.

Validator hanya membaca path yang disebut oleh tool edit, di bawah `cwd/.cognition/artifacts`, berakhiran `.json`. Ia menolak link/junction, traversal, path luar scope, JSON tidak valid dan artifact melebihi batas. Maksimum delapan path dan satu MiB per file; output gagal/terbatas adalah advisory. Tidak mengeksekusi command dari payload, tidak memanggil model/network, dan tidak menulis artifact. Isi file dan path tidak direfleksikan menjadi instruksi host.

Content hash menduplikasi hasil identik dalam satu event; tidak ada cache disk lintas proses pada kandidat ini. Check tetap idempotent dan bounded. Pengurangan overhead lintas event masih perlu pengukuran native sebelum memilih cache persistence. Hook tidak memblokir atau mengembalikan side effect edit yang sudah terjadi. Required security enforcement mengikuti mekanisme host yang terverifikasi, terpisah dari hook advisory ini.

## Dukungan dan batas

Baseline tetap bekerja tanpa MCP, database server, Docker, credential model, atau aplikasi mandiri. Tanpa hook/script, gunakan skill yang tersedia dan tampilkan limitasi material. Tanpa evidence/calculator jangan mengarang hasil. Kasus lokal dan Human Mastery Track tetap opt-in dan bukan pelatihan otomatis model.

Struktur dan CLI lokal diuji terpisah dari pemilihan skill oleh model serta delivery event native. Status dan evidence rebuild ada di [REBUILD_STATUS_V4_1.md](REBUILD_STATUS_V4_1.md). Sumber generator sudah diselaraskan: build_catalog → build_plugin (termasuk build_hybrid) → build_docs. build_docs pada 0.2.x memperbarui aset hybrid tanpa menimpa audit/status historis 3.1.
