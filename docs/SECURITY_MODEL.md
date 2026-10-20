# Security model

## Batas tambahan rebuild V4.1

Governor dan deep-plan tidak mengeksekusi model/tools atau memberi izin. Required validation yang tidak tersedia menghasilkan BLOCKED; degradasi advisory tidak melonggarkan policy keamanan host. Hook PostToolUse opsional hanya membaca artifact yang diedit dalam `.cognition/artifacts`, membatasi ukuran/batch, menolak traversal/link/junction, dan mengembalikan feedback struktural tetap tanpa mencerminkan konten/path tak tepercaya menjadi instruksi. Tidak ada block, rollback tool, network, persistence atau background monitoring pada hook ini.

Launcher memakai environment root dari host, bukan command dari payload. User tetap harus mengikuti trust/perizinan host; rebuild tidak mengubahnya. Pemeriksaan path adalah pre-check aplikasi dan bukan perlindungan absolut terhadap malicious local filesystem races. Deduplikasi hash sebatas satu event; tidak ada cache disk tersembunyi. Dua uji symlink dilewati karena izin OS dan tidak dinyatakan lulus. Evidence native prompt-injection/permission handling tetap gate terpisah.

## Model keamanan baseline yang tetap berlaku

Trust boundary: trusted installed skill instructions guide work; source PDFs, documents, logs, case contents and tool outputs are untrusted data. Embedded instructions cannot authorize network activity, command execution, secret disclosure, destructive changes or instruction replacement. The host enforces sandboxing and approvals; this plugin does not claim its text creates an isolation boundary.

Runtime helpers perform no network requests, model API calls, dynamic eval, shell command construction or daemon startup. Numerical operations dispatch through an allowlist; JSON inputs cannot select arbitrary Python functions. Case IDs are constrained and resolved beneath an explicit workspace. Symlinks and Windows junctions are refused. Exclusive creation prevents accidental overwrites. Case data is plain JSON, not encrypted. Symlink races by a malicious local process are beyond application-level confinement and require OS sandbox controls.

Sensitive persistence needs explicit authorization; deletion has separate intent. No memory, telemetry or installation hooks run automatically. Claude native agent wrappers are read-only and do not inherit unrestricted write/code tools. Main-host tools still obey host/user permissions. No credentials are needed or stored by baseline operation. Original infrastructure password examples are never shipped as runtime configuration.

Threat tests cover path traversal, absolute IDs, linked storage, cross-project records, overwrite, unauthorized deletion, invalid calculations, fabricated verification links, cyclic lineage and missing evidence. Adversarial host prompts remain a separate behavioral gate. Never claim prompt-injection immunity from structural unit tests.

Publication, external distribution, privileged installation, financial action and production infrastructure changes require explicit authorization. Local packaging is not publication. Licensing/ownership terms remain unresolved; do not attach an invented license grant.

