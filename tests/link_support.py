import os
import subprocess
from contextlib import contextmanager
from pathlib import Path


@contextmanager
def directory_link(link, target):
    link = Path(link)
    target = Path(target)
    try:
        link.symlink_to(target, target_is_directory=True)
    except OSError as symlink_error:
        if os.name != "nt":
            raise
        result = subprocess.run(
            ["cmd.exe", "/d", "/c", "mklink", "/J", str(link), str(target)],
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace",
            check=False,
        )
        if result.returncode != 0 or not link.exists():
            raise AssertionError(
                "Windows could create neither a directory symlink nor a junction: "
                f"symlink={symlink_error!r}; junction_exit={result.returncode}"
            ) from symlink_error
    try:
        yield link
    finally:
        if link.is_symlink():
            link.unlink()
        elif link.exists():
            link.rmdir()
