"""Validate the selected dataset and dependencies without any API call."""
import argparse
import importlib.metadata
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from research_assistant.data import load_project
from research_assistant.statistics import calculate


def main():
    """Audit selected inputs and optionally save their reproducibility manifest."""
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", default="config.json")
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    for package in ("anthropic", "streamlit", "python-dotenv", "pandas", "openpyxl"):
        print(f"{package}: {importlib.metadata.version(package)}")
    project = load_project(ROOT, args.config)
    if project["profile"]["name"] == "Fictional practice survey":
        result = calculate(project["data"], project["profile"], field="satisfaction", statistic="mean")
        if result["valid_n"] != 60 or result["value"] != 3.0:
            raise ValueError("Practice references do not match.")
    manifest = {"hashes": project["hashes"], "audit": project["audit"]}
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(project["audit"], indent=2))
    print("PASS: selected dataset audit. No API call made; model answers are not validated.")


if __name__ == "__main__":
    main()
