# Chapter 8: critical review and revision proposal

Date: 20 September 2026. Review ticket: T-018. This document records the review before editing.
The author subsequently approved the recommendations, which were applied under T-007 on the
same date. The revised chapter retains three sections and occupies pp. 117-118; the full thesis
remains 155 pages. The findings below describe the pre-revision text and its original line numbers.

## Assessment

Chapter 8 is a credible scientific conclusion and a useful basis for the final version. It
answers every research question, refers to G1–G4, and retains several qualifications that prevent
overstatement. Its strongest features are the task-dependent account of Hybroid and the decision
to distinguish a complete HGANN-Mal system comparison from an attention ablation. The corrected
RQ4 conclusion also agrees with Chapter 6 and both abstracts.

The chapter would benefit from a focused revision before submission. Its emphasis is uneven:
implementation details and numerical recapitulation occupy space that could explain the
dissertation's contribution more clearly. The ending stops at a narrow hypothetical attack,
without returning to the relationship between contextual representation and adversarial
evaluation. Chapters 6 and 7 now express that relationship more effectively than Chapter 8.

Retain the three sections and the two-page limit. The current build labels place the chapter
on printed pages 117–118, with references from page 119. TeXcount reports 712 main-text words,
excluding the question text supplied through macros. This is a source review; no judgement
about PDF appearance is made.

## Findings that affect scientific precision

### 1. Scope the answer to RQ3 more precisely

Location: `content/conclusion.tex:36–41`; compare `content/background.tex:588–598`,
`content/hgann-mal.tex:1060–1079` and `content/discussion.tex:35–49`.

The numerical ordering agrees with the published HGANN-Mal tables. HGNN+ exceeds GraphSAGE
by 3.8–6.7 percentage points of accuracy. HGANN-Mal exceeds the stronger non-attentive baseline
by 1.2, 1.7 and 4.1 points in three task/corpus combinations. For CICMalDroid binary detection,
its accuracy is 97.6% against 97.7%, so “was level” is an informal approximation, not an exact
tie or a demonstrated equivalence.

The sentence that these comparisons “close gap G3” is more categorical than the evidence
warrants. G3 includes the separate value of attention, while construction and weighting change
together in the comparison. The phrase “comparisons of complete systems” helps, but the answer
would be clearer if it explicitly identified the established system-level result and placed
the attention-specific question in the ablation agenda. Use “reported accuracy” to keep the
empirical scope apparent without repeating Chapter 5's limitations.

Retain the theoretical contribution, but describe it separately from the measured gain.
Chapter 5 shows a capacity of the stated operator; it does not show that training used that
capacity to produce the accuracy differences. Chapter 7 already makes this distinction well.

### 2. Resolve the inherited SWaT selection-language conflict

Location: `content/conclusion.tex:26`; compare `content/anomaly-detection.tex:798–804`,
`:916–921` and `:947–955`.

“Withheld from model development” implies that the reported test observations influenced
neither fitting nor configuration selection. Chapter 3 says the 24-component PCA configuration
was adopted because of its numerical F1 balance in the reported comparison, while also saying
that the later observations never entered model selection. These statements require an account
of when and on which partition the configuration was chosen.

This is an unresolved documentary inconsistency, not evidence that leakage occurred. Chapter 8
can state the supported chronological fact, namely evaluation on later test timestamps, without
adding the stronger assurance. The selection history belongs in Chapter 3 and should be settled
before retaining that assurance anywhere. Also identify the 24-component PCA configuration if
its 92.00% recall and 5.12% false-positive rate are retained; the full-input configuration has
different results.

### 3. Distinguish the two SAFAIR empirical settings

Location: `content/conclusion.tex:43–50`; compare `content/adversarial-evaluation.tex:483–515`,
`:635–698` and `:809–836`.

The 12.9-point PGD difference is correct: the partner benchmark reports attacked accuracies
of 83.7% for adversarial training and 70.8% for the activation detector. It comes from the
Vicomtech histopathology evaluation in D7.6 Table 2, not the facial-image contest in Table 1.
The compressed paragraph does not name that change of setting. Name the partner benchmark
and attacked accuracy if the number is retained.

The constant-predictor result is a mathematical property of accuracy-loss scoring. It does not
establish that the benchmark activation detector made constant predictions. Keep those claims
distinct. Preserve the accepted statement that the four contest rows do not establish a
general relationship between clean performance and robustness.

The G4 answer should identify the implemented evaluation procedure and the analytical scoring
results as the achieved contributions. Chapter 6 still distinguishes reusable interfaces from
experiment-level reproduction. “Closed for building and scoring” should not imply that the
entire reproducibility question has been settled.

## Findings that affect emphasis and structure

### 4. Lead the RQ1 answer with what was contributed

Location: `content/conclusion.tex:13–28`.

The opening moves almost immediately to nine false alarm episodes. This is relevant to legitimate
operational change, but it is a narrow starting point for the whole conclusion. “All nine false
alarm episodes had benign causes” also repeats part of the meaning of a false alarm.

Begin with the representation-level answer: local communication relations for IoT services,
and modular analysis of protocol records or process windows for industrial systems. Retain the
distinction between the two subquestions. The operational lesson about benign change can be
expressed briefly after the contribution, or remain in Chapter 3. Keep enough quantitative
evidence to anchor the answer without repeating every supporting count.

“Record false-positive rate” should become “record-level false-positive rate” if retained;
the present wording can sound like a claim about a record-setting result. “Approve” is clearer
than “legitimate” as a verb in the RQ1.1 answer.

### 5. Rebalance Section 8.2 around the dissertation's central contribution

Location: `content/conclusion.tex:55–73`; compare `content/introduction.tex:209–243` and
`content/discussion.tex:20–49`, `:92–106` and `:131–143`.

The current summary gives substantial detail to the industrial extractor, then compresses
Hybroid into its traffic features and modality comparison. Android analysis is the scientific
centre of the dissertation. Hybroid should be recognisable here as the complete multimodal
design, with the candidate's partial contribution to graph processing preserved where attribution
is stated. The full contribution is broader than a 13-feature flow pipeline.

HGANN-Mal deserves its own concise account of higher-order static representation and operator
analysis. The details of the third construction rule can remain in Chapter 5. Replace the
editorial verb “restores” with an account of what the formal construction and analysis establish.
If the linear-size result is retained, identify it as a bound on retained representation size
under the stated construction limits, rather than a runtime or general scalability claim.

Give SAFAIR a distinct contribution statement: an explicit evaluation design, reusable task
interfaces, and an analysis of how scores and detector responses affect interpretation.
Publication under the candidate's name is attribution evidence; the scientific summary should
explain what the software and analysis enable. Preserve partner attribution for the defence
algorithms and histopathology application.

Use the recovered space for a short synthesis connecting the two dissertation themes. Hybroid
examines context across observation sources; HGANN-Mal examines relations within static program
structure; SAFAIR supplies evaluation procedures and measurement analysis. This is a conceptual
connection. No common Android robustness experiment has been conducted.

### 6. Turn Section 8.3 into a short, ordered research agenda

Location: `content/conclusion.tex:81–86`; compare `content/hgann-mal.tex:1060–1079`,
`:1181–1185` and `content/discussion.tex:131–141`.

Retain the HGANN-Mal ablation first, as Chapter 5 promises. State its controls concisely:
identical hyperedges and preprocessing, a fixed normalisation convention, and repeated runs.
The comparison over topological hyperedges addresses construction; it answers a different
mechanistic question from replacing learned weighting on the same fused structure.

The next priority can follow Chapter 7: compare static relational encodings and the additional
value of traffic on a common cohort under time-ordered evaluation. Acquisition and computation
costs can be recorded separately. Then extend the evaluation to valid Android transformations
that preserve malicious functionality and assess the complete pipeline under stated attacker
access and budgets.

For Hybroid, traffic remaining unchanged is an intermediate hypothesis. The useful security
question is whether the unchanged dynamic evidence preserves the fused detector's decisions
when the static representation is manipulated. Move that example before the final synthesis
or omit it from the conclusion. End with the broader contribution and the question the proposed
evaluation would answer.

## Proposed arrangement within the existing two pages

| Part | Proposed treatment |
| --- | --- |
| 8.1 Answers to the Research Questions | Keep all question macros and gap references. Lead each answer with the result or implemented method. Retain selected numerical evidence and qualify the scope of G3/G4 closure. |
| 8.2 Summary of Contributions | Compress the industrial details. Give the Android systems explicit prominence, followed by the evaluation contribution and their conceptual relationship. |
| 8.3 Future Work | Keep controlled ablation first. Follow with common-cohort temporal evaluation and complete-system adversarial testing. Close with a brief dissertation-level statement. |

This revision can be achieved mainly by replacement and redistribution of existing text.
The existing three-section architecture is appropriate. New literature, a new limitations
section, or additional experiments are not prerequisites for this editorial improvement.
Actual claims of isolated attention gains, temporal generalisation, or Android robustness
would require the proposed evidence.

## Evidence and review limits

Chapter 8, Chapter 7, the research-question macros, the abstracts and the relevant introduction
sections were read, together with the gap definitions and the methods, results and limitations
that bear on the conclusion in Chapters 3–6. Original Android manuscript passages and HGANN-Mal
tables were checked. Existing full-text extractions of the IoT paper and D7.6 were inspected
for their relevant methods and results. No experiments were replicated.

The newer industrial results were checked against the current author-approved Chapter 3
account, not independently reconstructed from older reports with different evaluations.
`notes/known-issues-to-fix.md` and the legacy chapter source-record directories are absent from
this checkout. Current chapter qualifications and surviving tickets were used instead.

The strict Chapter 8 reference audit passes with zero direct citations. That confirms there
are no unresolved direct citekeys; it does not verify the scientific claims by itself. The
review uses the supporting contribution chapters and available primary material for that
purpose. No LaTeX, bibliography, figures or PDF were edited, and no compilation or visual
review was performed.
