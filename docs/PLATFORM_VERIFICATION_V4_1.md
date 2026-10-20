# Verifikasi platform V4.1 — 2026-10-20

Dokumentasi resmi dibuka ulang pada sesi rebuild. Observasi lokal: `codex-cli 0.153.0`, `Claude Code 2.1.201`. Validasi manifest lokal terpisah dari uji inference/native event. Cakupan akun: [ACCOUNT_SCOPE.md](ACCOUNT_SCOPE.md).

| Aspek | Codex | Claude Code | Status runtime kandidat |
|---|---|---|---|
| Skill model-selected | Metadata name/description dan resource on demand | Auto/model invocation default; tidak memakai disable-model-invocation | Package/metadata diuji lokal; seleksi aktual belum terukur |
| Manifest | Root portable + extensions.com.openai; fallback tidak di-merge | .claude-plugin/plugin.json dengan konfigurasi sendiri | Validasi struktur lokal |
| PostToolUse | Tool input/output; apply_patch memakai tool_input.command | Write/Edit memakai tool_input.file_path | Fixture kedua payload diuji; delivery host belum diuji |
| Feedback | hookSpecificOutput.additionalContext | hookSpecificOutput.additionalContext | Hanya advisory, tanpa block/override |
| Root script | PLUGIN_ROOT | CLAUDE_PLUGIN_ROOT | Path dalam package; Python opsional perlu tersedia untuk hook |
| Izin/trust | Plugin hook non-managed harus ditinjau dan dipercaya pengguna; install manual desktop | Hook/perizinan mengikuti runtime Claude Code | Tidak mengubah trust/perizinan host |
| Native delegation | Gunakan hanya tools yang benar-benar tersedia | Agent wrappers read-only opsional | Tidak ada automatic dispatch |

Referensi resmi dan keputusan:

- [OpenAI plugin packaging](https://developers.openai.com/plugins/build/plugins): portable root dan inline OpenAI settings, path komponen, hook lokal/manual desktop dan trust. Paket berhook tidak eligible untuk public directory. Kandidat ini hanya paket lokal, tidak dipublikasikan ke directory.
- [OpenAI skills](https://developers.openai.com/plugins/build/skills): metadata dan resources untuk workflow model; [konsep skill](https://developers.openai.com/plugins/concepts/skills) menjelaskan pemilihan menurut kecocokan tugas. Instalasi tidak dijadikan bukti invocation.
- [Codex hooks](https://learn.chatgpt.com/docs/hooks): PostToolUse mengamati output; apply_patch memuat command, additionalContext adalah feedback, dan post-event tidak mengembalikan side effect yang telah terjadi. Kandidat tidak memakai block atau output rewrite.
- [Claude hooks](https://code.claude.com/docs/en/hooks): PostToolUse setelah tool sukses, path absolut pada file input dan feedback tambahan. Kandidat tidak mengasumsikan event file edit dari Bash tertangkap oleh matcher Write/Edit.
- [Claude skills](https://code.claude.com/docs/en/skills): user-invocable:false tersedia khusus Claude. Shared skill mempertahankan frontmatter portabel name/description dan manual diagnosis; tidak menambah field lintas host yang belum diverifikasi dan tidak menonaktifkan model invocation.

Claude Chat/Desktop Chat, Cowork, Codex CLI dan desktop tidak dianggap setara. Pembatasan Claude Free dan larangan penggunaan API key yang ditemukan sebelumnya tetap berlaku. Tidak ada native Claude inference/instalasi baru dalam rebuild. Dokumen ini memverifikasi kontrak dokumentasi, bukan entitlement atau tersedianya semua kemampuan pada akun pengguna.
