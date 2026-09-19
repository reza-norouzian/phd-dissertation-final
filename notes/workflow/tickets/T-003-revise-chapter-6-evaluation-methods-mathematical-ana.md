---
id: T-003
title: Revise Chapter 6 evaluation methods, mathematical analysis and figures
status: review
priority: P0
chapter: 6
owner: claude
depends_on: []
blocks: []
tags: []
created: 2026-09-10
updated: 2026-09-19
---

## Goal

Implement the approved evidence-based Chapter 6 revision, preserve original SPARTA figures, correct unsupported inferences, and add mathematical analyses and attributed PDF-malware context.

## Why it matters

The current chapter confuses equal aggregate accuracy with constant predictions and treats
always-active binary label reversal as a majority-class classifier. It also omits source
measurements and gives little space to the mechanics of the evaluated defences. D-041
authorises an evidence-based revision with original report figures and explicit mathematics.

## Evidence for the Section 6.2 revision

- `sparta2021d71`: Sections 3.3.2--3.3.6 define affected ML assets, attack tactics and
  attacker knowledge. Full text inspected; reference-vault status `have`.
- `sparta2021d73`: Section 3.3 defines the contest objectives for face re-identification and
  facial-attribute alteration. Full text inspected; reference-vault status `have`.
- `sparta2022d76`: Section 3.1.3 reports clean and perturbed classification accuracy for the
  histopathology benchmark. Full text inspected; reference-vault status `have`.

## Evidence for the proposed benchmark-contribution clarification

Scope: proposed wording only, at the author's request; no chapter changes applied.

- `sparta2021d73`: Section 4.4 and Chapter 5 distinguish the contest from the planned
  reusable benchmark and specify its common component interfaces. Relevant full text
  inspected in this conversation; reference-vault status `have`; registered in MANIFEST.tsv.
- `sparta2022d76`: Sections 3.1.1--3.1.2 document the implemented modular tool, task
  adaptations and execution procedure. Section 3.1.3 and Table 2 report Vicomtech's use
  on histopathology classification. Chapter 3 full text inspected in this conversation;
  reference-vault status `have`; registered in MANIFEST.tsv.
- `norouzian2021adversarialbenchmark`: the versioned README and main.py document the
  checkpoint-based evaluation loop and JSON result output; attacks/base.py and
  attacks/attack_types/fgsm.py implement task-specific loss selection and its integration
  with a Foolbox attack. These files were read in full in this conversation at revision
  2fac62b947ed77a509f397a9cc316937291395f5. Reference-vault status `no-pdf` (software),
  registered in MANIFEST.tsv; metadata provenance in references/source-records/chapter6-software.md.
- The author's clarification identifies organising the competition and developing the
  reusable benchmark as contributions of the collaborative work. Proposed attribution
  must not imply sole authorship or ownership of the partner defence algorithms.
- The strict chapter audit passed before drafting the proposal: 24 cited, 0 needing
  attention. Standardisation refers to software interfaces and the execution procedure;
  the proposal does not claim community adoption or complete experimental reproducibility.

## Evidence for the Chapter 6 adversarial-ML orientation

- `biggio2018wildpatterns`: defines adversarial machine learning as the study of deliberately
  crafted training- or test-time perturbations and countermeasures, and distinguishes
  training-time poisoning from test-time evasion. Full text inspected; vault status `have`.
- `goodfellow2015explaining`: introduces FGSM as one update in the sign of the input-loss
  gradient under a max-norm budget. Full text inspected; vault status `have`.
- `kurakin2017bim`: defines the basic iterative method as repeated small FGSM-style updates
  clipped to the permitted max-norm neighbourhood and valid pixel range. Full text inspected;
  vault status `have`.
- `madry2018pgd`: describes PGD as multi-step projected gradient ascent on the loss within
  the perturbation set and evaluates multiple starting points. Full text inspected; vault
  status `have`.
- `carlini2017robustness`: formulates adversarial-example generation as constrained distance
  minimisation and develops attacks for L0, L2 and Linf distances. Full text inspected; vault
  status `have`.
- All five sources are registered in `references/MANIFEST.tsv`; the strict chapter audit
  passed before drafting. Chapter 2 retains the full taxonomy, while Chapter 6 receives a
  concise orientation and definitions at first use.

## Acceptance criteria

- [x] Revise 6.4-6.11 and align 6.1-6.3 and the introduction with the corrected contribution.
- [x] Define threat constraints, task-specific accuracy and attack success, and suite aggregation.
- [x] Derive delta cancellation, constant-predictor invariance, detector reversal and logit-threshold invariance.
- [x] Explain defence compositions and the 171-feature activation detector from D7.2.
- [x] Include four report figures (one from original assets, and Figures 6.1 to 6.3 redrawn after their originals under D-042 and D-043) and two plots of published values.
- [x] Restore the worst-perturbed contest column and retain unresolved task/submission discrepancies.
- [x] Include one short, attributed PDF-malware comparison using D7.5 Figure 15.
- [x] Document the versioned raw-versus-clipped code finding without asserting historical causality.
- [x] Recompute numerical differences and check the mathematical identities and image provenance.
- [x] Pass strict reference audits, build with latexmk, compare the two PDFs and inspect new log warnings.
- [x] Update current source records and planning state; leave all changes unstaged and visual review to the author.
- 2026-09-19 review -> in-progress (Author approved the concise Section 6.2 replacement and removal of the source-correction paragraph)
- 2026-09-19 in-progress -> review (Approved concise Section 6.2 applied; strict audit and compile pass, PDFs identical)
- 2026-09-19 review -> in-progress (Replace the Chapter 6 title throughout the thesis and planning records at the author's request)
- 2026-09-19 in-progress -> review (Chapter 6 title replaced throughout the thesis; strict audit and compile pass, PDFs identical)
- 2026-09-19 review -> in-progress (Apply the approved Chapter 6 revisions that foreground the competition and reusable benchmark framework, with an explicit citation to the versioned GitHub repository)
- 2026-09-19 in-progress -> review (Adversarial-ML orientation and first-use attack descriptions added; strict audit and compile pass)
- 2026-09-19 review -> in-progress (Clarify the Section 2.5 cross-reference and make its full descriptive phrase clickable)
- 2026-09-19 in-progress -> review (Section 2.5 cross-reference clarified and made fully clickable; strict audit and compile pass)
- 2026-09-19 review -> in-progress (Restore the original Section 6.3 wording and use the same numeric hyperlink form as the Section 6.4 reference)
- 2026-09-19 in-progress -> review (Section 2.5 now appears as the same clickable numeric cross-reference as Section 6.4; exact rendered wording verified and strict audit/build passed)
- 2026-09-19 review -> in-progress (Clarify that the contest comprised targeted face re-identification and attribute alteration, with attack and defence tracks for each task)
- 2026-09-19 in-progress -> review (Clarified and cited both contest tasks; strict audit and compile pass)
- 2026-09-19 review -> in-progress (Remove the redundant histopathology-budget sentence and identify the SAFAIR contest explicitly in the scoring subsection title)
- 2026-09-19 in-progress -> review (Removed the redundant budget qualification and clarified the SAFAIR scope in the subsection title; strict audit and compile pass)
- 2026-09-19 review -> in-progress (Remove the unnecessary forensic sampling passages from Section 6.5.1 and the dependent corpus-ratio comparison)
- 2026-09-19 in-progress -> review (Unnecessary Section 6.5.1 passages removed; dependent comparison deleted; strict audit and compile pass)
- 2026-09-19 review -> in-progress (Remove the requested data-governance reporting paragraph from Section 6.5.4)
- 2026-09-19 in-progress -> review (Section 6.5.4 data-governance paragraph removed; strict audit and clean rebuild pass)
- 2026-09-19 review -> in-progress (Remove the requested biometric-deployment qualification from Section 6.5.4)
- 2026-09-19 in-progress -> review (Biometric-deployment qualification removed; strict audit and compile pass)
- 2026-09-19 review -> in-progress (Remove the requested raw-output and histopathology-result qualification from Section 6.6)
- 2026-09-19 in-progress -> review (Raw-output and histopathology qualification removed; strict audit and compile pass)
- 2026-09-19 review -> in-progress (Remove the redundant D7.6 Figure 6 sentence from the targeted-runs paragraph)
- 2026-09-19 in-progress -> review (Redundant D7.6 Figure 6 sentence removed; strict audit and compile pass)
- 2026-09-19 review -> in-progress (Remove the redundant reproducibility checklist paragraph from Section 6.6)
- 2026-09-19 in-progress -> review (Redundant reproducibility checklist removed; strict audit and compile pass)
- 2026-09-19 review -> in-progress (Remove the redundant training-schedule qualification from Section 6.7 and review the remaining section)
- 2026-09-19 in-progress -> review (Section 6.7 qualification removed; section reviewed; strict audit and compile pass)
- 2026-09-19 review -> in-progress (Strengthen Figure 6.2 provenance and its links to the benchmark architecture and later results while preserving the author's caption edit)
- 2026-09-19 in-progress -> review (Figure 6.2 integrated with surrounding sections and results; all Chapter 6 figures audited; strict audit and compile pass)
- 2026-09-19 review -> in-progress (Remove the redundant history-protocol paragraph from Section 6.7 at the author's request)
- 2026-09-19 in-progress -> review (Redundant history-protocol paragraph removed; strict audit and compile pass)
- 2026-09-19 review -> in-progress (Remove the two redundant contest-result qualification paragraphs while preserving the dissertation-level RQ4 conclusion)
- 2026-09-19 in-progress -> review (Two redundant contest-result qualification paragraphs removed without weakening the RQ4 narrative; strict audit and compile pass)
