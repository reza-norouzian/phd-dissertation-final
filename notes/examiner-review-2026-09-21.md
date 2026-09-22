# Examiner review of the dissertation

Date: 2026-09-21. Ticket: T-029. Independent of the T-028 review; written from the built
PDF (`output/pdf/thesis.pdf`, 153 pages) and the chapter sources.

Read as a supervisor would read it before a defence. No thesis file was changed.

---

## Verdict in one paragraph

The dissertation is in good shape and is unusually honest about its own limits. Arithmetic
checks out: the S7-300 confusion matrix, its binary collapse, all per-class scores, the
macro and weighted averages, the SWaT counts and the Hybroid cohort figures all reproduce
exactly. The bibliography passes a strict audit in every chapter. What stands between the
current draft and a comfortable defence is not writing quality. It is four things: an
unfinished front matter, a central research question the evidence cannot answer as asked,
result tables that rest on single unrepeated runs, and one baseline table whose provenance
is not stated. Everything else is smaller.

---

## Critical: fix before anything is submitted

### C1. The front matter is still template text

`thesissetup.tex` carries `Your Chair or Institute`, `1. Prof. Dr. First Reviewer`,
`2. Prof. Dr. Second Reviewer`, `3. Prof. Dr. Optional Third Reviewer`,
`\thesisSubmissionDate` and `\thesisAcceptanceDate` as `DD.MM.YYYY`, and
`\thesisVersion` as `Draft`. All of these print on the title page and its verso.
`content/acknowledgements.tex` reads, in full, "Replace this text with your
acknowledgements." That sentence is on printed page vii of the compiled PDF.

This is a blocker, not a nit. Nothing else on this list matters until it is done.

### C2. RQ3 asks a question Chapter 5 cannot answer

RQ3 is worded as: to what extent do **attention-weighted** hypergraph representations
improve over pairwise graph models **and non-attentive hypergraph models**. Chapter 5
then states four separate times (5.1, 5.13, 5.14, 5.15) that hyperedge construction and
attention weighting were changed together, so no comparison isolates attention. Section
5.8 adds a further condition: uniform coefficients give `P_att = R^-1 P_0 R^-1`, so even
a naive ablation would change the scale of propagation, not only its weighting.

The chapter is right to say this. The problem is that Chapter 1 poses a question about
attention and Chapter 5 delivers an answer about complete configurations. An examiner will
open exactly here.

Two ways out, and the choice is yours:

1. Run the ablation. A non-attentive operator over the identical fused hyperedge set, with
   a stated normalisation convention, plus `HGANN-Mal` restricted to topological hyperedges
   alone. Two configurations, two corpora, three tasks. This is the single highest-value
   experiment left in the thesis.
2. Reword RQ3 so it asks about the construction-and-weighting configuration as a whole, and
   move attention isolation into future work where Chapter 8 already puts it.

Doing neither leaves a visible seam between Chapter 1 and Chapter 5.

### C3. Every headline number in Chapter 5 comes from one run

No configuration was repeated. There is no standard deviation, no confidence interval and
no significance test anywhere in Tables 5.2 and 5.3. Section 5.14 says so plainly. But the
margins being claimed are 0.3, 1.2, 1.6, 1.7, 1.9 and 4.7 points, and one of the four
task-corpus combinations is **minus** 0.1. The Abstract, Chapter 7 and Chapter 8 all carry
the "1.2 to 4.1 points" claim forward.

Five seeds per configuration, reporting mean and standard deviation, would cost very little
compute and would change how the whole chapter reads. Without it, the strongest empirical
claim of the dissertation is a set of unreplicated point estimates.

### C4. The Chapter 5 tables contain values no averaging convention allows

Section 5.14 establishes that four rows have `F1 > (P+R)/2`, which is impossible under
positive-class, macro or weighted averaging alike, and that the `HGANN-Mal` Drebin binary
row cannot be a macro average at the stated accuracy. The dissertation reprints the
published table unchanged and documents the defect.

That is a defensible choice for a published record, but the disclosure is buried in the
limitations section, twelve pages after the table. An examiner reading Table 5.2 sees bold
"best" values with no warning attached. Two fixes, both cheap:

- If the stored predictions still exist, recompute the table under one stated convention
  and print both. This is by far the better outcome.
- If they do not, say so in the caption of Tables 5.2 and 5.3 themselves, in one sentence,
  rather than only in 5.14.

---

## High: address before the defence

### H1. The SWaT study selects its final configuration on test results

Section 3.5 states that "Representations, model settings and detection thresholds are
selected from the training and validation data." Section 3.5.3 then says the 24-component
PCA configuration "is consequently adopted as the final configuration on the basis of its
numerical `F1` balance" — and that `F1` is the test-set value in Table 3.9. Those two
sentences contradict each other, four pages apart.

The defect ledger records this as **SW-01, open**. It cannot stay open. Either recover the
validation record that justified the choice, or state in Section 3.6 that the configuration
was chosen after seeing test scores. The second option is survivable; the contradiction is
not.

### H2. The SWaT detector is trained on data containing attacks

"All three partitions contain normal observations and labelled attack examples." Feature
selection uses training ground truth. The detector is reconstruction-based, and both
systems it derives from, MAD-GAN and TadGAN, fit a normal-only reference. Training a
reconstruction detector on a contaminated reference weakens its own premise: anomalous
patterns present during fitting can be absorbed into the learned representation, which
Section 3.2 itself notes for the service-graph method.

Section 3.5 acknowledges the exposure. It never explains why the protocol was chosen, and
no normal-only variant is reported. An examiner who knows MAD-GAN will ask why.

### H3. Chapter 3 reports no baseline of any kind

Twenty-four pages, seventeen references, no related-work section, and no comparison against
a single published detector for either the S7-300 study or the SWaT study. Not even against
MAD-GAN or TadGAN, from which the SWaT model is built.

Worse, Section 3.6 hands the examiner the argument: it cites Wolsing et al., who show that
deliberately simple process-value tests match far more elaborate detectors on industrial
data, and Bilot et al., who find the same in intrusion detection. The chapter states that no
such baseline was run. That concedes the point before anyone asks.

One simple per-variable threshold or residual test on the identical split would cost a day
and would convert the GAN section from "we measured our model" into "our model beats a
reasonable alternative." This is the second-highest-value experiment remaining.

### H4. The Hybroid baseline table has unstated provenance

Table 4.2 is captioned "Published binary-detection comparison with four baselines," which
reads as a common evaluation. Checking the source publication
(`publications/Hybroid/Hybroid.tex`, lines 348 and 413), the paper never states that SVM,
DREBIN, Adagio or CIC 2017 were re-run on CICAndMal2017 or on the 2,079-application cohort.
Adagio's 0.893 in the table matches the "detects 89% of the malware" figure that Adagio's
own paper reports on Adagio's own dataset.

So the four baselines may be numbers copied from four different papers evaluated on four
different corpora. Section 4.9 already derives, through Equation 4.6, that the Hybroid row
itself implies a malware prevalence of 50 per cent when the evaluated cohort is 18.2 to 20.5
per cent — so that row cannot be a pooled confusion matrix either.

State the provenance of the four baseline numbers explicitly in the caption. If they were
not re-run on the same cohort, say that, and consider whether Table 4.2 earns its place at
all. Leaving it as a comparison table invites the question in the room rather than on paper.

### H5. The page budget contradicts the stated thesis argument

| Component | Plan (v0.3) | Built | Delta |
|---|---:|---:|---:|
| Front matter | 10 | 18 | +8 |
| 1 Introduction | 9 | 8 | −1 |
| 2 Background | 15 | 16 | +1 |
| **3 Anomaly Detection** | **15** | **24** | **+9** |
| **4 Hybroid** | **23** | **16** | **−7** |
| 5 HGANN-Mal | 27 | 28 | +1 |
| 6 Adversarial evaluation | 15 | 18 | +3 |
| 7 Discussion | 4 | 4 | 0 |
| 8 Conclusion | 2 | 2 | 0 |
| References | 13 | 16 | +3 |
| Appendix A | 2 | 3 | +1 |
| **Total** | **139** | **153** | **+14** |

The total is inside the 170-page ceiling, so length is not the issue. The distribution is.
`notes/dissertation-structure-v0.3.md` states that "Android malware analysis forms the
scientific centre" and that "the two Android chapters receive 50 pages, the largest share
assigned to any research stream." They receive 44. Chapter 3, the supporting stream whose
RQ1.1 has no detection result and whose RQ1.2 has no baseline, receives 24 — eight pages
more than the first Android contribution.

A reader who counts pages will conclude the industrial work is the centre. Either shorten
Chapter 3 (the Raspberry Pi throughput subsection and parts of the corpus description are
the obvious candidates) or expand Chapter 4 back toward its allocation.

### H6. No prospective evaluation exists anywhere in the dissertation

Every empirical result uses a random or single-campaign split:

- Hybroid: five-fold random cross-validation on one 2015–2017 collection.
- HGANN-Mal: 70/20/10 random on Drebin (2010–2012) and CICMalDroid (2017–2018).
- SWaT: one collection campaign.
- S7-300: one plant, 24 hours.

The thesis cites Pendlebury et al. and Arp et al. in Chapters 1, 2, 4 and 5 as the standard
it should be judged against, and then meets that standard nowhere. Each chapter declares
this individually, which is correct. But no chapter says it once, plainly, at
dissertation level.

Chapter 7 mentions it obliquely ("Time-ordered evaluation addresses the additional
question"). Chapter 8 puts it in future work. Neither states the fact: this dissertation
contains no time-ordered evaluation. Own it in one sentence in Chapter 7. An examiner who
has to derive it themselves will weigh it more heavily than one who is told.

---

## Medium

### M1. LaTeX defect: unbalanced brace in Chapter 3

`content/anomaly-detection.tex:40` opens a group with a stray `{` before `\nadics{}` that
is never closed. The file ends at brace depth 1 and the build log carries
`(\end occurred inside a group at level 1)` at `output/pdf/thesis.log:2100`. It compiles,
but any group-scoped setting in that file now leaks to the end of the document. Delete the
brace.

### M2. Chapter 8 overstates the RQ1.1 answer

Table 1.2 in the Introduction is honest: for RQ1.1 it records "Service-graph updates and
resource measurements; detection accuracy unmeasured." Chapter 8's RQ1.1 paragraph says
"Unexpected relations trigger an alert and can be approved by the site owner as the
deployment changes" — with no statement that detection was never measured. A reader of the
conclusion alone would believe a working detector was demonstrated. Add the qualification;
Chapter 8 has room.

### M3. RQ1.1 rests on a two-page paper with fourth authorship

Section 3.6 states this plainly: a two-page PAM 2018 contribution, candidate fourth of four
authors, portable model proposed but not implemented, no measured detection result. It
nonetheless carries a numbered research subquestion, an Abstract paragraph and a Conclusion
paragraph.

The RQ wording is the specific problem. RQ1.1 asks how service relationships can be
represented "to identify unexpected interactions" — identification is promised and never
measured. Either narrow the wording to representation and maintenance cost, which is what
is actually answered, or fold the study into RQ1.2's chapter as a described design study
without its own question. Be ready to defend the current arrangement if you keep it.

### M4. Chapter 6 contains no experiment the candidate ran

RQ4's evidence is four contest rows (one of them a collapsed constant model), one partner
table from D7.6 and one partner PDF study. Section 6.10 is explicit and correct about
this. The candidate's contribution is the design, the software and the mathematical
analysis — and Equations 6.19 and 6.22 are genuinely good results.

But Section 6.9 proposes the experiment that would close the gap: "compare an ordinary
classifier with a training-selected constant baseline and the same classifier under output
thresholding." That study is small. Running it would turn the chapter's best analytical
result from a derivation into a demonstration, on the candidate's own data.

### M5. Confirm the SWaT confusion counts are recorded, not reconstructed

Table 3.10's counts reproduce Table 3.9's rounded percentages to four decimal places:
47,337/51,453 = 92.0005 per cent and 47,337/64,845 = 73.0002 per cent. All five rows of
Table 3.9 are internally consistent, so nothing is wrong arithmetically. But integer counts
that land this exactly on round percentages usually mean the counts were derived from the
percentages rather than the other way round.

The chapter presents them as measured ("The final 24-component PCA evaluation produced the
confusion matrix"). Since the source is an unpublished internal report, check the original.
If the counts were reconstructed, say so in the caption. The chapter is scrupulous about
provenance everywhere else; this is the one place it is not.

### M6. RQ2's effect size is at the resolution limit of its own data

Table 4.5's fusion contrasts are differences between two-decimal values read off published
figures, and three of the six are 0.01. Section 4.11 says the fold-level scores no longer
exist, so no uncertainty can be reconstructed. The answer to RQ2 therefore has a precision
comparable to its effect.

Consider stating the RQ2 conclusion qualitatively — fusion did not reduce detection
performance for any learner and improved it slightly for two, while the category result
depends on the learner — rather than quoting point differences that the data cannot support
to that precision.

### M7. The Drebin binary comparison mixes two collections

Section 5.14 records that the benign class comes from AndroZoo (crawling from late 2011)
while Drebin malware is 2010–2012, so a classifier can separate the two by build tooling
rather than by malice, and that around 49 per cent of Drebin samples are repackaged with no
deduplication applied.

The confound affects all five methods equally, so the comparison survives. But the 1.2-point
Drebin binary margin — the smallest of the three positive margins carried into the Abstract
and Chapter 8 — sits on the most confounded of the four cohorts. Neither Chapter 7 nor
Chapter 8 mentions this when synthesising. One clause would fix it.

### M8. No list of acronyms

APK, DEX, ART, CFG, FCG, GCN, GNN, HGNN, ICS, PLC, SCADA, IDC, SSIM, ASR, FPR, TPR, TNR,
PGD, BIM, FGSM, AUC, ROC, PCA, GAN, SWaT, IDC and more, all defined on first use and
scattered across 135 pages. The front matter already runs to 18 pages; one more list is
standard for a TUM dissertation in this area and costs nothing.

### M9. The decision register is discontinuous

`notes/workflow/DECISIONS.md` begins at D-001 on 13 September 2026. But
`dissertation-structure-v0.3.md` cites D-030, D-040 to D-048, D-050 to D-055 and D-060 as
governing decisions, and the chapter file headers cite D-008 through D-031. None of those
entries exist in the register.

Not a defect in the thesis, but it means any decision reference in a chapter header or in
the structure document dead-ends. This will cost you time the next time you or anyone else
asks why something was decided.

---

## Low

- Abstract paragraph order puts the IoT and industrial work first, ahead of the Android
  chapters that the structure document calls the scientific centre.
- The Abstract says `HGANN-Mal` "was level in the fourth" combination; Chapter 5 and
  Chapter 8 both give 97.6 against 97.7. Align the wording.
- Section 3.7 says the mechanisms "close gap G1 at the implementation level." Given no
  detection result for RQ1.1 and no baseline for RQ1.2, "address" is the supportable verb.
- 49 underfull vertical boxes in the log. Cosmetic, but worth one pass before printing.
- Chapter 3 is the only contribution chapter without a related-work section; Chapters 4, 5
  and 6 all have one. The asymmetry is visible in the table of contents.

---

## What is genuinely strong, and should be said

These are worth knowing, because they are what the defence should be built around.

- **Every number reproduces.** The S7-300 six-class matrix, its collapse to binary, all
  thirty per-class scores, macro and weighted `F1`, the PCAP byte totals including
  per-packet header overhead, the SWaT counts, the Hybroid cohort arithmetic and the
  prevalence bounds. Recomputed independently; no discrepancy found.
- **The bibliography is clean.** Strict audit passes on all five chapter files: 38, 119,
  17, 40, 37 and 25 citations, zero needing attention.
- **Section 5.8 is the best original work in the dissertation.** The coupling matrix
  (Eq. 5.19), the rank-one decomposition (Eq. 5.20), the static-ranking result
  (Eq. 5.22) transferred from Brody et al. to the hyperedge score, and the normalisation
  finding (Eq. 5.24) are real mathematical contributions that exist nowhere in the source
  publication. They do not depend on the single-run experiments at all.
- **Section 6.8.4 is the second.** The constant-classifier result and the label-reversal
  identity are clean, correct and consequential: they identify a defect in a scoring rule
  that an EU project actually used to rank submissions.
- **The honesty is an asset, not a liability.** Section 5.14 finding impossible values in
  the candidate's own published table, and Section 4.9 deriving that the candidate's own
  published row implies the wrong prevalence, are exactly what a committee wants to see.
  Do not let anyone talk you into softening them.

---

## Suggested order of work

1. Front matter (C1). An afternoon.
2. Fix the stray brace (M1). One minute.
3. Decide C2: run the ablation, or reword RQ3. This decision gates the rest.
4. Repeated runs for Chapter 5 (C3), and recompute Table 5.2/5.3 if predictions survive (C4).
5. One simple baseline for SWaT (H3) and resolve the selection contradiction (H1).
6. Caption fixes: baseline provenance (H4), SWaT counts (M5).
7. Page rebalancing (H5) and the one-sentence statements (H6, M2, M7).
8. Acronym list (M8), then the editorial pass.

Items 1 to 5 are what a committee will ask about. Items 6 to 8 are what makes the document
look finished.
