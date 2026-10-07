"""Render a clean reference figure from independently computed aggregate values."""
import json
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]


def main():
    """Keep the presentation reference distinct from unedited model-generated artifacts."""
    reference = json.loads((ROOT / "evaluation/reference/sfo-reference.json").read_text())
    values = [reference["results"][f"Q7ALL.{mode}"]["top_two_percent"] for mode in ["unweighted", "weighted"]]
    fig, ax = plt.subplots(figsize=(9, 5.6), layout="constrained")
    bars = ax.bar(["Respondents\nUnweighted", "Weighted estimates\nWEIGHT applied"], values,
                  color=["#24557A", "#C9743B"], width=0.55)
    ax.set(ylim=(0, 100), ylabel="Share of valid responses (%)")
    ax.bar_label(bars, labels=[f"{value:.1f}%" for value in values], padding=8, fontsize=18, weight="bold")
    ax.spines[["top", "right"]].set_visible(False)
    ax.set_axisbelow(True)
    ax.grid(axis="y", alpha=.18)
    ax.tick_params(axis="both", labelsize=11)
    fig.suptitle('Defining "happy": an overall SFO rating of 4 or 5', fontsize=17, weight="bold")
    ax.set_title("2018 SFO Customer Survey · Same 2,625 valid responses in both estimates", fontsize=11, pad=22)
    fig.supxlabel("Source: Q7ALL and WEIGHT. 184 missing ratings excluded.\n"
                  "Independent reference calculation; descriptive estimates, not a change over time.", fontsize=10)
    target = ROOT / "docs/images/sfo-reference-comparison.png"
    target.parent.mkdir(exist_ok=True)
    fig.savefig(target, dpi=160, facecolor="white")
    plt.close(fig)
    print(target)


if __name__ == "__main__":
    main()
