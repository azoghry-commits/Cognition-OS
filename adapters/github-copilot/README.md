# GitHub Copilot adapter

The canonical root `plugin.json` uses Agent Plugins 1.0. GitHub Copilot and compatible VS Code harnesses discover the shared `skills/` directory directly. Install from the repository or a reviewed marketplace source; project-only consumers can copy selected skills into `.github/skills/`, `.agents/skills/`, or `.claude/skills/` as supported by the active Copilot surface.

Custom agents and native orchestration vary across Copilot cloud agent, code review, CLI, app, and VS Code. Cognition OS therefore returns a deterministic DAG schedule and lets the active host execute each wave. No GitHub workflow, pull request, or repository setting is changed by installation.
