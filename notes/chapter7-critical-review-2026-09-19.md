# Chapter 7: critical review and revision proposal

Date: 19 September 2026. Review ticket: T-017. Recommendations only; the dissertation text
and compiled PDF have not been changed.

**Implementation update, 20 September:** the author approved a contribution-led revision
under D-003. T-004 records the applied four-section chapter and its successful build.
The review below preserves the pre-revision findings and line locations. The SWaT
selection-history question remains separate from this editorial revision.

## Overall assessment

Chapter 7 needs a substantive editorial revision. Its central distinctions are defensible,
but the chapter gives more attention to qualifying individual studies than to explaining
their joint significance. The result resembles a compressed collection of limitations.
An examiner needs a clearer account of what the dissertation contributes through the
combination of its studies.

Retain the chapter. Chapter 1 promises this comparison, and Chapter 5 refers to its account
of observation requirements. Removing it would leave the connection between the Android
work and the evaluation contribution underdeveloped. The appropriate revision is selective:
remove repeated detail, develop the strongest comparisons, and retain the qualifications
that determine what a result means.

The current chapter has 1,414 main-text words by TeXcount, plus headings and a table. Existing
build labels place it on printed pages 113--117. Seven sections divide this short text into
small discussions. A four-page target remains reasonable. Cutting half the prose would
leave too little room for interpretation; an initial cut of approximately 300--400 words of
repetition and incidental detail would create room for a stronger synthesis. The final
reduction should depend on the argument, with some of that space used for the missing
connections below.

## Scientific findings, in priority order

### 1. Reconcile the SWaT model-selection account before asserting test independence

**Location:** [Chapter 7, lines 168--170](/Users/reza/code_repo/PhD/thesis-v2/content/discussion.tex#L168).

Chapter 7 says that the chronological split prevents test observations from entering model
development. Chapter 3 states that representations and settings were selected on development
data ([lines 603--608](/Users/reza/code_repo/PhD/thesis-v2/content/anomaly-detection.tex#L603)).
However, its results section says that the 24-component PCA configuration was
"consequently adopted as the final configuration on the basis of its numerical F1 balance"
after comparing the test results
([lines 798--804](/Users/reza/code_repo/PhD/thesis-v2/content/anomaly-detection.tex#L798)).

These statements leave the selection procedure ambiguous. A chronological partition alone
does not prevent an author from selecting a configuration after inspecting its test score.
This is a wording conflict, not evidence that leakage occurred.

**Action:** establish whether validation selected the final PCA configuration before test
evaluation. If so, state that in Chapter 3 and describe the test ranking as a subsequent
observation. If the reported test scores determined the choice, qualify the selection claim
in both chapters. Do not strengthen Chapter 7's assurance without resolving this point.
The older supplied report describes a different evaluation; it cannot settle the selection
procedure of the current, later account.

### 2. Define the different meanings of additional context

**Location:** [Chapter 7, lines 21--59](/Users/reza/code_repo/PhD/thesis-v2/content/discussion.tex#L21).

The opening asks when additional context provides useful information. Two distinct design
choices then receive the same name:

- Hybroid adds an observation channel: recorded traffic alongside static program features.
- HGANN-Mal constructs groups within static evidence and changes how information propagates
  through those groups. Its inputs include method features and backward slices, not only
  call-graph topology.

Both descriptions appear in the chapter, but their consequences receive little analysis.
The comparisons do not establish a general relationship between an amount of context and
security performance. They support task-specific comparisons under their respective
protocols. A hyperedge also does not establish that its members participated in a malicious
execution.

Chapter 5 supplies a precise connection that Chapter 7 could use: attention reweights the
memberships fixed by construction and cannot introduce a missing membership
([lines 589--594](/Users/reza/code_repo/PhD/thesis-v2/content/hgann-mal.tex#L589)). This makes
the distinction between observation coverage and learned weighting concrete.

**Action:** organise the representation discussion around added observations versus a changed
encoding of available evidence. Explain what each comparison establishes. Use the
fixed-support property to connect model design to extraction limits. Avoid another general
statement that static analysis sees only what it can see.

### 3. Use the coverage consequences of the two Android evaluations

**Location:** [Chapter 7, lines 64--84 and 110--115](/Users/reza/code_repo/PhD/thesis-v2/content/discussion.tex#L64).

The chapter contains the necessary facts but distributes them across two sections. Their
joint interpretation is stronger than another list of exclusions.

**Hybroid:** both branches excluded the same 47 graph-extraction failures. This supports a
comparison on a common retained cohort. It also means that the reported network-only result
does not test whether traffic can recover useful decisions on applications for which static
extraction fails. Prediction gains on retained applications and coverage of submitted
applications are different outcomes. The original paper records the failures; T-012 supplies
the author's later common-cohort confirmation.

**HGANN-Mal:** the CICMalDroid evaluation uses a population selected after successful sandbox
execution and parsing of the resulting analysis records. The dataset paper confirms these
filters. A detector that needs no runtime capture at inference can still inherit selection
from dynamic analysis through its evaluation corpus. This does not establish that the
excluded applications were evasive, nor that HGANN-Mal would fail on them.

**Action:** merge observation requirements with extraction coverage. Retain each exclusion
fact once and explain its consequence for the evaluated population. These are useful
dissertation-level deductions from the existing record; they require no new experiment.

### 4. Make the cost comparison answer the question promised by Chapter 5

**Location:** [Chapter 7, lines 64--84](/Users/reza/code_repo/PhD/thesis-v2/content/discussion.tex#L64).

The section combines handset acquisition with industrial labelling effort and Raspberry Pi
throughput. These costs have different units, and the text acknowledges that the records
cannot relate them to corpus size. The comparison stops before giving a useful conclusion.

Chapter 5 already distinguishes the storage and propagation bounds of the retained
hypergraph from the greater cost of constructing it
([lines 1094--1131](/Users/reza/code_repo/PhD/thesis-v2/content/hgann-mal.tex#L1094)). That
distinction belongs here. Avoiding a runtime capture removes an acquisition requirement; it
does not establish lower total computation. Conversely, Hybroid's larger static-only corpus
demonstrates application at a larger corpus size, not a measured runtime advantage.

**Action:** remove the Raspberry Pi load and the attack-episode counts from this section.
Keep the acquisition distinction and one concise reference to Chapter 5's construction
analysis. Conclude that the existing evidence supports a comparison of requirements, not a
quantified cost-benefit ranking.

### 5. Preserve the status of the numerical comparisons

**Location:** [Chapter 7, lines 48--59](/Users/reza/code_repo/PhD/thesis-v2/content/discussion.tex#L48).

The Hybroid differences match Table 4.6. The HGANN-Mal differences match the published binary
table. The problem is their evidential status, not a discovered arithmetic error.

Chapter 4 identifies rounded fold means without fold-level outcomes or a stated metric
averaging convention. Chapter 5 reports single runs and identifies inconsistencies among
some published metric columns. Chapter 7 preserves the missing-ablation qualification, but
the nearby wording "fusion increased" and "advantage" gives the estimates more certainty
than their source discussions do. The later sentence about repeated runs is too distant and
too general to carry all of this qualification.

**Action:** identify the contrasts as reported point differences when they first appear.
Retain the main task-dependent pattern and cite the exact result table or figure. The
0.1-point accuracy and 0.3-point F1 example is optional; it adds little to the stronger
observation that the complete-system ordering varies with task and metric. Do not interpret
a small difference as stable superiority, equivalence, or a mechanism-specific trade-off.
Keep the distinction between system-level comparison and attribution to attention.

### 6. Integrate the methodological contribution of Chapter 6

**Location:** [Chapter 7, lines 89--105 and 183--185](/Users/reza/code_repo/PhD/thesis-v2/content/discussion.tex#L89).

The constant-classifier result is useful and should remain. The surrounding discussion gives
less attention to the candidate's evaluation design and reusable framework, which the latest
Chapter 6 revision places alongside the score analysis. Chapter 6 should contribute more
than a warning that predictive accuracy does not establish adversarial robustness.

A useful connection is the distinction between a reusable evaluation procedure and a valid
evaluation in a new domain. NADICS exposes interchangeable learning components; SAFAIR
exposes task-specific interfaces within a shared attack-execution procedure. Such interfaces
support controlled experiments. They do not establish transfer of a fitted detector or
validate a new threat model.

For Android, valid application transformations and their preservation of malicious behaviour
must replace image-specific perturbation constraints. The complete detector must be tested.
Even if a transformation leaves a traffic vector unchanged, the fused prediction can change
through the altered static vector. The unchanged branch alone gives no robustness guarantee.

**Action:** retain the constant-prediction identity, describe the framework's transferable
methodological contribution, and state the Android-specific conditions for its use. Preserve
the current distinction between an untested weakness and a demonstrated attack. Align the
RQ4 inference with the latest Chapter 6 and Chapter 8 wording: the available contest
aggregates do not establish a general clean-performance/robustness relationship.

### 7. Restore the process-data strand of Chapter 3 to the synthesis

**Location:** [Chapter 7, lines 21--36 and 190--204](/Users/reza/code_repo/PhD/thesis-v2/content/discussion.tex#L21).

The substantive comparison with Chapter 3 concerns communication relations and benign
changes. SWaT appears chiefly as a split and a class share. Its representation comparison is
more relevant to the chapter's central question: the complete process input had the highest
reported recall, while the more compressed input had a lower false-positive rate. The
operating objective therefore matters when interpreting a representation's value.

**Action:** add one concise connection to Table 3.6 after resolving Finding 1. Treat this as
a comparison of the reported configurations, since dimensionality and model capacity were
not isolated. Do not pool its scores with Android results or infer a common mechanism. One
sentence explaining temporal and multivariate process context would also prevent the opening
comparison from appearing to reduce all of Chapter 3 to network communication.

## Section-by-section editing decisions

| Current part | Retain | Cut or replace |
| --- | --- | --- |
| Opening | One statement of purpose and the conceptual status of the comparison. | Replace the broad question about additional context with the distinction between observation and representation. |
| 7.1 Communication and program context | Observed service relations versus statically recovered program relations; legitimate change as a bounded concern. | Compress the nine-alarm account and its numerical breakdown. The author already discusses it in Chapters 3 and 8. Include process context. |
| 7.2 Multimodal and higher-order representations | The within-system task-dependent patterns and the unresolved attention attribution. | Remove repeated pipeline description and, if space is needed, the tiny metric-difference example. Add the representational interpretation. |
| 7.3 Observation requirements and cost | Per-application traffic requirements, the static-only alternative, and the absence of comparable timing measurements. | Remove the Raspberry Pi rate and attack-episode counts. Move the unreachable-call hypothesis to the adversarial discussion or leave its detailed treatment in Chapters 4 and 8. |
| 7.4 Predictive and adversarial evaluation | The constant-classifier identity and the need for valid Android transformations. | Compress the SD anecdote. Use the space for the evaluation framework and whole-pipeline implication. |
| 7.5 Dataset limitations and failures | Common-cohort exclusion, inherited dynamic filtering, and the distinction between sample origin and capture conditions. | Remove the repeated 47-failure description if it remains in the merged cost/coverage section. Delete the generic closing paragraph about inconsistent records and arithmetic reproduction. |
| 7.6 Generalisation | The distinction between internal comparison and transfer; one statement of uncertainty and unresolved controls. | Prefer removing Table 7.1 and its introductory paragraph. It inventories conditions already described in the contribution chapters without supporting a new inference. Compress the repeated SWaT split counts. |
| 7.7 Android implications | A short synthesis of the design and evaluation consequences. | Remove the second summary of fusion gains and missing attention ablation. Replace "performed well" and "behaviour absent from its analysis" with specific statements. Leave the detailed research agenda to Chapter 8. |

Table 7.1 is not intrinsically invalid: it labels the different populations and avoids a
cross-study score ranking. Its weakness is its contribution to this argument. If retained,
it needs an explicit interpretation that uses its columns. The Drebin test composition can
also now be stated from the empirical counts in Chapter 5; a corpus-only description is no
longer the only available record. A new table is not necessary for a four-page discussion.

## Recommended outline, subject to author approval

The current plan fixes seven sections. The following four-section outline is a proposal,
not an adopted decision:

1. **What the contextual representations contribute.** Combine the useful parts of 7.1 and
   7.2. Distinguish added observations from relational encoding, then interpret the
   within-study contrasts. Include the process-data strand without creating a historical
   progression from IoT to Android.
2. **Observation requirements, cost and coverage.** Combine 7.3 with 7.5. Explain how data
   requirements and extraction determine the population for which prediction is evaluated.
   Distinguish acquisition effort from computation.
3. **Validity and scope of the evidence.** Combine 7.4 with 7.6. Separate a controlled
   predictive comparison from evidence of transfer or resistance to an adaptive attacker.
   Give the evaluation framework a clear methodological role.
4. **Implications for Android malware analysis.** Close with a short account of the design
   choices the evidence supports and the conditions a stronger claim would require. Do not
   answer every research question again.

If the seven headings must remain, the same content cuts and scientific corrections can be
made beneath them. Merging the headings should improve continuity, but does not resolve the
scientific issues on its own.

## Dependent consistency edits to consider during revision

- [Chapter 5, lines 70--73](/Users/reza/code_repo/PhD/thesis-v2/content/hgann-mal.tex#L70)
  says that no comparison between Hybroid and HGANN-Mal is offered anywhere in the dissertation.
  Specify **no direct numerical comparison**. The conceptual comparison is both promised
  and present.
- [Chapter 5, lines 184--188](/Users/reza/code_repo/PhD/thesis-v2/content/hgann-mal.tex#L184)
  calls the static analysis cost low and scalable. Narrow this to the absence of runtime
  acquisition and the per-application processing structure; neither Chapter 5 nor Chapter 7
  establishes a measured total-cost advantage. Keep the distinction from the construction
  bounds later in Chapter 5.
- The last paragraph of [Chapter 3](/Users/reza/code_repo/PhD/thesis-v2/content/anomaly-detection.tex#L993)
  says that no study shows transfer across time. Clarify the distinction between the SWaT
  within-campaign chronological hold-out and transfer to another campaign or installation.
- Preserve `chap:discussion`. Chapter 5 directly cites `sec:discussion:3` for acquisition
  requirements. If sections are merged, preserve that target at the relevant passage or
  update the caller. Update the structure plan and T-004 only after the author approves the
  structural change.

## Verification and limits of this review

I read Chapter 7 in full and checked it against the current contribution chapters, the
introduction and background, the conclusion and both abstracts. I inspected relevant
primary manuscript and full-text reference passages. T-017 records the claim-to-source map
and the live primary metadata checks. The existing Chapter 7 citation audit passes: five
citations, five available PDFs, no unresolved entries. The central problem is the use of
evidence in the discussion, not a lack of citations.

The source-publication defect ledger named by AGENTS.md is absent from this checkout, as
are the earlier section-source-record directories referenced by several tickets. I used
the surviving tickets and current limitation sections, and did not reconstruct missing
experimental records. The current numerical summaries remain reports of their respective
studies; this review does not independently validate the underlying predictions.

No LaTeX file was edited. No compilation or PDF visual review was performed. The proposed
reorganisation and the dependent edits above await the author's decision.
