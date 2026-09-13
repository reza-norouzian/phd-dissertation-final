# Figures

Place dissertation figures in this directory. Use descriptive filenames and prefer vector PDF
files for diagrams and plots when possible. `figures/` and `assets/` are both on
`\graphicspath`, so a figure here is included by filename alone.

## Thesis-native figures

Figures generated from source inside this repository live in `figures/src/`, and their built
PDFs are copied one level up by `figures/src/build.sh`. Run it from that directory:

```sh
cd figures/src && sh build.sh
```

Two toolchains are in use.

**TikZ.** `hybroid-detection-classifiers.tex` and `hybroid-categorisation-classifiers.tex`
(Chapter 4, Figures 4.7 and 4.8) share the style in `tum-dotplot.tex`, which documents the TUM
Corporate Design print palette and the geometry that makes the figures land at 1:1 on the page.
They are built with `pdflatex`.

**matplotlib.** `nadics-feature-importance.py` (Chapter 3, Figure 3.4) reads its data from
`nadics-feature-importance.json` and writes both a vector PDF for the thesis and a
screen-resolution PNG for review. It needs matplotlib, which is not part of the LaTeX
toolchain, so `build.sh` creates `figures/src/.venv` from `requirements.txt` on first run and
reuses it afterwards. The environment and the PNG are git-ignored; the PDF is tracked.

To regenerate that figure alone, after `build.sh` has created the environment once:

```sh
cd figures/src && .venv/bin/python nadics-feature-importance.py && cp nadics-feature-importance.pdf ../
```

The JSON is the figure's input of record. Editing it and re-running the script is the supported
way to change the figure; the PDF is never edited by hand.

## SWaT figures

`swat/` preserves the supplied context PDFs and screenshots, together with eight original
images extracted from the GAN report. Section 3.5 uses the original reconstruction and
detection plots. Its three context diagrams are corrected vector adaptations built from
`src/swat-ics-architecture.tex`, `src/swat-attack-taxonomy.tex`, and
`src/swat-collection-campaign.tex`, sharing `src/swat-figure-style.tex`. The GAN pipeline
(Figure 3.8) is a thesis-native diagram in `src/swat-gan-pipeline.tex`. It uses the same style,
adds the TUM accent orange #E37222 for the tags that mark use of attack ground truth, and is laid out in
millimetres at 140 mm width. `src/build.sh` installs all four PDFs in `swat/thesis/`. Captions
and numbering are supplied by the chapter, rather than embedded in the diagrams. See
`swat/README.md` for provenance.

## SPARTA figures

`sparta/report-originals/` preserves seven native image panels from D7.2, D7.5 and
D7.6. Three of the diagrams are redrawn for the thesis in the style of the SWaT figures:
the benchmark architecture (Figure 6.1, after D7.6 Figure 2) in
`src/sparta-benchmark-architecture.tex`, the autoencoder placement (Figure 6.2, after
D7.2 Figures 13 and 11) in `src/sparta-autoencoder-placement.tex`, and the detection
mechanisms (Figure 6.3, after D7.2 Figures 15 and 16) in
`src/sparta-detector-mechanisms.tex`. Their raster originals remain the source of
record. The two D7.5 panels enter Chapter 6 unchanged, in one figure, without redrawing
or resampling. The chapter's two analytical plots are generated from the reported
values in `src/sparta-reported-results.json`. `src/build.sh` installs all five vector
PDFs in `sparta/thesis/`. See `sparta/README.md` for extraction, source hashes and
regeneration commands.

## HGANN-Mal figures

`hgann-mal/` holds the five Chapter 5 figures. They are the author's own, supplied as PDF on
11 September 2026 and kept verbatim in `hgann-mal/supplied/`. The thesis includes copies cropped
to the drawing with `pdfcrop`, and three of them are set on landscape pages. They have no source
in this repository and are not built by `src/build.sh`; `src/hgann-mal-figure-check.py` checks
their numbers against the chapter's result tables and the source publication. See `hgann-mal/README.md` for hashes, placement, type
sizes and the open points inside the figures.
