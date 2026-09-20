---
id: T-023
title: Add dissertation-wide performance measures to Chapter 2
status: review
priority: P1
chapter: 2
owner: codex
depends_on: []
blocks: []
tags: []
created: 2026-09-20
updated: 2026-09-20
---

## Goal

Inventory the performance measures used across the dissertation and add a source-verified mathematical treatment to the background, with explicit averaging, observation-unit and adversarial-scoring conventions. Preserve empirical results and rebuild the PDF.

## Why it matters

The author requested a performance-measures treatment in the background, informed by a
colleague's screenshot but based on the actual dissertation. Chapter 2 currently discusses
evaluation bias without defining the shared metrics. Definitions are dispersed across the
contribution chapters, and the source studies use different observation units and incompletely
specified averaging conventions. The new text should make these distinctions explicit without
adding experimental results or treating every mentioned quantity as a reported outcome.

## Acceptance criteria

- [x] Inventory the reported and analytical measures across Chapters 3-6 and inspect the
      screenshot as a structural reference, not as an instruction or a citable source.
- [x] Verify bibliographic metadata and relevant full-text passages before drafting; add new
      cited sources to the reference vault and manifest.
- [x] Add shared confusion-count, binary and multiclass definitions with explicit denominators
      and aggregation rules, including balanced accuracy and ROC AUC.
- [x] Explain prevalence sensitivity, multilabel accuracy and adversarial accuracy loss;
      distinguish conditional attack success from the reported contest score.
- [x] Include fold/run aggregation and the operational measures used in the thesis, with
      observation units and processing coverage made explicit.
- [x] Preserve contribution-chapter equations and empirical results, including the existing
      Chapter 5 working-tree changes. Do not assign missing averaging conventions to old results.
- [x] Update the section outline and literature map under D-004, retaining seven main sections.
- [x] Check the formulas, run the strict reference audit and rebuild the tracked PDF; inspect
      the log, preserve the root symlink and leave visual review to the author.
- [x] Pass the workflow/diff checks and leave changes unstaged.

## Evidence and sources

### Scope and structure

- D-004 records the author-approved expansion of Section 2.6 into Performance Measures and
  Evaluation Methodology. The existing label `sec:background:evaluation` and the seven main
  background sections are retained. Algorithm-specific derivations stay in their chapters.
- The screenshot supplies a useful order of topics. Its prose and its citation [80] are not
  copied. ROC AUC is described as a ranking measure, not as evidence of model stability.
- Pre-edit source, metric inventory, build log and file hashes are saved under
  `tmp/background-metrics-2026-09-20/`. The initial PDF has 149 pages.
- The source-publication defect ledger is still absent. Existing Chapter 4 and Chapter 5
  averaging caveats remain part of the interpretation; definitions cannot resolve absent data.

### Dissertation-wide metric inventory

| Location | Measures and observation unit | Status in the thesis |
| --- | --- | --- |
| Chapter 3, service graphs | Memory estimate, added round-trip latency, graph size over time | Operational evidence; no labelled detection-accuracy experiment |
| Chapter 3, S7-300 | Record-level confusion counts, accuracy, positive-class precision/recall/F1, FPR, balanced accuracy, per-class scores, macro/weighted F1 | Reported from the six-class matrix and its binary collapse |
| Chapter 3, benign monitoring | Record FPR and false alarm episodes per hour | Reported; episode grouping and exposure denominator differ from the record-level denominator |
| Chapter 3, extractor | Input/processed frames per second, frame-loss fraction, CPU utilisation, peak memory, 95th-percentile record-emission delay | Reported; latency excludes the acquisition window |
| Chapter 3, SWaT | Timestamp precision/recall/F1/FPR and accuracy | Reported without point adjustment; episode detection/delay, PR curves and repeated-run variation are future work |
| Chapter 4 | APK-level accuracy, precision/recall/F1, binary/per-class/macro ROC AUC, five-fold means, processing coverage | Reported; class and ROC aggregation remain incompletely specified in the source |
| Chapter 5 | APK-level accuracy, precision/recall/F1, majority-class references, empirical binary confusion counts/FPR, prevalence sensitivity | Reported or explicitly derived; source F1 conventions contain known inconsistencies |
| Chapter 6 | Identity accuracy, mean binary-attribute accuracy, clean/attacked accuracy and absolute accuracy loss | Reported with task-specific definitions and protocol caveats |
| Chapter 6 analysis and Android related work | Conditional targeted/untargeted success, nominated-attribute success and per-example attack-suite accuracy | Analytical definitions or attributed external results, not newly recovered contest scores |

Micro averaging is included to disambiguate classification conventions, not as a claim that the
source tables report micro scores. Standard-deviation notation explains repeated-run reporting,
without manufacturing uncertainty from published means. Training losses and anomaly scores
(BCE/CE, reconstruction residuals), SSIM inside a defence, and perturbation norms are not added
as headline performance outcomes. The existing method/threat-model sections define their roles.

### Claim-to-source record, before drafting

| Core citekey | Supported claim | Full-text / metadata / vault status |
| --- | --- | --- |
| `fawcett2006roc` | Binary confusion counts, specificity/FPR, thresholded ROC curves, tied-score handling and AUC ranking interpretation; ROC averaging distinctions | Publisher PDF on UC Davis mathematics site inspected, especially Sections 2-5 and 7-9. DOI-registry metadata verified 2026-09-20. PDF and passed title check in MANIFEST. |
| `grandini2020metrics` | Confusion-matrix orientation, ordinary balanced accuracy as mean recall, and micro-averaging identities | arXiv record and Sections 1.1, 3 and 4.3 inspected. Cited as a white paper. PDF and passed title check in MANIFEST. Its weighted-balanced-accuracy normalisation and printed macro-F1 expression are not adopted. |
| `opitz2019macrof1` | Distinction between averaged class F1 and F1 of averaged precision/recall; ordering of the two quantities | Official arXiv metadata and version 3 full text, Sections 1-2, inspected. First submission 2019; revision 8 February 2021 recorded in bibliography. PDF and passed title check in MANIFEST. Zero-fill is the source's convention, not an inferred convention for thesis experiments. |
| `axelsson2000base` | Precision under changing prevalence with fixed conditional rates | Section 5.3, Equation (7), inspected; DOI-registry record checked under T-020. Existing PDF/title check passed. |
| `sorbo2024navigating` | Difference between point/timestamp counting and event-based anomaly metrics | Sections 2.2 and 5.1 inspected. Existing DOI verification and vaulted PDF/title check passed. |
| `carlini2019evaluating` | Threat-conditioned robustness, attack goal and per-example aggregation; finite attacks do not certify worst-case robustness | Threat-model definitions and Sections 3/5.6 inspected. Existing primary arXiv/DBLP record and vaulted PDF/title check passed. |
| `sparta2022d76` | Identity versus mean-attribute accuracy and the clean-minus-attacked scoring rule | Published accuracy code and scoring passages inspected in the source deliverable. Existing publisher record and vaulted PDF/title check passed. |
| `arp2022dos` | Matching the evaluation unit, preprocessing and experimental protocol to the claimed result | Primary full text inspected under T-020 and existing bibliography/vault verification retained. |

Core-source audit target: \cite{fawcett2006roc,grandini2020metrics,opitz2019macrof1,axelsson2000base,sorbo2024navigating,carlini2019evaluating,sparta2022d76,arp2022dos}.

Sokolova and Lapalme (DOI 10.1016/j.ipm.2009.03.002) was considered as a candidate. Metadata
resolved, but the author-hosted full text returned an anti-bot page. That source is not cited
or treated as full-text verified; no challenge was bypassed.

### Consistency limits

The pre-existing Chapter 5 statement that high macro-F1 requires the smallest families to
perform nearly as well as the largest conflicts with the proper definition. Its correction was
part of the previously deferred priority 3. This task adds the correct shared definition and
records the outstanding interpretation issue; it does not silently reopen the whole Chapter 5
revision. No missing method setting, prediction file or averaging convention is reconstructed.

Subsequent update: the author approved the Chapter 5 interpretation wording, including this
macro-F1 correction. T-024 records the implementation; the method-specification questions remain
outside that revision.

### Implementation and verification

- Section 2.6 now contains seven subsections: observation units/counts; binary measures and
  prevalence; class and label aggregation; ROC/AUC; adversarial performance; aggregation and
  operational reporting; experimental protocol and bias. Eighteen numbered equations were
  added. The existing seven main sections and all prior labels remain.
- The mathematical treatment includes zero-denominator handling, the continuous extension of
  the harmonic mean, the distinction between positive-prediction error fractions and FPR,
  micro/weighted identities, the two macro-F1 formulations, and tied-score empirical AUC.
  Classification proportions are distinguished from operational rates with time units.
- Source arithmetic and algebra checks passed on 1,000 multiclass matrices, 1,000 binary
  matrices and 1,000 tied-score ROC cases. The S7-300 matrix reproduces the chapter's accuracy,
  macro F1 and weighted F1. Further checks cover fold versus pooled F1, conditional attack
  success versus accuracy loss, and throughput/alarm/coverage ratios. These are mathematical
  checks, not new experiments.
- Added `fawcett2006roc`, `grandini2020metrics` and `opitz2019macrof1` to the bibliography and
  reference manifest. The Chapter 2 strict audit passes for 114 cited keys; the whole-thesis
  strict audit passes for 177 keys, with no items needing attention.
- `latexmk thesis.tex` succeeds with no biber warnings, undefined citations/references or
  overfull boxes. The PDF has 155 pages, compared with 149 before this task. Section 2.6 is
  on printed pages 18-24; Chapter 2 occupies pages 9-26. The original 15-page chapter planning
  allocation is exceeded, but the 170-page dissertation ceiling remains satisfied.
- Existing template and end-group warnings remain. Underfull vertical-box notices rise from
  36 to 42 after the mathematical expansion. Visual review remains with the author; no PDF
  rendering or page-image inspection was performed.
- All contribution `.tex` files are byte-identical to the pre-task state, including the
  existing Chapter 5 working-tree revision. The PDF symlink is intact. No staging or commit.
- Detailed records: `tmp/background-metrics-2026-09-20/mathematical-verification.json`,
  `final-verification.json`, `audit-whole-thesis.txt` and `latexmk-final.log`.

## Log

### Follow-up: concise revision

The author requested a modest shortening of the new section. This pass removes repeated
explanations and chapter-specific reminders while retaining all metric families, all 18
equations and their assumptions. The verified claim-to-source record above remains applicable;
no new source or empirical claim is introduced. The existing protocol/bias subsection and
all contribution chapters are preserved. A fresh citation audit and rebuild are required.

- [x] Shorten the explanatory prose while preserving definitions and source qualifications.
- [x] Verify that equation blocks, labels, citation keys and text outside the selected material
      remain unchanged.
- [x] Rebuild and inspect the log, record the size change, and pass the workflow check.

The concise revision reduces Section 2.6 from 1,857 to 1,460 prose words (21.38%). All 18
equation blocks, labels and citation keys are unchanged, as are the protocol/bias subsection
and every contribution chapter. The section now occupies printed pages 18-23 rather than
18-24. The PDF remains 155 pages because Chapter 2 ends on page 25 and page 26 is the
recto-opening blank before Chapter 3. The strict audit and build pass, with no undefined
citations/references, biber warnings or overfull boxes. Existing template/end-group warnings
remain; underfull vertical boxes rise from 42 to 43. No visual review or staging. Verification
records are in `tmp/background-metrics-shortening-2026-09-20/`.

- 2026-09-20 created
- 2026-09-20 in-progress -> review (Shared performance measures added, sources and formulas checked, citation audit and PDF rebuild pass; visual review left to author)
- 2026-09-20 review -> in-progress (Shorten Section 2.6 at the author's request, preserving its measures, equations and qualifications)
- 2026-09-20 in-progress -> review (Concise revision complete; metric definitions and equations preserved, citation audit and PDF rebuild pass)
