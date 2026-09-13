---
id: T-014
title: Preview redesigns for Figures 2.1 and 2.2
status: review
priority: P2
chapter: 2
owner: codex
depends_on: []
blocks: []
tags: []
created: 2026-09-13
updated: 2026-09-13
---

## Goal

Create two temporary design variants per figure, informed by the source publication diagrams, for author selection before thesis integration.

## Why it matters

The existing APK figure has cramped text and an unconnected hybrid panel. The hypergraph figure repeats the clique projection without visually demonstrating why its inverse is ambiguous.

## Acceptance criteria

- [x] Inspect the current figures and relevant publication diagrams.
- [x] Generate two temporary variants for each figure with the built-in image tool.
- [x] Inspect generated labels, memberships and arrows; record remaining limitations.
- [x] Save previews and prompts separately from the thesis and recommend a design direction.
- [x] Insert the author's selected imagegen variants 2.1 A and 2.2 B, with preview markers clipped and Figure 2.2's caption aligned to its panels.
- [x] Run the strict chapter citation audit and compile; inspect build warnings and confirm identical thesis PDFs.

## Evidence and sources

- Content contract: `content/background.tex`, Figures `fig:background:apk` and `fig:background:hypergraph`; inspected source and compiled pages 29 and 31. No section drafting or new thesis citations are in scope.
- `norouzian2021hybroid`: the original publication Figure 1 (PDF page 3) illustrates separate static/dynamic branches with feature combination. Inspected the figure and surrounding System Design source text. Full text present; vault status `have`, title check `yes`. Used for layout reference only.
- `zhou2006learning`: Figure 1 (PDF page 2) contrasts explicit memberships with pairwise representation. The full eight-page text was inspected. Full text present; vault status `have`, title check `yes`. Supports the existing projection example; retain the thesis six-node sets, not the paper's article example.
- `norouzian2025hgannmal`: inspected the local source and PDF structure. The original presents hyperedge construction as Algorithm 1, rather than a comparable introductory diagram. Full text present; vault status `have`, title check `yes`. The current thesis hyperedge-generation asset was also inspected as a local style reference, not misattributed to the original publication.
- Preserved sets: e1={m1,m2,m3}; e2={m3,m4,m5}; e3={m5,m6}. Seven undirected edges in the clique expansion. Variant B may expose the same membership as a 6x3 incidence matrix without changing the example.
- Integration source record: the revised Figure 2.2 caption uses the existing `zhou2006learning` citation for incidence membership and the loss of group identity under pairwise projection. Its full text was inspected during preview preparation; metadata verification is `doi`, and the reference vault remains `have` with title check `yes`. The pre-edit strict audit passes: 110 cited sources, zero needing attention. No new citations or empirical claims are introduced.

## Log

- 2026-09-13 Inserted stable copies `figures/background-apk-analysis.png` and `figures/background-hypergraph-projection.png`, preserving the selected imagegen raster designs. Top-only LaTeX trims of 115 bp and 42 bp hide the respective preview labels; figures use the text width. Updated Figure 2.2's caption and introductory sentence. Post-edit strict audit passes (110 cited, zero needing attention); latexmk succeeds (159 pages), and both tracked PDFs are identical. No overfull boxes or undefined-reference/citation warnings. Existing template and end-group warnings remain; changed float sizes alter the Chapter 2 underfull-vbox diagnostics. No visual PDF review performed, per repository instructions. All changes remain unstaged.
- 2026-09-13 The author selected the imagegen 2.1 A and 2.2 B previews in this conversation and requested insertion. These selections refer to T-014's saved PNGs; T-015 records a separate canvas with different A/B meanings and remains unchanged. Integrate the approved images as stable chapter assets; preserve original PNGs and clip only the temporary top labels through LaTeX.
- 2026-09-13 Four selected previews saved under `figures/previews/chapter2-2026-09-13/`, with complete prompts and provenance. Refined the graph previews to remove a generated spurious internal edge and make the ambiguity arrows explicit. Recommended A for each figure; B for 2.2 is an alternative if the incidence matrix should be illustrated. Original scientific wording retained; the README records the existing static-coverage overstatement and the surrounding sentence's unsupported description of lifting. No `.tex` files or thesis PDFs edited, so no compile was needed.
- 2026-09-13 created
- 2026-09-13 in-progress -> review (Four inspected imagegen previews and prompt records saved separately for author selection; thesis unchanged)
- 2026-09-13 review -> in-progress (Author selected the imagegen previews 2.1 A and 2.2 B in this task; insert the approved images and adapt panel references)
- 2026-09-13 in-progress -> review (Approved 2.1 A and 2.2 B inserted; caption aligned, strict audit and compile pass, tracked PDFs identical)
