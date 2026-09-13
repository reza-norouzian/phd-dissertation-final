---
id: T-010
title: Replace the Chapter 5 worked example with a concise operator statement
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

Remove the standalone synthetic attention example and preserve its useful conclusion in two sentences within the operator analysis.

## Why it matters

The synthetic six-method example occupies a subsection, one displayed equation and one table. It
proves a narrow representational property, but it uses no application data or trained parameter.
The same point can be stated beside the operator equations without interrupting the chapter with a
long constructed calculation.

## Acceptance criteria

- [x] Remove the standalone worked-example subsection, Equation `eq:hgann:example` and Table
      `tab:hgann:example`.
- [x] Preserve the useful operator conclusion in two sentences within Section 5.8, without a new
      heading.
- [x] State the experimental limit: the reported runs do not isolate whether the learned model
      used this capacity or whether it caused the accuracy difference.
- [x] Remove all cross-references to the deleted equation and table.
- [x] Update the Chapter 5 source records and supersede the worked-example clause of D-046.
- [x] Pass the strict Chapter 5 reference audit and compile with identical PDFs.
- [x] Read the log for new warnings; leave visual review to the author.
