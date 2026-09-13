---
id: T-006
title: Insert the author's five Chapter 5 figures
status: review
priority: P1
chapter: 5
owner: claude
depends_on: []
blocks: []
tags: []
created: 2026-09-11
updated: 2026-09-11
---

## Goal

Replace Figures 5.1 and 5.2 with the five figures the author supplied in ~/Downloads/chapter5, with captions from his brief (Chapter-5-refinements.md) corrected where they conflict with the chapter, and add supporting text only where the chapter lacks it.

## Why it matters

The two TikZ diagrams were schematic: a six-box pipeline, and one six-method call graph carrying
one hyperedge of each family. The author's figures draw Stages 3 and 4 in full, the class
structure of both corpora, and the four task and corpus combinations of the results, which the
chapter otherwise shows only as tables. After T-005 the chapter disputes the Macro-F1 label and
several conventions of the source, so the numbers and captions of the new figures have to agree
with it.

## Acceptance criteria

- [x] Former Figures 5.1 and 5.2 (TikZ pipeline and hyperedge diagram) removed; no reference to
      `fig:hgann:pipeline` or `fig:hgann:hyperedges` remains anywhere in `content/`.
- [x] Five supplied PDFs copied verbatim to `figures/hgann-mal/supplied/` (SHA-256 identical to
      the received files); the thesis includes `pdfcrop` copies whose content is unchanged.
- [x] Each figure sits beside the text it illustrates: node features in 5.6, hyperedge generation
      in 5.7, class distribution in 5.9, F1 and accuracy in 5.10.
- [x] Every number in the three data figures checked against Tables 5.3 to 5.6
      (`figures/src/hgann-mal-figure-check.py`: 50 pass, 0 fail, 2 notes on in-figure labels).
- [x] Captions taken from the brief and corrected where they conflict with the chapter (table
      below); descriptions used only where the chapter lacked the point.
- [x] Supporting text added only where missing: stage numbering (5.1, 5.4, 5.5); block labels and
      F = |O| + 328 (5.6); source list names and the panel 4B test (5.7); the excluded families,
      the CICMalDroid balance and the test-sample count (5.9); the cross-task accuracy step (5.10);
      the ranking of the F1 margins (5.12).
- [x] Strict audit passes; `latexmk` clean; PDFs identical; log read.
- [x] Author re-exports swapped in: F1 figure (CICMalDroid task label) and class-distribution
      figure (33.7 per cent), each cropped to the same page box as before.
- [x] Dataset Tables 5.3 and 5.4 cut at the author's request (D-048); their references point to
      Figure 5.3, whose caption takes over the citation and the role of Benign.
- [ ] In-figure points 1 to 5 of `figures/hgann-mal/README.md`, left to the author (new export or
      confirmation).
- [ ] Compiled-page visual review, left to the author under the project rules.
