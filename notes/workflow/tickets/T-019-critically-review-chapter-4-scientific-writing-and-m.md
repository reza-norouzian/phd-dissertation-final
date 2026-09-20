---
id: T-019
title: Critically review Chapter 4 scientific writing and mathematics
status: review
priority: P1
chapter: 4
owner: codex
depends_on: []
blocks: []
tags: [review]
created: 2026-09-20
updated: 2026-09-20
---

## Goal

Assess Chapter 4 for scientific accuracy, clarity, repetition and useful mathematical additions against its primary evidence and dissertation context; propose revisions without changing LaTeX or the compiled PDF.

## Why it matters

The author requested a short, structured proposal before any LaTeX revision. Chapter 4
contains the principal matched-modality evidence for RQ2, but its technical explanations and
claim-to-citation alignment need a separate check from the existence audit. Additional
mathematics should clarify documented operations and their limits, not imply that missing
implementation details or new experiments have been recovered.

## Acceptance criteria

- [x] Read Chapter 4 and the original Hybroid manuscript in full, with relevant dissertation
      context and the author decisions recorded in T-011 and T-012.
- [x] Inspect primary full-text passages for technical and literature claims; check live
      bibliographic records and distinguish source existence from claim support.
- [x] Identify scientific corrections, repeated material and vague prose with source locations.
- [x] Propose useful mathematical additions without inventing weights, application-level graph
      aggregation, training settings, statistical significance or empirical results.
- [x] Save a structured proposal and leave all LaTeX, bibliography and PDF files untouched.
- [x] Pass the final strict reference audit and workflow consistency check.

## Evidence and sources

- Review: [Chapter 4 proposal](/Users/reza/code_repo/PhD/thesis-v2/notes/chapter4-critical-review-2026-09-20.md).
- Complete current chapter and original manuscript:
  [chapter](/Users/reza/code_repo/PhD/thesis-v2/content/hybroid.tex) and
  [Hybroid source](/Users/reza/code_repo/PhD/thesis-v2/publications/Hybroid/Hybroid.tex).
  The original PDF's methods and algorithm were also inspected through text extraction.
- Context: workflow protocol, recent/open work, full current decision register, structure v0.3,
  Chapter 4 literature-map section, T-002/T-011/T-012, RQ macros, relevant Chapters 1/2/5,
  and complete current Chapters 7/8. The legacy defect ledger and Chapter 4 source-record
  directory are absent; their contents were not assumed.
- The initial strict audit passes: 43 citekeys, 39 PDFs, four recorded web resources, no
  unresolved vault entries. Live Crossref records were retrieved for 34 DOI-bearing sources;
  Chen et al. was checked against the publisher PDF after Crossref returned 404. NeurIPS,
  PMLR, arXiv and the relevant documentation supplied the other primary records. This is
  not a claim that all 39 cited papers were read in full or all their claims independently
  validated; full-text inspection concentrated on the claims relevant to this review.

### Claim-to-source record for the proposal

| Citekey or record | Claim supported and full-text inspection | Vault / primary-record status |
| --- | --- | --- |
| `norouzian2021hybroid` | Original manuscript read in full; PDF methods/Algorithm 1 checked. Supports the reported pipeline, CFG mean readout and empirical values. Does not supply the missing block weights or application-level composition. | `have`; DOI title/authors/venue checked. |
| `mikolov2013distributed` | Full-text skip-gram objective and alternative training formulations inspected. Supports a canonical explanatory objective, not an assertion about Hybroid's unreported optimizer or negative-sampling settings. | `have`; NeurIPS record checked. |
| `dai2016discriminative` | Full-text operator and Algorithm 1 inspected. Original structure2vec uses zero initialization; Hybroid reports a random-initialized adaptation. These must not be silently equated. | `have`; PMLR record checked. |
| `aosp2026dalvikbytecode`, `aosp2026art` | Official runtime/bytecode documentation inspected. Operands include literals and reference indices as well as registers; their encoded values are not simply runtime register contents. | Recorded web resources; live AOSP pages read. |
| `arora2014malware`, `zulkifli2018android` | Full-text approach/feature descriptions identify network-traffic methods, contrary to their placement under static permissions in Section 4.2. | Both `have`; both DOI records checked. |
| `li2019android`, `chen2018android` | Full-text feature descriptions concern manifest/API feature vectors, not the program-graph methods their current grouping suggests. | Both `have`; Li DOI and Chen publisher PDF checked. |
| `arp2014drebin`, `gascon2013structural`, `comparetti2010identifying` | DREBIN feature sets and Adagio representation inspected; Comparetti's REANIMATOR concerns dormant functionality in general malware binaries, not direct evidence for the specific Android manifest-rewriting claim. | All `have`; DOI records checked. |
| `lindorfer2015marvin`, `onwuzurike2018family` | Full-text modality comparisons inspected. MARVIN itself includes a static/dynamic/combined comparison; these examples do not establish the asserted field-wide rarity. | Both `have`; DOI records checked. |
| `aosp2026networksecurity`, `pourali2022hidden` | Target-API-dependent defaults checked in official documentation. ThirdEye's 22.92% concerns encryption/decryption for network transmission and shared storage; it should not be narrowed to network encryption alone. | Web record plus `have`; official page and DOI checked; relevant full text inspected. |
| `flood2024bad` | Full-text UNSW-NB15 TTL/OS-confounding analysis inspected. Supports a possible mechanism, not an observed Hybroid defect. | `have`; DOI checked. |
| `feng2025hgdetector` | Full-text methods and comparison context inspected. It uses both CICAndMal2017 and a filtered CICMalDroid2020 setting; its headline fusion gains need that context. | `have`; DOI checked. |
| `song2026fcghunter`, `li2025efficient` | Full-text attack construction and reported result passages inspected. Not all FCGHunter operators insert unreachable code; unchanged Hybroid flow features are not established. | Both `have`; DOI records checked. FCGHunter vault copy is arXiv v1 rather than the final typeset article. |
| `tran2025quantifying` | Vault v2 context inspected; current arXiv v3 metadata and first-page text checked. The title changed on 16 September 2026, and the current record states acceptance at IEEE DSAA 2026. | Vault remains v2, unchanged. Bibliography/title/status and version need coordinated revision if approved. |
| CICAndMal2017 official dataset page | Live family listing checked; corrected category counts are consistent with the chapter. The 2,079 common cohort remains the author-confirmed T-012 fact, not an independent reconstruction. | Dataset primary web page checked; no new chapter citation added. |

- TeXcount reports 6,226 main-text words, 739 caption words and three displayed equations.
  Existing build labels put Chapter 4 at page 45 and Chapter 5 at page 65. No compilation or
  PDF visual review was performed because this is a proposal-only task.

## Log

- 2026-09-20 created
- 2026-09-20 in-progress -> review (Source-backed scientific review and concise revision proposal complete; implementation awaits author approval)
