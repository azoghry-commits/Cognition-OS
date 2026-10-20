"""Record the V4.1 source transformation against stable source identities."""
import hashlib
import json
import re
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]

FEATURES=[
    ('Command Center / telemetry','A 3.1; B 1,3','Host task context and observed status; illustrative health/density values are excluded','advisory resource'),
    ('Problem Ingestion','A 3.2 phase 1; B 4','Observable task-context envelope; ask only blocking questions','skill + schema'),
    ('Framework Stack Builder / presets','A 3.2 phase 2; B 5','Small complementary selection with explicit semantic handoffs','routing + skill'),
    ('Thinking Canvas / drill-down / 5 Whys','A 3.2 phase 3; B 6','Optional inspectable Markdown/Mermaid/JSON artifacts within host work','artifact resource'),
    ('Adversarial Debate / rebuttals / jury','A 3.2 phase 4; B 7','Conditional bounded advocate/challenger/jury analysis; no forced consensus','deep advisory'),
    ('Scenario Simulator / sliders / distributions','A 3.2 phase 5; B 8','Supplied numerical parameters, local calculation, explicit distributions and seed','deterministic tool'),
    ('MECE / edge cases / contradiction review','A 3.3.1,5.1,5.2; B 9','Exact finite-universe sets when possible, otherwise qualified semantic review','validation + advisory'),
    ('Cognitive Bias Detector','A 3.3.1,4.1 AG-50; B 9','Evidence-span review without fabricated probability','advisory'),
    ('Executive Synthesis / Minto / storyboard','A 3.3.2,4.1 AG-43..45; B 13','Optional synthesis appropriate to original requested format','skill'),
    ('Export PDF/PPTX','A 2.2,7.2; B 13','Use existing authorized host artifact tools only when requested; no export service','optional retained feature'),
    ('Institutional Memory / case assistant','A 3.3.3,6.1; B 12','Explicitly authorized project cases, provenance and review before reuse','optional local knowledge'),
    ('Human Mastery Track / badges','A 3.3.4; B 14','Separate opt-in human learning; no assumed progress or model training','optional skill'),
    ('Agent orchestration / 52 roles','A 4.1,4.2,7.1; B 10,15','52 logical roles; host owns execution, no mandatory parallel processes','logical registry'),
    ('Inter-agent envelope','A 4.3','Versioned V4.1 request/result with explicit conversion from preserved 3.1 artifacts','schema'),
    ('EV and Monte Carlo','A 5.1,5.2; B 8,13','Retain formula; require input/model assumptions; no automatic PROCEED','calculation'),
    ('Bayesian updates / log odds','A 5.1,5.2','Use conditional likelihoods and justified independence; reject impossible evidence','calculation'),
    ('MECE score formula','A 5.1,5.2','Similarity cannot prove exclusivity/completeness; no invented integrity constants','qualified adaptation'),
    ('SQL users/problems/canvas/debates/simulations/alerts/cases','A 6.1','Host context, typed artifacts and opt-in local cases; no server database','schema + optional local files'),
    ('Reasoning Knowledge Graph / decision lineage','A 6.2; B 11','Observable artifact/evidence DAG; no hidden reasoning access','provenance validation'),
    ('LangGraph fan-out/fan-in / hardcoded sample','A 7.1','Host-native logical workflow; sample outputs are illustrative, never findings','skill + bounded plan'),
    ('REST routes / SSE / agent_thought / WebSocket','A 7.2','Native supported boundaries only; no mandatory server or reasoning interception','excluded infrastructure, retained capabilities'),
    ('React Flow / real-time UI','A 7.3','Host-owned output and optional diagrams; no standalone application','artifact resource'),
    ('Monorepo / Docker / deployment defaults','A 8.1,8.2','Single native plugin repository; no copied example passwords or infrastructure','native packaging'),
    ('Roadmap / KPIs / acceptance','A 1.3,8.3; B 1,3,15','V4.1 phase gates, actual host outcomes and A/B/C/D comparison','evaluation protocol')]

PDF_NOTES=[
    'Radial core illustration; optimal/risk/density labels are illustrative.',
    'Human/model/agent tripartite concept; absolute diagnosis/bias elimination lacks evidence.',
    'Four modules and 50/52/100% telemetry; transform to host-native capabilities.',
    'Four-stage intake and western stores -25%; do not force human wizard.',
    'SCQA→MECE→KT→RICE; handoff compatibility and missing inputs need explicit mapping.',
    'Revenue/cost tree, 340% stockout and 94% certainty are worked examples.',
    'Optimist, jury, challenger; conditional review, no mandatory consensus or real parallelism claim.',
    '65%, 2.4M, 0.3M, 0.8M gives exact net 0.655M; positive EV is not execution authority.',
    '99.2/78/92.5 metrics uncalibrated; example Asia/Europe text mismatches western-store explanation.',
    '52 trained-agent claim unsupported; MoSCoW quadrant conflicts with precise A catalog category.',
    'Lineage labels 5 Whys linked to KT Agent; preserve AG-10 versus AG-11 distinction.',
    'Netflix/Toyota/SpaceX cases and success-pattern assertion require external evidence before reuse.',
    '+1.2M EV and 94% unsupported under supplied inputs; export only when requested.',
    'Three mastery phases and progress badges; progress is illustrative and learning is optional.',
    '50×52 count is conceptual; unlimited decision quality is not a measured outcome.']


def build():
    sources=json.loads((ROOT/'docs/evidence/sources.json').read_text(encoding='utf-8'))
    for name,record in sources.items():
        assert hashlib.sha256((ROOT/name).read_bytes()).hexdigest()==record['sha256']
    text=(ROOT/'Cognition Os Master Blueprint.md').read_text(encoding='utf-8')
    headings=[{'line':i,'heading':line} for i,line in enumerate(text.splitlines(),1) if re.match(r'^#{2,4} ',line)]
    catalog=json.loads((ROOT/'cognitive-core/frameworks/registry.json').read_text(encoding='utf-8'))['frameworks']
    models=[]
    for entry in catalog:
        model=json.loads((ROOT/'cognitive-core/frameworks'/entry['path']).read_text(encoding='utf-8'))
        models.append({'framework_id':entry['id'],'agent_id':entry['agent_id'],'name':entry['name'],
            'source':model['source'],'source_contract':model['source_original'],
            'target':'Lazy-loaded canonical methodology, typed artifact and logical role selected by the host',
            'adaptation':'Framework steps, FW numbering and executable schemas are engineering adaptations',
            'behavioral_status':'NOT_RUN_ON_HOST'})
    record={'specification_version':'4.1','review_date':'2026-10-20','classification':'SOURCE_DERIVED + ENGINEERING_ADAPTATION',
            'sources':sources,'blueprint_lines_read':len(text.splitlines()),'blueprint_headings':headings,
            'pdf_pages_visually_reviewed':[{'page':i,'finding':note} for i,note in enumerate(PDF_NOTES,1)],
            'pdf_render':'pdftoppm -scale-to 1400 -png; tmp/pdfs/v4-1/page-01..15.png',
            'frameworks':models,'features':[{'name':n,'locator':loc,'transformation':t,'delivery':d} for n,loc,t,d in FEATURES],
            'limitations':['Source methodology is not empirical calibration.','Source gaps/corrections C01-C14 remain applicable; PDF page 11 adds role-label mismatch.','Native invocation and A/B/C/D performance are separate gates.']}
    (ROOT/'docs/evidence/v4-1-source-audit.json').write_text(json.dumps(record,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
    rows='\n'.join(f'| {n} | {loc} | {t} | {d} |' for n,loc,t,d in FEATURES)
    model_rows='\n'.join(f"| {m['framework_id']} / {m['agent_id']} | {m['name']} | A line {m['source']['line']} | Canonical skill resource + logical specialization |" for m in models)
    pages='\n'.join(f'| {i} | {note} |' for i,note in enumerate(PDF_NOTES,1))
    (ROOT/'docs/SOURCE_TRANSFORMATION_V4_1.md').write_text('''# Audit sumber dan transformasi V4.1

Audit 2026-10-20: Markdown lengkap (1.362 baris / delapan bagian) dibaca dan seluruh 15 halaman PDF diinspeksi dari render baru 1.400 px. Hash kedua sumber cocok dengan manifest sumber awal. Detail locator, input/output sumber per model dan klasifikasi ada di [evidence JSON](evidence/v4-1-source-audit.json).

Requirement baru berasal dari [prompt V4.1](evidence/master-implementation-prompt-v4.1.txt). Penamaan model, kategori, AG-01..52 dan lingkup sumber dipertahankan. Prosedur implementasi, FW numbering, schema, governor dan hook adalah adaptasi rekayasa, bukan kutipan spesifikasi produksi yang telah tervalidasi. Tidak ada peningkatan kualitas host yang disimpulkan dari audit ini.

## Source-to-agent transformation matrix

| Kapabilitas sumber | Locator | Transformasi V4.1 | Bentuk |
|---|---|---|---|
'''+rows+'''

## Seluruh 50 model

| Framework / logical role | Nama sumber | Locator | Peran target |
|---|---|---|---|
'''+model_rows+'''

AG-51 mengoordinasikan analisis terpilih; host tetap pemilik tugas. AG-52 menguji dukungan rekomendasi dan boleh menolak atau menyatakan bukti tidak cukup. Input/output dan tanggung jawab AG-51/52 berasal dari A 4.2, bukan dua proses model wajib.

## Inspeksi visual seluruh PDF

| Halaman B | Temuan / tindakan |
|---|---|
'''+pages+'''

## Gap, konflik dan keamanan

Register C01–C14 pada [audit baseline](SOURCE_ANALYSIS.md) tetap berlaku. Tambahan C15: pada B halaman 11, framework berlabel 5 Whys ditautkan ke KT Agent; sumber A memisahkan AG-10 dan AG-11. Rekonstruksi lineage harus memakai role ID yang benar. A 4.3 menyediakan dua contoh prompt rinci, sementara 50 tabelnya masih ringkas; kelengkapan metode/schema adalah adaptasi yang perlu evaluasi perilaku.

Formula EV, Bayes/log-odds, RICE, Monte Carlo dan heuristik MECE pada A 3.2/5 diaudit terhadap helper serta register koreksi. EV contoh: gross 1.455M dan net 0.655M. Rentang biaya triangular 1.20/1.25C, Beta clamping, uncalibrated confidence, VaR sign dan MECE similarity tidak dipromosikan menjadi bukti kebenaran. Helper numerik diuji terpisah.

Dependensi SCQA→MECE→KT/5 Whys→RICE adalah contoh sumber, bukan pipeline universal. Arsitektur SaaS, SQL, Cypher, endpoint REST/SSE, UI dan Docker tidak dipakai sebagai infrastruktur wajib; kapabilitasnya dipetakan di atas. Tidak ada fitur intelektual dihapus tanpa disposisi. Source passwords, contoh verdict dan label confidence tidak disalin ke konfigurasi runtime. Source/case content tetap data tidak tepercaya; izin dan side effect mengikuti host.
''',encoding='utf-8')
    print(f'Preserved source hashes; audited {len(models)} models, 52 logical roles, {len(FEATURES)} feature groups, 15 PDF pages.')


if __name__=='__main__':build()
