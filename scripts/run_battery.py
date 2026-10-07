"""Run real model trials through the same engine as Streamlit; never auto-grade prose."""
import argparse
import json
import os
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

import anthropic
from dotenv import load_dotenv
from research_assistant.data import load_project
from research_assistant.engine import answer_text, cleanup_files, evidence_zip, new_session, run_turn


def main():
    """Preserve one evidence bundle per trial, stop on service failures, and delete owned files."""
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", default="config.sfo.json")
    parser.add_argument("--env-file", type=Path, default=ROOT / ".env")
    parser.add_argument("--ids", nargs="*")
    parser.add_argument("--repeat", type=int, default=1)
    parser.add_argument("--question", help="Run a custom smoke check instead of battery questions.")
    parser.add_argument("--follow-up", help="Ask this in the same session after a custom question.")
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    if args.repeat < 1 or args.repeat > 3:
        parser.error("repeat must be between 1 and 3")
    load_dotenv(args.env_file)
    model = os.environ.get("ANTHROPIC_MODEL", "claude-opus-5")
    client = anthropic.Anthropic(timeout=180.0, max_retries=1)
    project = load_project(ROOT, args.config)
    battery = json.loads((ROOT / "evaluation/sfo-question-battery.json").read_text())
    questions = battery["original_questions"] + battery["historical_variants"]
    if args.question:
        questions = [{"id": "CUSTOM", "question": args.question}]
    elif args.ids:
        unknown = set(args.ids) - {q["id"] for q in questions}
        if unknown:
            parser.error(f"Unknown IDs: {unknown}")
        questions = [q for q in questions if q["id"] in args.ids]
    else:
        questions = battery["original_questions"]
    target = args.output or ROOT / "output/evaluation" / datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    target.mkdir(parents=True, exist_ok=False)
    commit = subprocess.run(["git", "rev-parse", "HEAD"], cwd=ROOT, capture_output=True, text=True).stdout.strip()
    dirty = bool(subprocess.run(["git", "status", "--porcelain"], cwd=ROOT, capture_output=True, text=True).stdout.strip())
    summary = {"model": model, "commit": commit, "working_tree_modified": dirty,
               "hashes": project["hashes"], "trials": [], "cleanup_failures": []}
    for question in questions:
        for trial in range(1, args.repeat + 1):
            session = new_session()
            trial_id = f"{question['id']}-trial-{trial}"
            record = None
            try:
                record = run_turn(client, project, session, question["question"], model)
                if args.follow_up and record["status"] == "completed":
                    run_turn(client, project, session, args.follow_up, model)
            except Exception as exc:
                # Do not print provider exception bodies: they may contain sensitive inputs.
                print(f"{trial_id}: {type(exc).__name__}", flush=True)
            finally:
                (target / f"{trial_id}.zip").write_bytes(evidence_zip(session))
                turns = session["turns"]
                for index, turn in enumerate(turns):
                    (target / f"{trial_id}-turn-{index+1}.md").write_text(answer_text(turn), encoding="utf-8")
                failures = cleanup_files(client, session)
                summary["cleanup_failures"].extend(failures)
                summary["trials"].append({"id": trial_id,
                    "execution": turns[-1]["status"] if turns else "error",
                    "grade": "NOT REVIEWED", "elapsed_seconds": sum(t["elapsed_seconds"] for t in turns),
                    "artifact_count": sum(len(t["artifacts"]) for t in turns),
                    "usage": [t["usage"] for t in turns]})
                (target / "run.json").write_text(json.dumps(summary, indent=2), encoding="utf-8")
            print(json.dumps(summary["trials"][-1]), flush=True)
            if not record or record["status"] == "error" or failures:
                raise SystemExit("Stopped after service/cleanup failure; inspect the saved run.")


if __name__ == "__main__":
    main()
