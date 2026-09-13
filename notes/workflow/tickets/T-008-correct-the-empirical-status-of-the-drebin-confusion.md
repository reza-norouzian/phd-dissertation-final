---
id: T-008
title: Correct the empirical status of the Drebin confusion matrix
status: review
priority: P1
chapter: 5
owner: claude
depends_on: []
blocks: []
tags: []
created: 2026-09-13
updated: 2026-09-13
---

## Goal

State the Chapter 5 Drebin confusion matrix as an empirical result and separate it from the illustrative class-balance calculation.

## Why it matters

Chapter 5 currently describes the measured confusion matrix as a reconstruction from aggregate
metrics. This misstates the provenance of the central Drebin binary result and makes an empirical
experiment appear hypothetical. The class-balance calculation that follows is illustrative and
must remain distinct from the measured matrix.

## Acceptance criteria

- [x] Record the author's correction as a superseding decision and in the Chapter 5 source record.
- [x] State the test partition and confusion matrix as empirical results in Section 5.10.
- [x] Keep the 10 per cent malware-share calculation clearly identified as a sensitivity analysis.
- [x] Remove surviving claims that the matrix was reconstructed or implied by the aggregate metrics.
- [x] Pass the strict Chapter 5 reference audit and compile the thesis with identical PDFs.
- [x] Read the build log for new warnings; leave visual review to the author.