# Troubleshooting

Plugin absent: confirm plugin.json at package root, supported schema and correct marketplace-root-relative source.path. For Claude ensure .claude-plugin/plugin.json exists and pass the plugin directory, not the marketplace directory, to --plugin-dir. Check organization installation policies. Desktop restart/refresh may be required.

Skills absent: inspect the installed cache copy for skills/<name>/SKILL.md, exact frontmatter and version. Root portable skills discovery uses fixed paths; do not add speculative fields. OpenAI inline extension overrides fallback settings completely.

References unavailable: resolve ../../ references from installed skill directory, not project cwd. Check package file inventory. If the host cannot read bundled assets, report the specific limitation and do not replace model-specific methods with generic advice.

Calculation fails: inspect missing keys, finite numbers, unit compatibility, distributions and probability ranges. Helper prints a FAILED JSON error to stderr and exits 2. Fix actual inputs; never clamp or invent defaults. If Python or execution is unavailable, use a verified host calculator or mark quantitative validation BLOCKED while continuing qualitative work.

Kepner-Tregoe blocked: complete What/Where/When/Extent and unaffected contrasts. Timing correlation alone does not confirm a root cause. Unsupported confidence or copied stockout examples indicate a failed behavioral evaluation.

Case write denied: confirm explicit authorization, project path, safe ID, sensitivity consent and no link/junction. Existing IDs require a new version ID, never forced overwrite. Cross-project records need reviewed migration. No case data is removed on uninstall.

Manifest validates but behavior fails: record actual activation, resource loads, tools, responses and failed rubric. JSON parsing is only one check. Review TEST_REPORT and PROJECT_STATUS for unverified host gates. Do not announce production readiness to bypass a failed gate.

