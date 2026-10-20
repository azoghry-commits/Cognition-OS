# Performance evaluation

## Protokol target V4.1 — belum dijalankan

Bandingkan A: host tanpa plugin, B: model-selected skills, C: B + hook deterministik yang didukung, dan D: C + deep advisory selektif. Sertakan tugas coding sederhana sebagai negative control serta arsitektur, debugging, insiden database, security review, keputusan strategis, implementasi multi-langkah, dokumentasi dan matematika. Ukur hasil deliverable asli, requirement coverage, regression, activation relevance, unnecessary activation, false-positive warning, calls/tokens/latency dan recovery bila teramati.

Satu host yang tidak mendukung hook tidak dapat diberi hasil C/D penuh; nyatakan dukungan parsial dan konfigurasi aktual. Jangan memakai invocation script manual sebagai bukti hook. Status eksperimen V4.1: `NOT_RUN`. Lihat [kajian konsep](CONCEPT_V4_1.md) dan [rencana migrasi](V4_1_MIGRATION_PLAN.md).

## Pengukuran dan rencana baseline 3.1

No baseline-versus-plugin native performance gain is claimed. Deterministic helper timing can be measured using `python scripts/benchmark.py` and is recorded separately in evidence/benchmark.json. Those measurements exclude model calls, skill activation, token use and user-task quality.

Native protocol: use examples A-E plus all 50 cognitive cases, fixed host/model/settings, equivalent input context, randomized order and repeated runs. Compare baseline, QUICK, STANDARD and DEEP. Record task quality using blinded method/evidence rubrics, activation precision/recall, chosen frameworks, tool/model calls, input/output tokens where exposed, elapsed time, correctness, traceability and user completion. Report missing instrumentation as NOT_VERIFIED rather than zero. Preserve raw transcripts and failures.

Current host comparison status: NOT_VERIFIED until actual runs are collected. Source targets (<30 minutes synthesis, <50 ms simulation, graph density and >90% confidence) are unvalidated product assertions. Registry coverage and metadata size are inspectable engineering metrics, not evidence of improved cognition.

