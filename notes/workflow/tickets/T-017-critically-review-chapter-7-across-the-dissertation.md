---
id: T-017
title: Critically review Chapter 7 across the dissertation
status: review
priority: P1
chapter: 7
owner: codex
depends_on: []
blocks: []
tags: [review]
created: 2026-09-19
updated: 2026-09-19
---

## Goal

Assess Chapter 7 against the research questions, current contribution chapters and underlying evidence; identify scientific weaknesses, repetition and justified cuts, and propose a concise revision without changing dissertation text before the author reviews the recommendations.

## Why it matters

The author requested a critical reading of Chapter 7 and advice on substantial cuts. The
chapter must connect the representation studies to the evaluation contribution without
repeating their limitations or implying a common experiment. Its existing seven-section
outline and four-page target belong to T-004 and structure v0.3. This review may recommend
a different outline, but it does not adopt that change on the author's behalf.

## Acceptance criteria

- [x] Read Chapter 7 in full and cross-check its argument against Chapters 1 to 6, Chapter 8,
      the abstracts, the research-question macros and the current structure plan.
- [x] Check the relevant original Android manuscripts and the full-text passages supporting
      Chapter 7's external citations; distinguish current author-confirmed records from the
      older source reports.
- [x] Identify scientific and cross-chapter issues with exact source locations; distinguish
      a wording conflict from evidence that an experiment was conducted incorrectly.
- [x] Provide section-by-section retain, cut and rewrite recommendations and an outline
      proposal that preserves the conceptual comparison and the chapter's Android focus.
- [x] Save the review, leave dissertation LaTeX and the compiled PDF unchanged, and report
      that no compilation or visual review was performed for this review-only task.
- [x] Pass the strict Chapter 7 reference audit and the workflow consistency check.

## Evidence and sources

### Scope and current records

- `content/discussion.tex`, read in full, lines 1--204. TeXcount reports 1,414 main-text
  words, seven sections and one table. Existing build labels place the chapter on printed
  pages 113--117; Chapter 8 begins on page 119. No PDF layout judgement is made.
- `content/introduction.tex`, `content/background.tex`, `content/anomaly-detection.tex`,
  `content/hybroid.tex`, `content/hgann-mal.tex`, `content/adversarial-evaluation.tex`,
  `content/conclusion.tex`, `content/abstract.tex` and `dissertationmacros.tex`.
- `notes/dissertation-structure-v0.3.md`, the full decision register, T-004, T-001, T-008
  and T-012. T-012 records the author's confirmation of Hybroid's common 2,079-sample
  evaluation cohort; the original paper reports 47 extraction failures but does not settle
  the common-cohort question on its own. T-008 records the empirical Drebin confusion matrix.
- The current SWaT evaluation follows the later author-approved account in Chapter 3 and
  structure v0.3 (D-054/D-055). The supplied older industrial report contains a different
  evaluation. It must not be used to replace the current results. This review identifies
  the selection-language conflict within the current chapter, without alleging leakage.
- `notes/known-issues-to-fix.md` and the old `notes/chapter*-source-records/` directories
  referenced by earlier tickets are absent from this checkout. Current limitations and
  surviving tickets provide the available defect record; this is a verification limit.

### Claim-to-source record for the review

All keys below already occur in `references/MANIFEST.tsv` with status `have` and a positive
title check. No new citation or bibliography entry is introduced. Full-text inspection means
inspection of the relevant argument, method and result passages, not independent replication
of the experiments.

| Citekey | What the inspected source supports | Full-text and metadata status |
| --- | --- | --- |
| `norouzian2021hybroid` | Static and traffic branches, application-level flow averaging, within-system modality evaluation, the 47 extraction failures and the separate large static corpus. | Original LaTeX method and evaluation sections inspected; source figure values cross-checked through the restored Chapter 4 record. Vault PDF available. DOI metadata rechecked with Crossref. |
| `norouzian2025hgannmal` | Static observation, the hyperedge families, and published binary/multiclass tables. Does not isolate attention or measure end-to-end acquisition cost. | Original LaTeX method and result tables inspected; vault PDF available. DOI metadata rechecked through the DOI resolver. |
| `lashkari2018toward` | CICAndMal2017 acquisition and the distinction between application provenance and common capture conditions. | Full-text dataset description inspected; vault PDF available. DOI metadata rechecked through the DOI resolver. |
| `mahdavifar2020dynamic` | CICMalDroid's successful-execution and analysis-file filters, and the retained class counts. | Full-text Sections IV--V and Table II inspected; vault PDF available. Crossref title, authors and DOI rechecked. |
| `sparta2022d76` | Reported SD constant attribute outputs at approximately 80% clean accuracy; contest and partner benchmark records. | Full-text SD account inspected; current Chapter 6 tables and analytical derivations checked separately. Local public deliverable in the vault; existing project metadata retained. |
| `song2026fcghunter` | Problem-space call-graph modifications subject to functionality preservation. Does not establish an attack against either dissertation Android system. | Full-text formulation and mutation operators inspected in the vaulted arXiv version. Published title, authors, year, volume and pages rechecked through the DOI resolver. |
| `carlini2019evaluating` | Explicit adversary goals/capabilities, valid perturbations and evaluation against the complete defence. | Full-text threat-model/evaluation passages inspected; arXiv primary record rechecked. Vault PDF available. |
| `arp2022dos` | Sampling-origin confounding and spurious predictive cues in the Android case study. Does not prove that either dissertation detector used such cues. | Full-text Section 4.1 and Table 1 inspected; USENIX title/authors record rechecked. Vault PDF available. |
| `pendlebury2019tesseract` | Different inferential scope of random cross-validation and time-ordered malware evaluation. | Full-text Section 3 and Table 1 inspected; USENIX title/authors record rechecked. Vault PDF available. |
| `gao2024comprehensive` | Performance changes under drift and other challenging conditions in independently evaluated Android detectors. | Full-text Section 4.3 and its interpretation inspected; Crossref title/authors/DOI rechecked. Vault PDF available. |

Before writing the review, `references/refcheck.py audit content/discussion.tex --strict`
passed: five citations, five available PDFs, zero unresolved entries. Temporary extracted
reference text and primary metadata were kept under `tmp/chapter7-critical-review-2026-09-19/`
during the review.

## Log

- 2026-09-19 created
- 2026-09-19 Review saved in `notes/chapter7-critical-review-2026-09-19.md`. Recommends
  retaining the chapter, cutting repeated detail and Table 7.1, and considering four connected
  sections subject to author approval. Identifies a SWaT selection-language conflict, two
  useful coverage deductions, and dependent wording changes in Chapters 3 and 5. The reference
  audit and workflow check pass. File/line links are valid; no LaTeX, bibliography or PDF
  changes were made, so no rebuild or visual review was performed.
- 2026-09-19 in-progress -> review (Critical review and revision proposal complete; structural changes await author approval; LaTeX and PDF unchanged)
