# Approval integrity and offline native-evaluation audit

New nonpilot host collection requires approval tied to the exact reviewed JSON content. Existing historical certificates and ZIPs are retained unchanged; unbound approval no longer authorizes a new live collection.

## Review fingerprints

```powershell
uv run --locked --extra dev python scripts/audit_context_host.py fingerprints --fixtures tests/native-evals/context-validity-v2
```

This prints hash_scheme, cases_sha256 and labels_sha256. It does not grant approval or modify any files. For a new suite, show the cases, provisional labels and these fingerprints to the human reviewer. After explicit approval, record approved=true, the reviewer statement/time and those exact fingerprint fields in human-review.json. Never refresh an old certificate automatically after changing inputs; obtain review of the changed content first.

The scheme is canonical-json-sha256-v1: finite JSON serialized with sorted object keys, compact separators and ASCII escapes. Formatting, key order and platform line endings do not change approval. Values, types, array order and metadata changes do. Duplicate JSON keys and nonfinite numbers are rejected. Hashes bind content; they do not authenticate the human reviewer or prevent someone with write access from falsifying a certificate.

A missing or mismatched binding blocks --run before creating output or calling the host. --pilot still uses its separate development case; preparing without --run remains possible and reports human_reviewed=false for historical unbound certificates. Consumed suites are diagnostic material, never fresh held-out evidence.

## Offline replay

From the repository root:

```powershell
uv run --locked --extra dev python scripts/audit_context_host.py audit --summary docs/evidence/context-validity-native-v2-2026-10-24.json --cohort heldout-batched-v2-corrected-20261024 --output tmp/offline-v2.json
```

Expected: exit0, status VERIFIED and summary_matches_recorded=true. The output file must not already exist. No model, network, provider credentials or external command is used. The tool reads the checksum from the trusted published summary outside the ZIP and locates its adjacent archive. Preserve that trusted summary/revision; changing both an archive and its trusted checksum is outside integrity verification.

The auditor bounds compressed/expanded sizes and entry count, rejects unsafe/duplicate paths and links, checks CRC and all frozen input hashes, and verifies the archived suite and source snapshot. It never extracts or executes archived Python. The local validity checker must match the frozen source (platform newlines normalized). Recorded run files, inputs, response files and raw events must agree. Each arm must contain exactly one run for every case, with complete execution, valid latency/token records and fixture-bound read/helper evidence. The replayed structured rubric must match both the original archived summary and the published summary.

The result records auditor/dependency source fingerprints for repeatability. It checks structured decisions and observed traces; it does not semantically judge explanations, prove general sandbox safety or remove the original dataset limitations.

## Historical compatibility

The complete v2 archive is supported and replays with its original product screening result. Its certificate is reported as LEGACY_UNBOUND and new_collection_approved=false. VERIFIED describes archive integrity and reproducibility, not retroactive approval under the new policy or permission to claim a pristine held-out set. The three partially exposed cases remain qualified exactly as in the original report.

Incomplete bundles lacking required frozen suite/runtime files are rejected rather than marked verified. Earlier bundles with a different layout or missing source snapshots may therefore require an explicit compatible audit adapter; this tool does not silently weaken verification to accept them.

## Verification

Regression tests cover changed cases/labels, type-sensitive canonical hashes, duplicate/nonfinite JSON, actual host-launch blocking, unchanged historical certificates, full v2 replay without subprocesses, external checksum mismatch, changed frozen inputs, missing/incomplete events, duplicated runs, response mismatch, unsafe paths and archive expansion limits. Existing historical result files are not rewritten by the audit.
