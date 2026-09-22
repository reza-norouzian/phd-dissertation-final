# Dissertation: supervisor-style review

21 September 2026. Reviewed all eight chapters, both abstracts, front matter and Appendix A,
using only the dissertation and supporting material in `thesis-v2`. Page numbers below are the printed
numbers in the current 153-page PDF. This was a scientific review, not a visual-layout review.

## Overall assessment

The dissertation has a coherent structure and identifiable contributions. I would request
major revisions before submission. The main weaknesses concern the verification and
reproducibility of the experiments, rather than a missing chapter or insufficient background.
Several weaknesses are already disclosed, but disclosure does not resolve them.

## Potentially critical

**1. Establish whether a training/test bug affected NADICS results.**
The archived code assigns the encoded test data to both the training and testing variables
(`publications/Anomaly Detection/NADICS_repo/nadics/main.py:202`). This is a confirmed code
defect; its effect on the reported S7-300 experiment is **unconfirmed**. Identify the exact
evaluated revision and verify sample separation. If that experiment used the defective path,
its results require re-evaluation. Location: Section 3.4, pp. 28-36.

## High priority

**2. Resolve conflicting accounts of test independence.**
Section 3.5 says validation selected the configuration, but later adopts PCA because of its
reported test F1. Reconcile this account against the experiment's selection records.
Hybroid's fitting boundaries and HGANN-Mal's normalisation
“across the corpus” also need an explicit account of which samples each fitted stage used.
Locations: Sections 3.5-3.6, 4.7-4.8 and 5.6.

**3. Supply a reproducible specification and evidence package.**
Key steps remain unspecified, especially Hybroid's application-vector construction and
HGANN-Mal's cross-method slicing. If the latter stays within one method, its slice hyperedges
would be discarded as singletons. Identify the implemented procedure and retain matching
configurations and run outputs. Matching outputs for the revised industrial experiments
were not located in this checkout. Locations:
Sections 3.4-3.5, 4.5-4.6 and 5.5-5.9.

**4. Resolve the metric inconsistencies.**
Four HGANN-Mal rows contain F1, precision and recall values incompatible with a common
averaging convention, even after rounding. Hybroid's averaging convention is also unresolved.
Recompute from predictions where possible. Otherwise, retain the affected scores as historical
records and exclude them from quantitative gain claims. The corrected Drebin matrix-derived
F1 distinction should remain. Locations: Sections 4.9-4.11 and 5.10-5.14.

**5. Strengthen the evidence for the main Android improvements.**
HGANN-Mal changes construction and attention together; its single runs do not establish
stable gains. Hybroid supplies rounded fold means without paired outcomes. Prioritise a
matched construction/attention ablation with repeated runs. Duplicate and collection-source
controls would test whether dataset shortcuts explain some performance. Until then, retain
the present restriction to descriptive, within-study comparisons. Locations: Sections 4.11-4.12
and 5.9-5.14.

**6. Complete the validation behind the reproducible-benchmark claim.**
The public SAFAIR code scores raw rather than budget-clipped attack outputs, and the
historical results lack complete run configurations. Supply a budget-checked, reproducible
example if validated benchmark software remains a central claim. Chapter 6 already supports
a design and metric-analysis contribution; it does not establish a general relation between
clean accuracy and robustness. Locations: Sections 6.6, 6.8 and 6.11.

## Before submission

Replace the title-page metadata and acknowledgements placeholders. The strict reference audit
passes for all 177 cited keys; all 165 cited PDFs exist and match their recorded hashes.
No dissertation text or PDF was changed. Detailed evidence and conditional findings are
recorded in [T-028](workflow/tickets/T-028-review-the-dissertation-end-to-end-for-critical-and.md).
