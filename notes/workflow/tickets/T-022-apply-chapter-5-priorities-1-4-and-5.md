---
id: T-022
title: Apply Chapter 5 priorities 1, 4 and 5
status: review
priority: P1
chapter: 5
owner: codex
depends_on: []
blocks: []
tags: []
created: 2026-09-20
updated: 2026-09-20
---

## Goal

Apply only the author's selected numerical reconciliation, readability and duplication refinements, and reference-scope corrections from T-020. Preserve the method specifications and equations; compile the tracked PDF.

## Why it matters

The author approved only priorities 1, 4 and 5 from the concise T-020 proposal. The
revision reconciles the published and matrix-derived Drebin F1, removes repeated and
editorial prose, and bounds literature claims to the cited evidence. Priority 2 (method
specification), priority 3 (broader empirical interpretation, including the macro-F1
inference), and additional mathematical derivations remain outside this request.

## Acceptance criteria

- [x] Identify 97.7% as the F1 calculated from the confirmed Drebin matrix and retain the
      published 97.8% in clearly qualified source tables and figures.
- [x] Consolidate repeated explanations and comparison warnings; replace informal or
      evaluative phrasing and remove both residual references to the deleted example.
- [x] Replace exclusive novelty claims with a bounded account of identified prior work;
      scope Fang et al.'s results and describe HGNNv2 as subsequent work.
- [x] Preserve all table bodies, figure assets, the construction algorithm and all 23
      numbered equations; do not supply missing implementation settings or add experiments.
- [x] Preserve the previous limitations reduction and the removal of the synthetic example.
- [x] Pass the strict citation audit and compile the tracked PDF; read the build log for
      new warnings and preserve the root PDF symlink. No visual review.
- [x] Pass the workflow and diff checks and leave changes unstaged.

## Evidence and sources

### Authorised scope and existing work

- Author request: "for now In the proposed improvement please apply the priority numbers
  1, 4,5." Numbering refers to the five-row proposal in the preceding response.
- Review evidence: T-020 and `notes/chapter5-critical-review-2026-09-20.md`.
- T-008 confirms the empirical status of the Drebin confusion matrix. The current chapter
  records TP=1085, FN=27, FP=24 and TN=1870; direct calculation gives F1=97.703737%,
  precision=97.835888%, recall=97.571942% and accuracy=98.303393%.
- T-009 and T-010 preserve the requested shortening of Section 5.14 and removal of the
  standalone worked example. Neither is reversed.
- The defect ledger and old Chapter 5 source-record directory remain absent. No archival
  record or experimental configuration is reconstructed.
- Pre-existing changes to Chapter 4 and its figures are left untouched. The shared PDF
  will be rebuilt from the current working tree.

### Claim-to-source record, completed before LaTeX editing

The primary texts and metadata inspected for T-020 remain available in the reference vault
and `tmp/pdfs/chapter5-critical-review-2026-09-20/`. The passages relevant to the approved
changes were inspected again. All cited keys below have `have` status and passed title
checks in `references/MANIFEST.tsv`; no new citekey is planned.

| Citekey | Claim supported | Full-text and metadata status |
| --- | --- | --- |
| `norouzian2025hgannmal` | Published pipeline, component choices and the source result values, including F1=97.8% | Original LaTeX read in full under T-020; result table re-read for this revision. DOI-registry title/authorship verified under T-020; PDF held. The empirical matrix has the separate T-008 author confirmation. |
| `zhang2023android` | Identified prior Android hypergraph system, its two construction rules and published evaluation | Full-text method and results inspected under T-020; DOI metadata verified; PDF held. The source does not establish that no other Android hypergraph work exists. |
| `feng2019hypergraph`, `gao2023hgnn`, `bai2021hypergraphattention` | Origins of the convolution, random-walk extension and learned incidence weighting | Primary formulation passages inspected under T-020; verified DOI records and PDFs held. No operator is changed here. |
| `he2023msdroid` | Local snippets around sensitive APIs under application labels | Full-text localisation passages re-inspected; publisher/DOI record verified under T-020; PDF held. |
| `fang2025kaa` | The evaluated GAT-based models and non-attentive baselines on the study's node-level tasks | Full-text Section 5.2 re-inspected; OpenReview verification and PDF held. Scope excludes a field-wide or Android-specific conclusion. |
| `brody2022gatv2` | Static-ranking result for additive attention and the revised scoring form | Full-text proof and scoring definitions inspected under T-020; arXiv verification and PDF held. Existing equations remain unchanged. |
| `gao2026hgnnv2` | Subsequent work on stability of hypergraph neural networks | Full-text introductory model description re-inspected; fresh Crossref record inspected under T-020; PDF held. Its existence does not invalidate the earlier experiment. |
| `arp2014drebin`, `allix2016androzoo`, `mahdavifar2020dynamic` | Dataset provenance and the distinct cohort definitions | Full-text collection/evaluation sections and DOI metadata checked under T-020; PDFs held. Cohort counts and selection procedures are preserved. |

### Verification record

- Baseline source, build log and word counts saved under
  `tmp/chapter5-priorities-145-2026-09-20/`.
- Strict citation audit must pass before drafting and after the revision.
- Source-preservation checks compare the equation, algorithm and table bodies and the figure
  hashes with the pre-edit state.

### Implementation and results

- The numerical reconciliation appears beside the empirical matrix, in the binary-table
  caption and in the metric-convention discussion. The F1 figure caption identifies the
  plotted numbers as published values. Both result tables now cite the source publication.
- Main prose decreased from 9,892 to 8,285 words by TeXcount (16.25%). The fifteen main
  sections are retained. Subheadings now describe component attribution, interpretability
  prospects and type-aware extensions without implying completed experiments.
- Removed exclusive novelty language and the claim that HGNNv2 supersedes the evaluated
  baselines. Scoped the KAA comparison to the paper's GAT-based models and node-level tasks;
  clarified Zhang et al.'s feature description against the primary source.
- Preserved all 23 equation blocks, the algorithm and all three table bodies exactly. Figure
  hashes are unchanged. Method Sections 5.4-5.6 and the deferred priority-3 passages are
  unchanged. No bibliography or reference-vault modification was needed.
- Strict audit passes for 36 cited keys, with no items needing attention. `latexmk thesis.tex`
  succeeds with the configured biber wrapper. The thesis decreases from 151 to 149 pages;
  Chapter 5 occupies printed pages 61-87, followed by the blank page 88, and Chapter 6 begins
  on page 89.
- No undefined citations/references or overfull boxes. Existing template and end-group
  warnings remain. Underfull vertical-box notices increase from 35 to 36; layout review is
  left to the author. No PDF rendering or visual inspection was performed.
- The root PDF symlink remains intact. The pre-existing Chapter 4 edits and figure changes
  were not modified. Validation details are in
  `tmp/chapter5-priorities-145-2026-09-20/verification.json`.

## Log

- 2026-09-20 created
- 2026-09-20 in-progress -> review (Priorities 1, 4 and 5 applied; citation audit, source-preservation checks and PDF rebuild pass; visual review left to the author)
