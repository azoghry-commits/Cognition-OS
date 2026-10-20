# Codex installation and lifecycle

## Kandidat rebuild V4.1 / paket 0.2.0

Build lokal: `python scripts/rebuild_plugin.py --package`. Paket runtime ada di `dist/cognition-os-0.2.0.zip`; marketplace lokal di `dist/cognition-os-marketplace-0.2.0.zip`; checksum ada di `dist/SHA256SUMS.json`. Verifikasi checksum/inventory sebelum memakai package. Build tidak mengubah source/cache personal maupun installed/enabled state.

Untuk update, simpan ZIP dan konfigurasi marketplace versi sebelumnya, pertahankan kasus pengguna di luar cache, lalu arahkan source marketplace yang telah ditinjau ke runtime kandidat dan refresh/install melalui UI atau perintah native yang tersedia. Verifikasi versi 0.2.0 dari installed manifest; discovery saja belum merupakan instalasi. Host mungkin memerlukan restart/chat baru untuk memuat skill terbaru.

Root manifest memilih `hooks/codex/hooks.json`. Hook hanya tersedia sesuai surface/instalasi yang didukung dan memerlukan review/trust pengguna pada host; build/enable plugin tidak memberi trust itu. Pastikan Python tersedia. Tanpa hook, skills dan helper yang didukung tetap dapat digunakan. Jalankan diagnosis setup, kemudian task natural dan negative control; simpan bukti skill/resource yang benar-benar dipilih, tool result, feedback event serta deliverable.

Rollback: pilih source/ZIP 0.1.0 yang dipertahankan, reinstall melalui mekanisme native, dan periksa installed version serta kompatibilitas artifact. Framework envelope 3.1 masih tersedia; request/result advisory 4.1 adalah kontrak baru. Jangan menghapus atau mengonversi `.cognition/cases` otomatis. Sesi rebuild telah memperbarui instalasi Codex-only ke 0.2.0; native CLI melaporkan installed/enabled, hash inventory dan helper terpasang diverifikasi. Backup ada di `dist/cognition-os-rollback-0.1.0.zip`; restore belum diuji. [Bukti instalasi](evidence/v4-1-codex-installation.json) dan [status acceptance](REBUILD_STATUS_V4_1.md).

## Riwayat instalasi baseline dan mekanisme lokal

For this user's account, use the existing ChatGPT login and ChatGPT Plus/Codex allowance. `codex login status` was verified to report ChatGPT authentication. No API key or Claude subscription is required by this package. Do not switch to API billing or buy credits. See ACCOUNT_SCOPE.md for the current authorization and deferred Claude tests.

Portable root plugin.json is canonical. Root extensions.com.openai replaces the optional .codex-plugin/plugin.json OpenAI settings wholesale; it does not merge. Both discover the same skills and canonical resources. No MCP/hook is required. No API credentials are needed. Python 3.10+ is optional when native validated calculation is unavailable.

The repo includes .agents/plugins/marketplace.json pointing to ./local-marketplace/plugins/cognition-os relative to the marketplace root. First run the packaging script, then scripts/prepare_local_marketplace.py once to stage the allowlisted runtime. Registering this repository then installs that clean snapshot rather than copying source documents, development dependencies and Git internals. Local installs use a cache copy; verify its content/version after changes. Review an existing staging directory before replacing it.

Observed on this account: cognition-os@cognition-os-local version 0.1.0 is installed and enabled. Open a fresh Codex desktop chat, select the Cognition OS setup skill and check activation. The earlier native CLI smoke failed before analysis on its model availability/context-budget settings; installation success does not certify that behavioral gate.

For a packaged marketplace, extract dist/cognition-os-marketplace-0.1.0.zip. It contains plugins/cognition-os and both marketplace catalogs. Add its root with `codex plugin marketplace add <absolute-marketplace-root>`. Current installed CLI 0.153.0 also exposes `codex plugin add cognition-os@cognition-os-local --json`; this command's availability was verified by local help, and must be distinguished from the official desktop installation walkthrough. Do not infer a successful desktop install from CLI help.

In a fresh native chat run the installed setup skill through the skill picker, then request Kepner-Tregoe for a deviation with missing IS NOT evidence. Confirm correct skill activation, referenced core file access, missing-data behavior and helper execution. Use references/examples/ev.json as the calculation smoke; require exact gross/net values within floating tolerance. Record actual tool and response evidence.

Personal marketplace instructions: maintain ~/.agents/plugins/marketplace.json, point its source at a plugin location relative to that marketplace root, restart the desktop host and install from the local source. This project does not modify personal files automatically. Repo settings .codex/config.toml can enable a trusted local-marketplace entry with [plugins."cognition-os@cognition-os-local"] enabled=true, but discovery alone is not installation proof.

Update: regenerate/validate, increment version, install/refresh the reviewed source and confirm cache content. Rollback: retain previous ZIP/version, restore its marketplace entry and reinstall after reviewing data schema compatibility. Removal: native plugin remove or verified CLI `codex plugin remove` usage. Preserve user .cognition/cases data; uninstall never deletes it. Claude agent files are not advertised as Codex-native registered agents.

