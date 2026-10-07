"""Compute independent reference answers with stdlib arithmetic, not the app calculator."""
import argparse
import csv
import hashlib
import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def number(value):
    """Parse a numeric code while preserving nonnumeric missing responses as None."""
    try:
        result = float(value)
        return result if math.isfinite(result) else None
    except (ValueError, TypeError):
        return None


def summarize(rows, field, valid_codes, weighted=False):
    """Calculate an independent reference using explicit loops and math.fsum."""
    values = [(number(row[field]), number(row["WEIGHT"]) if weighted else 1.0) for row in rows]
    pairs = [(value, weight) for value, weight in values if value in valid_codes]
    if any(weight is None or weight <= 0 for _, weight in pairs):
        raise ValueError("Invalid reference weight.")
    denominator = math.fsum(weight for _, weight in pairs)
    n = len(pairs)
    cells = [{"code": code, "n": sum(value == code for value, _ in pairs),
              "weighted_frequency": math.fsum(weight for value, weight in pairs if value == code),
              "percent": 100 * math.fsum(weight for value, weight in pairs if value == code) / denominator}
             for code in valid_codes] if denominator else []
    return {"field": field, "weighted": weighted, "selected_n": len(rows), "valid_n": n,
            "excluded_n": len(rows)-n, "sum_weights": denominator,
            "mean": math.fsum(value*weight for value, weight in pairs)/denominator if denominator else None,
            "top_two_percent": 100*math.fsum(weight for value, weight in pairs if value in [4, 5])/denominator if denominator else None,
            "nps": 100*math.fsum(weight*((value >= 9)-(value <= 6)) for value, weight in pairs)/denominator if field == "NETPRO" and denominator else None,
            "cells": cells}


def build(csv_path):
    """Build reference tables for factual, comparative, exploratory, and export checks."""
    with csv_path.open(encoding="utf-8-sig", newline="") as handle:
        rows = [{key.strip(): value.strip() for key, value in row.items()} for row in csv.DictReader(handle)]
    results = {}
    for field in [key for key in rows[0] if key.startswith("Q7")] + ["Q9Restroom", "NETPRO"]:
        valid = list(range(11)) if field == "NETPRO" else [1, 2, 3, 4, 5]
        for weighted in [False, True]:
            mode = "weighted" if weighted else "unweighted"
            results[f"{field}.{mode}"] = summarize(rows, field, valid, weighted)
    for group_field, groups in {"Q17LIVE": {"resident": ["1"], "elsewhere": ["2", "3"]},
                                 "Q11TSAPRE": {"yes": ["1"], "no": ["2"]},
                                 "Q19Clear": {"yes": ["1"], "no": ["2"]},
                                 "Q21Gender": {"male": ["1"], "female": ["2"]}}.items():
        for label, codes in groups.items():
            subset = [row for row in rows if row[group_field] in codes]
            for field, valid in [("Q7ALL", [1, 2, 3, 4, 5]), ("NETPRO", list(range(11)))]:
                for weighted in [False, True]:
                    mode = "weighted" if weighted else "unweighted"
                    result = summarize(subset, field, valid, weighted)
                    result["filter"] = {group_field: codes}
                    results[f"{field}.{group_field}.{label}.{mode}"] = result
    all_low_fields = ["Q7ART", "Q7STORE", "Q7SIGN", "Q7WALKWAY", "Q7SCREENS", "Q9Restroom"]
    all_low_n = sum(all(row[field] == "1" for field in all_low_fields) for row in rows)
    segments = []
    for purpose in [1, 2, 3, 4, 5, 6, 7, 10, 11, 12, 13]:
        for label, codes in {"resident": ["1"], "elsewhere": ["2", "3"]}.items():
            subset = [row for row in rows if row["Q17LIVE"] in codes and
                      str(purpose) in [row[f"Q2PURP{i}"] for i in [1, 2, 3]]]
            result = summarize(subset, "Q7ALL", [1, 2, 3, 4, 5], True)
            # Public segment summaries obey the reporting threshold.
            segments.append({"purpose": purpose, "residency": label, "valid_n": result["valid_n"],
                             "weighted_mean": result["mean"] if result["valid_n"] >= 20 else None})
    return {"method": "Independent Python stdlib csv + math.fsum; no app calculator imports.",
            "source_sha256": hashlib.sha256(csv_path.read_bytes()).hexdigest(),
            "rows": len(rows), "columns": len(rows[0]), "results": results,
            "all_six_lowest": {"fields": all_low_fields, "condition": "ALL fields equal 1", "n": all_low_n},
            "purpose_by_residency": segments,
            "note": "Reference cells include small counts for verification. The assistant must suppress small-cell percentages. No respondent records included."}


def main():
    """Write independent numerical references outside the assistant's input files."""
    parser = argparse.ArgumentParser()
    parser.add_argument("--csv", type=Path, default=ROOT / "data/private/2018 SFO Customer Survey.csv")
    parser.add_argument("--output", type=Path, default=ROOT / "evaluation/reference/sfo-reference.json")
    args = parser.parse_args()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(build(args.csv), indent=2) + "\n", encoding="utf-8")
    print(f"Wrote {args.output}")


if __name__ == "__main__":
    main()
