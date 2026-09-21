---
id: T-031
title: Apply the revised RQ3 across the dissertation
status: review
priority: P1
chapter: -
owner: claude
depends_on: [T-030]
blocks: []
tags: [research-questions, revision]
created: 2026-09-21
updated: 2026-09-21
---

## Goal

Replace RQ3 with the author-approved problem-level question and align Chapters 1, 2, 5 and 8, both abstracts and the plan, with minimal added text.

## Why it matters

The previous RQ3 asked for the benefit of attention over non-attentive hypergraph models,
which Chapter 5 cannot isolate (HG-01). The author approved a problem-level question under
D-007. Every passage that states, operationalises or answers RQ3 must follow the new wording,
without new experiments and without lengthening the chapters.

New wording (D-007): *How can higher-order relations within static Android program structure
be represented and learned, and to what extent do they improve malware detection and
classification over pairwise graph representations?*

## Acceptance criteria

- [x] Shared macro `\rqThreeText` replaced; Chapters 1, 5 and 8 inherit it.
- [x] Chapter 1 problem statement, RQ3 operationalisation, contribution and evidence map aligned.
- [x] G3 in Chapter 2 aligned with the problem-level question, without new citations.
- [x] Chapter 5 maps both parts of RQ3 to its sections; line 994 and the 5.14 baseline
      contradiction corrected; results and summary answer both parts.
- [x] Chapter 8 RQ3 answer covers both parts; both abstracts state the pairwise margin and
      replace the equivalence wording ("level" / "gleichauf").
- [x] Structure v0.3 and the HG-01 ledger entry updated.
- [x] Strict refcheck audits pass on all changed chapter files; latexmk runs clean and the log
      shows no new warnings; Chapter 8 and each abstract keep their page limits.

## Evidence and sources

### Claim-to-source record

| Source | What it supports | Full-text and verification status | Vault status |
| --- | --- | --- | --- |
| `norouzian2025hgannmal` | All accuracy values used in the revised answers. Hypergraph over the stronger pairwise model: 3.1 to 10.8 points across all twelve comparisons; HGANN-Mal over the stronger pairwise model: 5.0, 6.1, 7.0, 10.8; HGANN-Mal over the stronger non-attentive model: +1.2, -0.1, +1.7, +4.1. | Tables read in `publications/HGANN‑Mal/HGANN‑Mal.tex`, lines 419-424 (Drebin) and 448-454 (CICMalDroid); margins recomputed by script on 21 September 2026. Identity verified against the Springer DOI record under T-030. | `references/pdf/norouzian2025hgannmal.pdf`, 501,922 bytes, SHA-256 prefix `aeb85cda2fa1e68a`, matches MANIFEST line 203. |
| `zhang2023android` | Retained in G3 without change: prior Android hyperedges from call neighbours and shared permissions. | Previously verified under T-025; claim unchanged. | `references/pdf/zhang2023android.pdf`, 831,326 bytes, SHA-256 prefix `b3ac6fe91c2ee171`, matches MANIFEST line 293. |
| Chapter 5, no citekey | Construction, learned membership weights and operator analysis as the answer to the first part; complete-system attribution limits (5.13, 5.14). | Full chapter read under T-030 and again on 21 September 2026. | Repository source. |

No citekey is added. Existing citations in edited passages keep their claims.

### Outcome

Changed: `dissertationmacros.tex` (RQ3 macro); Chapter 1 problem statement, RQ3 paragraph,
HGANN-Mal contribution and Table 1.2 row; G3; Chapter 5 opening, section map, results
statement (5.10), line-994 wording, 5.14 baseline sentence and summary (now one paragraph per
part of RQ3); Chapter 8 RQ3 answer and a merged HGANN-Mal sentence in 8.2; both abstracts.
Chapters 3, 4, 6 and 7 checked: no RQ3 wording, and the Discussion already frames HGANN-Mal as
complete-system comparisons, so they are unchanged. No citekey added.

Strict audits pass: introduction 38, background 119, hgann-mal 37 keys, 0 needing attention.
`latexmk thesis.tex` exits 0: 153 pages (unchanged). Chapter 8 first overflowed to 3 pages;
merging the duplicated HGANN-Mal sentence restored pp. 115-116. Abstract and Kurzfassung each
remain one page. Log: 0 overfull, 0 undefined references, 0 biber warnings, underfull vboxes
49 -> 48 (page-break shifts), the pre-existing end-group notice unchanged. Root symlink intact.
No visual review, staging or commit.

## Log

- 2026-09-21 created
- 2026-09-21 in-progress -> review (Revised RQ3 applied thesis-wide; audits and rebuild pass; visual review left to the author)
