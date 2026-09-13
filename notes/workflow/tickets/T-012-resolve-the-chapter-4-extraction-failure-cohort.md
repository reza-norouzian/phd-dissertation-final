---
id: T-012
title: Resolve the Chapter 4 extraction-failure cohort
status: review
priority: P1
chapter: 4
owner: claude
depends_on: []
blocks: []
tags: []
created: 2026-09-13
updated: 2026-09-13
---

## Goal

Replace the final Chapter 4 pending marker with the author's confirmation that both analysis branches excluded the 47 failed applications and used the same 2,079-application cohort, then align dependent counts without recalculating published metrics.

## Why it matters

Chapter 4 reports 2,126 matched packages and captures but leaves the treatment of 47 failed graph
extractions unresolved. The author's confirmation fixes the effective cohort for the static,
dynamic and fused comparisons. Related class-share statements must distinguish the source corpus
from the evaluated subset because the class labels of the excluded applications are unavailable.

## Acceptance criteria

- [x] Replace the final Chapter 4 pending marker with the confirmed common cohort of 2,079
      applications.
- [x] Distinguish the 2,126-application source corpus from the 2,079-application evaluation cohort.
- [x] Retain the published accuracy, precision, recall and F1 values without recalculation.
- [x] Qualify class-share and per-category count arguments that depend on the unknown labels of the
      47 excluded applications.
- [x] Align Chapter 7 and the Chapter 4 source records with the confirmed cohort.
- [x] Record the author decision, run the strict reference audits for changed chapters, compile
      `thesis.tex`, inspect the log and confirm that the tracked PDFs are identical.
