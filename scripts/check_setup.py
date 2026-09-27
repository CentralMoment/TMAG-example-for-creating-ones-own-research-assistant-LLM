"""Validate local configuration and practice data without making an API call."""

import csv
import importlib.metadata
import json
from pathlib import Path


def main():
    """Check dependencies, selected files, and the known synthetic-data answers."""
    root = Path(__file__).resolve().parents[1]
    config = json.loads((root / "config.json").read_text(encoding="utf-8-sig"))
    for package in ("anthropic", "streamlit", "python-dotenv"):
        print(f"{package}: {importlib.metadata.version(package)}")
    for name in [config["prompt_file"], *config["files"]]:
        path = root / name
        if not path.is_file() or path.stat().st_size == 0:
            raise ValueError(f"Missing or empty file: {name}")
        print(f"Found: {name}")
    with (root / "data/example/survey.csv").open(newline="", encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle))
    values = [int(row["satisfaction"]) for row in rows]
    assert len(values) == 60 and sum(values) / len(values) == 3.0
    assert sum(value >= 4 for value in values) == 24
    print("PASS: local configuration and practice references. No API call made.")
    print("Next: configure .env, launch Streamlit, and run the manual question checks.")


if __name__ == "__main__":
    main()
