---
id: T-007
title: Draft Chapter 8 Conclusion and Future Work
status: review
priority: P1
chapter: 8
owner: claude
depends_on: []
blocks: []
tags: [writing]
created: 2026-09-12
updated: 2026-09-20
---

## Goal

At most two pages: answer RQ1-RQ4 in the macro wording, state the extent to which each
gap G1-G4 is addressed, summarise the contributions and prioritise future work. Keep the
HGANN-Mal ablation first, as Section 5.15 promises. Revise from the current Chapters 1-7
without new citations, using the author's approved T-018 recommendations of 20 September 2026.

## Why it matters

Chapter 8 is where Section 1.3 promises that each research question is answered in the words in
which it was asked, and where Section 1.6 promises that what remains open is stated. D-002, D-030
and D-034 require the questions to be typeset from dissertationmacros.tex. The skeleton comment
requires each answer to name its gap of Section 2.7 and to say how far it closes it, without
reprinting the gap. Section 5.15 states that Chapter 8 records the HGANN-Mal ablation as the first
item of future work. On 12 September 2026 the author limited the chapter to two pages, against a
five-page target in structure v0.3. The earlier ticket (old T-024) was lost in the tracker reset.

## Evidence for the RQ4 wording correction (19 September 2026)

The author approved replacing the ambiguous absence-of-relation wording with the narrower
statement that the contest results do not establish a general relation. This follows Chapter 6
Sections 6.8 and 6.11 and introduces no citation or empirical result. Underlying source
`sparta2022d76`, Section 2.8 and Table 1: relevant full text inspected again, vault status `have`,
registered in `references/MANIFEST.tsv`. The four aggregate rows do not establish a general
clean-performance/robustness relationship. The strict audit passed before drafting.

## Acceptance criteria

- [x] Three sections, Answers, Summary of Contributions and Future Work (`sec:conclusion:1` to `sec:conclusion:3`); the Limitations section of structure v0.3 is removed at the author's instruction (D-052).
- [x] At most two pages after the approved T-018 revision: pp. 117-118, References from p. 119;
      full thesis 155 pages (20 September 2026 rebuild).
- [x] Every research question typeset from its macro (D-002, D-030, D-034); none retyped.
- [x] Each main answer names its gap with `\gapref` and states the scope of the answer; no gap wording reprinted.
- [x] Every restated number matches the current chapter text and its source; no new empirical number.
- [x] The HGANN-Mal ablation is the first future-work item (Section 5.15).
- [x] Attribution consistent with D-017 and D-035, D-025, D-029, D-031, D-032; nothing removed under D-036 or D-040 reappears.
- [x] No citation added; strict audit of content/conclusion.tex passes.
- [x] No statement that details are unrecorded or that work cannot be reproduced (author's instruction, 11 September 2026).
- [x] latexmk succeeds, the root PDF symlink remains valid, and the log is read for new warnings.
- [x] British spelling (D-001), no em dashes.
- [x] Contribution-led tone, concise claim qualifications and no separate limitations section,
      following the approved T-018 proposal. Detailed limitations remain in Chapters 3-6.
- [x] Stronger Android emphasis, explicit partner-benchmark setting, controlled ablation and
      complete-system evaluation agenda, and a dissertation-level closing statement.

## Evidence for the approved T-018 revision (20 September 2026)

The author requested application of the review recommendations. The revision retains three
sections and the two-page limit. It narrows Chapter 8's SWaT wording to later test observations;
it does not infer or change Chapter 3's unresolved configuration-selection history. Numerical
results and attribution follow the current contribution chapters and the source inspections
recorded in T-018. Chapter 8 introduces no citation or new empirical result.

The core-source record below was added before drafting. Relevant original full text was
inspected in the preceding review in this conversation; the current chapter context was
checked again for this revision. All named keys already occur in `references/MANIFEST.tsv`.

| Source | Claim supported | Full-text and reference-vault status |
| --- | --- | --- |
| `aubet2018graph` | Node-local communication graphs and operator approval. The inspected latency example is omitted from the final conclusion to preserve its two-page limit. | Original approach/evaluation text inspected in the local extraction; `have`, positive title check, venue-verified metadata. |
| `iuno_ap4` | Modular NADICS interfaces and industrial protocol-feature extraction. | Relevant full text inspected during Chapter 7 revision and rechecked in the local extraction for this revision; current Chapter 3 account checked; `have`, positive title check, publisher-verified metadata. The later author-approved industrial numerical records remain distinct from this deliverable. |
| `norouzian2021hybroid` | Multimodal design and matched modality comparisons. | Original LaTeX method/evaluation text inspected; restored Chapter 4 contrasts checked; `have`, positive title check, DOI metadata previously verified. |
| `norouzian2025hgannmal` | Hypergraph construction and system-level comparisons across the two corpora. | Original LaTeX tables inspected; `have`, positive title check, DOI metadata previously verified. Chapter 5 supplies the operator analysis and its stated assumptions. |
| `sparta2022d76` | Contest and benchmark design, partner histopathology application, and the 83.7% versus 70.8% PGD comparison. | Relevant full-text Sections 2.8 and 3.1.3.1 and Tables 1-2 inspected; `have`, positive title check, publisher-verified metadata. Chapter 6 supplies the scoring derivations. |
| `norouzian2021adversarialbenchmark`, `norouzian2021safairtoolkit` | Separate benchmark and contest software contributions. | Source-inspection record and Chapter 6 attribution checked; `no-pdf` software entries, with primary repository provenance in the manifest. No claim of reproducing the historical experiments. |

The current author-approved Chapter 3 tables support the retained S7-300 and SWaT numbers.
The SWaT result is identified as the 24-component PCA configuration. Attribution follows
Chapter 1 and the contribution sections of Chapters 3 and 6; the candidate's partial role in
Hybroid graph processing is preserved. Future work follows Chapters 5 and 7 and is presented
as a proposed evaluation, not an empirical finding.

Before drafting, strict audits passed for `content/conclusion.tex` (zero direct citations)
and `content/discussion.tex` (eight cited sources, all available and verified). No bibliography
or manifest modification is necessary. The missing legacy defect ledger/source-record
directories remain a verification limit recorded in T-018.

## Revision outcome (20 September 2026)

Applied the approved recommendations in Chapter 8. The RQ1 opening now names the
representations; RQ1.2 identifies the SWaT PCA configuration and uses the supported later-test-data
description. RQ3 distinguishes complete-system comparisons from attention attribution and gives
the exact CICMalDroid binary accuracy comparison. RQ4 names the partner histopathology setting
and scopes G4 to design and measurement. Section 8.2 leads with the Android contributions and
retains the candidate's attribution boundaries. Future work begins with controlled ablation,
then proposes a common temporal cohort and complete-system adversarial evaluation, followed
by a brief dissertation-level closing statement.

Main-text word count decreases from 712 to 591 before question-macro expansion. Incidental
IoT latency and representation-size details are omitted from this conclusion; they remain in
their contribution chapters. No new literature, experiment or chapter section was added.
Chapter 3's selection-history question remains unresolved and was not changed by assumption.

The strict Chapter 8 audit and `latexmk thesis.tex`/subsequent `latexmk -silent thesis.tex`
builds pass. The final build places Chapter 8 on pp. 117-118 and the references on p. 119,
with 155 PDF pages in total. No undefined citations/references or overfull boxes occur.
The existing template/end-group warnings and 39 underfull notices remain unchanged.
The root symlink still targets `output/pdf/thesis.pdf`; `cmp` succeeds. Text extraction was
used only to locate an intermediate pagination overflow. No PDF rendering or visual review
was performed. All changes remain unstaged.

## Log

- 2026-09-19 review -> in-progress (Clarify that the contest results do not establish a general clean-performance versus robustness relation)
- 2026-09-19 in-progress -> review (RQ4 wording corrected and rebuilt without extending the two-page conclusion)
- 2026-09-20 review -> in-progress (Apply the approved T-018 Chapter 8 recommendations within the existing three sections and two-page limit)
- 2026-09-20 in-progress -> review (Approved Chapter 8 revision complete; two-page limit, citation audit and build pass)
