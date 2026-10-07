"""Check tracked and unignored files for accidental credentials or private inputs."""
import re
import subprocess
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PATTERNS = [rb"sk-ant-api[A-Za-z0-9_-]{15,}", rb"gh[pousr]_[A-Za-z0-9]{20,}"]


def main():
    """Report filenames only, never print a matched credential."""
    output = subprocess.check_output(["git", "ls-files", "-z", "--cached", "--others", "--exclude-standard"], cwd=ROOT)
    names = [name.decode("utf-8") for name in output.split(b"\0") if name]
    failures = []
    for name in names:
        path = ROOT / name
        if not path.is_file():
            continue
        if (name.startswith("data/private/") and not name.endswith(".gitkeep")) or name.startswith(("output/", "logs/")):
            failures.append((name, "private/generated input unexpectedly tracked"))
        if path.name == ".env" or "API key" in path.name:
            failures.append((name, "credential filename"))
        contents = [path.read_bytes()] if path.suffix not in [".png", ".jpg", ".zip"] else []
        if path.suffix == ".zip":
            with zipfile.ZipFile(path) as archive:
                contents = [archive.read(member) for member in archive.namelist() if not member.endswith("/")]
        if any(re.search(pattern, data) for pattern in PATTERNS for data in contents):
            failures.append((name, "credential-like content"))
    if failures:
        print(failures)
        raise SystemExit(1)
    print(f"PASS: {len(names)} publication files checked. Pattern scan is not a complete secret or privacy audit.")


if __name__ == "__main__":
    main()
