---
id: T-016
title: Write the Abstract and the Kurzfassung
status: review
priority: P1
chapter: front
owner: claude
depends_on: []
blocks: []
tags: [writing]
created: 2026-09-13
updated: 2026-09-13
---

## Goal

Replace the template placeholders in content/abstract.tex with an English Abstract and a German Kurzfassung, each at most one printed page, restating only results already in Chapters 3-8 and carrying no citations.

## Why it matters

The TUM regulations require an English abstract and a German Kurzfassung, and both pages still held
template placeholders. On 13 September 2026 the author asked for both, each at most one page. The
abstract is the part of the thesis most often read alone, so every number in it must match the
chapter that reports it.

## Acceptance criteria

- [x] English Abstract and German Kurzfassung in `content/abstract.tex`; placeholders removed.
- [x] Each text fits on one printed page (checked with `pdftotext` on the built PDF).
- [x] Every number restated from the current chapter text; no new empirical number.
- [x] No citation added; strict audit of `content/abstract.tex` passes.
- [x] Attribution consistent with Section 1.5: the IoT graph study is named as collaborative, the
      adversarial work is placed within SPARTA.
- [x] Terminology fixed by structure v0.3: \categoryclassification{} on CICAndMal2017; Drebin and
      CICMalDroid named as corpora only.
- [x] British spelling, no em dashes; German text uses decimal commas.
- [x] latexmk succeeds, the two PDFs are identical under `cmp`, and the log is read for new warnings.

### Result notes

- Page fit is limited by the German text. The first drafts overran by 47 English and about 110
  German words, so both were cut to the same content. The Kurzfassung is a close translation,
  with minor compressions to fit the page.
- The PGD sentence follows the Chapter 6 wording (attacked accuracy 12.9 points below adversarial
  training). The looser wording in Chapter 8 ("12.9 points less accurate") was not copied.
- Not in the abstract: the 97.0 per cent Hybroid detection accuracy (cut for length, since RQ2
  concerns the within-system contrast), the benign-day alarm episodes, and the Section 1.5
  authorship details.

## Evidence and sources

The abstract carries no citations. Each claim is restated from a chapter that has already passed its
own strict audit, and each chapter number traces to the source named below.

| Claim in the abstract | Chapter location | Underlying source |
| --- | --- | --- |
| Node-local whitelist of service relations; about 6 ms added to a 24 ms round trip | `anomaly-detection.tex` ll. 109-110, 977-980; `conclusion.tex` RQ1.1 | PAM 2018 two-page paper (`aubet2018graph`), candidate 4 of 4 |
| NADICS fixes interfaces around the learning stage | `conclusion.tex` RQ1.2; `anomaly-detection.tex` l. 983 | NADICS repository, IUNO AP4/AP7 |
| S7-300, random forest, session-disjoint split: attack F1 94.50 %, FPR 0.484 % | `anomaly-detection.tex` ll. 430-452 | internal experimental records (Ch. 3, T-001) |
| SWaT GAN: recall 92.00 %, FPR 5.12 % on the later 393,679 timestamps | `anomaly-detection.tex` ll. 590, 783, 839-841; D-055 | author's internal GAN report (Ch. 3) |
| Hybroid: 13 flow features on CICAndMal2017 | `hybroid.tex` ll. 852-859; macro `\netfeatures` | `publications/Hybroid/Hybroid.tex` ll. 67, 420 |
| Fusion +1 to +2 F1 points (detection); -2 to +3 points (category classification) | `hybroid.tex` ll. 861-864 | Hybroid paper, modality tables |
| HGANN-Mal hyperedges include backward slices of security-sensitive call sites; attention learns membership weights | `conclusion.tex` Section 8.2; `hgann-mal.tex` Sections 5.5, 5.7 | `publications/HGANN-Mal/HGANN-Mal.tex` |
| Every hypergraph operator above both pairwise operators on all four combinations | `hgann-mal.tex` ll. 940-944; `conclusion.tex` RQ3 | HGANN-Mal result tables |
| HGANN-Mal ahead of non-attentive operators by 1.2 to 4.1 accuracy points in three combinations, level in the fourth | `hgann-mal.tex` ll. 951-955, 1017, 1042 | HGANN-Mal result tables |
| Construction and attention changed together | `hgann-mal.tex` ll. 1263-1266; D-028 | T-012 answer of 14 August 2026 |
| Constant classifier has zero accuracy loss under label-preserving attacks | `adversarial-evaluation.tex` ll. 717-728, Eq. `eq:advml:constant` | derivation in Ch. 6 |
| Under PGD the zero-loss defence is 12.9 points below adversarial training | `adversarial-evaluation.tex` ll. 686-692 | SPARTA D7.6 Table 2 (`sparta2022d76`) |
| Four contest rows show no general clean-robustness relation | `adversarial-evaluation.tex` l. 556; `conclusion.tex` RQ4 | SPARTA D7.6 Table 1 |
| Open step: an ablation that isolates attention in HGANN-Mal | `conclusion.tex` Section 8.3 | none (future work) |

Full-text status: no source is cited in the abstract, so no new reference enters `references/MANIFEST.tsv`.

## Log

- 2026-09-13 created
- 2026-09-13 in-progress -> review (Abstract and Kurzfassung written from Chapters 3-8, one page each, compile clean)
