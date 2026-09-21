---
id: T-032
title: Correct HGANN-Mal result reporting across the dissertation
status: review
priority: P1
chapter: 5
owner: codex
depends_on: []
blocks: []
tags: []
created: 2026-09-21
updated: 2026-09-21
---

## Goal

Apply the author's corrected class-averaged metrics while retaining the confirmed fixed-split,
five-seed protocol and five-run mean reporting.

## Why it matters

The author supplied corrected metrics on 21 September 2026 after identifying values that
violated the relation between precision, recall and their harmonic mean. Three corrected
Drebin binary rows follow from complete confusion-matrix summaries. The author then confirmed
that the results still describe five training runs, not single-run evaluations. This correction
changes the affected macro metrics without changing the established aggregation protocol.

## Acceptance criteria

- [x] State the protocol and five-run metric aggregation in Chapter 5 and its table/figure captions.
- [x] Replace single-run qualifications with the actual limits: missing individual scores and fixed-partition scope.
- [x] Distinguish aggregate-matrix metrics from mean run metrics; following the author's later
  decision, remove dissertation reporting of the unresolved class-averaging issue.
- [x] Align the Introduction, background aggregation discussion, Discussion, Conclusion and both abstracts concisely.
- [x] Update the current plan, defect ledger and figure provenance without rewriting historical reviews.
- [x] Preserve table bodies, equations, method architecture and figure assets; add no inferred SD, confidence intervals or significance claims.
- [x] Pass strict reference audits, rebuild the tracked PDF and read the build log; no visual review.
- [x] Pass the workflow check and leave all changes unstaged.

### Superseding correction

- [x] Record the five corrected rows and three supporting confusion matrices before editing.
- [x] Replace the affected table cells and every dependent numerical comparison.
- [x] Retain the five-run-mean interpretation and align the confusion-matrix discussion with it.
- [x] Update the F1 figure without overwriting the author-supplied source PDF.
- [x] Mark HG-02 corrected and align HG-05 with the evidence now available.
- [x] Pass strict reference audits, the figure-data check, a LaTeX rebuild and the workflow check.

## Evidence and sources

### Claim-to-source record, before drafting

| Source | Supported claim | Full-text / reference-vault status |
| --- | --- | --- |
| Author's confirmations in this conversation, 21 September 2026 | Five different training seeds for every configuration and all four baselines; common fixed train/test/validation split; all metrics are five-run means; Drebin matrix aggregates the five runs. | Primary experimental clarification. Initial confirmations logged under T-020; the all-metric and matrix clarifications are recorded here. No external citekey or fabricated publication record. |
| `norouzian2025hgannmal` | Published results in both corpora, model comparisons and task definitions; numerical values remain unchanged. | Original LaTeX evaluation and both complete result tables inspected again. Metadata verified against Crossref DOI 10.1007/978-3-032-08124-7_23 on 21 September. Vault PDF physically present, 501,922 bytes, SHA-256 prefix `aeb85cda2fa1e68a`, matching the existing MANIFEST record. The publication omits repetition details; the author supplies that clarification. |
| Chapter 2, Equation `eq:background:run-aggregation` and metric definitions | A mean of nonlinear F1 scores need not equal F1 from aggregate counts. The inequality F1 <= (P+R)/2 under common class weighting survives arithmetic averaging over runs. | Existing dissertation derivations read; no new bibliographic claim or citekey. |

The author's later correction in the same conversation confirms this five-run interpretation
while replacing the five inconsistent result rows.

### Claim-to-source record for the superseding correction

| Source | Supported claim | Full-text / reference-vault status |
| --- | --- | --- |
| Author's corrected result record in this conversation, 21 September 2026 | Corrected five-run mean rows: Drebin binary GCN `(F1, P, R, Acc.) = (92.2, 93.0, 91.5, 92.8)`, HGNN `(96.6, 96.8, 96.3, 96.8)`, and HGANN-Mal `(98.2, 98.2, 98.2, 98.3)`; Drebin family HGANN-Mal `(93.9, 94.1, 93.8, 95.0)`; CICMalDroid category GCN `(82.2, 82.0, 82.4, 82.7)`. | Primary experimental correction supplied for the dissertation. The author explicitly confirmed that these are five-run results. No citekey applies. The original publication remains an unchanged historical source. |
| Author-supplied confusion-matrix summaries in this conversation, 21 September 2026 | Drebin binary `(TP, FN, FP, TN)`: GCN `(962, 150, 66, 1828)`, HGNN `(1049, 63, 33, 1861)`, HGANN-Mal `(1085, 27, 24, 1870)`. Each totals 1,112 malicious and 1,894 benign applications. | Primary experimental record for the five-run evaluations. Independent arithmetic reproduces every corrected binary row after rounding to one decimal place. The per-run matrices and the exact aggregation procedure remain unavailable. |
| `norouzian2025hgannmal` | Model definitions, task definitions and the unaffected result cells. Its printed values in the five corrected rows are retained only as publication history. | Complete source and vault record already inspected as documented above. |

No new bibliographic source is needed because the numerical correction and evaluation scope come
from the author. The existing strict audit remains the pre-drafting citation gate.

Pre-drafting strict audit: `references/refcheck.py audit content/hgann-mal.tex --strict`
passes for 37 keys, 36 PDFs and one documented web resource, with zero items needing attention.
No new source or citekey is required.

### Evidence boundaries

- Individual scores, exact seed identifiers and individual confusion matrices have not been supplied.
- The proposed SD/band table was confirmed to use accuracy and test-set size. Its values are
  binomial approximations, not empirical seed variability; do not insert them as run uncertainty.
- The supplied aggregate matrix totals 3,006, the size of one test partition. Its precise
  scaling/rounding procedure has not been supplied. Describe the reported aggregate and its
  derived rates without treating its cells as summed counts from 15,030 independent applications.
- The previous single-matrix feasibility argument should not be applied unchanged to mean
  precision/recall. The four violations of F1 <= (P+R)/2 remain valid under common run averaging.
- Initial build log: 153 pages, 21 warning messages, 48 underfull boxes, no overfull boxes or
  undefined references, and one pre-existing end-group notice. Snapshots are in ignored
  `tmp/hgann-five-runs-2026-09-21/`.
- The existing workflow check fails because T-031 names absent T-030 as a formal dependency.
  No T-030 file is recoverable from repository history. Preserve the historical reference in
  T-031's prose and remove the dangling machine-readable edge; do not reconstruct missing evidence.

## Log

### Outcome

- Chapter 5 now states the five-seed protocol for all configurations, fixed shared partitions,
  and arithmetic means for all tabulated learned-model metrics. Both result-table captions
  and both performance-figure captions identify the aggregation.
- The single-run limitation is replaced by missing run-level uncertainty and unmeasured
  partition sensitivity. The aggregate-matrix discussion distinguishes calculated F1 from
  mean run F1. The old single-matrix feasibility argument is removed; the four class-weight
  inequality violations remain and were checked to survive run averaging and rounding.
- Chapters 1, 2, 7 and 8 and both abstracts use the same interpretation. Current planning,
  HG-02/HG-05 and the figure provenance are aligned. Historical reviews remain dated records.
- All table bodies, equation and algorithm environments, citation occurrences and figure
  references in the six changed LaTeX files match the pre-edit snapshots. Figure assets and
  empirical values are untouched. Chapter 5 text-token count excluding comments falls by 19;
  net change across the six files is +24.
- Strict audits pass: Chapter 5 has 37 cited keys; the six edited files together have 139,
  132 with PDFs and zero needing attention. No citekey was added.
- `latexmk thesis.tex` exits 0 and produces 153 pages. Chapter 8 remains pp. 115-116;
  front-matter starts remain unchanged. The log has the same 21 warning messages, underfull
  boxes decrease from 48 to 45, and there are no overfull boxes, undefined references or Biber
  warnings. The pre-existing end-group notice remains. Root PDF symlink is intact.
- Build recovery: incomplete auxiliary files caused the first failure. Concurrent compilation
  and cleanup by a separate Claude process were then observed overwriting the same output
  directory. No external process was terminated. The final build ran after that process ended;
  its successful output is saved in ignored `tmp/hgann-five-runs-2026-09-21/build-final.txt`.
- `git diff --check` and `wf.py check` pass. The T-031 dependency repair is documented there.
  No visual review, staging, commit or push.

### Follow-up: remove the Section 5.14 threats-to-validity paragraph

On 21 September 2026, the author directed that the closing paragraph of Section 5.14 be removed
in full and that the dissertation no longer report the unresolved F1 class-averaging issue. The
paragraph, caption warnings and related Section 5.11 sentence were removed. Forward references
that depended on the deleted material were also removed; the result values and table bodies remain
unchanged. HG-02 stays open in the internal defect ledger, which records this editorial decision.

The strict Chapter 5 audit passes with 35 citekeys and zero items needing attention. After a stale
VS Code LaTeX Workshop process blocked on a malformed auxiliary file was stopped, regeneratable
intermediates were cleaned and `latexmk thesis.tex` completed successfully. The PDF now has 151
pages, no undefined references or citations, no overfull boxes and no Biber warnings. The existing
end-group notice and warning classes remain; there are 45 underfull vboxes. No visual review,
staging, commit or push was performed.

### Follow-up: correct five inconsistent macro-metric rows

The author supplied corrected values for five rows and confusion-matrix summaries for the three
Drebin binary rows. A later message clarified that the table still reports five-run means; the
temporary single-run interpretation was reverted before the build. Chapter 5 now states both
the macro class averaging and the five-seed run averaging.

The binary table now reports GCN `(92.2, 93.0, 91.5, 92.8)`, HGNN
`(96.6, 96.8, 96.3, 96.8)` and HGANN-Mal `(98.2, 98.2, 98.2, 98.3)` in F1, precision,
recall and accuracy order. The multiclass table reports 93.9 F1 for HGANN-Mal on Drebin
families and 82.2 F1 for GCN on CICMalDroid categories. The Drebin family F1 margin over the
strongest baseline changes from 1.9 to 1.6 points; accuracy comparisons do not change.

The included F1 figure was regenerated as a thesis-native vector asset from
`figures/src/hgann-mal-f1.tex`; the author-supplied original remains byte-for-byte unchanged.
The figure checker now validates all table F1 bounds, derives the three corrected binary rows
from the supplied matrices and compares the included figure with the tables: 78 checks pass.
HG-02 is marked corrected, while HG-05 retains the missing individual-run and partition-variation
limits.

Strict audits pass for Chapter 5 and the five other aligned LaTeX files. After terminating one
stale LaTeX Workshop build that had occupied the shared output directory for over 18 minutes,
`latexmk thesis.tex` completed successfully. The thesis remains 151 pages. The log has 44
underfull vboxes, no overfull boxes, undefined references or citations, or Biber warnings; the
pre-existing end-group notice remains. The root PDF symlink is intact. No visual review,
staging, commit or push was performed.

- 2026-09-21 created
- 2026-09-21 backlog -> in-progress (Author approved the correction and confirmed that all metrics are five-run means and the Drebin matrix is an aggregate.)
- 2026-09-21 in-progress -> review (Five-run reporting integrated across the dissertation; citation audits, source preservation checks and PDF rebuild pass.)
- 2026-09-21 review -> in-progress (Shorten the Chapter 2 aggregation and operational-reporting background at the author's request and remove the run-SD/confidence-interval caveat.)
- 2026-09-21 in-progress -> review (Author-requested Chapter 2 simplification applied; specified caveat removed, strict audit and forced PDF rebuild pass.)
- 2026-09-21 review -> in-progress (Remove the repeated run-uncertainty caveat from Section 7.3 and keep its synthesis contribution-led, at the author's request)
- 2026-09-21 in-progress -> review (Author-requested Section 7.3 reframing applied; strict audit, source-stable rebuild and workflow checks pass)
- 2026-09-21 review -> in-progress (Author supplied corrected macro metrics for five rows and clarified that the supporting Drebin matrices describe individual evaluations; align the thesis and resolve HG-02.)
- 2026-09-21 in-progress -> review (Five corrected five-run macro rows integrated; figure, audits, algebra checks and PDF rebuild pass)
