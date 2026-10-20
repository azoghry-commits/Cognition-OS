# Cognition OS native plugin

Version 0.1.0 implements the 3.1 design direction as shared native skills for Claude and Codex. It preserves 50 mental models and 52 logical specialists with progressive disclosure, optional deterministic calculations, evidence/provenance checks, project cases and a 90-day learning track. No standalone application, model API, server or database is required.

Start with [Claude installation](docs/INSTALLATION_CLAUDE.md) or [Codex installation](docs/INSTALLATION_CODEX.md), then run setup in the native host. Read [user guide](docs/USER_GUIDE.md), [observed validation](docs/TEST_REPORT.md), [platform limits](docs/PLATFORM_COMPATIBILITY.md) and [current status](docs/PROJECT_STATUS.md). The package remains a candidate while native behavioral and comparative evaluation gates are open.

Development (Python 3.10+):
```
python scripts/build_catalog.py
python scripts/build_plugin.py
python scripts/build_docs.py
python -m unittest discover -s tests -v
python scripts/validate_package.py
python scripts/benchmark.py
python scripts/package_release.py
```
Generate in this order. build_catalog preserves original source table identities; build_plugin derives wrappers/contracts; build_docs regenerates maintained guides. Test reports and project status are evidence records written separately. Package generation never publishes or edits personal host configuration.

Source documents remain in the repository but are excluded from installable runtime archives. Their ownership/license terms are not specified; no public license grant is implied. See [release gates](docs/RELEASE_CHECKLIST.md).
