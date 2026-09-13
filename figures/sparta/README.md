# SPARTA figures for Chapter 6

The original report panels retain their source colours and labels. JPEG files
contain the original embedded DCT streams. PNG files contain the original RGB
samples without resizing. No report plot has been digitised, smoothed or
upscaled. Placement size in LaTeX does not change the native pixel count. Three
report diagrams are redrawn as vector figures for the thesis at the
author's request (see Redrawn diagrams); their raster originals remain here as
the source of record.

## Original panels

All page numbers in the PDF-page column are one-based. The original figure
number and partner attribution belong in the dissertation caption when the
panels are assembled.

| Asset in `report-originals/` | Source figure | Printed / PDF page | Native pixels |
|---|---|---|---|
| `d76-fig02-benchmark-architecture.jpg` | D7.6 Figure 2 | 22 / 29 | 561 x 332 |
| `d72-fig13-input-autoencoder.png` | D7.2 Figure 13 | 14 / 21 | 380 x 210 |
| `d72-fig11-middle-autoencoder.png` | D7.2 Figure 11 | 14 / 21 | 407 x 207 |
| `d72-fig15-prediction-similarity.png` | D7.2 Figure 15 | 16 / 23 | 599 x 205 |
| `d72-fig16-activation-detector.png` | D7.2 Figure 16 | 16 / 23 | 401 x 228 |
| `d75-fig15-iter-fgsm-left.jpg` | D7.5 Figure 15, left | 23 / 34 | 717 x 478 |
| `d75-fig15-iter-fgsm-right.png` | D7.5 Figure 15, right | 23 / 34 | 715 x 477 |

The first five assets no longer enter the thesis directly. They are the
sources of the redrawn Figures 6.1 to 6.3. The two D7.5 panels are placed in
Chapter 6 unchanged.

`report-originals/MANIFEST.tsv` records the PDF source path and SHA256 hash,
original page and figure number, image-object identifier, native dimensions,
extraction method, output-file hash and decoded-pixel hash. Extraction verifies
both the native dimensions and pixel equality. For JPEG images, the script
reads the original `/DCTDecode` stream directly because pypdf's convenience
image extraction can re-encode these images.

Regenerate the assets from the repository root using Python with `pypdf` and
Pillow installed, for example the Codex bundled Python:

```sh
python3 figures/src/sparta-extract-report-figures.py
```

## Redrawn diagrams

Figures 6.1 to 6.3 are TikZ diagrams in the style of the SWaT figures
(`figures/src/swat-figure-style.tex`: TeX Gyre Heros, TUM blue #0065BD,
140 mm wide so that they are placed at 1:1). `figures/src/build.sh` builds them
and installs the PDFs in `thesis/`.

| Thesis asset | Redrawn after | Content added to the original, with its source | Builder |
|---|---|---|---|
| `thesis/sparta-benchmark-architecture.pdf` | D7.6 Figure 2 | One role line per box, paraphrasing D7.6 Section 3.1.1 | `figures/src/sparta-benchmark-architecture.tex` |
| `thesis/sparta-autoencoder-placement.pdf` | D7.2 Figures 13 and 11 | Symbols of Equation `eq:advml:compositions`; a legend separating the autoencoder, trained for the defence, from VGG16 and the DNN, which keep their original weights (D7.2 Section 2.3.2.3.2) | `figures/src/sparta-autoencoder-placement.tex` |
| `thesis/sparta-detector-mechanisms.pdf` | D7.2 Figures 15 and 16 | The six parameters D7.2 records, in place of Parameter 1-4; the 171 activation features and the per-class SVC (D7.2 Sections 2.3.2.3.3-2.3.2.3.4); the label-reversal response of D7.6 p. 28; the chapter's symbols and a legend | `figures/src/sparta-detector-mechanisms.tex` |

Box labels follow the originals, apart from the spellings scikit-learn and
Third-party. The five module colours of D7.6 Figure 2 carry no meaning and are
replaced by the brand colour. Figure 6.2 names the variants top and middle, as
D7.6 p. 29 and the benchmark table do. It draws both variants as horizontal
pipelines, so that the swap in position between the autoencoder and VGG16 is
visible directly. Figure 6.3 draws each detector in two lanes, the classifier
above and the detector below, which meet at the response.

## Derived plots

The two plots use `figures/src/sparta-reported-results.json`, which preserves
the numerical tokens as printed in D7.6, together with their source pages and
interpretive limits. Both PDFs contain vector marks and embedded fonts. Their
width is 141.6 mm, matching the existing dissertation plotting convention.

| Thesis asset | Source and content | Builder |
|---|---|---|
| `thesis/sparta-sd-comparison.pdf` | D7.6 Sections 2.8.1.2-2.8.1.3, approximate clean and transfer results | `figures/src/sparta-sd-comparison.py` |
| `thesis/sparta-benchmark-deltas.pdf` | D7.6 Table 2, accuracy loss in percentage points with clean baselines | `figures/src/sparta-benchmark-deltas.py` |

The SD diagram connects clean and transferred performance within each reported
configuration. It has no line between configurations and no fitted trend. The
84-85 interval is a reported range, not a confidence interval. These development
descriptions are not pooled with the differently labelled official contest
table.

The heatmap computes each loss as `100 * (clean accuracy - attacked accuracy)`
using decimal arithmetic before plotting. It uses a linear colour scale and
numerical labels to show small losses near zero. Its row groups are layout
choices, not claims of equal attack budgets. The original table does not
establish matched or fully specified attack configurations.

Regenerate both PDFs from the repository root with the existing figure
environment:

```sh
figures/src/.venv/bin/python figures/src/sparta-sd-comparison.py
figures/src/.venv/bin/python figures/src/sparta-benchmark-deltas.py
```

For optional PNG previews, add `--preview-dir /tmp/sparta-figure-preview` to
either command. Preview images do not enter the tracked figure tree. The
scripts require only the matplotlib and NumPy packages already listed in
`figures/src/requirements.txt`. The PDF metadata omits variable creation and
modification timestamps to permit repeatable regeneration in one environment.

## Checks and limits

Source-image QA verified the original panels against their report identities.
The extraction script checks all seven image objects. The plot builders check
the ranges and dimensions of the data, and the heatmap asserts the PGD losses
and the zero-loss activation-detector column. Reported numerical precision is
retained in the JSON; the heatmap labels use one decimal percentage point.

The original panels have modest intrinsic raster resolution, which a vector PDF
wrapper would not improve. Their labels and wording remain unchanged in
`report-originals/`. The three redrawn diagrams add no measured content. New
curves, uncertainty intervals and reconstructed individual-example statistics
are outside these assets' evidential scope.
