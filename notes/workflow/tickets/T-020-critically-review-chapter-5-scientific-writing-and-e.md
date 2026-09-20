---
id: T-020
title: Critically review Chapter 5 scientific writing and evidence
status: review
priority: P1
chapter: 5
owner: codex
depends_on: []
blocks: []
tags: []
created: 2026-09-20
updated: 2026-09-20
---

## Goal

Review the current Chapter 5, primary sources and dissertation context; propose concise scientific and editorial improvements without changing LaTeX or the compiled PDF.

## Why it matters

The author requested a concise proposal before any LaTeX changes. Chapter 5 already contains
23 numbered equations and an algorithm. This review distinguishes improvements to scientific
precision from additional formalism and separates editorial corrections from questions that
require implementation records or new evaluation. The earlier T-005 mathematical revision,
T-008 empirical-matrix correction, and T-009/T-010 reductions remain the starting point.

## Acceptance criteria

- [x] Read the complete current chapter and the complete original HGANN-Mal LaTeX source.
- [x] Check the RQ3/G3 framing and the relevant background, discussion and conclusion.
- [x] Inspect the earlier Chapter 5 tickets and respect the requested example and limitations cuts.
- [x] Check the central mathematical identities and arithmetic against the available evidence.
- [x] Identify repeated prose, unsupported interpretations and missing methodological specifications.
- [x] Inspect core source full texts and distinguish source availability from claim support.
- [x] Save a prioritised proposal without editing dissertation LaTeX, bibliography or PDF.
- [x] Run the strict Chapter 5 reference audit.
- [x] Pass the workflow consistency check and leave all changes unstaged.

## Evidence and sources

### Review scope

- Current chapter: `content/hgann-mal.tex`, all 1,267 lines, with 23 numbered equations,
  five figures and three tables. Original source: `publications/HGANN‑Mal/HGANN‑Mal.tex`,
  all 497 lines. No training implementation or per-application predictions are supplied in
  that publication directory.
- Context: workflow protocol and decision register, structure v0.3, Chapter 5 tickets
  T-005/T-006/T-008/T-009/T-010, Chapter 2 graph/learning/evaluation sections, RQ3 and
  attribution in Chapter 1, Chapter 7, Chapter 8, and the figure provenance README.
- `notes/known-issues-to-fix.md` and `notes/chapter5-source-records/` are absent. The current
  decision register does not contain the historical D-046 to D-060 entries named in the
  tickets. The review records this archival limit and does not reconstruct author decisions.

### Claim-to-source record for the review and proposed revision

All keys below already occur in `references/MANIFEST.tsv` with `have` and a passed title check.
Full-text inspection means the identified content was read, not merely a bibliography row.
Axelsson is a possible additional Chapter 5 citation, already cited in Chapter 2; no citation
has been added during this review.

| Citekey | What it supports | Full-text inspection and metadata status |
| --- | --- | --- |
| `norouzian2025hgannmal` | Published construction, attention formulation, joint objective, cohorts and result tables; limits of the published implementation description | Complete original LaTeX read. DOI-registry metadata freshly retrieved; vault PDF present. |
| `zhang2023android` | Earlier Android construction from call neighbourhoods and permissions, feature design and 80/20 family-classification evaluation | Method and evaluation sections inspected in the publisher full text. DOI metadata freshly retrieved. |
| `feng2019hypergraph` | Normalised hypergraph convolution and its spectral derivation | Convolution derivation and Equation (10) inspected. DOI metadata freshly retrieved. |
| `bai2021hypergraphattention` | Normalised incidence propagation and additive attention over supported memberships | Sections 3.1-3.3 inspected. DOI metadata freshly retrieved. |
| `zhou2006learning` | Weighted degrees, hypergraph random walk and quadratic energy identity | Sections 2-5 inspected in the proceedings PDF; primary title and equation checked. Existing verified DOI record retained. |
| `brody2022gatv2` | Static-ranking property of additive GAT scoring and its per-head scope | Sections 3.1-3.3 and Theorem 1 proof inspected in the ICLR full text; existing arXiv verification retained. The application to the chapter's score is a derivation. |
| `chitra2019randomwalks` | Scope of graph equivalence for edge-independent walks and the existence, not universality, of non-equivalent edge-dependent walks | Definitions and Theorems 3.1-3.2 inspected in the PMLR full text; existing arXiv verification retained. |
| `fang2025kaa` | Benchmark-specific attention comparisons and the distinction between node-level and graph-level evidence | Sections 5.2-5.3 and Tables 2-3 inspected in the ICLR full text; existing OpenReview verification retained. This does not establish a field-wide absence of attention gains. |
| `arp2022dos` | Sampling bias, label uncertainty and data snooping | Section 2, especially P1-P3, inspected in the USENIX full text; existing verified primary record retained. |
| `arp2014drebin` | Original corpus collection and scanner rule; family names from Kaspersky | Section III-A and Figure 4(c) inspected. Crossref metadata freshly retrieved. |
| `mahdavifar2020dynamic` | CICMalDroid collection, execution/JSON filtering, published category counts | Sections IV-V inspected. DOI metadata freshly retrieved. |
| `allix2016androzoo` | Collection dates and available APK/VirusTotal metadata, not this study's benign-selection threshold | Collection and metadata sections inspected. DOI metadata freshly retrieved. |
| `axelsson2000base` | Precision as a function of prevalence, TPR and FPR under fixed conditional rates | Section 5.3 and Equation (7) inspected. DOI metadata freshly retrieved. |

### Checks and limits

- Strict reference audit: 36 cited keys, 35 PDFs on disk, one documented Android web resource,
  zero items needing attention. This checks source records and availability, not the truth of
  every sentence or the completeness of a literature search.
- Arithmetic on the author-confirmed matrix gives precision 97.8359%, recall 97.5719%,
  F1 97.7037%, accuracy 98.3034%, and FPR 1.2672%. The published F1 of 97.8% therefore does
  not follow that matrix. The fixed-rate 10% prevalence calculation gives precision 89.5349%.
- Independent algebra checks on 200 synthetic hypergraphs passed for the two-stage messages,
  PSD/symmetry, energy identity, uniform-attention scaling, ranking and relabelling identities.
  These checks are not malware experiments and do not prove empirical benefit.
- Supporting extracts, public metadata and arithmetic results are in the ignored directory
  `tmp/pdfs/chapter5-critical-review-2026-09-20/`.
- Proposal: `notes/chapter5-critical-review-2026-09-20.md`.
- No LaTeX or PDF edit, compilation, visual review, staging or commit.

## Log

### Follow-up: priority 3 wording preview

The author asked to leave priority 2 aside and preview proposed wording for priority 3 in the
conversation before deciding whether to apply it. This is not authorisation to edit LaTeX or
to resolve missing method records by assumption. Existing methodological qualifications remain.

Claim-to-source record for the preview, checked before drafting:

- `norouzian2025hgannmal`: the original result tables were re-read. All hypergraph configurations
  have higher reported accuracy than the pairwise baselines, and HGANN-Mal exceeds the best
  non-attentive hypergraph accuracy in three of four task/corpus combinations. CICMalDroid
  binary accuracy is 97.6% versus HGNN+ at 97.7%. Full-text and DOI/vault verification from
  this ticket remain applicable. Current Sections 5.13-5.14 document the construction/attention
  confound and single-run scope; the preview introduces no new causal attribution.
- `opitz2019macrof1`: Sections 1-2 of the vaulted version 3 full text were re-read. Its classwise
  definition supports equal weighting of class F1 scores; a high mean does not establish uniform
  per-family performance. Metadata, revision date and full-text/vault status were verified under
  T-023. Section 2.6.3 supplies the corresponding dissertation definition. The source experiment's
  averaging convention remains unresolved, so the preview does not recast its F1 as verified macro-F1.

Preview source audit: \cite{norouzian2025hgannmal,opitz2019macrof1}.
The proposed replacements concern the results discussion and the Drebin family interpretation.
No LaTeX, bibliography, PDF or empirical result is changed, and no compilation is required.

Subsequent author approval: the author requested "add them". Implementation is recorded under
T-024, including replacement of the conflicting passages and narrow consistency changes to
the category discussion and chapter summary. Priority 2 remains outside the revision.

- 2026-09-20 created
- 2026-09-20 Reviewed the current chapter and source material; recorded the proposal and its evidence.
- 2026-09-20 in-progress -> review (Scientific and editorial review complete; concise proposal and evidence saved; dissertation edits await author approval)
