# Chapter 4: scientific review and revision proposal

Date: 20 September 2026. Review ticket: T-019. The author approved the proposal, which was
implemented under T-021 on the same date. The findings below describe the pre-revision chapter;
the final implementation summary is in Section 6.

The review concerns [Chapter 4](/Users/reza/code_repo/PhD/thesis-v2/content/hybroid.tex).
All line ranges below refer to its pre-revision version unless another file is named. The review
itself made no LaTeX, bibliography or PDF changes; the subsequent approved implementation did.
No PDF visual review was performed.

## Recommendation

Retain the chapter's thirteen-section structure and its reported results. Revise the technical
explanations, correct citation-to-claim mismatches, and consolidate repeated qualifications.
Add a small number of equations where they define an operation or expose a limitation. Aim
for the same overall length or a shorter chapter.

The strongest contribution is the within-system modality comparison: reported detection F1
improves by one or two percentage points with fusion, while category classification depends on
the learner. The common 2,079-application cohort, the distinction between binary and five-class
tasks, and the explicit decision-tree exception should remain. Preserve the candidate's
partial contribution to graph processing and the conceptual, rather than numerical or
historical, comparison with HGANN-Mal.

The main weakness is the balance between explanation and commentary about the source paper.
Several passages read as an audit of the publication. A dissertation should explain the method
directly, then state the particular uncertainty that limits a claim.

## 1. Corrections needed before stylistic refinement

### 1.1 Correct the opcode rationale

**Sections 4.5-4.6, lines 252-307 and 391-394.**

- Dalvik operands include literals and references to strings, types and methods, as well as
  register indices. The AOSP documentation does not support treating all operands as runtime
  register values. Describe opcode-only embedding as a deliberate abstraction with a bounded
  vocabulary and loss of operand information.
- A frequency plot does not establish a power law, and a power law is not a prerequisite for
  skip-gram. Explain the objective through local opcode co-occurrence. Retain the plot as an
  empirical frequency description, without presenting its shape as proof of validity.
- A fixed instruction vocabulary does not establish generalisation or test-set independence.
  Separate vocabulary coverage from the inductive application of a trained graph encoder.
- The feature and edge extraction steps need not be statistically independent or implemented
  as separate passes. The precise statement is that opcode embeddings omit callee identity,
  while graph construction can use call operands.

The operand explanation also occurs in
[Chapter 2, lines 63-73](/Users/reza/code_repo/PhD/thesis-v2/content/background.tex#L63).
A later approved correction should keep the two chapters consistent.

### 1.2 Make the pipeline internally consistent

**Sections 4.1, 4.6, 4.8 and 4.10, especially lines 24-26, 38-41, 382-389, 515-530 and 645-649.**

The opening suggests detection followed by classification into four malware categories.
Section 4.10 describes a separately evaluated five-class task that includes Benign. State the
two prediction tasks consistently; do not imply an evaluated cascade.

The architecture caption calls the fusion concatenation, while Section 4.8 says the operator
is not named. Resolve that disagreement before adding a concatenation equation. Preserve the
reported 64 static and 13 dynamic dimensions, but do not infer static dominance or a need for
reweighting from their counts. Feature count alone does not determine classifier influence.

Distinguish block embeddings, per-method CFG embeddings and the application-level vector.
The original paper defines a CFG pooling step but does not fully specify the application-level
composition. Formal notation must preserve that boundary. Similarly, describe the unspecified
weighting rule as under-specified, rather than saying the weighted-mean formula is inherently
undefined.

### 1.3 Correct the literature classification and update one source version

**Section 4.2, lines 82-93, 116-127 and 147-158.**

Arora et al. (2014) and Zulkifli et al. (2018), currently cited for permission-based static
analysis, describe network-traffic methods. Li et al. (2019) and Chen et al. (2018) describe
manifest/API feature vectors, not the graph-based category suggested by their placement.
Reassign the citations to the claims their methods support. DREBIN already supplies a verified
source for static permission and manifest features.

Comparetti et al. concerns dormant functionality in malware binaries. It is not direct
evidence for the specific Android manifest-rewriting claim. Narrow that claim or use a
verified Android-specific source after checking its full text.

MARVIN includes a static/dynamic/combined comparison in Section V-C and Figure 3. Citing it
does not establish that such comparisons are rare across the field. Frame the contribution as
Hybroid's matched comparison for its particular representations and tasks. If field-wide rarity
is retained, it needs review-level evidence. The same issue appears in
[G2 in Chapter 2](/Users/reza/code_repo/PhD/thesis-v2/content/background.tex#L579).

The current [arXiv record for Tran et al.](https://arxiv.org/abs/2508.06734v3) changed on
16 September 2026. Version 3 is titled *Evaluating Out-of-Distribution Robustness in
Graph-Based Android Malware Classification: A New Principled Benchmark*, and the record
states acceptance at IEEE DSAA 2026. The local bibliography and vault use the earlier title
and v2. The chapter's present-tense description as a preprint under review is stale. Update the
title, version and status together if approved, without inventing a proceedings DOI.

### 1.4 Narrow the network and threat-model claims

**Sections 4.3, 4.7 and 4.12, particularly lines 173-177, 417-425, 452-498, 773-795 and 834-847.**

Low reported TLS use does not establish that all other traffic is cleartext. Table 4.3 leaves
27.73-70.78% of the flows uncharacterised, and encryption can occur outside TLS. Retain the
valid conclusion: performance on encrypted traffic was not evaluated separately. Android's
default cleartext policy also needs its target-API qualification and allowance for opt-in.

The ThirdEye figure of 22.92% covers custom encryption/decryption for network transmission
and shared storage. It should not be restated as the proportion encrypting network content
alone. The statement that flow features have become the only available option is too broad;
the cited study itself uses instrumentation to investigate encrypted content.

TCP sequence-number unpredictability does not prove statistical independence from application
labels or capture conditions. Describe possible endpoint/capture confounding, not an
impossibility of carrying any application-associated information. Flood et al. supports a
mechanism observed in another corpus, not a measured effect in Hybroid.

Averaging removes inter-flow ordering and variation, but it retains means of recorded temporal
features such as duration. Clarify that an averaged `TotBytes` feature is mean transaction
bytes per record, not total bytes for the application capture. Low pairwise Kendall correlation
also does not prove independence or absence of nonlinear redundancy.

FCGHunter's construction includes executable no-operation-like methods as well as unreachable
calls. Restrict the unchanged-traffic hypothesis to transformations for which it is applicable;
even functional preservation does not establish identical timing-dependent flow features.
Neither cited attack measures Hybroid's robustness.

### 1.5 Improve the statistical interpretation without changing results

**Sections 4.4 and 4.9-4.12, especially lines 230-246, 552-590 and 765-812.**

The identity relating accuracy, precision, recall and class prevalence is useful for one
binary confusion matrix with a specified positive class. Inserting separate cross-validation
means into that nonlinear identity does not reconstruct a pooled confusion matrix. Present
the calculation as a conditional consistency diagnostic, and distinguish fold averaging from
class averaging. Do not treat it as proof that the reported experiments are invalid.

Five-fold cross-validation and a common cohort do not by themselves establish identical fold
assignments across configurations, training-only feature selection or nested model selection.
State what the paper documents, qualify stronger assurances, and do not infer that leakage
occurred. Apply the temporal-validity qualification to the principal experiment as well as the
larger static-only experiment. A large sample count demonstrates application at that scale,
not a computational scaling law or measured efficiency.

Judge external baselines by matched inputs, tuning and evaluation definitions. Paper length
is not a measure of scientific strength. A short poster can leave reproduction details
missing, but page count alone is not a reason to discount its result.

An additional check deserves a short source note: the five displayed class AUCs average to
0.9748, whereas the reported macro AUC is 0.976. Rounding of those five values alone does not
explain the difference. Averaging/interpolation procedures may matter; preserve the reported
0.976 and its status rather than silently replacing it with a recalculation.

## 2. Mathematical additions with a clear purpose

The chapter has three displayed equations, all within the graph update. More useful mathematics
would define the surrounding operations. The following are proposals, not recovered
implementation details.

| Location | Proposed addition | Scientific purpose and evidence boundary |
| --- | --- | --- |
| 4.5 | Canonical skip-gram log-probability objective, with opcode/context notation. | Explains what is learned and replaces the power-law justification. Cite Mikolov et al.; do not assert a particular optimiser or negative-sampling configuration for Hybroid. |
| 4.6 | Restore the per-method CFG readout from original Algorithm 1 and define dimensions. | Completes the documented message-passing operation; it does not define the missing application-level composition. |
| 4.7 | Express flow-record averaging and min-max scaling. | Makes the application-level observation unit and the meaning of averaged features explicit. State training-fold-only fitting as a requirement unless the historical procedure is confirmed. |
| 4.11 | Define the fusion gain already used in the results table. | Connects RQ2 to a precise comparison of reported mean scores, separately for each task and learner. |

For the CFG readout, the original algorithm supports

\[
h_f = W_2\left(\frac{1}{|V_f|}\sum_{v\in V_f}\mu_v^{(T)}\right),
\]

where \(V_f\) contains the basic blocks of method \(f\). The output dimension should remain
symbolic unless documented; do not assign the application's 64 dimensions to every intermediate
method vector. Hybroid reports random initial states, whereas the original structure2vec
algorithm uses zeros. Retain the distinction between an adaptation and its methodological source.

For fusion, define

\[
\Delta_M = \overline M_{\mathrm{fusion}}-
\max\!\left(\overline M_{\mathrm{static}},\overline M_{\mathrm{dynamic}}\right).
\]

This is the difference of reported mean scores, not a mean of foldwise maxima. For gradient
boosting, the reported F1 contrast is 0.97 minus 0.95 for detection, and 0.94 minus 0.91 for
categorisation. Those are descriptive differences, not significance tests.

A short optional derivation could show that a mean of extracted flow vectors is invariant to
their reordering. This establishes an information-loss property of the representation, not a
malware-detection guarantee. A theoretical benefit should not be presented as an experimentally
measured source of the observed fusion gains.

## 3. Repetition and prose to refine

| Repeated material | Recommended treatment |
| --- | --- |
| Unspecified metric averaging and absent fold dispersion in 4.4, 4.9-4.13. | Explain the convention issue once near the results. Keep only the short qualification needed beside each conclusion. |
| Decision-tree fusion loss in 4.10-4.13. | Explain it in 4.10 and quantify it in 4.11; remove the repeated numerical paragraph in 4.12. Retain a brief summary of learner dependence. |
| Unspecified weights and application pooling in 4.5, 4.6 and 4.12. | Define the scope beside the method, then consolidate the limitation without repeating the source criticism. |
| TLS percentages and observation exclusions in 4.3, 4.7 and 4.12. | Keep the protocol data in 4.7 and its external-validity interpretation in 4.12. Use 4.3 to define available observations. |
| Historical positioning and promises of later discussion. | Section 4.2 promises a return to HGDetector in 4.11, and 4.8 promises later accumulated evidence, but 4.11 contains neither. Remove those promises or supply a brief, accurately scoped comparison. |

Examples of concise replacements:

| Current wording | Proposed direction |
| --- | --- |
| “An accuracy figure for the combined system answers nothing on its own.” | “RQ2 requires a comparison with each single-modality model on the same evaluation cohort.” |
| “the company an operation keeps” | “the local opcode co-occurrence patterns” |
| “a reader who meets both without warning will take one of them for a mistake” | State the distinct roles of the representation-learning classifier and final classifier. |
| “which leaves the mean undefined” | “the publication does not specify the weighting rule” |
| “Its consequences were not visible in 2021.” | Describe feature-level fusion and the measured comparison; remove the unsupported historical assertion. |

Retain useful cross-references, but remove sentences whose main purpose is to announce what a
later section will say. Shorten the long opening and summary sentences by separating the
representation definition from the empirical result.

## 4. What can be added now, and what needs further evidence

**Available for an approved revision:** corrected technical prose and citation placement;
source-supported mathematical definitions; consistent task/fusion terminology; a concise
statement that results concern the successfully processed cohort. The confirmed exclusion
policy gives coverage of \(2079/2126=97.79\%\). This is processing coverage, not detection
accuracy, and does not assign labels or predictions to the excluded applications.

**Needs surviving records or new evaluation:** the exact block-weight rule and application
graph readout; reproducible fold/model-selection history; confidence intervals or significance
tests; per-class precision/recall and confusion matrices; feature-confounding ablations;
performance on failed extractions, newer traffic or adversarially modified APKs. Keep these
separate from editorial improvements. Do not restore the pending markers removed under T-011,
and do not reopen T-012's confirmed common-cohort decision.

## 5. Reference-check scope and approval order

The strict audit passes for all 43 citations: 39 PDFs and four recorded web resources.
That checks the bibliography/vault record, not whether each sentence follows from its source.
The review read the original Hybroid manuscript in full and inspected relevant primary full-text
passages for the findings above. It did not perform a new exhaustive review of all 39 papers.

Live Crossref records were retrieved for 34 DOI-bearing entries; Chen et al. was checked
against the publisher PDF. Official NeurIPS/PMLR records and Android documentation were also
checked, together with the CICAndMal2017 family listing and arXiv version records. The detailed
claim-to-source record is in
[T-019](/Users/reza/code_repo/PhD/thesis-v2/notes/workflow/tickets/T-019-critically-review-chapter-4-scientific-writing-and-m.md).
At the review stage, vault and bibliography files remained unchanged. The missing legacy defect ledger and
source-record directory limit archival reconstruction; no missing experimental detail was inferred.

Recommended sequence after approval:

1. Correct the scientific statements and their citations, with narrow Chapter 2 consistency edits
   only if authorised.
2. Consolidate repetition and revise the prose within the existing structure.
3. Add the selected equations and recheck their assumptions, then run the citation audit and
   compile. Leave PDF visual review to the author.

## 6. Approved implementation

T-021 applied the scientific and readability revision on 20 September 2026. The chapter retains
thirteen sections; Section 4.5 now uses the planned title, Opcode and Basic-Block Representation.
The revised text removes the field-wide rarity claim and misplaced citations, clarifies the
separate binary/five-class tasks, and resolves the fusion-caption contradiction without inventing
an undocumented operator. The graph-encoder description distinguishes basic blocks, methods
and the application-level vector. The observation section explains offline use and the need
for an APK/capture pair.

The added formalism comprises the canonical skip-gram objective, the published CFG readout,
flow averaging and scaling, a displayed conditional metric identity, and the fusion contrast.
The constant-benign reference of 79.5-81.8% accuracy is calculated from the possible cohort
counts, not reported as a new experiment. Repeated metric qualifications and source commentary
were consolidated, including the repeated decision-tree exception in the limitations section.
The weights and application-level composition remain explicitly under-specified.

Two related Chapter 2 passages were corrected: the description of encoded operands and the
G2 motivation. The Tran citation and reference-vault PDF were synchronised with arXiv v3, and
an official CICAndMal2017 web citation was added for the corrected family counts. Other chapter
text and all figure assets were left unchanged.

Verification:

- All numeric table entries, all section labels and all included figure paths are preserved.
  Hash checks confirm that all ten Hybroid PDF assets, including the nine used figures, are unchanged.
- The algebra checks cover the confusion-matrix identity, mean/scaling properties, six F1
  contrasts and the arithmetic mean of the displayed class AUCs. These are analytical checks,
  not new empirical evaluations.
- Main prose decreases from 6,226 to 3,838 words (38.4%); caption text decreases from 739 to
  593 words. Displayed equations increase from three to nine.
- Strict audits pass for Chapter 4 (40 citations) and Chapter 2 (110 citations).
- `latexmk thesis.tex` succeeds. Chapter 4 occupies printed pages 45-60, with Chapter 5 from
  page 61; the full PDF decreases from 155 to 151 pages. There are no undefined citations or
  references and no overfull boxes. The 39 underfull notices, template warnings and existing
  end-group warning remain; no new package/class warning types appear.
- The root PDF symlink remains intact. No visual review, staging, commit or push was performed.
