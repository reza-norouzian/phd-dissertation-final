# Source-publication issues and unresolved evidence

Re-established on 20 September 2026 under T-025. The earlier ledger named in `AGENTS.md`
was absent from the available repository and its history. This is a bounded index reconstructed
from the current chapters and surviving review tickets, not a recovered historical ledger.
Older issue numbers and decisions are not recreated.

## Status keys

- **corrected**: the dissertation corrects the source interpretation or supplies the supported
  formulation. The underlying publication is not modified.
- **declared**: the issue remains in the historical evidence and is stated as a limitation or
  qualification in the dissertation.
- **open**: evidence or an author decision is still needed; the entry states what is missing.

Editorial changes do not supply missing predictions, experimental settings or selection records.
Only mark an empirical issue corrected when the supporting record warrants it.

## Current issues

| ID | Source / issue | Status | Dissertation treatment and evidence |
| --- | --- | --- | --- |
| HY-01 | Hybroid's source category counts conflict with the official CICAndMal2017 listing | corrected | Chapter 4.4 uses the verified source-corpus composition; T-021 and the Chapter 4 review record the correction. |
| HY-02 | Extraction failures and the comparison cohort | declared | T-012 records the common retained cohort. Chapter 4.4 and 4.12 distinguish processing coverage from classification performance; the excluded applications' class labels remain unavailable. |
| HY-03 | Opcode/operand explanation and the untested power-law interpretation | corrected | Chapter 4.5 separates opcode abstraction from graph extraction and treats the frequency figure as descriptive; T-021. |
| HY-04 | Block-weighting rule and application-level composition are incompletely specified | declared | Chapter 4.5-4.6 and 4.12 retain these limits. The source does not establish the missing implementation choices; T-019/T-021. |
| HY-05 | Metric averaging, preprocessing boundaries and prospective evaluation | declared | Chapter 4.4, 4.9 and 4.12 preserve the published scores and distinguish missing conventions from evidence of leakage. Random splits do not establish later-period performance. |
| HG-01 | Construction and attention change together; no isolating ablation | declared | Chapter 5.13-5.14 and Chapters 7-8 restrict attribution to complete configurations. T-022/T-024 preserve that scope. Under D-007/T-031, RQ3 no longer asks for the attention effect; it remains a declared qualification of the answer. |
| HG-02 | Published Macro-F1 columns contain incompatible class-averaging values | corrected | On 21 September 2026 the author supplied corrected five-run macro means for five rows and confusion-matrix summaries for the three Drebin binary evaluations. T-032 independently reproduces every binary value. Chapter 5 reports the corrected rows and states the class and run averaging conventions; the source publication remains unchanged. |
| HG-03 | Interprocedural scope of the slicer is not fully documented | open | Original implementation or an author-confirmed specification is needed to establish which cross-method dependencies are traversed. The general slicing definition added in Chapter 2 does not resolve this; T-020 priority 2 remains separate. |
| HG-04 | Scope of corpus-wide feature fitting and related preprocessing settings | open | The original fitting boundary and implementation records are needed. No training-only boundary is inferred from the Chapter 2 reporting criteria; T-020 priority 2. |
| HG-05 | Run-level uncertainty, fixed random partitions and corpus-curation limits | declared | T-032 records five training seeds on shared fixed splits and five-run mean metrics for all five configurations. Individual scores are unavailable, so between-run SD and significance remain unreported. Partition sensitivity and remaining curation questions are unresolved. |
| SA-01 | D7.6's SD task label conflicts with the technical attribute-model description | declared | Chapter 6.5 and 6.8 preserve the official table and separate it from the described submissions; T-003. |
| SA-02 | Contest plan includes independent attacks but none were submitted | declared | Chapter 6.4 and 6.9 separate the planned and delivered protocols. No retrospective adaptive evaluation is implied. |
| SA-03 | Best/worst contest aggregates are not linked to common checkpoints and attack configurations | declared | Chapter 6.8 does not reinterpret these aggregates as matched worst-case outcomes. Historical run-level records are needed for reproduction. |
| SA-04 | Benchmark code can score raw rather than budget-clipped candidates and use target-label agreement in fields called accuracy | declared | Chapter 6.6 identifies the public code revision and distinguishes these findings from the unrecorded historical runs. The archived software is not changed by the dissertation revision. |
| SA-05 | Accuracy-loss ranking can reward low-utility constant predictions | declared | Chapter 6.8 derives the score's behaviour and reports clean and attacked utility together. Existing aggregate scores are preserved. |
| SW-01 | SWaT configuration-selection history | open | Chapter 3 states a validation-only selection procedure but also motivates the final PCA choice with the reported test-table F1. The original selection record or an author clarification is required. Chronology alone does not establish selection independence; the Chapter 7/8 reviews already flag this question. |
| SW-02 | SWaT representation table carried rounded precision and recall, and the PCA-24 confusion counts were derived from them | corrected | On 24 September 2026 the author supplied the recorded TP, FP, FN and TN counts for all five input representations (393,679 timestamps, 51,453 anomalous). Every precision, recall, $F_1$ and false-positive rate was recomputed from these counts and matches the author's table. Chapter 5 (Table 5.6, the PCA-24 confusion matrix, the derived measures and durations), the abstract (English and German) and the conclusion report the corrected values. This settles examiner-review item M5. |
| LT-01 | Fang et al.'s categorical attention statement conflicts with its Table 2 | corrected | T-025 uses task-dependent reported means in Chapters 2 and 5. No statistical-superiority claim is inferred from those means. |

## Source-record maintenance completed under T-025

- PScout's permission count is separated from its documentation findings in Chapter 2.
- Wolsing et al.'s literature-review population is distinguished from its empirical comparison.
- Maali et al.'s device-identification results are labelled with their actual prediction task.
- The Wang/Kleinberg title is corrected to **Hypergraph Projection and Its Remediation**.
- The canonical PDF for `pierazzi2020intriguing` is the four-author March 2020 manuscript
  (arXiv v2), not the six-author 2024 extension.
- The Chapter 2 source-record index links the current writing-ticket evidence.

## Supporting records

- [Chapter 4 review](chapter4-critical-review-2026-09-20.md) and T-019/T-021.
- [Chapter 5 review](chapter5-critical-review-2026-09-20.md) and T-020/T-022/T-024.
- [Chapter 7 review](chapter7-critical-review-2026-09-19.md) and
  [Chapter 8 review](chapter8-critical-review-2026-09-20.md).
- Chapter 6 revision ticket T-003 and Chapter 2 revision ticket T-025 (the ticket system was
  removed on 23 September 2026; both remain in git history).

Consult the original publications and internal research records before resolving an empirical
entry. This index records where the current dissertation handles a problem; it is not itself
verification of a scientific claim.
