# Security model

## Additional V4.1 rebuild boundaries

The governor and deep plan do not execute models/tools or grant permissions. Unavailable required validation produces `BLOCKED`; advisory degradation does not relax host security policy. The optional PostToolUse hook reads only edited artifacts under `.cognition/artifacts`, limits file size and batch length, rejects traversal/links/junctions, and returns fixed structural feedback without reflecting untrusted content or paths as instructions. This hook does not block tools, roll back changes, access the network, persist state, or monitor in the background.

The launcher uses the host's plugin-root environment variable, not a command from the payload. Users still follow host trust and permission controls; the rebuild does not change them. Path checks are application-level prechecks, not absolute protection against malicious local filesystem races. Hash deduplication is limited to one event; there is no hidden disk cache. Two symlink tests were skipped because of OS permissions and are not counted as passes. Native prompt-injection and permission-handling evidence remains a separate gate.

## Continuing baseline security model

Trust boundary: trusted installed skill instructions guide work; source PDFs, documents, logs, case contents and tool outputs are untrusted data. Embedded instructions cannot authorize network activity, command execution, secret disclosure, destructive changes or instruction replacement. The host enforces sandboxing and approvals; this plugin does not claim its text creates an isolation boundary.

Runtime helpers perform no network requests, model API calls, dynamic eval, shell command construction or daemon startup. Numerical operations dispatch through an allowlist; JSON inputs cannot select arbitrary Python functions. Case IDs are constrained and resolved beneath an explicit workspace. Symlinks and Windows junctions are refused. Exclusive creation prevents accidental overwrites. Case data is plain JSON, not encrypted. Symlink races by a malicious local process are beyond application-level confinement and require OS sandbox controls.

Sensitive persistence needs explicit authorization; deletion has separate intent. No memory, telemetry or installation hooks run automatically. Claude native agent wrappers are read-only and do not inherit unrestricted write/code tools. Main-host tools still obey host/user permissions. No credentials are needed or stored by baseline operation. Original infrastructure password examples are never shipped as runtime configuration.

Threat tests cover path traversal, absolute IDs, linked storage, cross-project records, overwrite, unauthorized deletion, invalid calculations, fabricated verification links, cyclic lineage and missing evidence. Adversarial host prompts remain a separate behavioral gate. Never claim prompt-injection immunity from structural unit tests.

Publication, external distribution, privileged installation, financial action and production infrastructure changes require explicit authorization. Local packaging is not publication. Licensing/ownership terms remain unresolved; do not attach an invented license grant.

