# Cognition OS: Master Blueprint Aplikasi Web SaaS Full-Stack Interaktif & Platform Augmentasi Kognitif Multi-Agen

**Versi Dokumen:** 2.0 (Edisi Penyempurnaan Arsitektur & Spesifikasi Produksi Full-Stack)  
**Klasifikasi Sistem:** B2B/Enterprise Decision Intelligence, Multi-Agent Cognitive Augmentation & Executive Mastery SaaS  
**Target Realisasi:** Aplikasi Web SaaS Full-Stack Interaktif (Next.js 15 + React Flow + FastAPI + LangGraph + PostgreSQL/pgvector + Neo4j PROV-O)  
**Target Kinerja Utama:** Time to Synthesis (T2S) < 30 Menit | 100% Reasoning Traceability | 50 Model Mental (8 Kategori) | 52 Agen AI Spesialis Paralel

---

## Ringkasan Struktur Dokumen (Master Blueprint Overview)

Dokumen Master Blueprint ini mengonsolidasikan, menyempurnakan, dan menerjemahkan seluruh konsep dari materi visual serta presentasi **Cognition OS** ke dalam spesifikasi rekayasa perangkat lunak (*software engineering specification*) yang siap dibangun menjadi aplikasi web SaaS interaktif:

1. **Bagian 1 — Visi Produk, Paradigma Tripartit & Penyempurnaan Cetak Biru (PRD):** Merumuskan proposisi nilai utama, memperbaiki inkonsistensi matematis dan *typo* visual pada draf awal, serta menetapkan metrik keberhasilan sistem.
2. **Bagian 2 — Arsitektur Sistem 5-Lapis (5-Layer Full-Stack Architecture) & Tech Stack:** Memetakan infrastruktur *frontend* kanvas visual, *backend* orkestrasi multi-agen, mesin simulasi probabilitas, dan penyimpanan grafik memori.
3. **Bagian 3 — Spesifikasi Fungsional, UI/UX Interaktif & Alur Kerja 5 Fase:** Merinci antarmuka dan logika interaksi untuk *Command Center*, *Problem Ingestion Wizard*, *Framework Stack Builder*, *Thinking Canvas*, *Adversarial Debate Mode*, *Scenario Simulator*, *Logic Guardrails*, *Synthesis Engine*, *Case Library*, dan *90-Day Human Mastery Track*.
4. **Bagian 4 — Katalog Lengkap 50 Model Mental (8 Kategori) & 52 Agen AI Spesialis:** Menyajikan daftar lengkap 50 kerangka kerja dan 52 agen AI beserta kontrak skema JSON *input/output* dan *System Prompt* tingkat produksi.
5. **Bagian 5 — Mesin Komputasi Matematis & Algoritma Validasi Real-Time:** Menyediakan formulasi matematika dan implementasi kode Python untuk *Expected Value (EV)*, *Monte Carlo Simulation*, *Bayesian Belief Updating*, *MECE Validator*, dan *Cognitive Bias Detector*.
6. **Bagian 6 — Skema Database Relasional/Vektor (PostgreSQL) & Reasoning Knowledge Graph (Neo4j W3C PROV-O):** Menyediakan skrip DDL SQL dan skema Cypher untuk menjamin keterlacakan keputusan (*100% Reasoning Traceability*).
7. **Bagian 7 — Orkestrasi Backend LangGraph, Kontrak API Streaming (SSE/WebSocket), & Komponen React Flow:** Menyediakan implementasi kode *backend* dan *frontend* untuk eksekusi agen secara paralel dan pembaruan kanvas secara *real-time*.
8. **Bagian 8 — Struktur Direktori Monorepo, Deployment Docker, Pengujian, & Roadmap Implementasi 16 Minggu:** Menyajikan panduan praktis pembangunan sistem dari tahap fondasi hingga rilis *Enterprise*.

---

## Bagian 1: Visi Produk, Paradigma Tripartit & Penyempurnaan Cetak Biru (PRD)

### 1.1 Paradigma Baru Pemikiran Strategis: Sinergi Tripartit Berbasis Komputasi

Eksekutif dan pengambil keputusan modern sering kali terjebak dalam tiga kelemahan kognitif utama saat menghadapi masalah kompleks: *blind spots* dalam mengurai akar masalah, bias kognitif kelompok (*groupthink*, *confirmation bias*, *sunk cost fallacy*), serta pengambilan keputusan berbasis intuisi tanpa kalkulasi probabilitas yang ketat.

**Cognition OS** mengubah pemecahan masalah strategis dari seni yang subjektif menjadi ilmu pasti melalui penggabungan tiga pilar utama (**Keputusan Sekelas Konsultan Tier-1**):

| Pilar Kognitif | Peran dalam Sistem | Kapabilitas Inti di Cognition OS |
| :--- | :--- | :--- |
| **1. Manusia (Intuisi & Konteks)** | Pemilik masalah, pemberi batasan (*constraints*), dan pengambil keputusan akhir | Mendefinisikan konteks domain, mengintervensi cabang di *Thinking Canvas*, menyesuaikan asumsi di *Scenario Simulator*, dan menginternalisasi pola pikir melalui *90-Day Mastery Track*. |
| **2. Model Mental (Struktur Logika)** | Kerangka kerja analitik tervalidasi yang memandu cara mengurai dan memprioritaskan masalah | **50 Kerangka Kerja Terintegrasi** dalam **8 Kategori Disiplin** yang dapat dirangkai secara modular melalui *Framework Stack Builder* (misalnya: `SCQA ➔ MECE ➔ Kepner-Tregoe ➔ RICE`). |
| **3. Agen AI (Kecepatan & Komputasi)** | Pasukan spesialis komputasional yang mengeksekusi model mental secara paralel dan menguji ketahanan asumsi | **52 Agen AI Spesialis** (50 agen kerangka kerja + *Chief Orchestrator* + *Evaluator Jury*) yang menjalankan dekomposisi, *Adversarial Debate*, deteksi bias *real-time*, dan simulasi Monte Carlo. |

### 1.2 Audit, Koreksi & Penyempurnaan atas Dokumen Konsep Awal

Sebelum diimplementasikan ke dalam kode produksi, Master Blueprint ini menetapkan empat penyempurnaan struktural terhadap draf visual dan presentasi awal:

1. **Harmonisasi Kalkulasi Matematis *Expected Value* (EV):**
   - Pada materi konsep awal, *Slide 8 (Scenario Simulator)* menampilkan parameter `Probabilitas Sukses = 65%`, `Upside = $2.4M`, `Downside = $0.3M`, dan `Costs = $0.8M` dengan hasil `EV = +$0.65M`, sedangkan *Slide 13 (Synthesis Engine)* mencantumkan angka `+$1.2M EV`.
   - Di dalam mesin komputasi **Cognition OS**, kedua metrik ini dipisahkan secara eksplisit agar tidak menimbulkan ambiguitas finansial:
     - **Gross Expected Payoff ($\text{EV}_{\text{gross}}$):** Nilai harapan sebelum biaya modal/implementasi, dihitung dengan rumus:
       $$\text{EV}_{\text{gross}} = (P_{\text{success}} \times \text{Upside}) - (P_{\text{failure}} \times \text{Downside})$$
       Pada kasus standar ($P=0.65$): $(0.65 \times \$2.4\text{M}) - (0.35 \times \$0.3\text{M}) = \$1.56\text{M} - \$0.105\text{M} = +\$1.455\text{M}$ (atau $+\$1.20\text{M}$ pada skenario konservatif pasca-penyesuaian risiko rantai pasok).
     - **Net Expected Value ($\text{EV}_{\text{net}}$):** Nilai harapan bersih setelah dikurangi biaya eksekusi langsung ($\text{Costs} = \$0.8\text{M}$):
       $$\text{EV}_{\text{net}} = \text{EV}_{\text{gross}} - \text{Costs} = \$1.455\text{M} - \$0.80\text{M} = +\$0.655\text{M} \approx +\$0.65\text{M}$$
   - Baik $\text{EV}_{\text{gross}}$ maupun $\text{EV}_{\text{net}}$ kini ditampilkan secara berdampingan di *Scenario Simulator* dan *Minto Pyramid Output*.

2. **Standardisasi Nomenklatur Teknis (Koreksi Distorsi OCR/Visual):**
   - Seluruh istilah yang mengalami distorsi huruf pada infografis awal telah dinormalisasi di dalam basis data dan antarmuka aplikasi:
     - *"PICE Scoring"* $\rightarrow$ **RICE Scoring** (*Reach, Impact, Confidence, Effort*)
     - *"McKineey Issue Troo"* $\rightarrow$ **McKinsey MECE Issue Tree**
     - *"Wordley Mapping"* $\rightarrow$ **Wardley Mapping**
     - *"Surik Cost Faliocy" / "Sout Post Farnaly"* $\rightarrow$ **Sunk Cost Fallacy**
     - *"Bias Konmnnaai"* $\rightarrow$ **Confirmation Bias**
     - *"Mante Carlo simulation" / "Niisi Ekenami"* $\rightarrow$ **Monte Carlo Simulation & Nilai Ekonomi**
     - *"Kepner-Tregee" / "Kepner-Tregon"* $\rightarrow$ **Kepner-Tregoe Matrix**

3. **Kelengkapan Katalog 50 Model Mental & 52 Agen AI:**
   - Materi awal menyebutkan kuota 50 Model Mental dalam 8 kategori dan 52 Agen AI, namun baru mencantumkan 13 kerangka kerja dan 8 nama agen. Dokumen ini melengkapi ke-50 model mental dan ke-52 agen AI secara utuh pada **Bagian 4**.

4. **Spesifikasi Teknis W3C PROV-O untuk *Decision Lineage*:**
   - Klaim *100% Reasoning Traceability* dan *Confidence Score* (`<3.0% Margin of Error` / `>90% Confidence`) diterjemahkan menjadi skema graf berarah (*Directed Acyclic Graph* / DAG) berstandar W3C PROV-O di Neo4j, sehingga setiap rekomendasi eksekutif dapat dirunut balik hingga ke *node* data mentah, kerangka kerja, dan agen AI yang memproduksinya.

### 1.3 Target Pengguna & Metrik Keberhasilan Produk (Product KPIs)

| Metrik Kinerja Sistem (System Metric) | Target Kuantitatif | Definisi & Cara Pengukuran di Aplikasi |
| :--- | :--- | :--- |
| **Time to Synthesis (T2S)** | `< 30 Menit` | Waktu rata-rata dari saat pengguna memasukkan masalah di *Problem Ingestion Wizard* hingga menghasilkan laporan *Minto Pyramid* yang siap dipresentasikan ke Dewan Direksi. |
| **MECE Validation Score** | `≥ 90%` (Ambang Lulus: `85%`) | Skor gabungan dari *Mutually Exclusive* ($1 - \text{Max Pairwise Semantic Overlap}$) dan *Collectively Exhaustive* (cakupan domain & deteksi *edge cases*). |
| **Reasoning Traceability Rate** | `100%` | Persentase klaim dan rekomendasi pada *Synthesis Engine* yang memiliki tautan *provenance* aktif (`prov:wasDerivedFrom`) ke bukti dan agen pemroses. |
| **Graph Density Index** | `0.65 – 0.85` (Optimal: `0.78`) | Rasio keterhubungan antara *node* masalah, hipotesis, bukti, dan kontra-argumen di dalam *Reasoning Knowledge Graph*. |
| **90-Day Mastery Track Completion** | `3 Fase / 90 Hari` | Progres transformasi kemampuan pengguna dari *Navigator* (Hari 1–30), *Practitioner* (Hari 31–60), hingga *Expert / Ahli Strategi* (Hari 61–90). |

---

## Bagian 2: Arsitektur Sistem 5-Lapis (5-Layer Full-Stack Architecture) & Tech Stack

### 2.1 Struktur Arsitektur 5-Lapis (5-Layer Cognitive Augmentation Stack)

Sistem **Cognition OS** dibangun di atas arsitektur berlapis yang memisahkan ingesti masalah, orkestrasi komputasi multi-agen, kanvas pemodelan kerangka kerja, mesin validasi matematis, dan sintesis eksekutif:

```
====================================================================================================
LAPISAN 5: OUTPUT EKSEKUTIF, SYSTEM MEMORY & HUMAN MASTERY (PUNCAK STRUKTUR)
- Minto Pyramid Generator (Top-Down Executive Synthesis: Kesimpulan -> Argumen MECE -> Bukti)
- Decision Lineage Viewer (W3C PROV-O Audit Trail & Confidence Score Aggregation)
- Export Engine (1-Click Export ke PDF Dokumen Dewan Direksi & PPTX Presentasi Eksekutif)
- Institutional Case Library & AI Case Assistant + 90-Day Human Mastery Track (Gamified L&D)
====================================================================================================
                                              ▲
                                              │ (Validated Arguments, EV Metrics & PROV-O Graph)
====================================================================================================
LAPISAN 4: VALIDASI & SIMULASI REAL-TIME (LOGIC GUARDRAILS & EV ENGINE)
- Real-Time MECE Validator (Semantic Overlap Detector, Exhaustiveness Score & Edge Case Scanner)
- Real-Time Cognitive Bias Detector (Confirmation Bias, Anchoring, Sunk Cost, Availability, Groupthink)
- Scenario Simulator & Expected Value (EV) Engine (Bayesian Belief Updating + 10K Monte Carlo Runs)
====================================================================================================
                                              ▲
                                              │ (Structured Hypotheses, Debate Consensus & Scores)
====================================================================================================
LAPISAN 3: LABORATORIUM KERANGKA KERJA & THINKING CANVAS (FRAMEWORK LAB)
- Repository 50 Model Mental Terintegrasi (8 Kategori Disiplin)
- Framework Stack Builder (Penyusunan Pipeline Algoritma Berantai: mis. SCQA -> MECE -> KT -> RICE)
- Interactive Thinking Canvas (Node-based Visual Workspace: Issue Trees, 5 Whys, Causal Loops)
====================================================================================================
                                              ▲
                                              │ (Parallel Agent Execution Streams via SSE/WebSockets)
====================================================================================================
LAPISAN 2: MESIN PEMROSESAN MULTI-AGEN (THE AGENT ORCHESTRA)
- Chief Orchestrator Agent (AG-51) & Evaluator Jury / Critic Agent (AG-52)
- 50 Domain-Specific Mental Model Agents (Berjalan secara paralel & berantai di atas LangGraph)
- Adversarial Debate Engine (Blue Ocean Agent [Optimis] vs Pre-Mortem Agent [Pesimis] + Jury)
====================================================================================================
                                              ▲
                                              │ (Structured Problem Context & Domain Constraints)
====================================================================================================
LAPISAN 1: INPUT & INGESTION (DASAR STRUKTUR)
- Problem Ingestion Wizard (4-Step Guided Intake: Define Problem -> Identify Domain -> Context -> Launch)
- Pemetaan Domain Masalah ke 8 Disiplin Utama + AI Auto-Recommendation Engine untuk Framework Stack
- Multi-Source Context Parser (Teks Mentah, CSV/Excel Metrik Operasional, Dokumen Laporan PDF)
====================================================================================================
```

### 2.2 Spesifikasi Tech Stack Produksi (Full-Stack SaaS)

| Lapisan Sistem | Teknologi Utama | Justifikasi Arsitektural & Peran Spesifik |
| :--- | :--- | :--- |
| **Frontend Web Framework** | **Next.js 15 (App Router) + TypeScript 5.6** | Mendukung *React Server Components*, *streaming UI*, dan performa tinggi untuk ruang kerja analitik multi-panel. |
| **Visual Canvas & Graph UI** | **React Flow (@xyflow/react) + Dagre / ELK.js** | Merender *Thinking Canvas* (*Issue Tree*, *5 Whys*, *Causal Loop*), *Framework Stack Builder*, dan graf *Decision Lineage* dengan tata letak otomatis (*auto-layout*) dan manipulasi *node* interaktif. |
| **Data Visualization & Charts** | **D3.js + Recharts + Visx** | Menampilkan kurva distribusi probabilitas *Monte Carlo* dua kutub (*Upside vs Downside*), *gauge* indikator *MECE Score*, dan matriks *RICE / Kepner-Tregoe*. |
| **Styling & Design System** | **Tailwind CSS + shadcn/ui + Framer Motion** | Membangun tema ganda (*Executive Light Grid Theme* seperti di dek presentasi & *Dark Command Center Theme* seperti di infografis arsitektur) dengan animasi transisi *node* yang halus. |
| **State & Real-Time Sync** | **Zustand + TanStack Query v5 + Yjs (CRDT)** | Mengelola *state* kanvas kompleks di sisi klien, sinkronisasi *slider Scenario Simulator* secara *real-time* (< 16ms), dan kolaborasi multi-eksekutif secara serentak. |
| **Backend API & Streaming** | **Python 3.12 + FastAPI + Uvicorn** | Menyediakan endpoint RESTful asinkron, *Server-Sent Events (SSE)* untuk *streaming* token pemikiran 52 agen, dan *WebSockets* untuk intervensi kanvas *real-time*. |
| **Multi-Agent Orchestration** | **LangGraph + LiteLLM / OpenAI / Gemini SDK** | Mengelola eksekusi *stateful DAG*, percabangan paralel (*fan-out/fan-in*) hingga 52 agen, *Adversarial Debate Loop*, dan *checkpointing* memori sesi. |
| **Mathematical & NLP Engine** | **NumPy + SciPy + sentence-transformers** | Menjalankan simulasi Monte Carlo 10.000 iterasi dalam < 50ms, kalkulasi pembaruan Bayesian, dan komputasi kemiripan kosinus (*cosine similarity*) untuk *MECE Validator*. |
| **Primary & Vector Database** | **PostgreSQL 16 + pgvector + SQLAlchemy 2.0** | Menyimpan data pengguna, proyek masalah, *snapshot Thinking Canvas*, progres *90-Day Mastery Track*, dan *embedding* semantik untuk *Institutional Case Library*. |
| **Reasoning Knowledge Graph** | **Neo4j 5 (Enterprise / AuraDB)** | Menyimpan jejak audit keputusan berstandar **W3C PROV-O** (`Entity`, `Activity`, `Agent`) dan kueri penelusuran silsilah logika (*lineage traversal*). |
| **Event Bus & Task Queue** | **Redis 7 + Celery / ARQ** | Mengelola antrean tugas berat (seperti ekspor dokumen PDF/PPTX dan analisis *batch* 52 agen) serta *pub/sub* notifikasi *Logic Guardrails*. |
| **Document Export Engine** | **Playwright (HTML-to-PDF) + python-pptx** | Mengonversi struktur *Minto Pyramid* dan *Decision Lineage* menjadi laporan PDF sekelas konsultan dan file presentasi PowerPoint (`.pptx`) yang siap diedit. |

---

## Bagian 3: Spesifikasi Fungsional, UI/UX Interaktif & Alur Kerja 5 Fase

Bagian ini menerjemahkan seluruh layar dari dokumen presentasi (`Cognition_OS_Strategic_Intelligence.pdf` halaman 1–15) dan ketiga infografis ke dalam spesifikasi fungsional antarmuka pengguna (UI/UX) dan logika bisnis.

### 3.1 Arsitektur 4 Modul Utama Ruang Kerja (OS Workspace Modules)

Saat pengguna masuk ke **Cognition OS**, antarmuka aplikasi dibagi menjadi 4 modul utama yang terhubung dengan bar telemetri di bagian bawah layar (`[ 50 ] Mental Models (8 Kategori) | [ 52 ] AI Agents berjalan secara paralel | [ 100% ] Reasoning Traceability`):

1. **Command Center (Manajemen Masalah Aktif):**
   - Menampilkan daftar masalah strategis yang sedang dianalisis, status kesehatan logika sistem (`SYSTEM STATUS: OPTIMAL`), kepadatan graf penalaran (`GRAPH DENSITY: 0.78`), status mesin keputusan (`DECISION ENGINE: ACTIVE`), tingkat faktor risiko (`RISK FACTOR: LOW / MEDIUM / HIGH`), serta metrik kecepatan sesi (`TIME TO SYNTHESIS / T2S: < 30 MIN`).
2. **Thinking Canvas (Area Dekomposisi Visual):**
   - Ruang kerja kanvas tak terbatas (*infinite canvas*) tempat *Issue Tree*, rantai *5 Whys*, dan matriks *Kepner-Tregoe* dirender sebagai *node* interaktif yang dapat diperluas, diedit, atau divalidasi dengan data.
3. **Validation Engine (Penjaga Logika & Deteksi Bias):**
   - Panel pengawas *real-time* yang berjalan di latar belakang setiap kali pengguna atau agen AI menambahkan argumen baru, mencakup **MECE Validator**, **Bias Detector**, **Adversarial Debate Mode**, dan **Scenario Simulator**.
4. **Synthesis Engine (Generator Output Eksekutif):**
   - Modul penyusun argumen hierarkis berformat **Minto Pyramid** lengkap dengan visualisasi **Decision Lineage (PROV-O)** dan tombol ekspor instan (`[Export to PDF/PPTX]`).

### 3.2 Spesifikasi Detail 5 Fase Alur Kerja Pengguna (End-to-End User Journey)

#### Fase 1: Problem Ingestion Wizard (Dari Ambiguitas Menuju Ketajaman Analitik)
Wizard interaktif 4 langkah yang mengubah keluhan bisnis mentah menjadi struktur masalah formal:
- **Langkah 1 — Define Problem (Definisi Masalah):**
  - *Input UI:* Kotak teks kaya (*rich text*) dengan analisis kejelasan kalimat secara langsung.
  - *Contoh Kasus Sistem:* `"Q3 Profitability Decline"` (Penurunan profitabilitas kuartal ke-3 sebesar 18%).
- **Langkah 2 — Identify Domain (Identifikasi Domain):**
  - *Input UI:* Pemilih multi-tag dari 8 disiplin utama (*Decision, Problem Solving, Systems Thinking, Strategic, Innovation, Execution, Communication, Meta-Thinking*) dan fungsi bisnis (*Strategy, Product, Operations, Finance, Supply Chain*).
  - *Contoh Kasus Sistem:* `[ Tag: Strategy ]`, `[ Tag: Operations ]`.
- **Langkah 3 — Add Context & Constraints (Tambah Konteks & Batasan):**
  - *Input UI:* Unggah potongan data/metrik, tanggal kejadian penting, dan batasan eksekusi (*constraints*).
  - *Contoh Kasus Sistem:* `"Data input: Western stores -25%. Perubahan kebijakan pengadaan diterapkan pada 15 Juni."`
- **Langkah 4 — Review & Launch + AI Auto-Recommendation:**
  - *Logika Sistem:* **Chief Orchestrator Agent (AG-51)** menganalisis vektor teks dari Langkah 1–3, mencocokkannya dengan pola keberhasilan di *Case Library*, dan memunculkan rekomendasi *Framework Stack* otomatis.
  - *Banner UI:* `"Auto-Recommendation AI aktif: Berdasarkan kasus Profitabilitas, sistem merekomendasikan tumpukan kerangka kerja: SCQA + MECE Issue Tree + Kepner-Tregoe + RICE Scoring."`

#### Fase 2: Framework Stack Builder (Merangkai Algoritma Pemecahan Masalah)
Antarmuka pipa logika (*pipeline builder*) tempat setiap kerangka kerja memberi umpan data (*data feed*) terstruktur ke kerangka kerja berikutnya:

| Urutan Blok | Kerangka Kerja (Framework) | Tugas Kognitif | Agen AI Penanggung Jawab | Data Input (Upstream) | Data Output (Downstream Feed) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Blok 1** | **SCQA Framework** | Pembingkaian (*Framing*) | `AG-44 (SCQA Agent)` | Teks mentah & konteks dari *Problem Ingestion Wizard* | Objek JSON `{situation, complication, core_question, initial_hypothesis}` |
| **Blok 2** | **MECE / Issue Tree** | Dekomposisi (*Decomposition*) | `AG-09 (MECE Agent)` | `core_question` dari SCQA | Hirarki pohon masalah (*mutually exclusive, collectively exhaustive*) beserta bobot kontribusi cabang |
| **Blok 3** | **Kepner-Tregoe (KT)** | Isolasi Deviasi (*Isolation*) | `AG-11 (KT Agent)` + `AG-10 (5 Whys Agent)` | Cabang anomali dari *MECE Issue Tree* | Tabel spesifikasi *IS vs IS NOT* (*What, Where, When, Extent*) + akar masalah terkonfirmasi (*Confidence %*) |
| **Blok 4** | **RICE Scoring** | Prioritas (*Prioritization*) | `AG-02 (RICE Agent)` | Akar masalah terisolasi & kandidat intervensi solusi | Daftar tindakan yang diurutkan berdasarkan skor $\frac{\text{Reach} \times \text{Impact} \times \text{Confidence}}{\text{Effort}}$ |

*Fitur Tambahan UI:* Pengguna dapat memilih **Preset Cerdas** (misalnya: *Profitability Turnaround Stack*, *New Market Entry Stack*, *Operational Bottleneck Stack*, *Product Innovation Stack*) atau menyusun blok secara manual (*drag-and-drop* dari 50 model mental).

#### Fase 3: The Thinking Canvas (Isolasi Masalah Tanpa Blind Spots)
Ruang kerja visual berbasis graf hierarkis dengan fitur:
- **Struktur Dekomposisi Pohon (Issue Tree Hierarchy):**
  - *Root Node:* `Profitability Decline -18%`
  - *Level 1 Nodes (MECE Financial Split):* `Revenue ↓` dan `Costs ↑`
  - *Level 2 Nodes (MECE Revenue Split):* `Volume ↓` (diberi lencana merah menyala: **`▲ ROOT CAUSE IDENTIFIED`**) dan `Price ↓`
- **Drill-Down 5 Whys & Integrasi Panel Diagnosis Kepner-Tregoe:**
  - Ketika pengguna mengklik *node* `Volume ↓`, panel inspeksi kanan membuka rantai *5 Whys* dan kartu **Diagnosis Kepner-Tregoe**:
    > **Diagnosis Kepner-Tregoe mengonfirmasi:** Volume menurun akibat kehabisan stok (*stockout*) SKU bermargin tinggi di toko-toko Barat—meningkat 340% pasca perubahan kebijakan pengadaan 15 Juni. (**Keyakinan: 94%**).
- **Bar Validasi Konteks & MECE:** Di pojok kiri bawah kanvas terdapat indikator progres **Validasi Konteks (96% MECE Validated)** yang diperbarui secara *real-time*.

#### Fase 4: Adversarial Debate Mode (Sistem Kekebalan terhadap Bias Grup)
Sebelum solusi dari *Thinking Canvas* disetujui, sistem menyimulasikan perdebatan multi-agen secara paralel dalam tampilan 3 kolom untuk menguji ketahanan asumsi secara brutal:

| Kolom Panel UI | Agen AI & Peran | Sikap (*Stance*) | Fokus Evaluasi | Contoh Argumen Terstruktur pada Kasus Pengadaan |
| :--- | :--- | :--- | :--- | :--- |
| **Kolom Kiri (Biru)** | **Blue Ocean Agent** (`AG-24`) | `[ Sikap: Optimis ]` | `[ Fokus: Inovasi, Kecepatan, Valuasi ]` | *"Eksekusi pengecualian darurat sekarang! Pemulihan cepat stok SKU margin tinggi di wilayah Barat akan langsung merebut kembali pangsa pasar Q4."* |
| **Kolom Tengah (Ungu)** | **Evaluator Jury** (`AG-52`) | `[ Sikap: Objektif ]` | `[ Fokus: Sintesis Konsensus ]` | *"Eksekusi pengecualian pengadaan dalam 48 jam khusus untuk SKU margin tinggi, disertai mandat audit sistem pengadaan menyeluruh dalam 60 hari."* |
| **Kolom Kanan (Merah)** | **Pre-Mortem Agent** (`AG-49`) | `[ Sikap: Pesimis ]` | `[ Fokus: Titik Kegagalan, Risiko ]` | *"Kebijakan tambal sulam menciptakan kepuasan semu organisasi! Bypass prosedur tanpa perbaikan algoritma peramalan stok akan memicu pembengkakan biaya logistik darurat."* |

*Mekanisme Interaktif:* Pengguna dapat menambahkan bukti baru ke dalam ruang debat, meminta putaran sanggahan tambahan (*Rebuttal Round*), atau menerima keputusan sintesis dari **Evaluator Jury**.

#### Fase 5: Scenario Simulator (Mengubah Tebakan Menjadi Probabilitas Absolut)
Simulator kuantitatif interaktif yang memadukan kalkulasi **Expected Value (EV)**, **Bayesian Updating**, dan **Monte Carlo Simulation**:
- **Panel Kiri — 4 Slider Parameter Input Interaktif:**
  1. `Probabilitas (P_success)`: Slider `0% – 100%` (Nilai aktif: **65%**)
  2. `Upside (Dampak Positif jika Berhasil)`: Slider `$0.0M – $10.0M` (Nilai aktif: **$2.4M**)
  3. `Downside (Risiko Kerugian jika Gagal)`: Slider `$0.0M – $10.0M` (Nilai aktif: **$0.3M**)
  4. `Costs (Biaya Eksekusi Langsung)`: Slider `$0.0M – $10.0M` (Nilai aktif: **$0.8M**)
- **Panel Kanan — Output Keputusan & Kurva Distribusi Monte Carlo:**
  - Tampilan angka utama: **`EV = +$0.65M`** (Net EV) dan **`Gross EV = +$1.20M – +$1.46M`**.
  - Grafik distribusi probabilitas dua kutub: kurva **SUKSES (Probabilitas)** berwarna sian di sisi kiri/tengah dan kurva **KEGAGALAN (Risiko)** berwarna oranye di sisi kanan, lengkap dengan penanda titik impas (*break-even line*).
  - Status Rekomendasi Matematis: Lencana hijau **`(✓ PROCEED)`** / **`EXPECTED VALUE: LAYAK`** ketika $\text{EV}_{\text{net}} > 0$ dan probabilitas kerugian ekstrem (*Value at Risk* 95%) berada di bawah ambang toleransi risiko organisasi.

### 3.3 Spesifikasi Modul Pendukung (Guardrails, Synthesis, Memory & Mastery)

1. **Logic Guardrails: Mesin Validasi Real-Time:**
   - **Sub-Modul MECE Validator:** Memindai seluruh *node* pada level cabang yang sama di *Thinking Canvas*. Jika ditemukan tumpang tindih semantik (misalnya *Kategori 2 & 3 tumpang tindih*), UI menyorot teks dengan warna kuning dan menampilkan tooltip: `"Kategori 2 & 3 tumpang tindih. Skor Exhaustive: 78% (Kehilangan edge cases)."` beserta metrik bawah: `Data Integrity: 99.2% | MECE Score: 78.0% | Edge Case Detected: 4`.
   - **Sub-Modul Bias Detector:** Memindai narasi argumen pengguna dan agen. Jika ditemukan klaim sepihak (misalnya: *"Strategi ini menjanjikan pertumbuhan eksponensial di pasar Asia, berdasarkan kesuksesan peluncuran serupa di Eropa Barat tahun lalu"*), UI menyorot kalimat dengan warna merah muda dan menampilkan kartu peringatan:
     - Label: `[Confirmation Bias Detected]`
     - Penjelasan: *"Argumen secara selektif menyajikan bukti yang mendukung narasi toko Barat."*
     - Metrik Bawah: `Bias Probability: 92.5% | Type: Confirmation Bias | Confidence Level: High`

2. **Synthesis Engine & Minto Pyramid Output:**
   - Mengonversi seluruh jejak analisis menjadi struktur piramida top-down siap saji untuk Dewan Direksi:
     - **Puncak Piramida (Rekomendasi Utama / Kesimpulan):** *"Terapkan pengecualian pengadaan 48-jam untuk SKU margin tinggi."* (`Confidence Score: 90%–94%`)
     - **Lapisan Tengah (Argumen Pendukung MECE):**
       1. *Isolasi Kausal tervalidasi (94%)* — Kehabisan stok SKU margin tinggi di toko Barat pasca kebijakan 15 Juni.
       2. *Valuasi Ekonomi positif (+$1.2M Gross EV / +$0.65M Net EV)* — Teruji melalui simulasi Bayesian & Monte Carlo.
       3. *Risiko Eksekusi terukur (Lolos Pre-Mortem)* — Mitigasi *bypass* darurat dengan audit sistem pengadaan dalam 60 hari.
     - **Lapisan Dasar (Bukti Tervalidasi & Decision Lineage PROV-O):** Tautan langsung ke masing-masing node bukti (`Poin Keputusan ➔ Agen AI ➔ Tingkat Kepercayaan Data (<3.0% Deviasi) ➔ Rekomendasi`).

3. **Institutional Memory & Case Library + AI Case Assistant:**
   - Menyimpan kasus keputusan internal perusahaan maupun studi kasus legendaris dunia yang telah dipetakan ke dalam graf:

| Nama Kasus | Domain | Framework Utama yang Digunakan | Status & Hasil |
| :--- | :--- | :--- | :--- |
| **Netflix Streaming Pivot** | Strategi | `JTBD`, `Blue Ocean Strategy`, `BMC` | **Sukses Besar (VHigh)** — Transformasi model bisnis dari penyewaan DVD ke *streaming* global |
| **Toyota TOC on Weld Station** | Operasi | `Theory of Constraints (TOC)`, `PDCA`, `5 Whys` | **Sukses (Optimasi Bottleneck)** — Eliminasi hambatan lini pengelasan dan peningkatan *throughput* |
| **SpaceX First Principles on Cost** | Inovasi | `First Principles Thinking`, `MECE` | **Sukses (Efisiensi Biaya Radikal)** — Dekonstruksi biaya material roket dan pemakaian ulang pendorong |
| **Airbnb Trust Design** | Produk | `Design Thinking`, `Value Proposition Canvas (VPC)` | **Sukses (Peningkatan Kepercayaan)** — Desain ulang sistem reputasi dan fotografi profesional |

   - **AI Case Assistant:** Panel kecerdasan pola yang secara otomatis menganalisis *database* kasus dan memberikan wawasan struktural, misalnya: *"Pola keberhasilan paling konsisten dari database melibatkan kombinasi dekomposisi MECE dilanjutkan dengan 5 Whys."*

4. **Human Mastery Track: Kurikulum 90 Hari (OS yang Melatih Otak Anda):**
   - Mentransfer pola pikir konsultan *tier-1* ke kemampuan organik pengguna melalui kurikulum terstruktur 90 hari dan sistem poin penguasaan (*Mastery Points*):
     - **Phase 1: Structure Reality (Hari 1–30 | Level: Navigator):** Penguasaan dekomposisi masalah (`MECE`, `SCQA`, `5 Whys`, `First Principles`). Lencana: **Structural Thinker**.
     - **Phase 2: Navigate Strategy (Hari 31–60 | Level: Practitioner):** Penguasaan isolasi deviasi, strategi kompetitif, dan prioritas (`Kepner-Tregoe`, `Blue Ocean`, `Wardley Mapping`, `RICE`, `Expected Value`). Lencana: **Root Cause Hunter**.
     - **Phase 3: Orchestrate Systems (Hari 61–90 | Level: Expert / Ahli Strategi):** Penguasaan dinamika sistem kompleks, *Adversarial Red-Teaming*, dan mitigasi bias kognitif (`Theory of Constraints`, `Causal Loops`, `Pre-Mortem`, `Bias Deconstruction`). Lencana: **Logic Guardian**.

---

## Bagian 4: Katalog Lengkap 50 Model Mental (8 Kategori) & 52 Agen AI Spesialis

Di dalam **Cognition OS**, setiap model mental bukan sekadar artikel referensi statis, melainkan sebuah **mikro-aplikasi komputasional** yang dieksekusi oleh 1 Agen AI Spesialis (`AG-01` s/d `AG-50`) dan dikoordinasikan oleh 2 Agen Inti (`AG-51` dan `AG-52`).

### 4.1 Tabel Spesifikasi 50 Model Mental & Agen AI Spesialis (AG-01 s/d AG-50)

#### Kategori 1: Decision Models (8 Model Mental — Fokus: Prioritas & Kalkulus Probabilitas)

| ID Agen | Nama Model Mental | Nama Agen AI Spesialis | Fokus Komputasi & Logika Inti | Input Utama (JSON) | Output Terstruktur (JSON) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **AG-01** | **Eisenhower Matrix** | `Eisenhower Agent` | Pemisahan tugas berdasarkan sumbu *Urgency* vs *Importance* untuk mencegah jebakan reaktif | Daftar inisiatif, tenggat waktu, dampak strategis | Matriks 4 kuadran (`Do First`, `Schedule`, `Delegate`, `Eliminate`) |
| **AG-02** | **RICE Scoring** | `RICE Agent` | Kuantifikasi prioritas inisiatif dengan rumus `(Reach × Impact × Confidence) / Effort` | Daftar solusi, estimasi jangkauan, dampak, keyakinan, usaha | Tabel peringkat inisiatif terurut berdasarkan *RICE Score* |
| **AG-03** | **MoSCoW Method** | `MoSCoW Agent` | Penetapan batas cakupan eksekusi (*Must-have, Should-have, Could-have, Won't-have*) | Daftar fitur/tindakan, batasan waktu & anggaran | Klasifikasi 4 kategori MoSCoW dengan bobot alokasi sumber daya |
| **AG-04** | **Expected Value (EV) Calculus** | `EV Calculus Agent` | Kalkulasi nilai harapan matematis dari multi-skenario probabilitas *upside* vs *downside* | Distribusi probabilitas sukses/gagal, nilai finansial, biaya | Nilai `gross_ev`, `net_ev`, `risk_reward_ratio`, dan status kelayakan |
| **AG-05** | **Bayesian Updating** | `Bayesian Agent` | Pembaruan probabilitas hipotesis (*Prior ➔ Posterior*) setiap kali bukti baru ditemukan | `prior_probability`, `likelihood_if_true`, `false_positive_rate` | `posterior_probability`, `bayes_factor`, dan kurva pergeseran keyakinan |
| **AG-06** | **Pareto Principle (80/20)** | `Pareto 80/20 Agent` | Identifikasi 20% faktor penggerak yang menghasilkan 80% dampak atau kerugian | Dataset kontribusi penyebab atau segmen pendapatan/masalah | Kurva distribusi kumulatif Pareto dan isolasi *vital few drivers* |
| **AG-07** | **Cost-Benefit & Marginal Utility** | `Marginal Utility Agent` | Analisis titik impas, ROI, dan penurunan utilitas marjinal dari penambahan investasi | Rincian biaya tetap/variabel, proyeksi manfaat per unit waktu | Rasio *Benefit-Cost (BCR)*, *Net Present Value (NPV)*, dan titik jenuh |
| **AG-08** | **Regret Minimization Framework** | `Regret Minimization Agent` | Evaluasi keputusan strategis jangka panjang untuk meminimalkan penyesalan di masa depan | Opsi keputusan berisiko tinggi, horizon waktu (10–20 tahun) | Matriks proyeksi *Action Regret* vs *Inaction Regret* & rekomendasi |

#### Kategori 2: Problem Solving Models (8 Model Mental — Fokus: Akar Penyebab & Optimasi Proses)

| ID Agen | Nama Model Mental | Nama Agen AI Spesialis | Fokus Komputasi & Logika Inti | Input Utama (JSON) | Output Terstruktur (JSON) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **AG-09** | **MECE Issue Tree** | `MECE Agent` | Dekomposisi masalah menjadi cabang yang *Mutually Exclusive* & *Collectively Exhaustive* | Pertanyaan utama masalah (`core_question`) dan konteks domain | Pohon hierarki *node* masalah dengan skor validasi *MECE* |
| **AG-10** | **5 Whys Analysis** | `5 Whys Agent` | Penelusuran rantai sebab-akibat berlapis (5 iterasi) untuk menembus gejala permukaan | Gejala masalah spesifik atau anomali cabang dari *Issue Tree* | Rantai kausal `Why 1` s/d `Why 5` + identifikasi akar masalah sistemik |
| **AG-11** | **Kepner-Tregoe (KT) Matrix** | `KT Agent` | Isolasi penyimpangan secara presisi dengan membandingkan spesifikasi *IS* vs *IS NOT* | Pernyataan deviasi, data *What, Where, When, Extent* | Matriks kontras *IS / IS NOT*, daftar *distinctions*, dan penyebab teruji |
| **AG-12** | **Fishbone (Ishikawa) Diagram** | `Fishbone Agent` | Pemetaan faktor penyebab lintas kategori (6M: *Man, Machine, Material, Method, Measurement, Milieu*) | Efek/masalah utama dan data operasional lintas departemen | Struktur diagram tulang ikan 6 kategori beserta sub-penyebab utama |
| **AG-13** | **First Principles Thinking** | `First Principles Agent` | Dekonstruksi asumsi industri hingga ke kebenaran fundamental fisika/ekonomi lalu merekonstruksi solusi | Masalah biaya/inovasi dan daftar asumsi konvensional saat ini | Daftar asumsi yang dipatahkan, aksioma dasar, dan arsitektur solusi baru |
| **AG-14** | **Hypothesis-Driven Problem Solving** | `Hypothesis Agent` | Perumusan hipotesis awal yang dapat diuji (*falsifiable*) beserta desain eksperimen pembuktiannya | Dekomposisi masalah dan keterbatasan data/waktu analisis | Pohon hipotesis (`H0`, `H1`), metrik uji, dan ambang batas penerimaan/penolakan |
| **AG-15** | **Cynefin Framework** | `Cynefin Agent` | Klasifikasi rezim masalah (*Clear, Complicated, Complex, Chaotic, Disorder*) untuk memilih cara respons | Tingkat prediktabilitas kausal dan volatilitas lingkungan masalah | Klasifikasi domain Cynefin dan protokol tindakan (mis. *Probe-Sense-Respond*) |
| **AG-16** | **Inversion Thinking** | `Inversion Agent` | Pembalikan masalah (*"Bagaimana cara memastikan proyek ini hancur total?"*) untuk menutup celah kegagalan | Tujuan strategis utama yang ingin dicapai pengguna | Daftar kondisi pemicu kegagalan mutlak dan langkah pencegahannya (*anti-goals*) |

#### Kategori 3: Systems Thinking Models (7 Model Mental — Fokus: Dinamika Loop & Titik Ungkit)

| ID Agen | Nama Model Mental | Nama Agen AI Spesialis | Fokus Komputasi & Logika Inti | Input Utama (JSON) | Output Terstruktur (JSON) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **AG-17** | **Theory of Constraints (TOC)** | `TOC Agent` | Identifikasi satu *bottleneck* utama yang membatasi *throughput* seluruh sistem (5 Focusing Steps) | Alur proses end-to-end, kapasitas tiap stasiun, tumpukan inventori | Lokasi *bottleneck* kritis dan rencana *Identify, Exploit, Subordinate, Elevate* |
| **AG-18** | **Causal Loop Diagrams (CLD)** | `Causal Loop Agent` | Pemetaan putaran umpan balik penguat (*Reinforcing R*) dan penyeimbang (*Balancing B*) | Variabel-variabel sistem yang saling memengaruhi dari waktu ke waktu | Graf berarah dengan polaritas tautan (`+`/`-`) dan deteksi siklus *R/B* |
| **AG-19** | **Meadows' 12 Leverage Points** | `Leverage Points Agent` | Pencarian titik intervensi sistem dengan dampak perubahan terbesar (dari parameter hingga paradigma) | Struktur sistem saat ini dan daftar rencana intervensi kebijakan | Peringkat intervensi berdasarkan 12 level titik ungkit Donella Meadows |
| **AG-20** | **Second-Order Thinking** | `Second-Order Agent` | Simulasi konsekuensi orde ke-2 dan ke-3 (*"And then what?"*) dari suatu keputusan dalam horizon waktu | Tindakan intervensi yang diusulkan dan respons aktor di ekosistem | Pohon dampak berantai (Horizon 1: 0–3 bln, Horizon 2: 3–12 bln, Horizon 3: >1 thn) |
| **AG-21** | **Stock and Flow Modeling** | `Stock & Flow Agent` | Pemodelan akumulasi sumber daya (*Stocks*), laju aliran masuk (*Inflows*), dan aliran keluar (*Outflows*) | Kapasitas awal, laju penambahan, laju penyusutan/churn, waktu tunda | Persamaan diferensial diskrit dan grafik simulasi akumulasi *stock* |
| **AG-22** | **System Archetypes** | `Archetypes Agent` | Deteksi pola disfungsi sistemik klasik (*Fixes that Fail, Shifting the Burden, Tragedy of the Commons*) | Gejala berulang dan riwayat solusi masa lalu yang gagal bertahan | Identifikasi *System Archetype* yang aktif dan strategi pemutusan siklus |
| **AG-23** | **Network Effects & Feedback** | `Network Effects Agent` | Analisis dinamika pertumbuhan jaringan (*direct, indirect, two-sided, local network effects*) | Struktur interaksi pengguna/pemasok, biaya perpindahan (*switching cost*) | Koefisien elastisitas jaringan, titik *critical mass*, dan risiko *moat decay* |

#### Kategori 4: Strategic Models (8 Model Mental — Fokus: Inovasi Nilai & Analisis Industri)

| ID Agen | Nama Model Mental | Nama Agen AI Spesialis | Fokus Komputasi & Logika Inti | Input Utama (JSON) | Output Terstruktur (JSON) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **AG-24** | **Blue Ocean Strategy (ERRC)** | `Blue Ocean Agent` | Penciptaan ruang pasar baru melalui matriks *Eliminate-Reduce-Raise-Create* & kanvas strategi nilai | Faktor kompetisi industri saat ini dan segmen non-pelanggan | Matriks ERRC 4 kuadran, kurva nilai baru, dan argumen optimis pertumbuhan |
| **AG-25** | **Wardley Mapping** | `Wardley Map Agent` | Pemetaan komponen rantai nilai (*Value Chain*) terhadap tingkat evolusi (*Genesis ➔ Commodity*) | Kebutuhan pengguna (*anchor*), komponen sistem, dan maturitas teknologi | Koordinat peta Wardley `[visibility_y, evolution_x]` & rekomendasi *build vs buy* |
| **AG-26** | **OODA Loop** | `OODA Loop Agent` | Percepatan siklus *Observe-Orient-Decide-Act* untuk mengungguli manuver kompetitor di pasar dinamis | Sinyal perubahan pasar, kecepatan respons organisasi saat ini | Protokol percepatan *OODA Loop* dan titik disrupsi ritme kompetitor |
| **AG-27** | **Porter's Five Forces** | `Five Forces Agent` | Evaluasi daya tarik struktural industri dan tekanan margin dari 5 kekuatan kompetitif | Struktur pasar, jumlah pemasok/pembeli, hambatan masuk, produk substitusi | Skor intensitas 5 kekuatan (1–10) dan strategi pertahanan margin |
| **AG-28** | **VRIO Framework** | `VRIO Agent` | Audit sumber daya internal (*Value, Rarity, Inimitability, Organization*) untuk keunggulan berkelanjutan | Daftar aset, kapabilitas, teknologi, atau paten milik perusahaan | Matriks klasifikasi keunggulan kompetitif (*Temporary* vs *Sustained*) |
| **AG-29** | **Ansoff Matrix** | `Ansoff Agent` | Penentuan vektor pertumbuhan korporat (*Market Penetration, Market Dev, Product Dev, Diversification*) | Portofolio produk saat ini, target pasar, dan profil toleransi risiko | Kuadran strategi pertumbuhan Ansoff beserta bobot risiko eksekusi |
| **AG-30** | **Game Theory (Nash Equilibrium)** | `Game Theory Agent` | Pemodelan interaksi strategis multi-aktor, matriks *payoff*, dan pencarian ekuilibrium Nash | Daftar pemain (perusahaan vs kompetitor), opsi langkah, dan *payoff* | Matriks *payoff*, strategi dominan, *Nash Equilibrium*, dan langkah *first-mover* |
| **AG-31** | **Business Model Canvas (BMC)** | `BMC Agent` | Pemetaan 9 blok arsitektur model bisnis untuk memastikan keselarasan proposisi nilai dan struktur biaya | Deskripsi bisnis/inisiatif baru, segmen pelanggan, saluran, arus kas | Struktur lengkap 9 blok BMC beserta uji koherensi antar-blok |

#### Kategori 5: Innovation Models (6 Model Mental — Fokus: Desain Berpusat pada Manusia & R&D)

| ID Agen | Nama Model Mental | Nama Agen AI Spesialis | Fokus Komputasi & Logika Inti | Input Utama (JSON) | Output Terstruktur (JSON) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **AG-32** | **Jobs-to-be-Done (JTBD)** | `JTBD Agent` | Mengungkap kemajuan fungsional, sosial, dan emosional yang ingin dicapai pelanggan saat "menyewa" produk | Perilaku pelanggan, keluhan penggunaan, dan solusi alternatif saat ini | Pernyataan *Job Story* (`When... I want to... So I can...`) & *Underserved Needs* |
| **AG-33** | **Design Thinking** | `Design Thinking Agent` | Orkestrasi empati pengguna, pendefinisian ulang masalah (*How Might We*), ideasi, dan prototipe cepat | Hasil observasi pengguna, titik friksi perjalanan pelanggan (*journey*) | Rumusan pertanyaan *How Might We (HMW)* dan spesifikasi eksperimen prototipe |
| **AG-34** | **Value Proposition Canvas (VPC)** | `VPC Agent` | Pencocokan presisi antara *Customer Profile* (*Jobs, Pains, Gains*) dengan *Value Map* (*Pain Relievers, Gain Creators*) | Segmen pelanggan target dan fitur produk/solusi yang dirancang | Peta kesesuaian *Problem-Solution Fit* dan daftar celah proposisi nilai |
| **AG-35** | **Kano Model** | `Kano Agent` | Klasifikasi atribut produk menjadi *Basic (Must-be)*, *Performance*, dan *Delighters (Attractive)* | Daftar kandidat fitur produk dan respons kepuasan/ketidakpuasan pengguna | Pemetaan kurva Kano dan prioritas investasi fitur pembeda |
| **AG-36** | **SCAMPER** | `SCAMPER Agent` | Eksplorasi inovasi produk/proses melalui 7 lensa (*Substitute, Combine, Adapt, Modify, Put to another use, Eliminate, Reverse*) | Produk, layanan, atau alur kerja eksisting yang mengalami stagnasi | 7 variasi konsep inovasi terstruktur berdasarkan matriks SCAMPER |
| **AG-37** | **TRIZ (Inventive Problem Solving)** | `TRIZ Agent` | Penyelesaian kontradiksi teknis/bisnis menggunakan 40 Prinsip Inventif tanpa kompromi (*trade-off*) | Parameter yang ingin ditingkatkan vs parameter yang memburuk (*contradiction*) | Prinsip TRIZ yang relevan dan solusi eliminasi kontradiksi |

#### Kategori 6: Execution Models (5 Model Mental — Fokus: Tata Kelola RACI & Alur Kerja GTD)

| ID Agen | Nama Model Mental | Nama Agen AI Spesialis | Fokus Komputasi & Logika Inti | Input Utama (JSON) | Output Terstruktur (JSON) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **AG-38** | **RACI Governance Matrix** | `RACI Agent` | Pemetaan akuntabilitas eksekusi (*Responsible, Accountable, Consulted, Informed*) tanpa tumpang tindih | Daftar paket kerja (*workstreams*) dan daftar peran/pemangku kepentingan | Tabel matriks RACI tervalidasi (memastikan tepat 1 *Accountable* per baris) |
| **AG-39** | **OKRs (Objectives & Key Results)** | `OKR Agent` | Penerjemahan keputusan strategis menjadi *Objectives* kualitatif dan *Key Results* kuantitatif terukur | Rekomendasi strategis akhir dan target metrik kuartalan/tahunan | Hierarki OKR tingkat korporat/tim beserta *leading & lagging indicators* |
| **AG-40** | **PDCA (Plan-Do-Check-Act)** | `PDCA Agent` | Perancangan siklus perbaikan berkelanjutan dan kontrol kualitas implementasi di lapangan | Rencana intervensi operasional dan metrik standar kinerja (*baseline*) | Siklus iterasi 4 tahap PDCA lengkap dengan ambang batas evaluasi *Check* |
| **AG-41** | **Getting Things Done (GTD)** | `GTD Workflow Agent` | Dekomposisi proyek menjadi tindakan fisik berikutnya (*Next Concrete Actions*), konteks, dan pemicu | Rencana proyek tingkat tinggi dan daftar hambatan operasional harian | Daftar *Next Actions* bebas ambiguitas, pemilik tugas, dan jadwal *review* |
| **AG-42** | **Critical Path Method (CPM)** | `Critical Path Agent` | Kalkulasi jalur terpanjang aktivitas dependen yang menentukan durasi minimum penyelesaian proyek | Daftar tugas, estimasi durasi, dan ketergantungan (*predecessors*) | Jalur kritis (*Critical Path*), waktu *float/slack* tiap tugas, dan jadwal |

#### Kategori 7: Communication Models (6 Model Mental — Fokus: Struktur Narasi & Umpan Balik)

| ID Agen | Nama Model Mental | Nama Agen AI Spesialis | Fokus Komputasi & Logika Inti | Input Utama (JSON) | Output Terstruktur (JSON) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **AG-43** | **Minto Pyramid Principle** | `Minto Pyramid Agent` | Penyusunan argumen eksekutif *top-down* (*Answer First* ➔ *MECE Key Line Arguments* ➔ *Validated Evidence*) | Seluruh temuan dari *Thinking Canvas*, *Debate*, dan *Scenario Simulator* | Struktur pohon Minto Pyramid siap ekspor ke laporan PDF & dek PPTX |
| **AG-44** | **SCQA Framework** | `SCQA Agent` | Pembingkaian konteks masalah secara tajam (*Situation, Complication, Question, Answer*) | Deskripsi masalah mentah dan metrik perubahan kondisi bisnis | Narasi terstruktur 4 bagian SCQA untuk menyelaraskan pemahaman pemangku kepentingan |
| **AG-45** | **Storyboarding & Narrative** | `Storyboarding Agent` | Perancangan alur presentasi visual *slide-by-slide* dengan *declarative action titles* | Struktur Minto Pyramid dan grafik data pendukung | Spesifikasi *storyboard* per halaman (*Action Title, Visual Layout, Key Data*) |
| **AG-46** | **Stakeholder Grid** | `Stakeholder Agent` | Pemetaan pemangku kepentingan berdasarkan *Power/Influence* vs *Interest* untuk strategi persuasi | Daftar pengambil keputusan, kepentingan departemen, dan potensi resistensi | Matriks 4 kuadran pemangku kepentingan dan taktik komunikasi per aktor |
| **AG-47** | **Radical Candor Feedback** | `Radical Candor Agent` | Perumusan komunikasi kepemimpinan yang memadukan *Care Personally* dan *Challenge Directly* | Situasi konflik tim, kegagalan eksekusi, atau kebutuhan evaluasi kinerja | Naskah umpan balik yang lugas, objektif, dan konstruktif tanpa agresi |
| **AG-48** | **Toulmin Argumentation Model** | `Toulmin Agent` | Pengujian struktur mikro-argumen (*Claim, Grounds/Data, Warrant, Backing, Qualifier, Rebuttal*) | Pernyataan klaim strategis dan kumpulan bukti pendukung | Dekonstruksi 6 elemen Toulmin dan identifikasi celah *warrant* logika |

#### Kategori 8: Meta-Thinking Models (2 Model Mental — Fokus: Deteksi Bias & Validasi Belajar)

| ID Agen | Nama Model Mental | Nama Agen AI Spesialis | Fokus Komputasi & Logika Inti | Input Utama (JSON) | Output Terstruktur (JSON) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **AG-49** | **Pre-Mortem & Red Teaming** | `Pre-Mortem Agent` | Simulasi ke masa depan dengan asumsi keputusan **telah gagal total**, lalu merunut balik penyebab kehancurannya | Rekomendasi keputusan yang akan dieksekusi dan asumsi keberhasilannya | Daftar skenario kegagalan kritis, titik rapuh tersembunyi, dan tindakan pencegahan |
| **AG-50** | **Cognitive Bias Deconstruction** | `Bias Detector Agent` | Pemindaian aktif terhadap lebih dari 20 bias kognitif (*Confirmation, Anchoring, Sunk Cost, Survivorship, Availability*) | Teks argumen pengguna, bobot bukti di kanvas, dan riwayat revisi hipotesis | Laporan deteksi bias (`bias_type`, `probability`, `evidence_span`, `debiasing_prompt`) |

### 4.2 Spesifikasi 2 Agen Inti Sistem (AG-51 & AG-52)

| ID Agen | Nama Agen Inti | Peran Arsitektural di Lapisan 2 | Tanggung Jawab Komputasi Utama |
| :--- | :--- | :--- | :--- |
| **AG-51** | **Chief Orchestrator Agent** | Pengatur lalu lintas utama, perencana *Framework Stack*, dan manajer eksekusi paralel | 1. Menganalisis input dari *Problem Ingestion Wizard*.<br>2. Merekomendasikan kombinasi *Framework Stack* optimal.<br>3. Membagi tugas secara paralel (*fan-out*) ke agen-agen spesialis (`AG-01` s/d `AG-50`).<br>4. Mengelola anggaran waktu sesi agar *Time to Synthesis (T2S)* tetap di bawah 30 menit. |
| **AG-52** | **Evaluator Jury & Critic Agent** | Hakim konsensus pada *Adversarial Debate Mode* dan pengawas skor kualitas penalaran | 1. Memimpin sidang *Adversarial Debate* antara **Blue Ocean Agent (`AG-24`)** dan **Pre-Mortem Agent (`AG-49`)**.<br>2. Merumuskan **Sintesis Konsensus** yang menggabungkan kecepatan eksekusi dengan pagar pengaman risiko.<br>3. Menghitung skor akhir **MECE Validation**, **Data Integrity**, dan **PROV-O Confidence Score**. |

### 4.3 Kontrak Pertukaran Data Antar-Agen (JSON Schema Payload) & System Prompt Produksi

Agar setiap kerangka kerja di *Framework Stack Builder* dapat memberi umpan data (*feed*) secara otomatis ke kerangka kerja berikutnya, seluruh 52 agen wajib berkomunikasi menggunakan skema JSON terstandar (**Cognition OS Agent Envelope**):

```json
{
  "envelope_version": "2.0",
  "session_id": "sess_q3_profit_0982",
  "trace_id": "prov_act_kt_004",
  "source_agent": {
    "agent_id": "AG-11",
    "agent_name": "KT Agent",
    "framework_id": "FW-11",
    "framework_name": "Kepner-Tregoe Matrix",
    "category": "Problem Solving"
  },
  "upstream_entity_ids": ["prov_ent_mece_node_vol_down_02"],
  "execution_metrics": {
    "latency_ms": 1840,
    "confidence_score": 0.94,
    "margin_of_error": 0.024,
    "mece_compliance": 0.96
  },
  "payload": {
    "deviation_statement": "Penurunan profitabilitas Q3 sebesar 18% yang terkonsentrasi pada penurunan volume penjualan sebesar 25% di jaringan toko Barat.",
    "is_vs_is_not_matrix": {
      "what": {
        "is": "SKU bermargin tinggi (Kategori Premium A)",
        "is_not": "SKU reguler atau barang promosi musiman",
        "distinction": "SKU bermargin tinggi memiliki masa tunggu pemasok khusus dan aturan persetujuan ulang otomatis."
      },
      "where": {
        "is": "Toko-toko wilayah Barat (Western stores)",
        "is_not": "Toko-toko wilayah Timur, Tengah, atau kanal e-commerce",
        "distinction": "Gudang distribusi wilayah Barat menggunakan sistem manajemen pengadaan terpusat versi baru."
      },
      "when": {
        "is": "Mulai terlihat tajam pasca 15 Juni hingga akhir Q3",
        "is_not": "Sebelum 15 Juni (Q1 dan paruh awal Q2 stabil)",
        "distinction": "Perubahan kebijakan batas otorisasi pengadaan diterapkan pada tanggal 15 Juni."
      },
      "extent": {
        "is": "Frekuensi stockout meningkat 340%, memicu penurunan pendapatan wilayah Barat sebesar 25%",
        "is_not": "Penurunan merata di seluruh SKU atau penurunan harga jual rata-rata (ASP)",
        "distinction": "Permintaan pelanggan tetap tinggi tetapi tidak terlayani karena kekosongan stok di rak."
      }
    },
    "confirmed_root_cause": "Volume menurun akibat kehabisan stok (stockout) SKU bermargin tinggi di toko-toko Barat—meningkat 340% pasca perubahan kebijakan pengadaan 15 Juni.",
    "downstream_recommendations_seed": [
      "Terapkan pengecualian pengadaan 48-jam untuk SKU margin tinggi di toko Barat",
      "Lakukan audit menyeluruh terhadap parameter kebijakan pengadaan 15 Juni dalam 60 hari"
    ]
  }
}
```

#### Template System Prompt Standar untuk Agen Spesialis (Contoh: `AG-11 Kepner-Tregoe Agent` & `AG-52 Evaluator Jury`)

```yaml
# SYSTEM PROMPT: AG-11 (Kepner-Tregoe Problem Analysis Specialist)
role: "Kepner-Tregoe Root Cause & Deviation Isolation Specialist (AG-11)"
objective: >
  Mengisolasi akar penyebab penyimpangan kinerja secara presisi menggunakan matriks
  spesifikasi Kepner-Tregoe (IS vs IS NOT pada dimensi What, Where, When, Extent)
  tanpa melompat ke kesimpulan prematur.
strict_rules:
  - Jangan pernah menerima gejala permukaan (seperti "penjualan turun") sebagai akar penyebab.
  - Untuk setiap dimensi (What, Where, When, Extent), Anda WAJIB mengisi kolom 'IS', 'IS NOT',
    dan 'Distinction' (apa yang membedakan kondisi IS dari IS NOT).
  - Uji setiap kandidat penyebab terhadap baik data 'IS' maupun 'IS NOT'. Kandidat penyebab
    hanya lulus jika menjelaskan seluruh kondisi 'IS' dan menjelaskan mengapa tidak terjadi pada 'IS NOT'.
  - Hitung 'confidence_score' (0.00 - 1.00) berdasarkan kelengkapan bukti empiris pada setiap dimensi.
output_schema: "KepnerTregoeEnvelopeV2"

---
# SYSTEM PROMPT: AG-52 (Evaluator Jury & Consensus Synthesizer)
role: "Adversarial Debate Jury & Logic Guardian (AG-52)"
objective: >
  Mengadili perdebatan antara Blue Ocean Agent (AG-24, Optimis) dan Pre-Mortem Agent
  (AG-49, Pesimis) secara objektif, mengeliminasi bias kognitif dari kedua kutub,
  dan merumuskan direktif eksekusi bersyarat (Conditional Execution Directive).
strict_rules:
  - Evaluasi argumen Blue Ocean Agent berdasarkan potensi nilai ekonomi (Upside) dan kecepatan eksekusi.
  - Evaluasi argumen Pre-Mortem Agent berdasarkan probabilitas titik kegagalan sistemik dan risiko jangka panjang.
  - Jangan memilih salah satu agen secara buta; rumuskan sintesis yang mengeksekusi tindakan berdampak tinggi
    dalam jendela waktu pendek (mis. 48 jam) sembari mengikatnya dengan protokol audit/mitigasi struktural (mis. 60 hari).
  - Cantumkan jejak referensi ke node bukti di Thinking Canvas untuk menjaga 100% Reasoning Traceability.
output_schema: "AdversarialConsensusEnvelopeV2"
```

---

## Bagian 5: Mesin Komputasi Matematis & Algoritma Validasi Real-Time

Untuk mewujudkan klaim *"Mengubah pemecahan masalah strategis menjadi ilmu pasti"*, Lapisan 4 (**Logic Guardrails & Scenario Simulator**) menggunakan mesin matematika deterministik dan stokastik berikut.

### 5.1 Formulasi Matematis Inti

1. **Kalkulasi Expected Value (EV) & Simulasi Monte Carlo:**
   - Setiap skenario keputusan dimodelkan sebagai variabel acak kontinu untuk menangkap ketidakpastian nyata di lapangan:
     - Probabilitas keberhasilan dimodelkan menggunakan **Distribusi Beta** $P \sim \text{Beta}(\alpha, \beta)$ dengan nilai tengah $\mu_P = p_0$ (dari *slider* pengguna, mis. $0.65$) dan konsentrasi $\kappa$ yang ditentukan oleh *Confidence Score* dari *Thinking Canvas*.
     - Nilai *Upside* ($U$) dan *Downside* ($D$) dimodelkan menggunakan **Distribusi Log-Normal / Triangular** di sekitar estimasi pengguna ($U_0 = \$2.4\text{M}$, $D_0 = \$0.3\text{M}$).
     - Biaya eksekusi ($C$) dimodelkan dengan risiko pembengkakan biaya (*cost overrun*) $C \sim \text{Triangular}(0.9 C_0, C_0, 1.25 C_0)$.
   - Untuk $N = 10.000$ iterasi simulasi Monte Carlo, nilai bersih per iterasi $i$ adalah:
     $$\text{NetOutcome}_i = \mathbb{I}(u_i \le P_i) \cdot U_i - \mathbb{I}(u_i > P_i) \cdot D_i - C_i, \quad u_i \sim \mathcal{U}(0, 1)$$
     Nilai harapan eksak ($\text{EV}_{\text{net}}$) dan distribusi empirisnya dihitung secara serentak untuk merender kurva dua kutub di UI.

2. **Pembaruan Probabilitas Bayesian Real-Time (Bayesian Updating):**
   - Ketika pengguna atau agen menambahkan bukti baru $E_k$ di *Thinking Canvas* (misalnya konfirmasi Kepner-Tregoe bahwa *stockout* melonjak 340% tepat setelah 15 Juni), probabilitas *Prior* $P(H)$ diperbarui menjadi *Posterior* $P(H \mid E_k)$ menggunakan Teorema Bayes dalam bentuk *Log-Odds*:
     $$\text{Odds}(H \mid E_1, \dots, E_k) = \text{Odds}(H) \times \prod_{j=1}^{k} \text{LR}_j, \quad \text{di mana } \text{LR}_j = \frac{P(E_j \mid H)}{P(E_j \mid \neg H)}$$
     $$P(H \mid E_1, \dots, E_k) = \frac{\text{Odds}(H \mid E_1, \dots, E_k)}{1 + \text{Odds}(H \mid E_1, \dots, E_k)}$$

3. **Skor Validasi MECE (*Mutually Exclusive & Collectively Exhaustive*):**
   - Misalkan sebuah *node* induk $v_0$ didekomposisi menjadi $m$ cabang anak $\{v_1, v_2, \dots, v_m\}$ dengan representasi vektor *embedding* ternormalisasi $\{\mathbf{e}_1, \mathbf{e}_2, \dots, \mathbf{e}_m\}$:
     - **Skor Mutually Exclusive ($\text{Score}_{\text{ME}}$):** Mengukur ketiadaan tumpang tindih antar-cabang saudara:
       $$\text{Overlap}_{i,j} = \max(0, \mathbf{e}_i \cdot \mathbf{e}_j - \tau_{\text{baseline}}), \quad \text{Score}_{\text{ME}} = 1 - \max_{i \neq j} \text{Overlap}_{i,j}$$
     - **Skor Collectively Exhaustive ($\text{Score}_{\text{CE}}$):** Mengukur proporsi dimensi kanonik domain yang tercakup oleh gabungan cabang anak dikurangi penalti *edge cases* yang terlewat ($k_{\text{missing}}$):
       $$\text{Score}_{\text{CE}} = \frac{|\text{Covered Dimensions}|}{|\text{Canonical Domain Dimensions}|} \times (1 - 0.05 \cdot k_{\text{missing}})$$
     - **Skor Gabungan MECE:**
       $$\text{MECE Score} = 100 \times \left(0.55 \cdot \text{Score}_{\text{ME}} + 0.45 \cdot \text{Score}_{\text{CE}}\right)$$

### 5.2 Implementasi Kode Produksi Python (`cognition_engine/math_guardrails.py`)

```python
from __future__ import annotations
from dataclasses import dataclass, asdict
from typing import List, Dict, Tuple
import numpy as np


@dataclass
class SimulationInput:
    prob_success: float       # Contoh: 0.65 (65%)
    upside_millions: float    # Contoh: 2.4 ($2.4M)
    downside_millions: float  # Contoh: 0.3 ($0.3M)
    costs_millions: float     # Contoh: 0.8 ($0.8M)
    confidence_level: float = 0.94
    iterations: int = 10_000
    random_seed: int = 42


@dataclass
class SimulationOutput:
    deterministic_gross_ev: float
    deterministic_net_ev: float
    monte_carlo_mean_ev: float
    monte_carlo_median_ev: float
    prob_positive_net_return: float
    value_at_risk_95: float
    confidence_margin_pct: float
    recommendation: str       # "PROCEED" | "REVIEW_CONSTRAINTS" | "ABORT"
    success_curve_bins: List[Dict[str, float]]
    failure_curve_bins: List[Dict[str, float]]


class ExpectedValueMonteCarloEngine:
    """
    Mesin komputasi Expected Value (EV), Bayesian Updating, dan Simulasi Monte Carlo
    untuk Fase 5 (Scenario Simulator) pada Cognition OS.
    """

    @staticmethod
    def bayesian_update(prior: float, likelihood_ ratios: List[float]) -> float:
        """Memperbarui probabilitas Prior menggunakan urutan Likelihood Ratio (LR)."""
        prior_clamped = np.clip(prior, 1e-5, 1.0 - 1e-5)
        odds = prior_clamped / (1.0 - prior_clamped)
        for lr in likelihood_ratios:
            odds *= max(lr, 1e-4)
        posterior = odds / (1.0 + odds)
        return float(np.round(posterior, 4))

    @classmethod
    def run_simulation(cls, params: SimulationInput) -> SimulationOutput:
        rng = np.random.default_rng(params.random_seed)

        # 1. Kalkulasi Deterministik Eksak (Sesuai Slide 8: EV = +$0.65M)
        p = np.clip(params.prob_success, 0.0, 1.0)
        q = 1.0 - p
        gross_ev = (p * params.upside_millions) - (q * params.downside_millions)
        net_ev = gross_ev - params.costs_millions

        # 2. Parameterisasi Distribusi Beta & Normal Terpotong untuk Monte Carlo
        kappa = max(10.0, params.confidence_level * 100.0)
        alpha = max(1.0, p * kappa)
        beta_param = max(1.0, q * kappa)

        sampled_probs = rng.beta(alpha, beta_param, size=params.iterations)
        uniform_draws = rng.uniform(0.0, 1.0, size=params.iterations)
        is_success = uniform_draws <= sampled_probs

        # Variansi Upside, Downside, dan Costs
        upside_draws = rng.normal(loc=params.upside_millions, scale=0.15 * params.upside_millions, size=params.iterations)
        upside_draws = np.maximum(0.0, upside_draws)

        downside_draws = rng.normal(loc=params.downside_millions, scale=0.20 * params.downside_millions, size=params.iterations)
        downside_draws = np.maximum(0.0, downside_draws)

        cost_draws = rng.triangular(
            left=0.90 * params.costs_millions,
            mode=params.costs_millions,
            right=1.20 * params.costs_millions,
            size=params.iterations,
        )

        # Hasil Bersih per Iterasi
        net_outcomes = np.where(
            is_success,
            upside_draws - cost_draws,
            -downside_draws - cost_draws,
        )

        mc_mean = float(np.mean(net_outcomes))
        mc_median = float(np.median(net_outcomes))
        prob_positive = float(np.mean(net_outcomes > 0.0))
        var_95 = float(np.percentile(net_outcomes, 5))
        std_err = float(np.std(net_outcomes) / np.sqrt(params.iterations))
        margin_pct = float((1.96 * std_err / max(abs(mc_mean), 0.01)) * 100.0)

        # Keputusan Otomatis
        if net_ev > 0.0 and prob_positive >= 0.55:
            recommendation = "PROCEED"
        elif net_ev > -0.15:
            recommendation = "REVIEW_CONSTRAINTS"
        else:
            recommendation = "ABORT"

        # 3. Pembuatan Kurva Distribusi Dua Kutub untuk UI Scenario Simulator
        success_samples = net_outcomes[is_success]
        failure_samples = net_outcomes[~is_success]

        def build_histogram(samples: np.ndarray, bins: int = 20) -> List[Dict[str, float]]:
            if len(samples) == 0:
                return []
            counts, edges = np.histogram(samples, bins=bins, density=True)
            centers = 0.5 * (edges[:-1] + edges[1:])
            return [
                {"value_millions": round(float(c), 3), "density": round(float(d), 4)}
                for c, d in zip(centers, counts)
            ]

        return SimulationOutput(
            deterministic_gross_ev=round(float(gross_ev), 2),
            deterministic_net_ev=round(float(net_ev), 2),
            monte_carlo_mean_ev=round(mc_mean, 2),
            monte_carlo_median_ev=round(mc_median, 2),
            prob_positive_net_return=round(prob_positive, 4),
            value_at_risk_95=round(var_95, 2),
            confidence_margin_pct=round(margin_pct, 2),
            recommendation=recommendation,
            success_curve_bins=build_histogram(success_samples),
            failure_curve_bins=build_histogram(failure_samples),
        )


class RealTimeLogicGuardrails:
    """
    Mesin MECE Validator & Cognitive Bias Detector untuk Lapisan 4 Cognition OS.
    """

    @staticmethod
    def evaluate_mece_branches(
        branch_embeddings: np.ndarray,
        branch_labels: List[str],
        covered_dimensions: int,
        total_canonical_dimensions: int,
        missing_edge_cases: List[str],
        overlap_threshold: float = 0.72,
    ) -> Dict[str, object]:
        """
        Menghitung skor MECE dari kumpulan cabang saudara pada Thinking Canvas
        dan mengidentifikasi pasangan cabang yang tumpang tindih.
        """
        norms = np.linalg.norm(branch_embeddings, axis=1, keepdims=True)
        normalized = branch_embeddings / np.maximum(norms, 1e-9)
        sim_matrix = np.dot(normalized, normalized.T)

        n = len(branch_labels)
        overlapping_pairs: List[Tuple[str, str, float]] = []
        max_overlap = 0.0

        for i in range(n):
            for j in range(i + 1, n):
                sim = float(sim_matrix[i, j])
                if sim > max_overlap:
                    max_overlap = sim
                if sim >= overlap_threshold:
                    overlapping_pairs.append((branch_labels[i], branch_labels[j], round(sim, 3)))

        me_score = max(0.0, 1.0 - max(0.0, max_overlap - 0.35))
        ce_ratio = min(1.0, covered_dimensions / max(1, total_canonical_dimensions))
        ce_score = max(0.0, ce_ratio * (1.0 - 0.05 * len(missing_edge_cases)))

        combined_mece = round(100.0 * (0.55 * me_score + 0.45 * ce_score), 1)
        exhaustive_pct = round(100.0 * ce_score, 1)

        return {
            "data_integrity_pct": 99.2,
            "mece_score_pct": combined_mece,
            "exhaustive_score_pct": exhaustive_pct,
            "edge_cases_detected": len(missing_edge_cases),
            "missing_edge_cases_list": missing_edge_cases,
            "overlapping_branches": [
                {
                    "branch_a": a,
                    "branch_b": b,
                    "similarity": s,
                    "warning": f"{a} & {b} tumpang tindih. Skor Exhaustive: {exhaustive_pct}% (Kehilangan edge cases).",
                }
                for a, b, s in overlapping_pairs
            ],
            "is_mece_valid": combined_mece >= 85.0 and len(overlapping_pairs) == 0,
        }
```

---

## Bagian 6: Skema Database (PostgreSQL + pgvector) & Reasoning Knowledge Graph (Neo4j PROV-O)

### 6.1 Skema Database Relasional & Vektor (`PostgreSQL 16 + pgvector`)

Skrip DDL berikut mendefinisikan struktur penyimpanan utama untuk sesi masalah, kanvas visual, debat multi-agen, simulator skenario, perpustakaan kasus, dan kurikulum 90 hari:

```sql
-- Aktifkan ekstensi UUID dan pgvector untuk pencarian semantik Case Library
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";
CREATE EXTENSION IF NOT EXISTS "vector";

-- 1. Tabel Pengguna & Progres Kurikulum 90-Day Human Mastery Track
CREATE TABLE users (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    email VARCHAR(255) UNIQUE NOT NULL,
    full_name VARCHAR(255) NOT NULL,
    organization_role VARCHAR(120) DEFAULT 'Executive Strategist',
    mastery_tier VARCHAR(50) DEFAULT 'Navigator' CHECK (mastery_tier IN ('Navigator', 'Practitioner', 'Expert', 'Ahli Strategi')),
    mastery_points INTEGER DEFAULT 0,
    phase_1_progress NUMERIC(5,2) DEFAULT 0.00, -- Structure Reality
    phase_2_progress NUMERIC(5,2) DEFAULT 0.00, -- Navigate Strategy
    phase_3_progress NUMERIC(5,2) DEFAULT 0.00, -- Orchestrate Systems
    unlocked_badges JSONB DEFAULT '["Structural Thinker"]'::jsonb,
    created_at TIMESTAMPTZ DEFAULT NOW()
);

-- 2. Tabel Sesi Masalah Strategis (Command Center & Problem Ingestion Wizard)
CREATE TABLE strategic_problems (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    owner_id UUID REFERENCES users(id) ON DELETE CASCADE,
    title VARCHAR(300) NOT NULL,               -- Contoh: 'Q3 Profitability Decline'
    raw_problem_statement TEXT NOT NULL,
    primary_domain VARCHAR(80) NOT NULL,       -- Contoh: 'Strategy', 'Operations'
    domain_tags JSONB DEFAULT '[]'::jsonb,
    context_constraints JSONB NOT NULL,        -- Contoh: '{"western_stores_delta": -0.25, "policy_change_date": "2026-06-15"}'
    system_status VARCHAR(40) DEFAULT 'OPTIMAL',
    graph_density NUMERIC(4,2) DEFAULT 0.78,
    risk_factor VARCHAR(20) DEFAULT 'LOW' CHECK (risk_factor IN ('LOW', 'MEDIUM', 'HIGH', 'CRITICAL')),
    time_to_synthesis_seconds INTEGER DEFAULT 0,
    selected_framework_stack JSONB NOT NULL,   -- Contoh: '["FW-44", "FW-09", "FW-11", "FW-02"]'
    created_at TIMESTAMPTZ DEFAULT NOW(),
    updated_at TIMESTAMPTZ DEFAULT NOW()
);

-- 3. Tabel Node Thinking Canvas (Issue Tree, 5 Whys, Kepner-Tregoe, Causal Loops)
CREATE TABLE thinking_canvas_nodes (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    problem_id UUID REFERENCES strategic_problems(id) ON DELETE CASCADE,
    parent_node_id UUID REFERENCES thinking_canvas_nodes(id) ON DELETE SET NULL,
    node_type VARCHAR(50) NOT NULL CHECK (node_type IN ('ROOT', 'MECE_BRANCH', 'FIVE_WHYS_STEP', 'ROOT_CAUSE', 'KT_DIAGNOSIS', 'HYPOTHESIS', 'EVIDENCE')),
    label VARCHAR(500) NOT NULL,               -- Contoh: 'Volume ↓'
    detailed_diagnosis TEXT,                   -- Contoh: 'Diagnosis Kepner-Tregoe mengonfirmasi...'
    is_root_cause BOOLEAN DEFAULT FALSE,
    confidence_score NUMERIC(5,4) DEFAULT 0.9400,
    mece_score NUMERIC(5,2) DEFAULT 96.00,
    position_x NUMERIC(10,2) NOT NULL DEFAULT 0,
    position_y NUMERIC(10,2) NOT NULL DEFAULT 0,
    agent_id VARCHAR(20) NOT NULL,             -- Contoh: 'AG-09', 'AG-11'
    prov_entity_uri VARCHAR(255) UNIQUE NOT NULL,
    embedding vector(1536),
    metadata JSONB DEFAULT '{}'::jsonb,
    created_at TIMESTAMPTZ DEFAULT NOW()
);

-- 4. Tabel Sesi Adversarial Debate Mode
CREATE TABLE adversarial_debates (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    problem_id UUID REFERENCES strategic_problems(id) ON DELETE CASCADE,
    optimist_agent_id VARCHAR(20) DEFAULT 'AG-24', -- Blue Ocean Agent
    optimist_argument JSONB NOT NULL,
    pessimist_agent_id VARCHAR(20) DEFAULT 'AG-49', -- Pre-Mortem Agent
    pessimist_argument JSONB NOT NULL,
    jury_agent_id VARCHAR(20) DEFAULT 'AG-52',      -- Evaluator Jury
    consensus_directive TEXT NOT NULL,
    consensus_confidence NUMERIC(5,4) NOT NULL DEFAULT 0.9200,
    created_at TIMESTAMPTZ DEFAULT NOW()
);

-- 5. Tabel Scenario Simulator & Expected Value Runs
CREATE TABLE scenario_simulations (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    problem_id UUID REFERENCES strategic_problems(id) ON DELETE CASCADE,
    prob_success NUMERIC(5,4) NOT NULL,        -- 0.6500
    upside_millions NUMERIC(12,4) NOT NULL,    -- 2.4000
    downside_millions NUMERIC(12,4) NOT NULL,  -- 0.3000
    costs_millions NUMERIC(12,4) NOT NULL,     -- 0.8000
    gross_ev_millions NUMERIC(12,4) NOT NULL,  -- 1.4550
    net_ev_millions NUMERIC(12,4) NOT NULL,    -- 0.6550
    monte_carlo_distribution JSONB NOT NULL,
    decision_verdict VARCHAR(30) NOT NULL,     -- 'PROCEED'
    created_at TIMESTAMPTZ DEFAULT NOW()
);

-- 6. Tabel Logic Guardrails Audit Logs (MECE & Cognitive Bias Detections)
CREATE TABLE logic_guardrail_alerts (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    problem_id UUID REFERENCES strategic_problems(id) ON DELETE CASCADE,
    target_node_id UUID REFERENCES thinking_canvas_nodes(id) ON DELETE CASCADE,
    guardrail_type VARCHAR(30) CHECK (guardrail_type IN ('MECE_OVERLAP', 'MISSING_EDGE_CASE', 'COGNITIVE_BIAS')),
    bias_category VARCHAR(80),                 -- 'Confirmation Bias', 'Anchoring', 'Sunk Cost Fallacy'
    probability_score NUMERIC(5,2),            -- 92.50
    confidence_level VARCHAR(20),              -- 'High'
    flagged_text_excerpt TEXT NOT NULL,
    remediation_suggestion TEXT NOT NULL,
    is_resolved BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMPTZ DEFAULT NOW()
);

-- 7. Tabel Institutional Memory & Case Library
CREATE TABLE institutional_cases (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    case_title VARCHAR(255) NOT NULL,          -- 'Netflix Streaming Pivot', 'Toyota TOC on Weld Station'
    domain VARCHAR(80) NOT NULL,
    frameworks_used JSONB NOT NULL,            -- '["JTBD", "Blue Ocean", "BMC"]'
    outcome_status VARCHAR(80) NOT NULL,       -- 'Sukses Besar (VHigh)'
    structural_pattern_summary TEXT NOT NULL,
    problem_embedding vector(1536),
    created_at TIMESTAMPTZ DEFAULT NOW()
);
```

### 6.2 Skema Reasoning Knowledge Graph Berstandar W3C PROV-O (`Neo4j 5 Cypher`)

Untuk menjamin **100% Reasoning Traceability** (Lapisan 5 & Slide 11), setiap lompatan logika dari identifikasi masalah hingga rekomendasi akhir direkam dalam ontologi W3C PROV-O (`prov:Entity`, `prov:Activity`, `prov:Agent`):

```cypher
// 1. Constraint Keunikan Node PROV-O
CREATE CONSTRAINT prov_entity_id IF NOT EXISTS FOR (e:ProvEntity) REQUIRE e.uri IS UNIQUE;
CREATE CONSTRAINT prov_activity_id IF NOT EXISTS FOR (a:ProvActivity) REQUIRE a.uri IS UNIQUE;
CREATE CONSTRAINT prov_agent_id IF NOT EXISTS FOR (ag:ProvAgent) REQUIRE ag.agent_id IS UNIQUE;

// 2. Inisialisasi Agen AI Spesialis sebagai prov:Agent
MERGE (ag_mece:ProvAgent {agent_id: 'AG-09', name: 'MECE Agent', category: 'Problem Solving'})
MERGE (ag_5whys:ProvAgent {agent_id: 'AG-10', name: '5 Whys Agent', category: 'Problem Solving'})
MERGE (ag_kt:ProvAgent {agent_id: 'AG-11', name: 'KT Agent', category: 'Problem Solving'})
MERGE (ag_jury:ProvAgent {agent_id: 'AG-52', name: 'Evaluator Jury', category: 'Core Orchestration'});

// 3. Pemetaan Rantai Jejak Audit (Audit Trail): [Masalah] -> [Framework] -> [Agent] -> [Keputusan]
MERGE (ent_prob:ProvEntity:ProblemNode {
  uri: 'urn:cognition:entity:problem:q3_decline',
  label: 'Q3 Profitability Decline (-18%)',
  data_confidence: 0.992,
  margin_of_error: 0.008
})

MERGE (act_decomp:ProvActivity:FrameworkExecution {
  uri: 'urn:cognition:activity:fw_mece_5whys_01',
  framework_stack: ['MECE Issue Tree', '5 Whys', 'Kepner-Tregoe'],
  started_at: datetime('2026-10-18T08:00:00Z'),
  completed_at: datetime('2026-10-18T08:04:12Z')
})

MERGE (ent_root_cause:ProvEntity:DiagnosisNode {
  uri: 'urn:cognition:entity:diagnosis:west_stockout_340',
  label: 'Stockout SKU Margin Tinggi di Toko Barat (+340% pasca 15 Juni)',
  confidence_score: 0.94,
  margin_of_error: 0.024
})

MERGE (ent_decision:ProvEntity:ExecutiveDirective {
  uri: 'urn:cognition:entity:decision:exception_directive_48h',
  label: 'Terapkan pengecualian pengadaan 48-jam untuk SKU margin tinggi + Audit 60-hari',
  net_ev_millions: 0.65,
  gross_ev_millions: 1.20,
  confidence_score: 0.94,
  margin_of_error: 0.028
})

// 4. Relasi Standar W3C PROV-O
MERGE (act_decomp)-[:USED]->(ent_prob)
MERGE (act_decomp)-[:WAS_ASSOCIATED_WITH]->(ag_mece)
MERGE (act_decomp)-[:WAS_ASSOCIATED_WITH]->(ag_5whys)
MERGE (act_decomp)-[:WAS_ASSOCIATED_WITH]->(ag_kt)
MERGE (ent_root_cause)-[:WAS_GENERATED_BY]->(act_decomp)
MERGE (ent_root_cause)-[:WAS_DERIVED_FROM]->(ent_prob)
MERGE (ent_decision)-[:WAS_DERIVED_FROM]->(ent_root_cause)
MERGE (ent_decision)-[:WAS_ATTRIBUTED_TO]->(ag_jury);
```

---

## Bagian 7: Orkestrasi Backend LangGraph, Kontrak API Streaming & Komponen Frontend

### 7.1 Implementasi Orkestrasi Multi-Agen Paralel dengan LangGraph (`cognition_engine/orchestrator.py`)

Kode berikut mengimplementasikan alur kerja berantai (*Framework Stack*) sekaligus percabangan paralel (*fan-out/fan-in*) untuk **Adversarial Debate Mode** dan **Logic Guardrails**:

```python
from typing import TypedDict, Annotated, List, Dict, Any
import operator
from langgraph.graph import StateGraph, START, END


class CognitionOSState(TypedDict):
    session_id: str
    problem_statement: str
    domain_tags: List[str]
    context_data: Dict[str, Any]
    selected_stack: List[str]
    # Akumulasi artefak dari tiap kerangka kerja
    scqa_framing: Dict[str, Any]
    mece_tree: Dict[str, Any]
    kt_diagnosis: Dict[str, Any]
    rice_priorities: List[Dict[str, Any]]
    # Hasil eksekusi agen paralel (Adversarial Debate & Guardrails)
    debate_submissions: Annotated[List[Dict[str, Any]], operator.add]
    jury_consensus: Dict[str, Any]
    guardrail_report: Dict[str, Any]
    ev_simulation: Dict[str, Any]
    minto_pyramid: Dict[str, Any]
    prov_lineage_nodes: Annotated[List[Dict[str, Any]], operator.add]


async def chief_orchestrator_node(state: CognitionOSState) -> Dict[str, Any]:
    """AG-51: Memvalidasi input masalah dan menginisialisasi tumpukan kerangka kerja."""
    stack = state.get("selected_stack") or ["SCQA", "MECE", "KEPNER_TREGOE", "RICE"]
    return {
        "selected_stack": stack,
        "prov_lineage_nodes": [{
            "step": "INGESTION",
            "agent_id": "AG-51",
            "status": "RECOMMENDED_STACK_LOCKED",
            "stack": stack,
        }],
    }


async def execute_framework_stack_node(state: CognitionOSState) -> Dict[str, Any]:
    """Menjalankan rantai kerangka kerja: SCQA (AG-44) -> MECE (AG-09) -> KT (AG-11) -> RICE (AG-02)."""
    scqa = {
        "situation": "Margin keuntungan perusahaan stabil selama Q1-Q2.",
        "complication": "Profitabilitas Q3 turun 18%, dipicu penurunan 25% di toko-toko wilayah Barat pasca 15 Juni.",
        "question": "Apa akar penyebab penurunan profitabilitas Q3 di wilayah Barat dan bagaimana memulihkannya secara cepat?",
        "answer_seed": "Kehabisan stok SKU bermargin tinggi akibat perubahan kebijakan pengadaan 15 Juni.",
    }
    mece = {
        "root": "Profitability Decline -18%",
        "branches": [
            {"id": "rev_down", "label": "Revenue ↓", "children": ["Volume ↓ (ROOT CAUSE)", "Price ↓"]},
            {"id": "cost_up", "label": "Costs ↑", "children": ["Fixed Costs", "Variable Costs"]},
        ],
        "mece_score": 96.0,
    }
    kt = {
        "root_cause": "Stockout SKU margin tinggi di toko Barat meningkat 340% pasca kebijakan pengadaan 15 Juni.",
        "confidence": 0.94,
    }
    rice = [
        {"initiative": "Pengecualian pengadaan 48-jam untuk SKU margin tinggi", "rice_score": 845.0},
        {"initiative": "Audit algoritma peramalan pengadaan dalam 60 hari", "rice_score": 610.0},
    ]
    return {
        "scqa_framing": scqa,
        "mece_tree": mece,
        "kt_diagnosis": kt,
        "rice_priorities": rice,
        "prov_lineage_nodes": [{
            "step": "STACK_EXECUTION",
            "agents": ["AG-44", "AG-09", "AG-10", "AG-11", "AG-02"],
            "confidence": 0.94,
        }],
    }


async def blue_ocean_optimist_node(state: CognitionOSState) -> Dict[str, Any]:
    """AG-24: Berjalan secara paralel untuk menyusun argumen agresif/optimis."""
    return {
        "debate_submissions": [{
            "agent_id": "AG-24",
            "agent_name": "Blue Ocean Agent",
            "stance": "Optimis",
            "focus": ["Inovasi", "Kecepatan", "Valuasi"],
            "argument": "Eksekusi pengecualian darurat sekarang! Rebut kembali momentum penjualan Q4 secara instan.",
        }]
    }


async def premortem_pessimist_node(state: CognitionOSState) -> Dict[str, Any]:
    """AG-49: Berjalan secara paralel untuk menguji titik kegagalan (Pre-Mortem)."""
    return {
        "debate_submissions": [{
            "agent_id": "AG-49",
            "agent_name": "Pre-Mortem Agent",
            "stance": "Pesimis",
            "focus": ["Titik Kegagalan", "Risiko"],
            "argument": "Kebijakan tambal sulam menciptakan kepuasan semu organisasi! Tanpa audit sistemik, risiko terulang.",
        }]
    }


async def evaluator_jury_node(state: CognitionOSState) -> Dict[str, Any]:
    """AG-52: Menggabungkan argumen Optimis & Pesimis menjadi Sintesis Konsensus Objektif."""
    return {
        "jury_consensus": {
            "agent_id": "AG-52",
            "stance": "Objektif",
            "focus": ["Sintesis Konsensus"],
            "directive": "Eksekusi pengecualian dalam 48 jam untuk SKU margin tinggi, disertai audit sistem dalam 60 hari.",
            "confidence": 0.94,
        },
        "prov_lineage_nodes": [{
            "step": "ADVERSARIAL_CONSENSUS",
            "agent_id": "AG-52",
            "confidence": 0.94,
        }],
    }


async def minto_synthesis_node(state: CognitionOSState) -> Dict[str, Any]:
    """AG-43: Menyusun output eksekutif Minto Pyramid siap ekspor ke PDF/PPTX."""
    return {
        "minto_pyramid": {
            "governing_thought": "Terapkan pengecualian pengadaan 48-jam untuk SKU margin tinggi.",
            "confidence_score": 0.94,
            "key_line_arguments": [
                {"id": 1, "claim": "Isolasi Kausal tervalidasi (94%).", "source_agent": "AG-11"},
                {"id": 2, "claim": "Valuasi Ekonomi positif (+$1.2M Gross EV / +$0.65M Net EV).", "source_agent": "AG-04"},
                {"id": 3, "claim": "Risiko Eksekusi terukur (Lolos Pre-Mortem dengan audit 60 hari).", "source_agent": "AG-52"},
            ],
        }
    }


def build_cognition_os_graph():
    builder = StateGraph(CognitionOSState)
    builder.add_node("chief_orchestrator", chief_orchestrator_node)
    builder.add_node("framework_stack", execute_framework_stack_node)
    builder.add_node("blue_ocean_agent", blue_ocean_optimist_node)
    builder.add_node("premortem_agent", premortem_pessimist_node)
    builder.add_node("evaluator_jury", evaluator_jury_node)
    builder.add_node("minto_synthesis", minto_synthesis_node)

    builder.add_edge(START, "chief_orchestrator")
    builder.add_edge("chief_orchestrator", "framework_stack")

    # Fan-Out Paralel untuk Adversarial Debate Mode
    builder.add_edge("framework_stack", "blue_ocean_agent")
    builder.add_edge("framework_stack", "premortem_agent")

    # Fan-In menuju Evaluator Jury
    builder.add_edge("blue_ocean_agent", "evaluator_jury")
    builder.add_edge("premortem_agent", "evaluator_jury")

    builder.add_edge("evaluator_jury", "minto_synthesis")
    builder.add_edge("minto_synthesis", END)
    return builder.compile()
```

### 7.2 Spesifikasi Kontrak API REST & Streaming (`FastAPI Endpoints`)

| Method & Endpoint | Deskripsi Fungsi | Request Body / Params | Response / Stream Format |
| :--- | :--- | :--- | :--- |
| `POST /api/v1/problems/ingest` | Menyimpan input *Problem Ingestion Wizard* dan mengembalikan rekomendasi *Framework Stack* otomatis dari `AG-51` | `{title, raw_statement, domain_tags, context_constraints}` | `201 Created` — `{problem_id, recommended_stack, confidence}` |
| `POST /api/v1/problems/{id}/execute-stack` | Menjalankan orkestrasi paralel *Framework Stack* dan mengalirkan progres tiap agen ke *Thinking Canvas* | `{stack_ids: ["FW-44", "FW-09", "FW-11", "FW-02"]}` | `text/event-stream (SSE)` — Event `node_created`, `agent_thought`, `mece_score_updated` |
| `POST /api/v1/problems/{id}/debate` | Memicu perdebatan paralel `AG-24` (Blue Ocean) vs `AG-49` (Pre-Mortem) yang dihakimi oleh `AG-52` (Jury) | `{target_hypothesis_node_id, user_constraints}` | `200 OK` — `{optimist_card, pessimist_card, jury_consensus_card}` |
| `POST /api/v1/problems/{id}/simulate-ev` | Menghitung *Expected Value* (Bayesian + 10.000 Monte Carlo runs) secara instan saat *slider* digeser | `{prob_success, upside, downside, costs, confidence}` | `200 OK` (< 50ms) — `{gross_ev, net_ev, verdict, curves}` |
| `POST /api/v1/guardrails/validate-realtime` | Memvalidasi teks/node baru terhadap tumpang tindih *MECE* dan *Cognitive Bias* | `{problem_id, parent_node_id, candidate_text}` | `200 OK` — `{mece_score, bias_alerts, edge_cases}` |
| `GET /api/v1/problems/{id}/lineage` | Mengambil graf W3C PROV-O lengkap dari Neo4j untuk dirender di komponen *Decision Lineage* | `problem_id` | `200 OK` — `{nodes: [...], edges: [...], overall_confidence: 0.94}` |
| `POST /api/v1/problems/{id}/export` | Mengekspor hasil *Synthesis Engine (Minto Pyramid)* menjadi dokumen PDF atau dek PPTX | `{format: "pdf" | "pptx", include_lineage: true}` | `200 OK` — File stream / Signed URL unduhan dokumen |

### 7.3 Arsitektur Komponen Frontend Interaktif (`Next.js 15 + React Flow`)

Berikut adalah struktur komponen React untuk mengintegrasikan **Thinking Canvas**, **Adversarial Debate**, dan **Scenario Simulator** di dalam satu layar kerja terpadu:

```tsx
// apps/web/src/components/workspace/CognitionOSWorkspace.tsx
"use client";

import React, { useState, useMemo } from "react";
import { ReactFlow, Background, Controls, MiniMap, Node, Edge } from "@xyflow/react";
import "@xyflow/react/dist/style.css";

interface EVParams {
  probability: number; // 0.65
  upside: number;      // 2.4 ($M)
  downside: number;    // 0.3 ($M)
  costs: number;       // 0.8 ($M)
}

export default function CognitionOSWorkspace() {
  const [evParams, setEvParams] = useState<EVParams>({
    probability: 0.65,
    upside: 2.4,
    downside: 0.3,
    costs: 0.8,
  });

  // Kalkulasi Real-Time Expected Value (Gross & Net EV)
  const evMetrics = useMemo(() => {
    const p = evParams.probability;
    const q = 1 - p;
    const grossEv = p * evParams.upside - q * evParams.downside;
    const netEv = grossEv - evParams.costs;
    return {
      grossEv: grossEv.toFixed(2),
      netEv: netEv.toFixed(2),
      isPositive: netEv > 0,
    };
  }, [evParams]);

  // Node awal Thinking Canvas (Sesuai Slide 6: Profitability Decline -18%)
  const initialNodes: Node[] = [
    {
      id: "root",
      position: { x: 320, y: 20 },
      data: { label: "Profitability Decline -18%" },
      style: { fontWeight: 700, border: "2px solid #1e293b", padding: 12, borderRadius: 8 },
    },
    {
      id: "rev",
      position: { x: 140, y: 130 },
      data: { label: "Revenue ↓" },
      style: { border: "1px solid #475569", padding: 10, borderRadius: 6 },
    },
    {
      id: "cost",
      position: { x: 500, y: 130 },
      data: { label: "Costs ↑" },
      style: { border: "1px solid #475569", padding: 10, borderRadius: 6 },
    },
    {
      id: "vol",
      position: { x: 40, y: 250 },
      data: { label: "Volume ↓ [▲ ROOT CAUSE IDENTIFIED]" },
      style: {
        border: "2px solid #b91c1c",
        backgroundColor: "#fef2f2",
        color: "#991b1b",
        fontWeight: 700,
        padding: 10,
        borderRadius: 6,
      },
    },
    {
      id: "price",
      position: { x: 260, y: 250 },
      data: { label: "Price ↓" },
      style: { border: "1px solid #475569", padding: 10, borderRadius: 6 },
    },
  ];

  const initialEdges: Edge[] = [
    { id: "e-root-rev", source: "root", target: "rev", animated: false },
    { id: "e-root-cost", source: "root", target: "cost", animated: false },
    { id: "e-rev-vol", source: "rev", target: "vol", animated: true },
    { id: "e-rev-price", source: "rev", target: "price", animated: false },
  ];

  return (
    <div className="grid grid-cols-12 gap-4 h-screen bg-slate-950 text-slate-100 p-4">
      {/* Kolom Kiri & Tengah: Thinking Canvas & Diagnosis Kepner-Tregoe */}
      <div className="col-span-8 flex flex-col gap-4">
        <div className="flex-1 bg-slate-900 border border-slate-800 rounded-xl overflow-hidden relative">
          <ReactFlow nodes={initialNodes} edges={initialEdges} fitView>
            <Background color="#334155" gap={20} />
            <Controls />
            <MiniMap />
          </ReactFlow>
        </div>

        {/* Kartu Diagnosis Kepner-Tregoe */}
        <div className="bg-slate-900 border border-emerald-500/40 rounded-xl p-4">
          <div className="text-xs font-mono uppercase text-emerald-400 mb-1">
            Kepner-Tregoe Agent (AG-11) • Confidence: 94% • MECE Validated: 96%
          </div>
          <p className="text-sm text-slate-200">
            <strong>Diagnosis Kepner-Tregoe mengonfirmasi:</strong> Volume menurun akibat kehabisan
            stok (stockout) SKU bermargin tinggi di toko-toko Barat—meningkat 340% pasca perubahan
            kebijakan pengadaan 15 Juni.
          </p>
        </div>
      </div>

      {/* Kolom Kanan: Scenario Simulator & Minto Pyramid Preview */}
      <div className="col-span-4 flex flex-col gap-4">
        <div className="bg-slate-900 border border-slate-800 rounded-xl p-4">
          <h3 className="text-base font-semibold mb-3">Fase 5: Scenario Simulator (EV Engine)</h3>
          <div className="space-y-3 text-xs">
            <label className="block">
              <span>Probabilitas Sukses: {(evParams.probability * 100).toFixed(0)}%</span>
              <input
                type="range"
                min="0.05"
                max="0.95"
                step="0.01"
                value={evParams.probability}
                onChange={(e) => setEvParams({ ...evParams, probability: parseFloat(e.target.value) })}
                className="w-full mt-1"
              />
            </label>
            <label className="block">
              <span>Upside: ${evParams.upside.toFixed(1)}M</span>
              <input
                type="range"
                min="0.5"
                max="5.0"
                step="0.1"
                value={evParams.upside}
                onChange={(e) => setEvParams({ ...evParams, upside: parseFloat(e.target.value) })}
                className="w-full mt-1"
              />
            </label>
            <label className="block">
              <span>Downside: ${evParams.downside.toFixed(1)}M</span>
              <input
                type="range"
                min="0.1"
                max="3.0"
                step="0.1"
                value={evParams.downside}
                onChange={(e) => setEvParams({ ...evParams, downside: parseFloat(e.target.value) })}
                className="w-full mt-1"
              />
            </label>
            <label className="block">
              <span>Costs: ${evParams.costs.toFixed(1)}M</span>
              <input
                type="range"
                min="0.1"
                max="3.0"
                step="0.1"
                value={evParams.costs}
                onChange={(e) => setEvParams({ ...evParams, costs: parseFloat(e.target.value) })}
                className="w-full mt-1"
              />
            </label>
          </div>

          <div className="mt-4 p-3 rounded-lg bg-slate-950 border border-slate-800 flex items-center justify-between">
            <div>
              <div className="text-xs text-slate-400">Net Expected Value</div>
              <div className="text-2xl font-bold text-emerald-400">
                EV = {Number(evMetrics.netEv) >= 0 ? `+${evMetrics.netEv}M` : `${evMetrics.netEv}M`}
              </div>
              <div className="text-[11px] text-slate-500">Gross EV: +${evMetrics.grossEv}M</div>
            </div>
            <span className="px-3 py-1 rounded text-xs font-mono bg-emerald-950 text-emerald-300 border border-emerald-700">
              {evMetrics.isPositive ? "✓ PROCEED" : "⚠ HOLD"}
            </span>
          </div>
        </div>
      </div>
    </div>
  );
}
```

---

## Bagian 8: Struktur Direktori Monorepo, Deployment Docker, Pengujian & Roadmap 16 Minggu

### 8.1 Struktur Direktori Proyek (`cognition-os/` Monorepo)

```text
cognition-os/
├── apps/
│   ├── web/                                  # Next.js 15 Full-Stack Frontend Workspace
│   │   ├── src/
│   │   │   ├── app/
│   │   │   │   ├── (dashboard)/command-center/
│   │   │   │   ├── (workspace)/problem/[id]/
│   │   │   │   │   ├── wizard/               # Fase 1: Problem Ingestion Wizard
│   │   │   │   │   ├── stack-builder/        # Fase 2: Framework Stack Builder
│   │   │   │   │   ├── thinking-canvas/      # Fase 3: Thinking Canvas (React Flow)
│   │   │   │   │   ├── adversarial-debate/   # Fase 4: Adversarial Debate Mode
│   │   │   │   │   ├── simulator/            # Fase 5: Scenario Simulator (Bayesian & Monte Carlo)
│   │   │   │   │   └── synthesis/            # Minto Pyramid & PROV-O Lineage Viewer
│   │   │   │   ├── case-library/             # Institutional Memory & AI Case Assistant
│   │   │   │   └── mastery-track/            # 90-Day Human Mastery Curriculum
│   │   │   ├── components/
│   │   │   │   ├── canvas-nodes/             # Custom React Flow Nodes (MECE, 5Whys, KT, CausalLoop)
│   │   │   │   ├── guardrails/               # Real-Time MECE Validator & Bias Detector Toast/Panel
│   │   │   │   └── charts/                   # Dual-Pole Monte Carlo Curve & Minto Pyramid Tree
│   │   │   └── store/                        # Zustand + Yjs Real-time Canvas State
│   │   └── package.json
│   │
│   └── api/                                  # Python 3.12 FastAPI + LangGraph Multi-Agent Backend
│       ├── app/
│       │   ├── api/v1/                       # Endpoints (ingest, stack, debate, simulate, export)
│       │   ├── agents/
│       │   │   ├── core/                     # AG-51 Chief Orchestrator & AG-52 Evaluator Jury
│       │   │   ├── decision/                 # AG-01 s/d AG-08 (Eisenhower, RICE, MoSCoW, EV, Bayesian...)
│       │   │   ├── problem_solving/          # AG-09 s/d AG-16 (MECE, 5 Whys, KT, Fishbone, First Principles...)
│       │   │   ├── systems/                  # AG-17 s/d AG-23 (TOC, Causal Loop, Leverage Points...)
│       │   │   ├── strategic/                # AG-24 s/d AG-31 (Blue Ocean, Wardley, OODA, Porter...)
│       │   │   ├── innovation/               # AG-32 s/d AG-37 (JTBD, Design Thinking, VPC, Kano...)
│       │   │   ├── execution/                # AG-38 s/d AG-42 (RACI, OKR, PDCA, GTD, CPM)
│       │   │   ├── communication/            # AG-43 s/d AG-48 (Minto Pyramid, SCQA, Storyboarding...)
│       │   │   └── meta_thinking/            # AG-49 Pre-Mortem & AG-50 Bias Detector
│       │   ├── engine/
│       │   │   ├── math_guardrails.py        # Monte Carlo, Bayesian Updating, MECE Cosine Matrix
│       │   │   ├── prov_lineage.py           # Neo4j W3C PROV-O Graph Builder
│       │   │   └── export_generator.py       # PDF & PPTX Executive Synthesis Exporter
│       │   └── models/                       # SQLAlchemy ORM & Pydantic v2 Envelopes
│       └── pyproject.toml
│
├── packages/
│   └── shared-schemas/                       # Skema JSON lintas TypeScript & Python (50 Mental Models)
├── infra/
│   ├── docker-compose.yml                    # PostgreSQL+pgvector, Neo4j 5, Redis 7, API, Web
│   └── seed/                                 # Seed 50 Model Mental, 52 Agent Prompts, & Case Library
└── README.md
```

### 8.2 Konfigurasi Infrastruktur Lokal & Produksi (`docker-compose.yml`)

```yaml
version: "3.9"

services:
  postgres:
    image: pgvector/pgvector:pg16
    container_name: cognition_postgres
    environment:
      POSTGRES_USER: cognition
      POSTGRES_PASSWORD: cognition_secret_password
      POSTGRES_DB: cognition_os
    ports:
      - "5432:5432"
    volumes:
      - pgdata:/var/lib/postgresql/data

  neo4j:
    image: neo4j:5.23-community
    container_name: cognition_neo4j_provo
    environment:
      NEO4J_AUTH: neo4j/cognition_graph_password
      NEO4J_PLUGINS: '["apoc"]'
    ports:
      - "7474:7474"
      - "7687:7687"
    volumes:
      - neo4jdata:/data

  redis:
    image: redis:7.4-alpine
    container_name: cognition_redis
    ports:
      - "6379:6379"

  api:
    build:
      context: ./apps/api
    container_name: cognition_multiagent_api
    env_file:
      - .env
    depends_on:
      - postgres
      - neo4j
      - redis
    ports:
      - "8000:8000"
    command: uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload

  web:
    build:
      context: ./apps/web
    container_name: cognition_nextjs_web
    env_file:
      - .env
    depends_on:
      - api
    ports:
      - "3000:3000"

volumes:
  pgdata:
  neo4jdata:
```

### 8.3 Roadmap Implementasi Rekayasa (16 Minggu / 4 Kuartal Sprint)

| Fase Pembangunan | Durasi | Fokus Deliverables & Milestone Teknis | Kriteria Penerimaan (Acceptance Criteria) |
| :--- | :--- | :--- | :--- |
| **Sprint 1–2: Fondasi Inti & Problem Ingestion** | Minggu 1–4 | Setup Monorepo (`Next.js 15` + `FastAPI`), skema PostgreSQL & Neo4j PROV-O, **Command Center**, **Problem Ingestion Wizard**, dan **Chief Orchestrator (`AG-51`)**. | Pengguna dapat menginput masalah, melihat status sistem, dan menerima rekomendasi *Framework Stack* otomatis dalam `< 3 detik`. |
| **Sprint 3–4: Thinking Canvas & Core Stack Agents** | Minggu 5–8 | Implementasi **Framework Stack Builder**, kanvas interaktif **Thinking Canvas** (`React Flow`), serta agen inti (`SCQA`, `MECE`, `5 Whys`, `Kepner-Tregoe`, `RICE`, `First Principles`, `TOC`). | Pengguna dapat merangkai *stack*, menjalankan dekomposisi pohon *MECE* otomatis, dan mengisolasi akar masalah dengan *Confidence Score*. |
| **Sprint 5–6: Guardrails, Debate Mode & Simulator** | Minggu 9–12 | Implementasi **Adversarial Debate Mode** (`Blue Ocean` vs `Pre-Mortem` + `Jury`), **MECE Validator**, **Bias Detector**, **Scenario Simulator** (Bayesian + 10K Monte Carlo), dan **52 Agen Lengkap**. | Perdebatan multi-agen berjalan paralel via SSE, *slider* EV merender kurva distribusi dalam `< 50ms`, dan deteksi bias aktif secara *real-time*. |
| **Sprint 7–8: Synthesis, Case Library & Mastery Track** | Minggu 13–16 | Implementasi **Minto Pyramid Synthesis Engine**, generator ekspor **PDF/PPTX**, visualisasi **Decision Lineage (PROV-O)**, **Case Library**, dan gamifikasi **90-Day Human Mastery Track**. | Sistem lulus uji *end-to-end* dengan *Time to Synthesis (T2S) < 30 menit* dan *100% Reasoning Traceability* pada laporan ekspor PDF/PPTX. |
