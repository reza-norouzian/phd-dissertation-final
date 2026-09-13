#!/usr/bin/env python3
"""
Feature-importance figure for the 63-field NADICS extraction schema.

Composition follows the convention used in applied ML papers: a ranked
horizontal bar panel for the individual fields, a share-versus-size panel
that shows which groups pay for themselves, and a cumulative (Pareto) panel
that shows how concentrated the ranking is.

Sized to the thesis text width (141.6 mm) so it can be dropped in at 1:1.
Palette is the TUM Corporate Design print ramp already used by
figures/src/tum-dotplot.tex: a single-hue lightness ramp, so the figure
survives greyscale printing and red-green colour deficiency.
"""

import json
import pathlib

import matplotlib as mpl
mpl.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Patch

HERE = pathlib.Path(__file__).parent
DATA = json.loads((HERE / "nadics-feature-importance.json").read_text())

# ----------------------------------------------------------------- style ----
TEXTWIDTH_IN = 141.6 / 25.4          # thesis \textwidth
FIG_H_IN = 4.50
GROUPS = ["A", "B", "C", "D", "E"]
COLOR = {                            # TUM CD print ramp, dark -> light
    "A": "#003359",                  # TUM Blau dunkel 2
    "B": "#005293",                  # TUM Blau dunkel 1
    "C": "#0065BD",                  # TUM Blau, Pantone 300 C, at 100 %
    "D": "#64A0C8",                  # Akzent Pantone 542
    "E": "#98C6EA",                  # Akzent Pantone 283
}
GREY_XL, GREY_L, GREY_M, GREY_D = "#E4E4E2", "#CCCCCC", "#808080", "#333333"

mpl.rcParams.update({
    "font.family": "sans-serif",
    "font.sans-serif": ["Helvetica", "Arial", "DejaVu Sans"],
    "font.monospace": ["Menlo", "DejaVu Sans Mono"],
    "font.size": 7.0,
    "axes.labelsize": 7.0,
    "xtick.labelsize": 6.5,
    "ytick.labelsize": 6.5,
    "axes.edgecolor": GREY_M,
    "axes.linewidth": 0.5,
    "xtick.major.width": 0.5,
    "ytick.major.width": 0.5,
    "xtick.color": GREY_M,
    "ytick.color": GREY_M,
    "text.color": GREY_D,
    "axes.labelcolor": GREY_D,
    "pdf.fonttype": 42,
    "svg.fonttype": "none",
    "figure.dpi": 110,
})

feats = sorted(DATA["features"], key=lambda f: f["rank"])
gshare = DATA["group_importance_percent"]
gname = DATA["group_names"]
gcount = DATA["group_field_counts"]
N_TOP = 15

fig = plt.figure(figsize=(TEXTWIDTH_IN, FIG_H_IN))
# Two grids, because panel (a) needs a wide label gutter and the bottom row
# does not; one shared `left` would waste a third of the bottom row.
gs_top = fig.add_gridspec(1, 1, left=0.278, right=0.988, top=0.960, bottom=0.487)
gs_bot = fig.add_gridspec(1, 2, left=0.088, right=0.988, top=0.363, bottom=0.098,
                          wspace=0.34)
ax_a = fig.add_subplot(gs_top[0, 0])
ax_b = fig.add_subplot(gs_bot[0, 0])
ax_c = fig.add_subplot(gs_bot[0, 1])


def strip(ax, keep=("bottom",)):
    for side in ("top", "right", "left", "bottom"):
        ax.spines[side].set_visible(side in keep)


# ------------------------------------------- (a) ranked feature importance --
top = feats[:N_TOP]
y = np.arange(len(top))[::-1]
vals = [f["importance_percent"] for f in top]

ax_a.barh(y, vals, height=0.66, color=[COLOR[f["group"]] for f in top], zorder=3)
for yi, v in zip(y, vals):
    ax_a.text(v + 0.14, yi, f"{v:.2f}", va="center", ha="left",
              fontsize=6.2, color=GREY_D, zorder=4)

ax_a.set_yticks(y)
# Monospace plus a constant character count: right-aligning equal-width labels
# lines the identifiers up in their own column and left-aligns the names.
_w = max(len(f["feature"]) for f in top)
ax_a.set_yticklabels(
    [f"{f['feature_id']:>3s}  {f['feature']:<{_w}s}" for f in top],
    family="monospace", fontsize=6.4, color=GREY_D)
ax_a.tick_params(axis="y", pad=0)
ax_a.set_xlim(0, max(vals) * 1.14)
ax_a.set_ylim(-0.7, len(top) - 0.3)
ax_a.set_xlabel("Assigned importance (per cent of total)", labelpad=3)
ax_a.xaxis.grid(True, color=GREY_L, linewidth=0.4, zorder=0)
ax_a.set_axisbelow(True)
strip(ax_a)
ax_a.tick_params(axis="y", length=0)

ax_a.legend(
    handles=[Patch(facecolor=COLOR[g], label=f"{g}   {gname[g]}") for g in GROUPS],
    loc="lower right", bbox_to_anchor=(1.0, 0.115), frameon=False, fontsize=6.3,
    handlelength=1.1, handleheight=0.85, labelspacing=0.32, borderpad=0.0,
)
ax_a.text(0.998, 0.018,
          f"top {N_TOP} of 63 fields carry {sum(vals):.1f} per cent",
          transform=ax_a.transAxes, ha="right", va="bottom",
          fontsize=6.2, color=GREY_M, style="italic")

# --------------------------------------------- (b) group share versus size --
x = np.arange(len(GROUPS))
imp = [gshare[g] for g in GROUPS]
size = [gcount[g] / 63 * 100 for g in GROUPS]
w = 0.36

ax_b.bar(x - w / 2, imp, w, color=[COLOR[g] for g in GROUPS], zorder=3)
ax_b.bar(x + w / 2, size, w, color=GREY_XL, edgecolor=GREY_M, linewidth=0.5,
         zorder=3)

for xi, (a, b) in enumerate(zip(imp, size)):
    ax_b.text(xi - w / 2, a + 1.0, f"{a:.1f}", ha="center", va="bottom",
              fontsize=5.9, color=GREY_D)
    ax_b.text(xi + w / 2, b + 1.0, f"{b:.1f}", ha="center", va="bottom",
              fontsize=5.9, color=GREY_M)

ax_b.set_xticks(x)
ax_b.set_xticklabels(GROUPS)
ax_b.set_ylim(0, 51)
ax_b.set_yticks([0, 10, 20, 30, 40])
ax_b.set_ylabel("Per cent", labelpad=2)
ax_b.set_xlabel("Feature group", labelpad=2)
ax_b.yaxis.grid(True, color=GREY_L, linewidth=0.4, zorder=0)
ax_b.set_axisbelow(True)
strip(ax_b)
ax_b.legend(
    handles=[Patch(facecolor=COLOR["C"], label="share of importance"),
             Patch(facecolor=GREY_XL, edgecolor=GREY_M, linewidth=0.5,
                   label="share of fields")],
    loc="upper left", bbox_to_anchor=(-0.02, 1.04), frameon=False, fontsize=5.9,
    handlelength=1.0, handleheight=0.8, labelspacing=0.22, borderpad=0.0,
)

# --------------------------------------------------- (c) cumulative share --
allv = np.array([f["importance_percent"] for f in feats])
cum = np.cumsum(allv)
rank = np.arange(1, len(allv) + 1)

ax_c.fill_between(rank, 0, cum, color=COLOR["E"], alpha=0.30, zorder=2,
                  linewidth=0)
ax_c.plot(rank, cum, color=COLOR["C"], linewidth=1.15, zorder=3)

marks = []
for thr in (80, 90):
    k = int(np.searchsorted(cum, thr) + 1)
    marks.append((thr, k))
    ax_c.plot([0, k, k], [thr, thr, 0], color=GREY_M, linewidth=0.45,
              linestyle=(0, (2.2, 1.8)), zorder=4)

k10 = 10
ax_c.plot([k10], [cum[k10 - 1]], marker="o", markersize=2.8,
          markeredgewidth=0, color=COLOR["C"], zorder=5)
ax_c.annotate(f"10 fields\n{cum[k10 - 1]:.1f} per cent",
              xy=(k10, cum[k10 - 1]), xytext=(k10 + 4.5, cum[k10 - 1] - 27),
              fontsize=5.9, color=GREY_D, linespacing=1.3, va="center",
              arrowprops=dict(arrowstyle="-", linewidth=0.45, color=GREY_M,
                              shrinkA=0, shrinkB=2))

ax_c.text(0.985, 0.045,
          "\n".join(f"{t} per cent at {k} fields" for t, k in marks),
          transform=ax_c.transAxes, ha="right", va="bottom",
          fontsize=5.9, color=GREY_M, linespacing=1.35)

ax_c.set_xlim(0, len(allv))
ax_c.set_ylim(0, 104)
ax_c.set_xlabel("Fields, ranked", labelpad=2)
ax_c.set_ylabel("Cumulative per cent", labelpad=2)
ax_c.set_yticks([0, 25, 50, 75, 100])
ax_c.set_xticks([0, 20, 40, 63])
ax_c.yaxis.grid(True, color=GREY_L, linewidth=0.4, zorder=0)
ax_c.set_axisbelow(True)
strip(ax_c)

# ------------------------------------------------------------ panel letters -
for ax, letter, dx, dy in ((ax_a, "a", -106, 3), (ax_b, "b", -32, 3),
                           (ax_c, "c", -32, 3)):
    ax.annotate(f"({letter})", xy=(0, 1), xycoords="axes fraction",
                xytext=(dx, dy), textcoords="offset points",
                ha="left", va="bottom", fontsize=7.6, fontweight="bold",
                color=GREY_D)

out_pdf = HERE / "nadics-feature-importance.pdf"
out_png = HERE / "nadics-feature-importance.png"
fig.savefig(out_pdf)
fig.savefig(out_png, dpi=300)

print(f"group shares sum to {sum(imp):.6f}")
print(f"all 63 sum to       {cum[-1]:.6f}")
print(f"top 10 / 15         {cum[9]:.4f} / {cum[14]:.4f}")
for g in GROUPS:
    print(f"  {g}: {gshare[g]:6.2f} % over {gcount[g]:2d} fields "
          f"-> {gshare[g] / gcount[g]:.3f} % per field")
print(f"wrote {out_pdf.name}, {out_png.name}")
