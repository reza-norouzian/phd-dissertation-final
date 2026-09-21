---
id: T-028
title: Review the dissertation end to end for critical and high-priority issues
status: review
priority: P1
chapter: -
owner: codex
depends_on: []
blocks: []
tags: [review, evidence, dissertation-wide]
created: 2026-09-21
updated: 2026-09-21
---

## Goal

Read the current dissertation and its supporting empirical records as a supervisor; deliver a short, plain-language report of critical and high-priority issues, with exact locations and required remedies. Do not revise the dissertation.

## Why it matters

The author requested a supervisor-style reading of the complete current dissertation and a
short report restricted to critical and high-priority weaknesses. Previous chapter revisions
corrected many interpretations, but declared limitations and missing experimental records
still need assessment against the research questions. This ticket does not authorise changes
to chapter text or reversal of accepted attribution and empirical-status decisions.

## Acceptance criteria

- [x] Read all included chapters, both abstracts, front matter and Appendix A.
- [x] Compare research questions and contribution claims with the methods, results and conclusions.
- [x] Check candidate high-priority findings against original source material and surviving author confirmations.
- [x] Distinguish confirmed contradictions from missing evidence and already disclosed scope limits.
- [x] Save a concise report with locations, consequences and minimum remedies.
- [x] Run the strict whole-thesis citation audit and the workflow consistency check.
- [x] Leave dissertation sources and the compiled PDF unchanged; report review scope and limits.

## Evidence and sources

### Review evidence and boundaries

- Scope is restricted to `thesis-v2` at the author's explicit request. Material from adjacent
  or earlier checkouts is excluded from this assessment and its supporting evidence.
- Current manuscript: `thesis.tex`, `dissertationmacros.tex`, `thesissetup.tex`, all included
  `content/*.tex`, and both generated Appendix A table fragments.
- Reader version: `output/pdf/thesis.pdf`, 153 pages, generated 21 September 2026 at 00:28 CEST.
  Text extraction supports reader-page locators; this is a scientific/content review, not a
  page-by-page visual-layout review.
- Governing context: workflow README, the complete current decision register, structure v0.3,
  the defect ledger, and current revision tickets. Preserve D-002 through D-006 and the
  author-confirmed empirical matrix/cohort in T-008 and T-012.
- Core empirical sources being inspected: the original Hybroid and HGANN-Mal publications,
  the SWaT internal report and archived code, the IUNO deliverables and NADICS repository,
  the two-page service-graph paper, and the relevant SPARTA deliverable passages and
  versioned-software records.
- Prior review reports are leads for unresolved questions, not substitutes for reading the
  current chapter. In particular, the current Chapter 3 results describe an author-confirmed
  later evaluation, so a difference from the older report is a provenance question, not proof
  that the current values are false.
- No new dissertation source is cited or drafted. The whole-thesis strict audit reports
  177 cited keys, 165 local PDFs and zero unresolved entries. This checks the reference
  records; it does not verify empirical outputs or every source-to-claim relationship.

### Coverage completed

- Read the complete current text of Chapters 1-8, both abstracts, title pages,
  acknowledgements, Appendix A and its two included table fragments. Checked the master
  input list, shared RQ macros, metadata and current PDF outline/page labels.
- Read both original Android publications in full: Hybroid, 20 PDF pages, and HGANN-Mal,
  21 PDF pages. Compared their methods and numerical tables with the current dissertation.
- Read the complete two-page service-graph source. Inspected the industrial-method passages
  of IUNO AP4 (printed pp. 12-13) and AP7 (pp. 29-30), and the original SWaT report's methods,
  results and discussion. The older report and tuning code describe an earlier evaluation;
  they are not evidence that the author-confirmed replacement results are false.
- Compared the SPARTA contest and benchmark tables with D7.6 (printed pp. 16-19 and 28-29),
  and inspected the versioned benchmark's complete `main.py` and Foolbox's clipping contract.
  Retrieved these two files from their pinned primary GitHub URLs; their full SHA-256 hashes
  match `references/source-records/chapter6-software.md`. No downloaded code was executed.
- Recalculated the S7-300 six-class and binary metrics, the SWaT PCA24 matrix metrics and the
  author-confirmed HGANN Drebin binary metrics. These counts reproduce the current reported
  rounded values, including the separately identified 97.7% Drebin F1.
- Physically checked the 165 cited PDFs against their recorded sizes and 16-hex SHA-256
  prefixes. All match. An initial scratch check compared full hashes against the stored
  prefixes; its mismatch output was a checking-script error, not a vault defect.

### Evidence-package limits within this checkout

The current checkout contains aggregate results and plotting inputs, but no located run
manifest/prediction package that connects the revised industrial tables to the evaluated
code and sample partitions. Existing aggregate author confirmations remain valid evidence of
their stated provenance; they do not enable independent reproduction. A restricted evidence
package is sufficient where industrial data cannot be released publicly. The current T-001
records the author's confirmation of the industrial contribution boundary, and current T-008
and T-012 settle the empirical Drebin matrix and retained Hybroid cohort. None is reopened.

### Findings and exact evidence

#### R1. Confirmed NADICS defect, conditional critical impact

`publications/Anomaly Detection/NADICS_repo/nadics/main.py:201-215` assigns the result of
`pre.encode(...)` to `training, training, newFeatures`. In `preprocessor.py:39-67`, encoding
mutates the supplied frames and returns them. The second assignment binds `training` to
the same encoded frame as `testing`. `samplingRatio` then samples both from that test frame
(`preprocessor.py:82-84`); feature and label extraction follow at `main.py:228-231`.

The implementation defect is established by the source. Its use in the current S7-300
experiment is not established. `content/anomaly-detection.tex:175-217` describes the released
framework and `:333-393` describes categorical encoding and training-only fitting for the
industrial experiment. A corrected/private evaluation revision could resolve the apparent
disconnect. Require the evaluated revision and split checks; do not claim that the current
94.50% F1 was generated by this bug. Do not repair the historical source or rerun experiments
under a read-only review request.

#### R2. Model-development boundaries remain unclear in the manuscript

- SWaT: `content/anomaly-detection.tex:603-608` states training/validation-only selection;
  `:798-804` says the final PCA configuration is consequently adopted for its reported test
  F1. Lines `:917-921` and `:947-955` incorrectly make chronology itself sufficient to
  prevent selection leakage. Distinguish validation selection from subsequent test ranking
  and reconcile the account against the experiment's selection records. This is a
  contradictory account, not proof of contamination in the final run. The current defect
  ledger already records this unresolved issue as SW-01.
- Hybroid: `content/hybroid.tex:356-369`, `:436-451` and `:705-712` leave the relationship
  between cross-validation, supervised representation fitting and feature preparation
  incompletely specified. The source publication does not recover all those boundaries.
- HGANN: `content/hgann-mal.tex:227-233` says standardisation is across the corpus, while
  `:265-269` leaves raw counts versus IDF weighting open. The fitting population is not
  specified. A literal whole-corpus fit would differ from the inductive protocol described
  in Chapter 2. Verify the implemented procedure; do not edit it into an assumed train-only
  procedure.

#### R3. Reproducibility includes central algorithmic choices

- Hybroid's block weights and application composition are unspecified at
  `content/hybroid.tex:241-247` and `:314-320`.
- `content/hgann-mal.tex:215-222` describes a backward CFG walk. Chapter 2 defines the CFG
  as intra-procedural (`content/background.tex:143-174`), but the slice rule at
  `content/hgann-mal.tex:360-374` assumes a set of methods. If the slice has one method,
  the extension has no distinct pair and the filter at `:389-395` rejects it. This is a
  conditional consequence of the written specification, not an observed empty slice family.
- Duplicate-edge handling and zero-degree nodes remain unspecified (`:403-409`). Readout
  alternatives appear at `:654-656`; the labelled-subset loss at `:698-713` is a valid
  possible formulation, not proof of which joint/separate training scheme was executed.
  Exact configurations and consistent application partitions across heads are required.
- The original HGANN publication contains no experimental training configuration that fills
  these gaps. The source directory contains the publication and its TeX/BibTeX materials,
  not a located training implementation or predictions.

The report does not propose restoring deleted worked examples or pending markers. A compact
verified configuration record and a restricted run archive would be more useful.

#### R4. Published metrics remain internally inconsistent

`content/hgann-mal.tex:833-839`, `:926-932` and `:1118-1127` preserve and disclose four
incompatible rows. For a common positive-class/macro/support-weighted convention,
F1 cannot exceed `(P+R)/2`. Accounting for rounding to 0.1 percentage point gives:

| Row | Lowest compatible F1 | Highest bound from reported P/R |
| --- | ---: | ---: |
| GCN, Drebin binary | 92.15 | 91.90 |
| HGNN, Drebin binary | 96.15 | 96.10 |
| HGANN, Drebin families | 94.15 | 94.00 |
| GCN, CICMalDroid categories | 82.35 | 82.25 |

These are inherited numerical/definition conflicts, not transcription errors introduced by
the current dissertation. The separate matrix-derived Drebin F1 of 97.7037% is already
handled correctly under T-022; do not reopen its empirical status. However,
`content/hgann-mal.tex:967-975` still compares published F1 margins quantitatively, and the
tables/figure visually rank those unresolved scores. Preserve the historical record but
separate it from the metrics used as evidence for gain claims.

Hybroid's metric-averaging caveats are at `content/hybroid.tex:491-507` and `:610-619`.
Its displayed per-class AUCs average to 0.9748 rather than the printed macro 0.976. The
current chapter discloses this correctly; the remedy needs predictions or scoring code,
not an invented replacement convention.

#### R5. Attribution, variability and dataset controls

`content/hgann-mal.tex:980-998` explicitly confirms that construction and attention change
together. Lines `:1079-1083` confirm single runs. The mathematical operator analysis does
not substitute for the missing matched ablation. Hybroid's differences at
`content/hybroid.tex:636-673` come from rounded fold means without paired predictions.

Relevant controls include consistent tuning and normalisation, repeated seeds, and tests
for related applications across partitions. HGANN's mixed-source benign/malicious cohorts
and absence of duplicate grouping are recorded at `:750-765`, `:803-810` and `:1128-1135`.
Hybroid's capture-related fields are discussed at `content/hybroid.tex:688-695`.
These are risks, not proven explanations of the reported gains. A new cross-study ranking
of Hybroid and HGANN is not required by the accepted monograph scope. Current conclusions
must remain descriptive unless stronger controls are supplied.

#### R6. Benchmark validation remains distinct from the valid metric critique

At public revision `2fac62b947ed77a509f397a9cc316937291395f5`, benchmark `main.py:134-135`
scores the raw output rather than the separate clipped tensor. Foolbox 3.3.1
`attacks/base.py:409-434` applies the budget to the clipped return. Benchmark `main.py:40-42`
and `:131-135` also replace true labels with target labels in targeted runs.

The current chapter accurately discloses these facts at `content/adversarial-evaluation.tex:344-356`.
D7.6 Tables 1 and 2 match the reproduced numbers, but historical attack settings/checkpoint
associations remain unresolved (`:486-524`, `:588-633`). There is no evidence linking the
public-code defect to a particular historical result. A validated new example would strengthen
the reproducible-software part of RQ4; it must be labelled as a new evaluation and must not
silently replace historical results. The constant-prediction and response-policy derivations
remain valid independently of those missing records. A general clean-performance/robustness
relationship, or Android adversarial robustness, is not established and is not claimed in the
current conclusion.

### Lower-priority and correctly handled points

- The current abstracts still describe the 97.6 versus 97.7 accuracy comparison as "level";
  the contribution chapter and conclusion correctly avoid a statistical-equivalence claim.
  This is a minor consistency correction, not an additional critical finding.
- Title pages retain institute/reviewer/date placeholders, and acknowledgements retain the
  replacement instruction. Verify formal metadata with the author before submission.
- All eight chapters and the appendix are included. The 153-page total is below the accepted
  170-page maximum. No chapter expansion, new RQ or general trade-off claim is proposed.
- Attribution is explicit; the confirmed service-graph, partial Hybroid and partner-defence
  boundaries are preserved. Absence of an Android adaptive-attack experiment is a disclosed
  scope limit, not evidence that the dissertation has claimed such a result.
- Some planning page ranges are historical. Reader locations in the report were taken from
  the current PDF rather than copied from those older build notes.

## Log

- 2026-09-21 created
- 2026-09-21 The author restricted the review to this checkout. Earlier-checkout material was
  excluded from the report and supporting evidence; no further access to those folders.
- 2026-09-21 Completed the scientific review and saved
  `notes/dissertation-supervisor-review-2026-09-21.md` (534 words). The conditional critical
  finding is a directly verified defect in this checkout's archived NADICS encoding path;
  its impact on the reported industrial experiment remains unconfirmed. Five high-priority
  groups concern protocol clarity, reproducibility, metric consistency, controlled evidence
  and benchmark validation. Strict citation audit and physical PDF checks pass. Workflow
  check reports 28 tickets with no problems. Dissertation source/PDF diff is empty; no build,
  visual review, experiment rerun, staging or commit was performed.
- 2026-09-21 in-progress -> review (Thesis-v2-only supervisor review complete; concise report and source-backed findings saved; thesis unchanged)
