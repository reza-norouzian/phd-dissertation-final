---
id: T-034
title: Move the anomaly-detection chapter after the Android chapters and renumber the research questions
status: done
priority: P1
chapter: -
owner: claude
depends_on: []
blocks: []
tags: []
created: 2026-09-23
updated: 2026-09-23
---

## Goal

Apply D-009: Android chapters become Chapters 3 and 4, anomaly detection Chapter 5; RQ and gap order follows; reorder Introduction, Background, Discussion, Conclusion and abstracts with minimal wording changes; rebuild the PDF.

## Why it matters

The Android publications carry the main contribution. Placing them first, with the questions,
gaps and all summaries in the same order, lets a reader follow the thesis from start to end
without the numbering jumping between RQ2, RQ3 and RQ1.

## Acceptance criteria

- [x] `thesis.tex` inputs Hybroid (3), HGANN-Mal (4), anomaly detection (5); Chapters 6-8 unchanged.
- [x] Question macros renumbered (rqOne = Hybroid, rqTwo = HGANN-Mal, rqThree/rqThreeOne/rqThreeTwo = anomaly); wording unchanged.
- [x] Introduction: problem-statement RQ numbers, RQ boxes and lead-in, publication table, individual-contribution paragraphs, structure paragraph and RQ map table follow the new order.
- [x] Background: gaps reordered and relabelled (G1 Hybroid, G2 HGANN-Mal, G3 network/process, G4 unchanged); decision-unit table rows and metric-scope reference follow the new order.
- [x] Chapters 3-5: RQ and gap numbers in framing, limitations and summaries renumbered.
- [x] Discussion 7.1 and 7.3 paragraphs follow the chapter order; chapter range updated.
- [x] Conclusion answers ordered RQ1, RQ2, RQ3 (3.1, 3.2), RQ4 with matching gaps.
- [x] Abstract and Kurzfassung: Android paragraph precedes the IoT/industrial paragraph.
- [x] Structure v0.3 updated (D-009 note, RQ section, page plan, chapter outline, current-state statements).
- [x] Strict citation audits pass; clean isolated latexmk build installed as the tracked PDF.

## Evidence and sources

- No citation, claim, number or method description is added; existing text is reordered and
  renumbered. Wording changes are limited to the RQ lead-in (two sentences), one pronoun in the
  individual-contribution paragraphs ("He" -> "The candidate"), and "come first and" in the
  structure paragraph.
- Strict `refcheck.py audit` passes for all eight edited chapter files.

## Log

- 2026-09-23 created
- 2026-09-23 backlog -> in-progress (Author requested the reorder in chat (D-009))
- 2026-09-23 in-progress -> review (Reorder and renumbering applied end to end; audits and isolated 151-page build pass; visual review left to the author)
