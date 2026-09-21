# HGANN-Mal figures for Chapter 5

The five figures in Chapter 5 began as the author's own PDF files, supplied on 11 September 2026
with a brief that gives a caption and description for each. He drew them as HTML and printed them
from Chrome with TUM Neue Helvetica embedded. The four unchanged figures still require a new
author export for content revisions. On 21 September 2026, T-032 replaced the included F1 chart
with a thesis-native vector reproduction because five corrected metrics made the supplied chart
stale. The author-supplied F1 PDF remains unchanged in `supplied/`.

## Files

`supplied/` holds the files exactly as received. Four thesis assets are cropped copies whose
content differs only in the page box. The F1 asset is generated from
`figures/src/hgann-mal-f1.tex` and carries the corrected five-run means.

| Thesis asset | Supplied file | Figure and placement |
|---|---|---|
| `hgann-mal-node-features.pdf` | `fig5-pipline-stage-3.pdf` | 5.1, Stage 3; Section 5.6, landscape page |
| `hgann-mal-hyperedge-generation.pdf` | `fig4-pipeline-stage-4.pdf` | 5.2, Stage 4; Section 5.7, landscape page |
| `hgann-mal-class-distribution.pdf` | `hgann-mal-class-distribution_new.pdf` | 5.3; Section 5.9, text width |
| `hgann-mal-f1.pdf` | `figures/src/hgann-mal-f1.tex`; original: `hgann-mal-f1_new.pdf` | 5.4; Section 5.10, text width |
| `hgann-mal-accuracy.pdf` | `fig3-acc-dif.pdf` | 5.5; Section 5.10, landscape page |

SHA-256 of the supplied files, identical to the files received:

```
6a4a970219eec46d00f4f064215a2024061b34481f3e680693ab97ec4166cad3  fig3-acc-dif.pdf
07c93480f9758cea0742e31fa725605af581c3cdefa2a94c97addcd85e5d3773  fig4-pipeline-stage-4.pdf
4f734fd7e562b9b22fa6378a9f5a07b9a6c41951e18673614bdd81676a099e9b  fig5-pipline-stage-3.pdf
87aacdc2f859b5246ede5aeb09d804866bcd6039c96591b15b43d6bd73165d42  hgann-mal-class-distribution_new.pdf
6f20680a7066ad1815f4e1a7e5ed091e7fb209140df40fc3982d7f29c679f79e  hgann-mal-f1_new.pdf
```

The two `_new` files are the author's re-exports of 11 September 2026. `hgann-mal-f1_new.pdf`
corrects the CICMalDroid task label and replaces `fig2-hgann-mal-macro-f1.pdf` (SHA-256
`e6227e89...44b2`). `hgann-mal-class-distribution_new.pdf` prints SMS malware as 33.7 per cent
and replaces `fig1-hgann-mal-dataset-dist.pdf` (SHA-256 `b87de627...bce3`). The originals remain
in the author's download folder.

The corrected thesis-native F1 asset has SHA-256
`8c8c4f5c6a92565e5458a33e039c86bce129fe01878a01e413163a579b06d06d`. Its source records every
bar value and the four differences from the strongest baseline.

After a new export, replace the file in `supplied/` and crop it again from this directory:

```sh
pdfcrop --margins 1 supplied/fig5-pipline-stage-3.pdf hgann-mal-node-features.pdf
pdfcrop --margins 1 supplied/fig4-pipeline-stage-4.pdf hgann-mal-hyperedge-generation.pdf
pdfcrop --margins 1 supplied/hgann-mal-class-distribution_new.pdf hgann-mal-class-distribution.pdf
pdfcrop --margins 1 supplied/fig3-acc-dif.pdf hgann-mal-accuracy.pdf
pdflatex -interaction=nonstopmode -halt-on-error -output-directory=tmp/pdfs/hgann-f1 figures/src/hgann-mal-f1.tex
cp tmp/pdfs/hgann-f1/hgann-mal-f1.pdf figures/hgann-mal/hgann-mal-f1.pdf
```

## Placement and type size

The text block is 402.6 pt wide and 681.4 pt high (141.6 mm by 239.7 mm). The table gives the size
at which the text of each figure prints, measured from the font sizes in the PDF.

| Figure | Placed at | Scale | Body text | Smallest text | Body text at text width |
|---|---|---|---|---|---|
| 5.1 node features | text height, landscape | 0.54 | 5.3 pt | 4.0 pt | 3.1 pt |
| 5.2 hyperedge generation | text height, landscape | 0.56 | 5.9 pt | 3.0 pt | 3.5 pt |
| 5.3 class distribution | text width | 0.93 | 6.6 pt | 6.0 pt | 6.6 pt |
| 5.4 F1 | text width | 1.00 | 6.2 pt | 5.8 pt | 6.2 pt |
| 5.5 accuracy | text height, landscape | 0.79 | 8.2 pt | 7.0 pt | 4.8 pt |

Figures 5.1, 5.2 and 5.5 are set as `sidewaysfigure`, as the IUNO test environment is in
Chapter 3, because at text width their body text would print at 3 to 5 pt. Figures 5.1 and 5.2
remain small on a landscape page. A new export with larger type, or with a narrower canvas at the
same type size, would correct that; the thesis-native figures print their labels at 7 to 9 pt.

## Captions

The captions come from the author's brief. Where the brief conflicts with the chapter, the
caption follows the chapter, and T-006 records each change and its reason.

On 21 September 2026 the author confirmed that all learned-model scores are means over five
training runs with different seeds on fixed partitions, including all four baselines. T-032
updates the captions of the F1 and accuracy figures to state this aggregation. The corrected F1
asset replaces five stale values and changes the Drebin family gain from 1.9 to 1.6 points.
Individual run scores remain unavailable, so the figures do not show uncertainty across seeds.
The supplied Drebin binary confusion-matrix summaries reproduce the corrected macro rows.

## Open points inside the figures

These points were found when the figures were checked against the chapter. Resolved items remain
as provenance; unresolved items need a new author export or a decision.

1. Resolved on 11 September 2026. The original F1 chart, panel (b), labelled the CICMalDroid
   multiclass task "Family classification" and its gain "fam."; the re-export
   `hgann-mal-f1_new.pdf` reads "Category classification" and "cat.".
2. Resolved on 11 September 2026. `hgann-mal-class-distribution.pdf`, panel (b), printed SMS
   malware as 33.6 per cent, as the source publication's table does, against the 33.7 of the
   chapter's majority baseline (3,904 of 11,598 is 33.66 per cent); the re-export
   `hgann-mal-class-distribution_new.pdf` prints 33.7.
3. `hgann-mal-hyperedge-generation.pdf`: the sidebar calls the code2vec embeddings E, which is
   also the edge set of G = (V, E); the chapter writes c_v. Panel 4B labels the similarity as a
   cosine ("cos sim = τ = 0.80"); the author confirmed this on 11 September 2026, together with a
   search within one application, and Section 5.7 now states both. The brief's caption said that
   4A and 4C draw the same call graph; they do not, and the sentence was left out.
4. Resolved on 11 September 2026. `hgann-mal-node-features.pdf` says that the embedding comes
   from "the decompiled method, encoded by a pre-trained code2vec model". The author confirmed
   this (decompilation to Java with Androguard's DAD, a ready-made code2vec model), and
   Section 5.6 now states it. At his request the 320-dimensional width is not explained; the
   chapter keeps its remark that the width differs from that of the released model.
5. `hgann-mal-f1.pdf` and `hgann-mal-accuracy.pdf` use the source publication's name HGNNP. The
   chapter says HGNN+, and both captions give the mapping.

Both procedures were confirmed by the author on 11 September 2026 (D-049), and the matching
pending markers in Sections 5.6 and 5.7 are resolved.

## Checks

`figures/src/hgann-mal-figure-check.py` extracts the text of the included F1 asset and the two
author-supplied data figures with `pdftotext`. It compares every printed number with the result
tables of `content/hgann-mal.tex`
(`tab:hgann:binary`, `tab:hgann:multi`) and with the two dataset tables of the source
publication, which the chapter reprinted until T-006 cut them. A problem inside a figure is
printed as a note and does not fail the check. Run it from the repository
root:

```sh
python3 figures/src/hgann-mal-figure-check.py
```
