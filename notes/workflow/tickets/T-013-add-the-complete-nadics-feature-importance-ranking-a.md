---
id: T-013
title: Add the complete NADICS feature-importance ranking as Appendix A
status: review
priority: P2
chapter: 3
owner: claude
depends_on: []
blocks: []
tags: [writing, appendix]
created: 2026-09-13
updated: 2026-09-13
---

## Goal

List all 63 NADICS extraction fields with their random-forest importance in an appendix,
generated from the same JSON as Figure 3.4, and state the importance method in Section 3.4.1.

## Why it matters

Figure 3.4 and Section 3.4.1 show only the fifteen most important fields, so the importances of
the other 48 fields were not in the thesis, and the chapter did not say how the importance was
computed.

## Acceptance criteria

- [x] The author's JSON of 2026-09-13 checked against `figures/src/nadics-feature-importance.json`:
      same 63 fields, groups, ranks and percentages, same group shares. The repository JSON is
      unchanged.
- [x] Tables A.1 (all 63 fields, `longtable`) and A.2 (group summary) generated from that JSON by
      `figures/src/nadics-feature-importance-table.py`, which asserts ranks 1..63, the 100 per cent
      total and the group sums; `build.sh` and `figures/README.md` updated.
- [x] Section 3.4.1 states the method given by the author: the random forest of Section 3.4.2 is
      fitted to the training partition, the importance of a field is the impurity decrease of its
      splits across the trees, normalised over the 63 fields. It points to Appendix A.
- [x] Figure 3.4 caption and axis label, the Section 3.4.1 prose and the Section 3.6 limitation
      use "importance" wording consistent with that method.
- [x] Cumulative thresholds quoted in Section 3.4.1 (10 fields 54.5, 24 fields 80, 36 fields 90
      per cent) reproduced by Table A.1 (54.47, 80.72, 90.41).
- [x] Placeholder `Supplementary Material` chapter (label `app:supplementary`, never referenced)
      replaced.
- [x] Strict audit passes for `content/appendix.tex` and `content/anomaly-detection.tex`;
      `latexmk` clean, log read, both PDFs identical.
- [ ] Optional: cite Breiman (2001), `breiman2001random`, for impurity importance once its PDF is
      in the reference vault and it passes the strict audit.
- [ ] Compiled-page visual review, left to the author under the project rules.

## Evidence and sources

- `figures/src/nadics-feature-importance.json`: the 63 importances, groups, ranks, group shares.
- Importance method: the author's statement of 2026-09-13 (random forest on the training data,
  impurity decrease of each feature's splits, ranked).
- No bibliographic source is cited in the new text.

## Log

- 2026-09-13 created
- 2026-09-13 generator and Appendix A written, chapter pointer and method sentence added; build clean
- 2026-09-13 in-progress -> review
- 2026-09-13 review -> in-progress (Tighten the Chapter 3 method statement to the author's requested training-splits-ranking sequence)
- 2026-09-13 in-progress -> review (Minimal feature-importance method statement incorporated; strict audits and compile pass, PDFs identical)
