"""Independently check captured local-tool arithmetic; this does not grade model prose."""
import argparse
import csv
import json
import math
import sys
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(Path(__file__).resolve().parent))
from build_reference import number, summarize


def review(directory, csv_path):
    """Compare captured calculations with independent stdlib arithmetic and policy boundaries."""
    with csv_path.open(encoding="utf-8-sig", newline="") as handle:
        rows = [{k.strip(): v.strip() for k, v in row.items()} for row in csv.DictReader(handle)]
    profile = json.loads((ROOT / "profiles/sfo.json").read_text(encoding="utf-8"))
    checks = []
    for path in sorted(directory.glob("*.zip")):
        with zipfile.ZipFile(path) as archive:
            for filename in archive.namelist():
                if not filename.endswith("evidence.json"):
                    continue
                record = json.loads(archive.read(filename))
                for index, actual in enumerate(record["calculations"]):
                    selected = rows
                    for condition in actual["filters"]:
                        selected = [row for row in selected if number(row[condition["field"]]) in condition["codes"]]
                    valid = profile["fields"][actual["field"]]["valid_codes"]
                    expected = summarize(selected, actual["field"], valid, actual["weighted"])
                    errors = []
                    for name in ["selected_n", "valid_n", "excluded_n"]:
                        if actual[name] != expected[name]:
                            errors.append(name)
                    if not math.isclose(actual["sum_weights"], expected["sum_weights"], abs_tol=1e-8):
                        errors.append("sum_weights")
                    if actual["valid_n"] < 20 or (actual["statistic"] == "percentage" and actual.get("numerator_n", 20) < 20):
                        if actual["value"] is not None or actual["status"] != "suppressed":
                            errors.append("suppression")
                    elif actual["statistic"] == "distribution":
                        for cell, reference in zip(actual["cells"], expected["cells"]):
                            if cell["n"] != reference["n"] or cell["code"] != reference["code"]:
                                errors.append("cell count/code")
                            for name in ["percent", "weighted_frequency"]:
                                if cell["n"] < 20:
                                    if cell[name] is not None:
                                        errors.append("cell suppression")
                                elif not math.isclose(cell[name], reference[name], abs_tol=1e-8):
                                    errors.append(name)
                    else:
                        value = expected.get(actual["statistic"])
                        if actual["statistic"] == "percentage":
                            eligible = [row for row in selected if number(row[actual["field"]]) in valid]
                            numerator = math.fsum(number(row["WEIGHT"]) if actual["weighted"] else 1
                                for row in eligible if number(row[actual["field"]]) in actual["success_codes"])
                            value = 100 * numerator / expected["sum_weights"]
                        if value is None or not math.isclose(actual["value"], value, abs_tol=1e-8):
                            errors.append("value")
                    checks.append({"trial": path.stem, "turn": filename.split("/")[0], "calculation": index,
                                   "field": actual["field"], "statistic": actual["statistic"],
                                   "arithmetic": "FAIL" if errors else "PASS", "errors": errors})
    return {"scope": "Captured local-tool arithmetic only; question interpretation, hosted code, artifacts and prose require review.",
            "checked": len(checks), "failed": sum(c["arithmetic"] == "FAIL" for c in checks), "checks": checks}


def main():
    """Save an arithmetic check without converting it into an overall model grade."""
    parser = argparse.ArgumentParser()
    parser.add_argument("directory", type=Path)
    parser.add_argument("--csv", type=Path, default=ROOT / "data/private/2018 SFO Customer Survey.csv")
    args = parser.parse_args()
    result = review(args.directory, args.csv)
    (args.directory / "arithmetic-review.json").write_text(json.dumps(result, indent=2), encoding="utf-8")
    print({key: value for key, value in result.items() if key != "checks"})
    if result["failed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
