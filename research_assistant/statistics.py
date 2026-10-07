"""Trusted descriptive statistics: fixed code, allowlisted fields, no generated eval()."""

import numpy as np
import pandas as pd


def calculate(frame, profile, *, field, statistic, weighted=False, filters=None, success_codes=None):
    """Calculate a mean, percentage, NPS, or distribution with explicit denominator rules."""
    if field not in profile["fields"]:
        raise ValueError("Field is not in the reviewed profile.")
    if not isinstance(weighted, bool):
        raise ValueError("weighted must be true or false.")
    spec = profile["fields"][field]
    if statistic not in spec.get("statistics", []):
        raise ValueError("Statistic is not approved for this field.")
    selected = frame
    for condition in filters or []:
        name, codes = condition["field"], condition["codes"]
        if name not in profile["fields"] or not codes:
            raise ValueError("Filters require an approved field and at least one code.")
        allowed = {str(x) for x in profile["fields"][name]["valid_codes"]}
        if not set(map(str, codes)).issubset(allowed):
            raise ValueError("Filter includes an invalid or missing code.")
        selected = selected.loc[selected[name].str.strip().isin(list(map(str, codes)))]
    values = pd.to_numeric(selected[field], errors="coerce")
    valid = values.isin(spec["valid_codes"])
    weights = pd.Series(1.0, index=selected.index)
    if weighted:
        weight_field = profile.get("weight_field")
        if not weight_field:
            raise ValueError("This dataset has no approved weight field.")
        weights = pd.to_numeric(selected[weight_field], errors="coerce")
        if (~np.isfinite(weights) | weights.le(0)).any():
            raise ValueError("Invalid weights; resolve them before calculating.")
    values, weights = values[valid], weights[valid]
    n = len(values)
    result = {"field": field, "statistic": statistic, "weighted": weighted,
              "filters": filters or [], "valid_codes": spec["valid_codes"],
              "selected_n": len(selected), "valid_n": n, "excluded_n": len(selected) - n,
              "denominator": "valid answers after filters", "sum_weights": float(weights.sum()),
              "dictionary_reference": spec.get("dictionary_reference"), "value": None}
    result["reporting_rules"] = {"suppress_below_n": 20, "strong_caution_below_n": 30,
                                 "caution_below_n": 50}
    if n < 20:
        result.update(status="suppressed", caution="Fewer than 20 valid answers; count only.")
        return result
    result.update(status="computed", caution=("Very small subgroup (n<30)." if n < 30 else
                                               "Small subgroup (n<50)." if n < 50 else ""))
    if statistic == "mean":
        result["value"] = float(np.average(values, weights=weights))
    elif statistic == "percentage":
        if not success_codes or not set(success_codes).issubset(spec["valid_codes"]):
            raise ValueError("Supply nonempty success_codes drawn from valid response codes.")
        result["success_codes"] = success_codes
        result["numerator_n"] = int(values.isin(success_codes).sum())
        if result["numerator_n"] < 20:
            result.update(status="suppressed", caution="Numerator cell has n<20; counts only.")
            return result
        result["value"] = float(np.average(values.isin(success_codes), weights=weights) * 100)
    elif statistic == "nps":
        scores = (values.ge(9).astype(int) - values.le(6).astype(int)) * 100
        result["value"] = float(np.average(scores, weights=weights))
    elif statistic == "distribution":
        cells = []
        for code in spec["valid_codes"]:
            members = values.eq(code)
            cell_n = int(members.sum())
            # Counts may be shown, but each tiny cell's percentage and weighted mass are withheld.
            cells.append({"code": code, "n": cell_n,
                          "percent": float(weights[members].sum() / weights.sum() * 100) if cell_n >= 20 else None,
                          "weighted_frequency": float(weights[members].sum()) if cell_n >= 20 else None,
                          "status": "computed" if cell_n >= 20 else "suppressed",
                          "caution": ("Suppressed because n<20." if cell_n < 20 else
                                      "Very small cell (n<30)." if cell_n < 30 else
                                      "Small cell (n<50)." if cell_n < 50 else "")})
        result["cells"] = cells
    return result


def tool_definition(profile):
    """Describe the narrowly scoped local calculator to the model."""
    return {"name": "survey_statistic", "description":
            "Trusted descriptive calculator. Prefer it for supported fields. Filters are AND across fields, OR across codes. "
            "Reports exclusions, unweighted n, weights and suppression. Available definitions: " + str(profile["fields"]),
            "input_schema": {"type": "object", "properties": {
                "field": {"type": "string", "enum": list(profile["fields"])},
                "statistic": {"type": "string", "enum": ["mean", "percentage", "distribution", "nps"]},
                "weighted": {"type": "boolean"},
                "filters": {"type": "array", "items": {"type": "object", "properties": {
                    "field": {"type": "string"}, "codes": {"type": "array", "items": {"type": "integer"}}},
                    "required": ["field", "codes"], "additionalProperties": False}},
                "success_codes": {"type": "array", "items": {"type": "integer"}}},
                "required": ["field", "statistic"], "additionalProperties": False}}
