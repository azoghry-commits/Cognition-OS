"""Run the locked repository quality gates from one cross-platform command."""

import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def run(*arguments: str) -> None:
    command = [sys.executable, *arguments]
    print(f"+ {' '.join(command)}", flush=True)
    subprocess.run(command, cwd=ROOT, check=True)


def main() -> int:
    run("-m", "pip_audit", "--progress-spinner", "off")
    run("-m", "ruff", "check", "cognition", "scripts", "tests")
    run("-m", "mypy", "cognition")
    run("-m", "coverage", "run", "-m", "pytest")
    run("-m", "coverage", "report", "--fail-under=80")
    run("scripts/validate_package.py")
    run("scripts/package_release.py")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
