# Development and release workflow

## Where work is recorded

| Record | Purpose |
| --- | --- |
| GitHub Issues | Scoped work, acceptance criteria, links to evidence |
| Feature branch + pull request | Implementation, review and CI results |
| `docs/MEASURED_SCAFFOLDING_ANALYSIS.md` | Feasibility, risks and executable next steps |
| `docs/ARCHITECTURE_DECISIONS.md` | Durable architecture decisions |
| `docs/DEVELOPMENT_LOG.md` | Dated execution notes and unresolved work |
| `CHANGELOG.md` | User-visible changes by package version |
| Git tag + GitHub Release | Immutable source reference, release notes, ZIPs and checksums |

## Branches

Keep `main` as the reviewed integration branch. Use short-lived `feat/<topic>`, `fix/<topic>` and `docs/<topic>` branches, then open a PR into main. A permanent develop branch adds little value for this project today. Preserve unrelated local changes and stage only the intended files. Enable required CI and PR review through repository settings when the owner selects those rules.

## Versions

Package version and conceptual specification version are separate. `4.1` is the conceptual specification; `0.5.0` is the current package. Use MAJOR.MINOR.PATCH: incompatible contract change, backward-compatible feature, compatible fix. During 0.x, document breaking changes explicitly and use a minor bump for them. Development changes live under Unreleased until a release is cut. The next feature target is 0.6.0; it is not released merely because a plan exists.

Canonical generator version is `scripts/build_catalog.py:VERSION`; synchronize generated manifests with `python scripts/rebuild_plugin.py --package`. Review the resulting diff because generators can rewrite files. Never overwrite a published tag. New correction means a new version.

## Release procedure

1. Merge reviewed work; resolve version consistency, licensing and the release checklist. Record outstanding native behavioral gates explicitly.
2. Run the locked quality gate documented in `docs/TEST_PLAN.md` from a clean checkout of the selected commit, including Ruff, the 70% runtime coverage floor, tests, and package validation.
3. Run `uv run --locked --extra dev python scripts/package_release.py`; retain all versioned ZIPs and `dist/SHA256SUMS.json`.
4. Create an annotated `v<package-version>` tag at that exact reviewed commit. Push the tag, then create a GitHub Release with substantive notes and those verified artifacts. Mark engineering candidates as prerelease; this does not certify production readiness.
5. Check the release target SHA, uploaded filenames/checksums and installation smoke. Retain the previous release for rollback.

Historical changelog entries do not prove that GitHub Releases existed. Do not retrospectively tag undocumented or untested historical builds as verified releases.

Repository About description: Portable cognitive assistance for agent hosts: 50 mental models, adaptive scaffolding, evidence checks and governed improvement.

References: [GitHub releases](https://docs.github.com/en/repositories/releasing-projects-on-github/about-releases), [managing releases](https://docs.github.com/en/repositories/releasing-projects-on-github/managing-releases-in-a-repository).

## Current links

- [0.5.0 engineering prerelease](https://github.com/azoghry-commits/Cognition-OS/releases/tag/v0.5.0)
- [Measured scaffolding PR](https://github.com/azoghry-commits/Cognition-OS/pull/1)
- [Real host evaluation backlog](https://github.com/azoghry-commits/Cognition-OS/issues/2)
