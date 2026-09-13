---
id: T-007
title: Draft Chapter 8 Conclusion and Future Work
status: review
priority: P1
chapter: 8
owner: claude
depends_on: []
blocks: []
tags: [writing]
created: 2026-09-12
updated: 2026-09-12
---

## Goal

At most two pages: answer RQ1-RQ4 in the macro wording (D-002), close G1-G4 by \gapref with the extent of closure, summarise contributions, state limitations and future work (HGANN-Mal ablation first, as Section 5.15 promises), written from the current text of Chapters 1-7, no new citations.

## Why it matters

Chapter 8 is where Section 1.3 promises that each research question is answered in the words in
which it was asked, and where Section 1.6 promises that what remains open is stated. D-002, D-030
and D-034 require the questions to be typeset from dissertationmacros.tex. The skeleton comment
requires each answer to name its gap of Section 2.7 and to say how far it closes it, without
reprinting the gap. Section 5.15 states that Chapter 8 records the HGANN-Mal ablation as the first
item of future work. On 12 September 2026 the author limited the chapter to two pages, against a
five-page target in structure v0.3. The earlier ticket (old T-024) was lost in the tracker reset.

## Acceptance criteria

- [x] Three sections, Answers, Summary of Contributions and Future Work (`sec:conclusion:1` to `sec:conclusion:3`); the Limitations section of structure v0.3 is removed at the author's instruction (D-052).
- [x] At most two pages: Chapter 8 on pp. 121-122, References still from p. 123.
- [x] Every research question typeset from its macro (D-002, D-030, D-034); none retyped.
- [x] Each answer names its gap with `\gapref` and states how far it is closed; no gap wording reprinted.
- [x] Every restated number matches the current chapter text and its source; no new empirical number.
- [x] The HGANN-Mal ablation is the first future-work item (Section 5.15).
- [x] Attribution consistent with D-017 and D-035, D-025, D-029, D-031, D-032; nothing removed under D-036 or D-040 reappears.
- [x] No citation added; strict audit of content/conclusion.tex passes.
- [x] No statement that details are unrecorded or that work cannot be reproduced (author's instruction, 11 September 2026).
- [x] latexmk succeeds, the two PDFs are identical under cmp, and the log is read for new warnings.
- [x] British spelling (D-001), no em dashes.
- [x] No limitation statements anywhere in the chapter (author's instruction, 12 September 2026, D-052); the freed space extends Section 8.2.
