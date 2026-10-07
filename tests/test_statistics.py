"""Boundary and independent-reference tests for research rules."""
import json
from pathlib import Path

import pandas as pd
import pytest

from research_assistant.data import audit_survey, read_survey
from research_assistant.statistics import calculate

ROOT = Path(__file__).resolve().parents[1]
PROFILE = {"id_field": "id", "weight_field": "w", "fields": {
    "rating": {"valid_codes": [1, 2, 3, 4, 5], "missing_codes": ["0", "6", "BLANK", ""],
               "statistics": ["mean", "percentage", "distribution"]},
    "group": {"valid_codes": [1, 2], "missing_codes": ["0"], "statistics": ["distribution"]}}}


def sample(n=60):
    """Build a fixture whose unequal weights expose denominator errors."""
    return pd.DataFrame({"id": list(map(str, range(n))), "rating": ["1", "5"]*(n//2),
                         "group": ["1", "2"]*(n//2), "w": ["1", "3"]*(n//2)})


def test_weights_and_missing_codes():
    """A weighted mean must use matching valid rows, not all respondents."""
    data = sample()
    data.loc[0, "rating"] = "BLANK"
    result = calculate(data, PROFILE, field="rating", statistic="mean", weighted=True)
    assert result["valid_n"] == 59 and result["excluded_n"] == 1
    assert result["value"] == pytest.approx((29 + 30*5*3)/(29+30*3))
    with pytest.raises(ValueError):
        calculate(data.assign(w="-1"), PROFILE, field="rating", statistic="mean", weighted=True)


@pytest.mark.parametrize("n,status,caution", [(0,"suppressed",True),(19,"suppressed",True),
    (20,"computed",True),(29,"computed",True),(30,"computed",True),(49,"computed",True),(50,"computed",False)])
def test_suppression_boundaries(n, status, caution):
    """Small-group rules are enforced on the valid unweighted count."""
    data = sample(60).iloc[:n]
    result = calculate(data, PROFILE, field="rating", statistic="mean")
    assert result["status"] == status
    assert bool(result["caution"]) == caution
    assert (result["value"] is None) == (status == "suppressed")


def test_cell_suppression_and_filter_validation():
    """A large overall base cannot authorize a tiny cell's percentage."""
    data = sample().assign(rating=["1"] + ["5"]*59)
    result = calculate(data, PROFILE, field="rating", statistic="distribution")
    assert result["cells"][0]["percent"] is None
    assert result["cells"][0]["caution"] == "Suppressed because n<20."
    assert result["reporting_rules"]["suppress_below_n"] == 20
    assert result["cells"][4]["percent"] == pytest.approx(100*59/60)
    with pytest.raises(ValueError):
        calculate(data, PROFILE, field="rating", statistic="mean", filters=[{"field":"group","codes":[0]}])


def test_rare_numerator_and_weight_type():
    """Percentage requests cannot bypass the distribution's small-cell rule."""
    data = sample().assign(rating=["1"] + ["5"]*59)
    result = calculate(data, PROFILE, field="rating", statistic="percentage", success_codes=[1])
    assert result["value"] is None and result["numerator_n"] == 1
    assert result["valid_n"] == 60 and result["status"] == "suppressed"
    with pytest.raises(ValueError):
        calculate(data, PROFILE, field="rating", statistic="mean", weighted="false")


def test_audit_rejects_duplicate_ids_and_unexpected_codes():
    """Data faults are surfaced before the first upload."""
    data = sample()
    data.loc[0, "id"] = "1"
    data.loc[0, "rating"] = "99"
    audit = audit_survey(data, PROFILE)
    assert audit["status"] == "FAIL" and len(audit["errors"]) == 2


def test_sfo_against_independent_reference():
    """Compare all supported SFO means against independent stdlib computations."""
    path = ROOT / "data/private/2018 SFO Customer Survey.csv"
    if not path.exists():
        pytest.skip("Optional SFO source data not installed.")
    data = read_survey(path)
    profile = json.loads((ROOT / "profiles/sfo.json").read_text())
    reference = json.loads((ROOT / "evaluation/reference/sfo-reference.json").read_text())
    for key, expected in reference["results"].items():
        if len(key.split(".")) != 2:
            continue
        actual = calculate(data, profile, field=expected["field"], statistic="mean", weighted=expected["weighted"])
        assert actual["valid_n"] == expected["valid_n"]
        assert actual["value"] == pytest.approx(expected["mean"], abs=1e-12)
