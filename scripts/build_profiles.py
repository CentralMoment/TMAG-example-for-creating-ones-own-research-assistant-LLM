"""Create the reviewed SFO/practice field profiles; no model or API is involved."""
import csv
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def rating(reference):
    """Describe the 1-5 scale and its dictionary location."""
    return {"valid_codes": [1, 2, 3, 4, 5], "missing_codes": ["", "0", "6", "BLANK"],
            "statistics": ["mean", "percentage", "distribution"], "dictionary_reference": reference}


def main():
    """Write transparent profiles that research owners can review and adapt."""
    fields = {name: rating("Code List!A234:C255") for name in ["Q7ART", "Q7FOOD", "Q7STORE",
        "Q7SIGN", "Q7WALKWAY", "Q7SCREENS", "Q7INFODOWN", "Q7INFOUP", "Q7WIFI", "Q7ROADS",
        "Q7PARK", "Q7AIRTRAIN", "Q7LTPARKING", "Q7RENTAL", "Q7ALL"]}
    fields["Q9Restroom"] = rating("Code List!A376:C389; 1=Dirty, 5=Clean")
    fields["NETPRO"] = {"valid_codes": list(range(11)), "missing_codes": ["", "11", "BLANK"],
                         "statistics": ["mean", "percentage", "distribution", "nps"],
                         "dictionary_reference": "Code List!A579:C591"}
    for name, codes, missing, reference in [
        ("Q17LIVE", [1, 2, 3], ["", "0"], "Code List!A592:C596"),
        ("Q11TSAPRE", [1, 2, 3, 4], ["", "0"], "Code List!A434:C439"),
        ("Q19Clear", [1, 2], ["", "0"], "Code List!A625:C628"),
        ("Q21Gender", [1, 2, 3], ["", "0"], "Code List!A638:C642")]:
        fields[name] = {"valid_codes": codes, "missing_codes": missing,
                        "statistics": ["percentage", "distribution"], "dictionary_reference": reference}
    sfo = {"name": "SFO 2018 reviewed descriptive fields", "id_field": "RESPNUM",
           "weight_field": "WEIGHT", "expected_shape": [2809, 97], "fields": fields}
    with (ROOT / "data/example/survey.csv").open() as handle:
        columns = len(next(csv.reader(handle)))
    practice = {"name": "Fictional practice survey", "id_field": "respondent_id",
                "weight_field": None, "expected_shape": [60, columns],
                "fields": {"satisfaction": rating("data/example/dictionary.md")}}
    target = ROOT / "profiles"
    target.mkdir(exist_ok=True)
    for name, profile in [("sfo", sfo), ("practice", practice)]:
        (target / f"{name}.json").write_text(json.dumps(profile, indent=2) + "\n", encoding="utf-8")
    for filename, name in [("config.json", "practice"), ("config.sfo.json", "sfo")]:
        path = ROOT / filename
        config = json.loads(path.read_text(encoding="utf-8"))
        config.update(profile_file=f"profiles/{name}.json", data_file=config["files"][0],
                      dictionary_file=config["files"][1])
        path.write_text(json.dumps(config, indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
