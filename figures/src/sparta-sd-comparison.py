#!/usr/bin/env python3
"""Plot published SD development configurations; no fitted trend or CI.

Default output is the thesis vector PDF. Use --preview-dir for optional PNGs
outside the tracked figure tree. Numeric source tokens reside in the JSON.
"""
import argparse
import json
from decimal import Decimal
from pathlib import Path

import matplotlib as mpl
mpl.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

HERE = Path(__file__).resolve().parent
OUTPUT = HERE.parent / "sparta/thesis/sparta-sd-comparison.pdf"
DATA = json.loads((HERE / "sparta-reported-results.json").read_text())
BLUE, DARK, LIGHT, GREY = "#0065BD", "#003359", "#98C6EA", "#333333"
mpl.rcParams.update({
    "font.family": "sans-serif",
    "font.sans-serif": ["DejaVu Sans"],
    "font.size": 7.5, "axes.labelsize": 7.5,
    "xtick.labelsize": 7, "ytick.labelsize": 7.5,
    "axes.edgecolor": "#808080", "axes.linewidth": .5,
    "text.color": GREY, "axes.labelcolor": GREY,
    "xtick.color": GREY, "ytick.color": GREY,
    "pdf.fonttype": 42, "svg.fonttype": "none",
})


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--preview-dir", type=Path)
    args = parser.parse_args()
    configs = DATA["sd_development"]["configurations"]
    assert len(configs) == 2
    fig, ax = plt.subplots(figsize=(141.6 / 25.4, 2.25))
    fig.subplots_adjust(left=.285, right=.968, bottom=.24, top=.77)
    for y, row in zip([1, 0], configs):
        clean = float(Decimal(row["clean"]))
        low = float(Decimal(row["transfer_lower"]))
        high = float(Decimal(row["transfer_upper"]))
        assert 0 <= low <= high <= clean <= 100
        ax.plot([high, clean], [y, y], color=LIGHT, linewidth=1.2, zorder=2)
        ax.plot(clean, y, "o", color=BLUE, markersize=5, zorder=4)
        ax.annotate("~" + row["clean"], (clean, y), xytext=(0, 8),
                    textcoords="offset points", ha="center", color=BLUE)
        if low == high:
            ax.plot(low, y, "o", markerfacecolor="white", markeredgecolor=DARK,
                    markeredgewidth=1.1, markersize=5, zorder=4)
            label = "~" + row["transfer_lower"]
        else:
            ax.plot([low, high], [y, y], color=DARK, linewidth=2.2, zorder=4)
            for x in [low, high]:
                ax.plot([x, x], [y-.075, y+.075], color=DARK,
                        linewidth=1.0, zorder=4)
            label = row["transfer_lower"] + "-" + row["transfer_upper"]
        ax.annotate(label, ((low+high)/2, y), xytext=(0, 8),
                    textcoords="offset points", ha="center", color=DARK)
    ax.set_xlim(70, 95)
    ax.set_ylim(-.35, 1.55)
    ax.set_xticks([70, 75, 80, 85, 90, 95])
    ax.set_xlabel("Reported accuracy (%)", labelpad=4)
    ax.set_yticks([1, 0], ["Second configuration", "Third configuration"])
    ax.tick_params(axis="y", length=0, pad=8)
    ax.tick_params(axis="x", length=3, width=.5)
    ax.xaxis.grid(True, color="#E4E4E2", linewidth=.6, zorder=0)
    ax.set_axisbelow(True)
    for side in ["top", "right", "left"]:
        ax.spines[side].set_visible(False)
    fig.legend(handles=[
        Line2D([], [], marker="o", linestyle="none", color=BLUE,
               markersize=4.5, label="Clean images"),
        Line2D([], [], marker="o", linestyle="none", markerfacecolor="white",
               markeredgecolor=DARK, markersize=4.5, label="Transferred attacks"),
        Line2D([], [], color=DARK, linewidth=2, marker="|", markersize=6,
               label="Reported range"),
    ], loc="upper center", bbox_to_anchor=(.54, .98), ncols=3,
       frameon=False, fontsize=7, handlelength=1.2, columnspacing=1.5)
    fig.text(.285, .035, "Approximate published values; range is not a confidence interval.",
             fontsize=6.7, color="#666666", ha="left")
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(OUTPUT, metadata={"CreationDate": None, "ModDate": None,
                                "Title": "Reported SD development configurations"})
    if args.preview_dir:
        args.preview_dir.mkdir(parents=True, exist_ok=True)
        fig.savefig(args.preview_dir / (OUTPUT.stem + ".png"), dpi=200)
    plt.close(fig)
    print(f"Wrote {OUTPUT}")


if __name__ == "__main__":
    main()
