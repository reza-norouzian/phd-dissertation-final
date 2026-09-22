---
id: T-033
title: Apply the revised RQ2 across the dissertation
status: review
priority: P1
chapter: -
owner: claude
depends_on: []
blocks: []
tags: [research-questions, revision]
created: 2026-09-22
updated: 2026-09-22
---

## Goal

Replace RQ2 with the author-approved problem-level question and align Chapters 1, 2, 4 and 8 and the plan, with minimal added text.

## Why it matters

The previous RQ2 asked only for the extent of the fusion benefit and named the thesis's own
feature types (code-graph representations, network-flow features). On 22 September 2026 the
author replaced it with a problem-level question under D-008. The new question has two parts:
how the two sources can be represented jointly, and how their combination affects predictive
performance against either source alone. Every passage that states, operationalises or answers
RQ2 must address both parts, without new experiments and without lengthening the chapters.

New wording (D-008): *How can static program structure and observed network behaviour be
jointly represented for Android malware detection and category classification, and how does
their combination affect predictive performance compared with either source alone?*

## Acceptance criteria

- [x] Shared macro `\rqTwoText` replaced; Chapters 1, 4 and 8 inherit it.
- [x] Chapter 1 problem statement, RQ2 operationalisation, Hybroid contribution and Table 1.2
      row aligned with both parts.
- [x] G2 and the hybrid-analysis foundation in Chapter 2 aligned, without new citations.
- [x] Chapter 4 maps both parts of RQ2 to its sections; Section 4.11 and the summary answer
      the second and first parts respectively.
- [x] Chapter 8 RQ2 answer covers both parts and keeps the two-page limit.
- [x] Structure v0.3 updated.
- [x] Strict refcheck audits pass on all changed chapter files; latexmk runs clean and the log
      shows no new warnings.

## Evidence and sources

### Claim-to-source record

| Source | What it supports | Full-text and verification status | Vault status |
| --- | --- | --- | --- |
| `norouzian2021hybroid` | The joint representation named in the revised answers: a 64-dimensional code vector from program graphs, 13 flow features averaged per application, feature-level concatenation into 77 inputs. All fusion contrasts (detection +1 to +2 points of F1; categorisation -2 to +3). | Chapter 4 Sections 4.5-4.8 and 4.11 read on 22 September 2026; values unchanged from the chapter, which was checked against the paper's Figures 8 and 9 under T-021. | `references/pdf/norouzian2021hybroid.pdf`, 899,705 bytes, SHA-256 prefix `0ac8f6ea5a3dff66`, matches MANIFEST line 200. |
| `lindorfer2015marvin` | Retained in G2 and 2.3 without change: within-system benefit of combining static and dynamic features. | Previously verified under T-025; claim unchanged. | `references/pdf/lindorfer2015marvin.pdf`, 878,249 bytes, prefix `fb9510cd7df67f58`, matches MANIFEST line 162. |
| `onwuzurike2018family` | Retained in Chapter 1, G2 and 2.3 without change: modality comparison through a common behavioural model. | Previously verified under T-025; claim unchanged. | `references/pdf/onwuzurike2018family.pdf`, 694,384 bytes, prefix `1eb456ac92b3b2e2`, matches MANIFEST line 204. |
| Chapter 4, no citekey | Application-level alignment as the answer to the first part; the within-system contrasts (Table 4.4) as the answer to the second. | Full chapter read on 22 September 2026. | Repository source. |

No citekey is added. Existing citations in edited passages keep their claims.

### Outcome

Changed: `dissertationmacros.tex` (RQ2 macro); Chapter 1 problem statement (common-unit
requirement and both parts of RQ2), RQ2 operationalisation, Hybroid contribution sentence and
Table 1.2 row; Section 2.3 feature-level fusion sentence, G2 heading and body; Chapter 4
opening (part-to-section map), Section 4.11 opening and summary (one paragraph per part);
Chapter 8 RQ2 answer; structure v0.3. Chapters 3, 5, 6 and 7 and both abstracts checked: the
abstracts already state the joint representation and both contrasts, and the Discussion frames
Hybroid as a matched comparison, so they are unchanged. No citekey added; no value changed.

Strict audits pass: introduction 38, background 119, hybroid 40 keys, 0 needing attention.
`latexmk thesis.tex` exits 0: 151 pages (unchanged). A first build reached 153 pages because
the longer Chapter 4 opening pushed the 4.2 heading off p. 49; the part-to-section map was
moved into the contribution paragraph, which restored every chapter start (Ch4 p. 49, Ch5
p. 65, Ch8 pp. 113-114). Log: 0 overfull and 0 underfull hboxes, 0 undefined references,
0 biber warnings, underfull vboxes 44 -> 48 (page-break shifts only), pre-existing end-group
notice unchanged. Root symlink intact. No visual review, staging or commit.

## Log

- 2026-09-22 created
- 2026-09-22 backlog -> in-progress (Author approved the revised RQ2 in chat (D-008); applying it thesis-wide)
- 2026-09-22 in-progress -> review (Revised RQ2 applied thesis-wide; audits and rebuild pass; visual review left to the author)
