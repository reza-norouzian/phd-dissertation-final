---
id: T-021
title: Apply the approved Chapter 4 scientific and readability revision
status: review
priority: P1
chapter: 4
owner: codex
depends_on: []
blocks: []
tags: [writing, revision]
created: 2026-09-20
updated: 2026-09-20
---

## Goal

Apply T-019: correct scientific explanations and citations, add supported mathematical definitions, improve readability and remove repetition while preserving the empirical results and thirteen-section structure; rebuild the tracked PDF.

## Why it matters

The author approved T-019 on 20 September 2026 and asked that readability also receive
attention. The revision will use a contribution-led account of Hybroid, retain its empirical
evidence and remove repeated qualifications without concealing the remaining evidence limits.
Two narrow Chapter 2 corrections are needed for consistency with the approved opcode and G2
revisions. No new experimental result or historical implementation detail is authorised.

## Acceptance criteria

- [x] Correct the opcode rationale, task definitions, fusion wording and network claims.
- [x] Correct claim-to-citation placement and synchronise the Tran reference with arXiv v3.
- [x] Add source-supported skip-gram, CFG-readout, flow-preprocessing and fusion-contrast
      equations, with explicit notation and no invented implementation settings.
- [x] Consolidate repeated qualifications and revise the prose throughout the chapter.
- [x] Preserve all empirical table values and figure assets, the 2,079-application cohort,
      attribution, section labels, and the T-011 decision not to restore pending markers.
- [x] Apply only the related Chapter 2 operand and G2 consistency corrections.
- [x] Pass strict citation audits and numerical/source-preservation checks; compile the thesis,
      read the log for new warnings, and retain the root PDF symlink. No visual review.
- [x] Record the changes, word-count comparison and build outcome; leave changes unstaged.

## Evidence and sources

- Approved review: [T-019 proposal](/Users/reza/code_repo/PhD/thesis-v2/notes/chapter4-critical-review-2026-09-20.md).
- The original Hybroid manuscript was read in full during T-019 and its method equations and
  numerical records are being reused. The full claim-to-source inspection record and fresh
  primary-metadata verification are in T-019. The following record governs this writing task.

| Core citekeys | Claim supported and inspected full text | Reference-vault / metadata status |
| --- | --- | --- |
| `norouzian2021hybroid` | Published methods, Algorithm 1, data and performance results. Supports CFG pooling, flow means and min-max scaling; does not specify block weights or application-level composition. Original TeX read in full and relevant PDF text inspected. | `have`; DOI registry checked in T-019. |
| `mikolov2013distributed` | Section 2 canonical skip-gram objective and softmax, with alternative approximations. Supports an explanatory objective, not a claim about Hybroid's unreported training approximation. Full-text objective inspected. | `have`; NeurIPS primary record checked. |
| `dai2016discriminative` | Original structure2vec operator and Algorithm 1 inspected. Hybroid's random-initialised adaptation is attributed to Hybroid rather than substituted for Dai's zero-initialised operator. | `have`; PMLR record checked. |
| `aosp2026dalvikbytecode`, `aosp2026art` | Official documentation inspected: encoded operands include registers, literals and reference indices; ART executes DEX bytecode. Supports the narrow Chapter 2 consistency correction. | Recorded `no-pdf` web resources; primary pages inspected. |
| `arp2014drebin`, `aafer2013droidapiminer`, `peiravian2013machine`, `li2019android`, `chen2018android` | Static feature definitions. Relevant full-text feature descriptions inspected; citations will be attached to manifest/API feature claims. | All `have`; DOI records, or Chen publisher PDF, verified. |
| `arora2014malware`, `zulkifli2018android`, `malik2016credroid` | Network-traffic features and classifiers. Full-text method descriptions inspected; correct the first two sources' placement under static permissions. | All `have`; DOI records checked. |
| `gascon2013structural`, `narayanan2018apk2vec`, `onwuzurike2019mamadroid`, `xu2017neural`, `yan2019classifying` | Distinct graph representations and vertex-feature choices; do not equate CFGs with call graphs or all graph-based systems with Hybroid's architecture. Relevant primary method passages inspected. | All `have`; primary DOI records checked. |
| `lindorfer2015marvin`, `onwuzurike2018family` | Within-system static/dynamic/combined comparisons. Supports a conditional, representation-specific G2 account, not a quantified assertion that such comparisons are rare. Full-text comparisons inspected. | Both `have`; DOI metadata checked. |
| `lashkari2018toward`, `cicandmal2017dataset` | CICAndMal2017 acquisition and official family listing. The paper and live dataset page were inspected. The website supports the corrected 104/101/112/109 category counts; 2,079 is the separate author-confirmed T-012 cohort. | Paper `have`; official dataset web entry added and audited before drafting. |
| `aosp2026networksecurity`, `pourali2022hidden`, `flood2024bad` | Target-API-dependent cleartext defaults, encrypted-channel measurement scope and potential capture/OS confounding. Relevant official documentation and full-text study passages inspected. | Web resource plus two `have` PDFs; primary records checked. |
| `feng2025hgdetector`, `tran2025quantifying` | Later hybrid and graph-feature studies, with their own corpora/protocols. HGDetector methods/results inspected. Tran v3 methods and evaluation inspected; prior v2 title and review status replaced together. | Both `have`; DOI/arXiv primary records checked; Tran vault refreshed to v3 before drafting. |
| `pendlebury2019tesseract`, `song2026fcghunter`, `li2025efficient` | Temporal evaluation requirements and graph-based attack scope. Primary full-text passages inspected. No Hybroid temporal/adversarial result is inferred. | All `have`; publisher/DOI records checked. |

- All retained citations were already covered by the strict T-019 audit. The updated/added
  records were checked before chapter prose changed. No unverified candidate was used.
- The pre-draft gate passed for Chapter 4 and Chapter 2 and separately for the new dataset
  entry and refreshed Tran v3 record. All reference changes preceded prose drafting.
- Analytical additions are distinguished from experiments: commutativity of the extracted-flow
  mean, the bounded mean readout for at least one propagation round, the single-confusion-matrix
  identity, and the reported-score fusion contrast. The 79.5-81.8% constant-benign accuracy
  interval follows from 1,653-1,700 possible benign applications out of 2,079. It is a calculated
  reference, not a newly run classifier. No published performance value is replaced.
- The legacy defect ledger and Chapter 4 source-record directory remain absent. No released
  implementation will be used to fill the publication's gaps, in line with the governing scope.
- Baseline: TeXcount 6,226 main-text words, 739 caption words and three displayed equations.
  The current compiled thesis has 155 pages and 39 underfull notices, with existing template
  and end-group warnings. Review and Chapter 5 files already present in the working tree are
  outside this revision and will be preserved.

## Implementation and verification

- The main chapter was revised throughout for direct exposition and reduced duplication.
  The practical observation requirements are explicit; the unknown application-level graph
  composition was not replaced with an invented formula or a concatenation claim.
- All numbers in the six tables and all thirteen section labels are preserved. Figure input
  paths and sizes are unchanged; hashes of all ten Hybroid PDF assets match the baseline.
- The analytical checks pass, including the six F1 fusion differences and the AUC arithmetic
  check. Canonical model definitions are distinguished from undocumented historical settings.
- Main prose: 6,226 -> 3,838 words; captions: 739 -> 593; displayed equations: 3 -> 9.
- Strict audits: Chapter 4, 40 citations; Chapter 2, 110 citations; no unresolved entries.
- Final `latexmk thesis.tex` succeeds: 151 pages, Chapter 4 on pp. 45-60, Chapter 5 from p. 61.
  No undefined citations/references or overfull boxes. The 39 underfull notices and existing
  template/end-group warnings remain, with no new package/class warning types. Biber reports
  no warnings or errors. The root PDF symlink resolves to the tracked build output.
- No visual review or version-control staging/commit/push was performed. The T-020 Chapter 5
  review files already in the working tree are untouched.

## Log

- 2026-09-20 created
- 2026-09-20 in-progress -> review (Approved scientific and readability revision complete; source checks, strict citation audits and rebuild pass)
