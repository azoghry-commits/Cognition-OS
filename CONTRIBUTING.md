# Contributing to Cognition OS

Keep each contribution focused enough that a reviewer can understand the behavior change, its evidence, and its rollback path without reconstructing unrelated work.

## Change workflow

1. Start from a clear user, host, or maintenance problem.
2. Make one coherent feature or fix per commit. Keep formatting-only or broad refactoring work separate.
3. Add or update the test that proves the changed behavior in the same commit. Documentation-only changes should identify the source or behavior they clarify.
4. Run the locked local quality gates before opening a pull request:

   ```powershell
   uv sync --locked --extra dev
   uv run --locked --extra dev pip-audit --progress-spinner off
   uv run --locked --extra dev ruff check cognition scripts tests
   uv run --locked --extra dev mypy cognition
   uv run --locked --extra dev coverage run -m pytest
   uv run --locked --extra dev coverage report --fail-under=80
   uv run --locked --extra dev python scripts/validate_package.py
   ```

5. In the pull request, describe the final behavior, the checks you ran, and any remaining limitation.

Generated package archives, credentials, private data, machine-specific state, and unrelated files do not belong in a contribution. Changes to contracts, persistence, permissions, dependencies, or distribution require an explicit rationale and compatible migration or rollback notes.

The repository has no public license grant. Discuss licensing with the maintainer before contributing code intended for redistribution.
