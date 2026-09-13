#!/usr/bin/env python3
"""Plot accuracy losses from D7.6 Table 2 using exact Decimal subtraction.

Rows are reported attack names, not evidence of equal attack budgets. The
colour scale is linear; cell labels preserve small losses near zero.
"""
import argparse
import json
from decimal import Decimal
from pathlib import Path

import matplotlib as mpl
mpl.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import LinearSegmentedColormap

HERE = Path(__file__).resolve().parent
OUTPUT = HERE.parent / "sparta/thesis/sparta-benchmark-deltas.pdf"
DATA = json.loads((HERE / "sparta-reported-results.json").read_text())
ORDER = ["FGSM", "BIM", "PGD", "L2 Basic Iter", "Additive noise", "Deep Fool", "Newton Fool"]
LABELS = ["FGSM", "BIM", "PGD", r"$L_2$ basic iterative", "Additive noise", "DeepFool", "NewtonFool"]
mpl.rcParams.update({
    "font.family": "sans-serif",
    "font.sans-serif": ["DejaVu Sans"],
    "font.size": 7, "axes.labelsize": 7,
    "xtick.labelsize": 7, "ytick.labelsize": 7,
    "text.color": "#333333", "axes.labelcolor": "#333333",
    "xtick.color": "#333333", "ytick.color": "#333333",
    "pdf.fonttype": 42, "svg.fonttype": "none",
})


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--preview-dir", type=Path)
    args = parser.parse_args()
    source = DATA["benchmark"]
    columns = source["defences"]
    lookup = {r["label"]: r["accuracies"] for r in source["attacks"]}
    exact = [[(Decimal(c["clean_accuracy"]) - Decimal(lookup[r][c["id"]])) * 100
              for c in columns] for r in ORDER]
    losses = np.array([[float(v) for v in row] for row in exact])
    assert losses.shape == (7, 5) and np.all((losses >= 0) & (losses <= 85))
    assert exact[2] == [Decimal(v) for v in ["0.7", "0.9", "0.4", "0.7", "0.0"]]
    assert all(row[-1] == 0 for row in exact)
    cmap = LinearSegmentedColormap.from_list(
        "tum_blue", ["#F3F7FA", "#98C6EA", "#64A0C8", "#0065BD", "#003359"])
    fig = plt.figure(figsize=(141.6 / 25.4, 3.60))
    ax = fig.add_axes([.230, .330, .755, .560])
    im = ax.pcolormesh(np.arange(6)-.5, np.arange(8)-.5, losses,
                       cmap=cmap, vmin=0, vmax=85, shading="flat",
                       rasterized=False)
    ax.set_xlim(-.5, 4.5)
    ax.set_ylim(6.5, -.5)
    headers = ["Adversarial\ntraining", "Top\nautoencoder", "Middle\nautoencoder",
               "Prediction\nsimilarity", "Activation\ndetector"]
    ax.set_xticks(np.arange(5), headers)
    ax.xaxis.tick_top()
    ax.tick_params(axis="x", length=0, pad=7)
    ax.set_yticks(np.arange(7), LABELS)
    ax.tick_params(axis="y", length=0, pad=6)
    ax.set_xticks(np.arange(-.5, 5, 1), minor=True)
    ax.set_yticks(np.arange(-.5, 7, 1), minor=True)
    ax.grid(which="minor", color="white", linewidth=.7)
    ax.tick_params(which="minor", length=0)
    for split in [2.5, 4.5]:
        ax.axhline(split, color="white", linewidth=3)
    for spine in ax.spines.values():
        spine.set_visible(False)
    for i, row in enumerate(exact):
        for j, value in enumerate(row):
            ax.text(j, i, f"{value:.1f}", ha="center", va="center",
                    fontsize=7.5, color="white" if value >= 45 else "#003359")
    # A separately labelled baseline strip makes low loss distinguishable
    # from high absolute accuracy without blending the two measurements.
    ax.text(-.025, -.12, "Clean accuracy (%)", transform=ax.transAxes,
            ha="right", va="center", fontsize=6.7)
    for j, col in enumerate(columns):
        value = Decimal(col["clean_accuracy"]) * 100
        ax.text((j+.5)/5, -.12, f"{value:.1f}", transform=ax.transAxes,
                ha="center", va="center", fontsize=7.2)
    cax = fig.add_axes([.360, .170, .490, .030])
    cb = fig.colorbar(im, cax=cax, orientation="horizontal", ticks=[0, 20, 40, 60, 80])
    cb.solids.set_rasterized(False)
    cb.solids.set_edgecolor("face")
    cb.outline.set_visible(False)
    cb.ax.tick_params(length=2, width=.4, labelsize=6.5)
    cb.set_label("Accuracy loss from each defence's clean baseline (percentage points)",
                 fontsize=6.7, labelpad=4)
    fig.text(.230, .020, "Reported attack settings are not established as matched or fully specified.",
             fontsize=6.5, color="#666666", ha="left")
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(OUTPUT, metadata={"CreationDate": None, "ModDate": None,
                                "Title": "Accuracy losses from SPARTA D7.6 Table 2"})
    if args.preview_dir:
        args.preview_dir.mkdir(parents=True, exist_ok=True)
        fig.savefig(args.preview_dir / (OUTPUT.stem + ".png"), dpi=200)
    plt.close(fig)
    for name, row in zip(ORDER, exact):
        print(f"{name}: " + ", ".join(f"{v:.1f}" for v in row) + " pp")
    print(f"Wrote {OUTPUT}")


if __name__ == "__main__":
    main()
