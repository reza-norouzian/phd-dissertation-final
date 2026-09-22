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
updated: 2026-09-22
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

### Follow-up: shorten Section 2.6.3

The author requested a substantial reduction of the multiclass and multilabel aggregation
subsection. The existing claim-to-source record for `grandini2020metrics`,
`opitz2019macrof1`, and `sparta2022d76` remains applicable: it covers class aggregation,
macro-$F_1$, and attribute accuracy, with inspected full texts and verified vault records.
This revision adds no source or empirical claim. It will retain the definitions needed to
interpret the contribution chapters, remove secondary exposition, and preserve the subsection
label and citation set. A strict citation audit and thesis rebuild are required.

- [x] Shorten Section 2.6.3 substantially without changing metric meanings.
- [x] Check the revised text against the adjacent binary and ROC subsections.
- [x] Run the strict reference audit, rebuild the tracked PDF, and inspect the log.

The revision reduces Section 2.6.3 from 290 to 175 prose words according to `texcount`, a
39.7% reduction. It removes the expanded one-versus-rest count display, the separate
micro-average ratio display, the macro-$F_1$ inequality, and the majority-class aside. The
remaining text retains classwise, macro, weighted and micro aggregation; the macro-$F_1$
convention; the zero-denominator qualification; and multilabel attribute accuracy. The
subsection label and its three citation keys are unchanged.

The strict Chapter 2 citation audit passes with 120 cited keys and none requiring attention.
`latexmk thesis.tex` succeeds and rebuilds the tracked 151-page PDF. The log contains no
undefined citations or references, Biber warnings, or overfull boxes. Its 43 underfull
vertical-box notices and the template/end-group warnings match the existing warning classes.
No visual review, staging, commit, or push was performed.

### Follow-up: remove Section 2.6.6

The author approved removal of the standalone aggregation and operational-reporting subsection.
Its operational quantities are already defined with their data in Chapter~3, while Chapter~4
states its processing coverage at the cohort definition. The fold/run distinction remains
necessary because Chapter~5 cites Equation~`eq:background:run-aggregation`; it will be retained
in shortened form at the opening of the experimental-protocol subsection. This change adds no
citation or empirical claim, so the verified source record above remains applicable.

- [x] Remove the standalone subsection and its redundant operational equations.
- [x] Retain a concise fold/run aggregation definition without breaking Chapter~5's reference.
- [x] Run the strict reference audit, rebuild the tracked PDF, and inspect the log.

Section 2.6.6, `Aggregation and Operational Reporting`, has been removed. Its throughput,
false-alarm-rate, and processing-coverage equations were deleted because Chapters~3 and~4
define these study-specific quantities with their data. The arithmetic-mean equation and two
sentences distinguishing class, fold, and run aggregation now sit under the reporting criteria
in `Experimental Protocol and Bias`; the existing Chapter~5 cross-reference remains valid.
That subsection is now numbered 2.6.6.

The strict Chapter 2 citation audit passes with 120 cited keys and none requiring attention.
`latexmk thesis.tex` succeeds and rebuilds the tracked 151-page PDF. The log contains no
undefined citations or references, Biber warnings, or overfull boxes. It contains 44 underfull
vertical-box notices and the existing template/end-group warning classes. No visual review,
staging, commit, or push was performed.

### Follow-up: concise experimental protocol and bias

The author approved a 120--150-word treatment of the remaining evaluation principles and
explicitly requested complete removal of `Event definitions and benchmark labels`. Retain
the subsection title and label, remove the paragraph headings and averaging equation, and
make Chapter 5's existing arithmetic-mean statement self-contained. No empirical result or
experimental protocol changes. Preserve the earlier uncommitted Section 2.6.6 removal.

#### Claim-to-source record before drafting

| Core source / evidence | Retained claim | Full-text, metadata and vault status |
| --- | --- | --- |
| `pendlebury2019tesseract` | Prospective Android evaluation uses temporally ordered training/test data and a test population appropriate to deployment. | Re-inspected Section 4.1, constraints C1--C3, in the existing full-text extraction. Cached USENIX primary record and prior metadata-verification response checked. Vault: `have`, `title_ok=yes`. |
| `arp2022dos` | Keep test information out of preprocessing and model selection; use suitable baselines under a common evaluation protocol. | Re-inspected P3/P5 and P6 in the existing full-text extraction. Cached USENIX author/title/year record checked. Vault: `have`, `title_ok=yes`. Controlled component comparisons remain a methodological requirement, not a new empirical attribution. |
| `irolla2018duplication` | Repackaged applications can create dependence between training and test samples. | Re-inspected the abstract, introduction and duplicate-analysis passages in the existing publisher-text extraction; the cached publisher/DOI metadata record is verified. Vault: `have`, `title_ok=yes`. No claim that all classifiers suffer equally. |
| Existing Chapter 4 protocol and T-032 author-confirmed repetition record | Hybroid uses five-fold means; HGANN-Mal uses five training runs on a fixed partition. | Re-read the current protocol passages; T-032 records the author's five-run clarification. No new numerical claim or reinterpretation of the publication. The nonlinear-metric averaging distinction is already established in this ticket. |

All retained citation keys already have manifest rows. The strict Chapter 2 audit passed
before drafting (120 cited keys, none requiring attention).

- [x] Reduce the subsection to two short paragraphs; remove the event-definitions passage
      and averaging equation, and repair the sole Chapter 5 equation reference.
- [x] Correct the stale subsection numbering in the current planning outline.
- [x] Pass strict citation audits and source checks; rebuild the tracked PDF and inspect
      warnings, with visual review left to the author.

Implementation: the subsection now has 121 prose words, compared with 389 before this pass
(`texcount`, excluding headings and mathematics), a 68.9% reduction. Two paragraphs replace
the five paragraph headings. The complete event-definitions and benchmark-labels passage and
the fold/run mean equation are removed. The title and subsection label remain; Chapter 5 now
states its five-run arithmetic means without the obsolete equation reference. No result or
protocol changed. Source comparisons confirm that all other Chapter 2 text is preserved and
that Chapter 5 differs only by that reference deletion. Updated the current plan's subsection
numbering and recorded the author-approved reductions without overwriting historical notes.

Verification: strict audits pass for Chapter 2 (112 cited keys) and Chapter 5 (35), with none
requiring attention. `latexmk thesis.tex` exits 0 and produces the tracked 151-page PDF.
There are no undefined citations/references, Biber warnings or overfull boxes. The 21 existing
template/package warning messages are unchanged; underfull vertical boxes decrease from 44
to 42, and the existing end-group notice remains. The root PDF symlink is intact. No visual
review, staging, commit or push. Pre-edit source/log snapshots are in
`/tmp/thesis-protocol-3OuQWC/`.

### Follow-up: simplify the opening sentence

The author requested plainer wording for the opening statement on temporal order and deployment
conditions. The existing `pendlebury2019tesseract` claim-to-source record above remains
applicable; no citation or scientific claim changes.

- [x] Split the sentence into two direct statements while preserving its meaning.
- [x] Pass the strict Chapter 2 citation audit and rebuild the tracked PDF.

The revised text states that training samples should be collected before the test period and
that the test set should match expected deployment conditions. The strict audit passes with
112 cited keys and none requiring attention. A pre-existing external LaTeX process remained
stalled on the shared output directory and corrupted its intermediates during a forced rebuild.
An isolated `latexmk` build therefore produced the verified 151-page PDF, which was installed
atomically as the tracked output. The isolated log contains no undefined citations/references,
Biber warnings or overfull boxes; the existing 21 template/package warnings, 42 underfull
vertical boxes and end-group notice remain. No visual review, staging, commit or push.

- 2026-09-20 created
- 2026-09-20 in-progress -> review (Shared performance measures added, sources and formulas checked, citation audit and PDF rebuild pass; visual review left to author)
- 2026-09-20 review -> in-progress (Shorten Section 2.6 at the author's request, preserving its measures, equations and qualifications)
- 2026-09-20 in-progress -> review (Concise revision complete; metric definitions and equations preserved, citation audit and PDF rebuild pass)
- 2026-09-22 review -> in-progress (Shorten Section 2.6.3 substantially at the author's request while preserving its core definitions and verified citations)
- 2026-09-22 in-progress -> review (Section 2.6.3 shortened by 39.7%; core aggregation definitions retained; strict audit and 151-page rebuild pass)
- 2026-09-22 review -> in-progress (Remove Section 2.6.6 and retain only the fold/run distinction within the experimental-protocol subsection)
- 2026-09-22 in-progress -> review (Removed Section 2.6.6; kept concise fold/run aggregation under evaluation protocol; audit and rebuild pass)
- 2026-09-22 review -> in-progress (Shorten Experimental Protocol and Bias to two paragraphs and remove event definitions and benchmark labels at the author's request)
- 2026-09-22 in-progress -> review (Concise evaluation principles complete; event-definitions passage removed; audits and PDF rebuild pass)
- 2026-09-22 review -> in-progress (Simplify the opening sentence of Experimental Protocol and Bias at the author's request)
- 2026-09-22 in-progress -> review (Opening sentence simplified; strict audit and isolated PDF rebuild pass)
