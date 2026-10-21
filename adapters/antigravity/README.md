# Antigravity adapter

Use `dist/cognition-os-antigravity-<version>.zip` or install this repository as a local plugin. The Antigravity package keeps the root `plugin.json` minimal and exposes the shared `skills/`, optional `agents/`, and local helper resources without duplicating the cognitive core.

Antigravity App, CLI, and IDE can discover the same `SKILL.md` bundles. Workspace-only installation may instead place selected skill folders under `.agents/skills/`. Native agents, hooks, browser tools, background work, and parallel capacity remain host capabilities; the plugin queries or observes them before relying on them.

For dependency-aware analysis, call `python scripts/cognition.py analysis-plan` with the step DAG and observed host capacity. Steps in the same returned wave are independent. Antigravity may dispatch them concurrently when its current surface exposes authorized subagents; otherwise execute the returned sequential fallback.
