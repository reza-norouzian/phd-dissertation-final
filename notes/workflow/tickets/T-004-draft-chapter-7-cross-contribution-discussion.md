---
id: T-004
title: Draft Chapter 7 Cross-Contribution Discussion
status: review
priority: P1
chapter: 7
owner: claude
depends_on: []
blocks: []
tags: [writing]
created: 2026-09-10
updated: 2026-09-11
---

## Goal

Four pages relating the contributions of Chapters 3 to 6 along the seven sections fixed by the structure plan, written from the current chapter text, conceptual only, with no numerical comparison between Hybroid and HGANN-Mal.

## Why it matters

Chapter 7 is the only place where the four research streams are set against one another.
Chapter 1 promises it in Sections 1.2, 1.4 and 1.6, the Chapter 3 summary names it as a
consequence of the missing transfer evidence, and Chapter 5 promises it in Sections 5.1, 5.3
and 5.15. Section 5.3 cites Section 7.3 by label for a direct comparison of acquisition cost.
On 10 September 2026 the thesis stood at 145 pages against a 150-page ceiling with Chapters 7
and 8 as stubs, and the author fixed the length of this chapter at four pages. The earlier
ticket for this chapter (old T-023, created 13 August 2026) was lost in the tracker reset; its
three acceptance criteria are carried over below.

## Acceptance criteria

- [x] Seven sections under the headings and labels of structure v0.3; `sec:discussion:3` keeps its label because Section 5.3 cites it.
- [ ] At most four pages. (Met by the 10 September draft; the 11 September revision runs to five pages, see log.)
- [x] No numerical comparison between Hybroid and HGANN-Mal, whose protocols differ (old T-023).
- [x] The conceptual comparison is stated as conceptual (old T-023).
- [x] The scope of generalisation is bounded honestly, against the standard of Section 2.6 (old T-023).
- [x] No claim that HGANN-Mal corrects a Hybroid limitation, and no developmental sequence from the IoT work to the Android work (structure v0.3, Section 1.2).
- [x] Every number restated from Chapters 3 to 6 matches the current chapter text and its source; no new empirical number.
- [x] Only keys already cited elsewhere in the thesis; strict audit of content/discussion.tex passes.
- [x] latexmk succeeds, the two PDFs are identical under cmp, and the log is read for new warnings.
- [x] The author's writing rules hold: British spelling (D-001), no em dashes.
