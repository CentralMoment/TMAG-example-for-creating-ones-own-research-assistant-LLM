"""Load and audit survey inputs without changing the original files."""

import hashlib
import json
from pathlib import Path

import numpy as np
import pandas as pd
from openpyxl import load_workbook


def sha256(path):
    """Fingerprint a file so changes cannot silently reuse an old conversation."""
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def read_survey(path):
    """Preserve literal missing codes and normalize header whitespace only."""
    frame = pd.read_csv(path, dtype=str, keep_default_na=False)
    names = frame.columns.str.strip()
    if names.duplicated().any():
        raise ValueError("Column names collide after trimming whitespace.")
    frame.columns = names
    return frame


def audit_survey(frame, profile, dictionary_path=None):
    """Report schema, code, identifier, weight, and documented skip-pattern issues."""
    errors, warnings = [], []
    expected = profile.get("expected_shape")
    if expected and list(frame.shape) != expected:
        errors.append(f"Expected shape {expected}; found {list(frame.shape)}.")
    required = set(profile["fields"]) | {profile["id_field"]}
    if profile.get("weight_field"):
        required.add(profile["weight_field"])
    missing = sorted(required - set(frame.columns))
    if missing:
        errors.append(f"Missing columns: {missing}")
    identifier = profile["id_field"]
    if identifier in frame:
        if frame[identifier].str.strip().eq("").any() or frame[identifier].duplicated().any():
            errors.append("Respondent IDs must be populated and unique.")
    fields = {}
    for field, spec in profile["fields"].items():
        if field not in frame:
            continue
        values = frame[field].str.strip()
        codes = {str(x) for x in spec["valid_codes"]}
        allowed = codes | set(spec.get("missing_codes", []))
        unexpected = sorted(set(values) - allowed)
        if unexpected:
            errors.append(f"{field}: undocumented codes {unexpected}")
        fields[field] = {"valid_n": int(values.isin(codes).sum()),
                         "missing_or_inapplicable_n": int((~values.isin(codes)).sum()),
                         "unexpected_codes": unexpected}
    weight_field = profile.get("weight_field")
    weight_report = None
    if weight_field and weight_field in frame:
        weights = pd.to_numeric(frame[weight_field], errors="coerce")
        invalid = ~np.isfinite(weights) | weights.le(0)
        weight_report = {"invalid_n": int(invalid.sum()), "sum": float(weights[~invalid].sum())}
        if invalid.any():
            errors.append("Weights must be finite and positive; resolve invalid weights before analysis.")
    dictionary_report = None
    if dictionary_path and Path(dictionary_path).suffix.lower() == ".xlsx":
        workbook = load_workbook(dictionary_path, read_only=True, data_only=True)
        sheet = workbook["Code List"]
        documented = {str(row[0]).strip().casefold() for row in sheet.values if row[0] is not None}
        undocumented = sorted(c for c in frame if c.casefold() not in documented)
        dictionary_report = {"sheet": "Code List", "columns_not_named": undocumented}
        workbook.close()
        if undocumented:
            warnings.append(f"Columns not explicitly named in dictionary: {undocumented}")
    # The dictionary describes the follow-up, but does not establish a mandatory skip rule.
    skip_review = None
    if {"Q11TSAPRE", "Q12PRECHECKRATE"}.issubset(frame):
        mask = frame.Q11TSAPRE.ne("1") & frame.Q12PRECHECKRATE.isin(["1", "2", "3", "4", "5"])
        skip_review = {"precheck_rating_without_reported_precheck_use_n": int(mask.sum()),
                       "action": "Review eligibility; do not silently delete these records."}
    return {"status": "FAIL" if errors else "PASS", "rows": len(frame), "columns": len(frame.columns),
            "errors": errors, "warnings": warnings, "fields": fields,
            "weights": weight_report, "dictionary": dictionary_report, "skip_review": skip_review,
            "scope": "Configured fields only; not a full survey-methodology or disclosure audit."}


def load_project(root, config_name="config.json"):
    """Load configuration, audit selected data, and fingerprint all authoritative inputs."""
    root = Path(root)
    config_path = root / config_name
    config = json.loads(config_path.read_text(encoding="utf-8-sig"))
    names = [config["prompt_file"], *config["files"], config["profile_file"]]
    paths = [root / name for name in names]
    if len({Path(n).name for n in config["files"]}) != len(config["files"]):
        raise ValueError("Uploaded files must have distinct basenames.")
    hashes = {name: sha256(path) for name, path in zip(names, paths)}
    hashes[config_name] = sha256(config_path)
    profile = json.loads((root / config["profile_file"]).read_text(encoding="utf-8"))
    csv_path = root / config["data_file"]
    if config["data_file"] not in config["files"]:
        raise ValueError("data_file must also be listed in files.")
    frame = read_survey(csv_path)
    dictionary_path = root / config["dictionary_file"]
    if config["dictionary_file"] not in config["files"]:
        raise ValueError("dictionary_file must also be listed in files.")
    audit = audit_survey(frame, profile, dictionary_path)
    if audit["errors"]:
        raise ValueError("Data audit failed: " + " ".join(audit["errors"]))
    # These shared instructions are also authoritative and included in evidence hashes.
    policy_path = root / "prompts/research-policy.md"
    hashes["prompts/research-policy.md"] = sha256(policy_path)
    # Record source hashes even when a trial is run from an uncommitted working tree.
    for path in sorted((root / "research_assistant").glob("*.py")):
        hashes[path.relative_to(root).as_posix()] = sha256(path)
    prompt = (root / config["prompt_file"]).read_text(encoding="utf-8") + "\n\n" + policy_path.read_text(encoding="utf-8")
    fingerprint = hashlib.sha256(json.dumps(hashes, sort_keys=True).encode()).hexdigest()
    return {"config": config, "profile": profile, "data": frame, "audit": audit,
            "prompt": prompt, "hashes": hashes, "fingerprint": fingerprint,
            "paths": [root / n for n in config["files"]]}
