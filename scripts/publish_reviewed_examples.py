"""Publish selected, already-reviewed examples without raw provider traces or uploaded files."""
import argparse
import json
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def main():
    """Require explicit selection after a person has reviewed answers and generated artifacts."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source", type=Path)
    parser.add_argument("destination", type=Path)
    parser.add_argument("--ids", nargs="+", required=True, help="Exact ZIP stems, reviewed before publication")
    parser.add_argument("--include-artifacts", action="store_true")
    args = parser.parse_args()
    args.destination.mkdir(parents=True, exist_ok=True)
    entries = []
    for trial in args.ids:
        if Path(trial).name != trial:
            parser.error("IDs must be basenames.")
        with zipfile.ZipFile(args.source / f"{trial}.zip") as archive:
            for name in archive.namelist():
                if not name.endswith("evidence.json"):
                    continue
                prefix = name.split("/")[0]
                target = args.destination / trial / prefix
                target.mkdir(parents=True, exist_ok=True)
                record = json.loads(archive.read(name))
                # Explicit allowlist: raw stdout may contain respondent records or comments.
                safe = {key: record[key] for key in ["question", "model", "started_utc", "hashes", "status",
                    "elapsed_seconds", "usage", "calculations", "artifacts", "artifact_errors"]}
                (target / "calculations.json").write_text(json.dumps(safe, indent=2) + "\n", encoding="utf-8")
                (target / "answer.md").write_bytes(archive.read(f"{prefix}/answer.md"))
                artifact_links = []
                if args.include_artifacts:
                    for member in archive.namelist():
                        if member.startswith(f"{prefix}/artifacts/"):
                            (target / Path(member).name).write_bytes(archive.read(member))
                            artifact_links.append(f"- [{Path(member).name}]({trial}/{prefix}/{Path(member).name})")
                entries.append(f"- [{trial} / {prefix}]({trial}/{prefix}/answer.md) · "
                               f"[calculations]({trial}/{prefix}/calculations.json)")
                entries.extend(artifact_links)
    (args.destination / "README.md").write_text(
        "# Reviewed example selection\n\nObserved model outputs, not reference answers. "
        "See the validation report for grades and limitations. Provider traces, identifiers, "
        "and original uploaded files are omitted. Answers and artifacts were selected after review; "
        "this script is not a privacy classifier.\n\n" + "\n".join(entries) + "\n", encoding="utf-8")
    for filename in ["run.json", "arithmetic-review.json"]:
        if (args.source / filename).exists():
            data = json.loads((args.source / filename).read_text())
            data.pop("cleanup_failures", None)
            (args.destination / filename).write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")
    print(args.destination)


if __name__ == "__main__":
    main()
