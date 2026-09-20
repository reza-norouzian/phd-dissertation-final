# Chapter 5: scientific and editorial revision proposal

Date: 20 September 2026. Review ticket: T-020.
The author subsequently approved priorities 1, 4 and 5 from the five-row conversational
proposal. Their implementation is recorded under T-022. The author later approved the priority-3
interpretation passages; T-024 records their insertion and the related consistency corrections.
Priority 2 (method specification) remains outside the requested revisions. The shared metric
definitions were added to Chapter 2 under T-023; further Chapter 5 mathematics was not requested.
The review itself changed no dissertation
LaTeX, bibliography or PDF; the findings and line locations below describe the pre-revision
`content/hgann-mal.tex`.

T-022 retains the published table and figure values and identifies the matrix-derived Drebin
F1 of 97.7% separately. It reduces main prose from 9,892 to 8,285 words, scopes the literature
claims and removes the obsolete example references. All 23 numbered equations, the algorithm,
and the table bodies remain unchanged. The rebuilt thesis has 149 pages, with Chapter 5 on
printed pages 61-87 and a recto-opening blank on page 88. No visual review was performed.

## Assessment

The chapter contains a substantial method description and useful mathematical analysis. Its
construction algorithm, explicit propagation operator and distinction between family and
category classification provide a sound basis for revision. The energy identity, attention
ranking result and sparse-computation bounds serve scientific purposes. The chapter already
has 23 numbered equations; increasing that count is not the main priority.

The most useful revision would improve the precision of the empirical claims and specify the
implemented procedure more clearly. Several passages read as commentary on the source paper
or on the writing process. Repeated qualifications interrupt the account of the contribution.
Retain the chapter structure and shorten these passages to make room for a compact description
of the experimental configuration. Preserve the concise limitations section requested in
T-009 and the removal of the synthetic worked example requested in T-010.

## 1. Corrections supported by the current evidence

### 1.1 Reconcile the Drebin binary F1 with the confirmed confusion matrix

Locations: lines 890-909, 967-979 and 1223-1231, Table 5.2 and Section 5.14.

T-008 establishes the matrix as empirical. The chapter reports TP = 1,085, FN = 27,
FP = 24 and TN = 1,870, over 3,006 test applications. These counts give

\[
F_1=\frac{2TP}{2TP+FP+FN}=\frac{2170}{2221}=97.7037\%.
\]

The rounded value is 97.7%, while Table 5.2 reproduces the paper's 97.8%. Precision, recall
and accuracy do round to the corresponding published values. The description of this entire
row as positive-class metrics is therefore incomplete.

**Proposal:** distinguish the published number from the value calculated from the confirmed
matrix, then obtain the author's approval for the presentation. Preserve the provenance of
both. Do not silently alter the source table or manufacture revised values for other rows.
F1 comparisons elsewhere need caution because the chapter already establishes inconsistent
averaging conventions. Accuracy remains interpretable as the reported metric, subject to the
experimental limitations.

This proposal does not reinstate the CICMalDroid binary-row analysis removed under T-009.

### 1.2 Correct the interpretation of macro-F1

Location: lines 1021-1026, Section 5.11.

An aggregate macro-F1 of 94.2% does not require every small family to perform nearly as well
as every large family. Equal class weighting prevents large classes from dominating the
average, but an average can conceal poor individual classes. Moreover, the averaging
convention for this row remains unresolved.

**Proposal:** describe equal class weighting without the per-family inference. Per-class
scores and supports would answer the question if predictions are available. No new worked
example is needed in the chapter.

### 1.3 Align the conclusion with the comparison actually performed

Locations: lines 940-958, 1042-1055 and 1252-1264, Sections 5.10, 5.12 and 5.15.

Common call graphs and features control input differences. They do not isolate the effect of
representation from the operators and other model settings. The statement that the difference
therefore belongs to the representation is too categorical. The stronger interpretation also
conflicts with the complete-configuration framing now used in Chapters 7 and 8.

The 97.6% versus 97.7% CICMalDroid binary accuracies are observed point estimates. Calling the
systems "level" does not establish statistical equivalence. Likewise, the larger multiclass
margin supports a description of these experiments, not a general rule that grouping helps
multiclass decisions most.

**Proposal:** lead with the reported system-level accuracy differences. Keep the contribution
of attention as an unresolved attribution question. Identify behavioural explanations as
hypotheses and omit them where the chapter offers no discriminating evidence.

### 1.4 Remove the remaining references to the deleted example

Locations: lines 698-699 and 1259-1260, Sections 5.8 and 5.15.

"The example above" and "A constructed example shows" remain after the T-010 deletion. The
current chapter contains no such example. Remove the residual references and retain the
concise representational statement already present at lines 651-654. Restoring the example
would reverse the author's earlier instruction.

## 2. Methodological details that need records or confirmation

### 2.1 Identify the population used to fit preprocessing

Locations: lines 275-278 and 313-317, Section 5.6; compare Chapter 2, lines 507-510.

The chapter says that features are standardised "across the corpus". Read literally, this
includes the test data and conflicts with Chapter 2's train-only preprocessing principle.
The source publication states z-score normalisation but does not settle the fitting
population. The alternative of raw opcode counts or TF-IDF also leaves the actual evaluated
feature representation unclear.

**Proposal:** verify which partition supplied the scaling statistics and, if applicable, IDF
weights. State the observed procedure. If the whole corpus was used, disclose it or perform
a separately authorised re-evaluation; an editorial change cannot establish train-only fitting.

### 2.2 Explain how a slice includes several methods

Locations: lines 263-270, 408-443 and Algorithm 5.1; compare Chapter 2, lines 181-186.

Section 5.5 describes a backward walk over the CFG of enclosing code. Chapter 2 defines that
CFG as intra-procedural. Section 5.7 then assumes a slice member set containing several
methods, without explaining how dependencies cross method boundaries.

The distinction matters: if a slice stays in one method, its method set has size one. The
shortest-path extension has no distinct pair to connect, and the cardinality filter rejects
the candidate. Under that interpretation, the slice-aware family would contribute nothing.
This is a conditional consequence of the description, not a finding about the implementation.

**Proposal:** recover the inter-procedural slicing rule or the rule that maps a slice to
multiple methods. A short, verified explanation would resolve a central gap in the method.

### 2.3 Add a compact configuration record

Locations: Sections 5.6-5.9 and the baseline descriptions in Sections 5.10 and 5.13.

The paper supplies alternatives and typical values where a reproducible account needs the
configuration that produced the tables. A compact table should identify the chosen read-out
and backbone dimensions, followed by the training settings. Record optimiser, learning rate,
model-selection rule and seed if available. State the treatment of zero-degree methods and
the duplicate-edge policy, which the chapter already marks as unrecorded.

The two-head objective needs particular care. Equation (5.21) already gives a mathematically
valid labelled-subset formulation. It does not establish whether the experiments used that
mask, separate task training, or another procedure. If the heads were trained jointly, the
application partitions must remain consistent across the binary and family objectives so that
family-test applications do not enter training through the binary head. Specify BCE on logits
unambiguously, as the source does with `BCEWithLogits`.

Also distinguish shared features from shared hyperedges. Section 5.13 states that the
non-attentive baselines use a different construction. "The same representation" is an
ambiguous description of that comparison.

The source directory contains no training implementation or prediction files. Missing
settings cannot be supplied from the default settings of the cited libraries or other papers.
This review does not reopen the author's confirmed decompilation and within-APK cosine-search
procedures, or request restoration of removed pending markers.

## 3. Mathematics: retain the useful analysis and add selectively

### Recommended changes to the existing exposition

- Retain the energy identity and message expansion. The static-ranking result and the
  uniform-attention scaling relation are also valid under their stated assumptions.
- Restrict the eigencomponent damping interpretation at lines 555-559 to multiplication by
  the linear propagation matrix. The learned projection and nonlinear activation are additional
  operations; the whole layer is not just that spectral filter.
- Replace "averaging" at lines 632-637 with "non-negative aggregation" where appropriate.
  The attentive propagation rows need not sum to one. Equation (5.17) already demonstrates a
  scale change under uniform coefficients.
- Clarify that type labels are not explicit model inputs. The construction family also
  determines membership through H. Topological and semantic edges become indistinguishable
  only when their member sets and weights coincide, not merely because both weights equal one
  (lines 459-468).
- Clarify that the cardinality cap rejects a method's centred topological candidate; it does
  not necessarily remove that method from other hyperedges (lines 442-449).
- Preserve the distinction between ranking attention keys and explaining a prediction.
  Equation (5.13) includes both membership coefficients and degree/edge weights; feature
  values and the classifier also affect the final decision. One list of keys is an inspection
  of the mechanism, not a validated explanation of the predicted class (lines 1134-1148).

### One useful additional equation

Section 5.10 already gives a prevalence sensitivity calculation in prose. Its scientific
purpose would be clearer with the short identity

\[
\operatorname{Precision}(\pi)=
\frac{\pi\,\operatorname{TPR}}
{\pi\,\operatorname{TPR}+(1-\pi)\operatorname{FPR}},
\]

where pi is the malware prevalence and the conditional rates are held fixed. The confirmed
counts give precision 89.5349% at 10% prevalence, which agrees with the existing 89.5%.
Axelsson's Section 5.3, Equation (7), supplies the primary reference; Chapter 2 already cites
that source. This is a sensitivity calculation, not measured deployment performance.

### Optional operator result, lower priority

For the stated binary-degree normalisation, positive weights, positive vertex degrees and
finite softmax scores, the fixed-input attentive propagation matrix satisfies
`||P_att||_2 <= 1`. The argument is short: its entries lie between zero and those of P_0;
monotonicity of the spectral radius for non-negative matrices gives
`rho(P_att) <= rho(P_0) = 1`; symmetry and positive semidefiniteness identify its spectral
norm with that radius. The entrywise comparison is not a claim of Loewner ordering.

This could complete the existing operator analysis in a few lines if the author wants a
further mathematical result. It provides no guarantee about the learned projection, the
input-dependent attention Jacobian, optimisation or adversarial robustness. It has lower
priority than specifying the evaluated model and reconciling the metrics.

## 4. Readability and duplication

| Locations | Proposed refinement |
| --- | --- |
| 5.1 and 5.2 | Combine the repeated three-family description and repeated claim that the field contains one competitor. Keep the relation to Hybroid, but replace "buys context" with a direct account of observation requirements. |
| 5.3 and 5.14 | Explain static observability once. Retain a short limitation reference instead of repeating the missing-method argument. Remove the unsupported claim that a missing method necessarily damages this representation more than a permission bag. |
| 5.7 and 5.13 | Describe unused type tags once and shorten the proposed type-aware extension. Calling it the "cleanest" or "cheapest" improvement requires evidence the chapter does not supply. |
| 5.9-5.12 | Define cohorts and task labels in 5.9, then keep only the reminders needed to read each result. Use direct result statements instead of "Three readings follow" and comments about what sounds impressive. |
| 5.1, 5.13-5.15 | Give the full account of the construction/attention confound in one place. Retain brief scope qualifications beside the central claims and in the summary. |
| 5.13 headings | Use neutral headings such as "Component attribution" and "Possible extensions". The current ablation/interpretability headings can imply completed analyses where the text describes proposed experiments. |

These cuts should make the contribution easier to follow while retaining the evidence limits.
They should also provide space for the configuration table without expanding the chapter.

## 5. References and evidence boundaries

The strict audit passes: 36 citations, 35 local PDFs and one documented Android permissions
web resource. Core full-text checks and fresh DOI metadata retrievals are recorded in T-020.
Source availability is separate from support for a particular sentence.

The claim "exactly one prior application" is repeated in Sections 5.1-5.2. The literature map
records a search exercise, but the available records do not establish an exhaustive search
with a reproducible scope and cutoff. Use a bounded description of the closest identified
prior work, or document that search before making an exclusive novelty claim. Zhang et al.'s
paper supports the technical comparison, not the absence of all other systems.

Keep the GAT and KAA results within their stated settings. Brody et al.'s static-ranking proof
does apply to this additive score, as the chapter derives. Fang et al.'s node-level benchmark
comparison does not establish that attention fails across the field or on Android hypergraphs.
Describe later operators such as HGNNv2 as subsequent developments, rather than suggesting
that a newer publication by itself invalidates the original comparison.

Two archival inconsistencies should remain visible to later work. The defect ledger and old
Chapter 5 source-record directory are absent. Structure v0.3 also still calls the Drebin
benign source/count unresolved, whereas the current chapter names AndroZoo and T-008 confirms
the empirical matrix. Align that planning statement with the accepted evidence when the
author approves the revision; do not revert confirmed facts to match stale planning text.

## 6. Recommended order

1. After approval, correct the supported numerical interpretations and obsolete references.
   Refine the prose and align the result claims with Chapters 7 and 8.
2. Recover the methodological details above and add only the verified configuration. Complete
   the mathematical explanation where it directly clarifies that procedure.
3. Treat further empirical work as a separate decision. Cached predictions could support
   per-class reporting; cached hypergraphs could establish the size and actual contribution
   of each construction family. A controlled construction-by-attention comparison with
   repeated runs would provide the strongest new evidence. Paired inference requires paired
   predictions and an appropriate sampling unit, not just the published aggregate scores.

No compilation or PDF visual review was performed because this task requests a proposal only.
