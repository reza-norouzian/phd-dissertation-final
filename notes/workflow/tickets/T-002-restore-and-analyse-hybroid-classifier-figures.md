---
id: T-002
title: Restore and analyse Hybroid classifier figures
status: review
priority: P0
chapter: 4
owner: claude
depends_on: []
blocks: []
tags: []
created: 2026-08-20
updated: 2026-08-20
---

## Goal

Restore the classifier and ROC figures from Hybroid Section 3.5, revise the Chapter 4 results narrative, and keep all result claims within the evidence of norouzian2021hybroid.

## Why it matters

Chapter 4 preserves the point values from Hybroid Section 3.5 in tables but contains no
results figure. The slash-separated modality values obscure the comparison that answers RQ2,
and the ROC curves have been reduced to scalar AUC values.

## Acceptance criteria

- [x] Reserve prominent, self-contained placeholders for the author to replace with the final
      detection and categorisation classifier figures.
- [x] Reproduce the detection and per-class categorisation ROC plots from the published vector
      content.
- [x] Retain the baseline table and add a compact comparison of fusion against the better
      single modality.
- [x] Correct the interpretation of ties, rounded metrics, fusion effects and absent fold-level
      dispersion without adding claims beyond the paper.
- [x] Cite `norouzian2021hybroid` for every inserted result figure and for the revised result claims.
- [x] Run the strict Chapter 4 reference audit and compile `thesis.tex`; inspect the log for new
      warnings. Visual review remains with the author.