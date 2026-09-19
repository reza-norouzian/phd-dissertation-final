---
id: T-003
title: Revise Chapter 6 evaluation methods, mathematical analysis and figures
status: review
priority: P0
chapter: 6
owner: claude
depends_on: []
blocks: []
tags: []
created: 2026-09-10
updated: 2026-09-19
---

## Goal

Implement the approved evidence-based Chapter 6 revision, preserve original SPARTA figures, correct unsupported inferences, and add mathematical analyses and attributed PDF-malware context.

## Why it matters

The current chapter confuses equal aggregate accuracy with constant predictions and treats
always-active binary label reversal as a majority-class classifier. It also omits source
measurements and gives little space to the mechanics of the evaluated defences. D-041
authorises an evidence-based revision with original report figures and explicit mathematics.

## Evidence for the Section 6.2 revision

- `sparta2021d71`: Sections 3.3.2--3.3.6 define affected ML assets, attack tactics and
  attacker knowledge. Full text inspected; reference-vault status `have`.
- `sparta2021d73`: Section 3.3 defines the contest objectives for face re-identification and
  facial-attribute alteration. Full text inspected; reference-vault status `have`.
- `sparta2022d76`: Section 3.1.3 reports clean and perturbed classification accuracy for the
  histopathology benchmark. Full text inspected; reference-vault status `have`.

## Acceptance criteria

- [x] Revise 6.4-6.11 and align 6.1-6.3 and the introduction with the corrected contribution.
- [x] Define threat constraints, task-specific accuracy and attack success, and suite aggregation.
- [x] Derive delta cancellation, constant-predictor invariance, detector reversal and logit-threshold invariance.
- [x] Explain defence compositions and the 171-feature activation detector from D7.2.
- [x] Include four report figures (one from original assets, and Figures 6.1 to 6.3 redrawn after their originals under D-042 and D-043) and two plots of published values.
- [x] Restore the worst-perturbed contest column and retain unresolved task/submission discrepancies.
- [x] Include one short, attributed PDF-malware comparison using D7.5 Figure 15.
- [x] Document the versioned raw-versus-clipped code finding without asserting historical causality.
- [x] Recompute numerical differences and check the mathematical identities and image provenance.
- [x] Pass strict reference audits, build with latexmk, compare the two PDFs and inspect new log warnings.
- [x] Update current source records and planning state; leave all changes unstaged and visual review to the author.
- 2026-09-19 review -> in-progress (Author approved the concise Section 6.2 replacement and removal of the source-correction paragraph)
- 2026-09-19 in-progress -> review (Approved concise Section 6.2 applied; strict audit and compile pass, PDFs identical)
- 2026-09-19 review -> in-progress (Replace the Chapter 6 title throughout the thesis and planning records at the author's request)
- 2026-09-19 in-progress -> review (Chapter 6 title replaced throughout the thesis; strict audit and compile pass, PDFs identical)
