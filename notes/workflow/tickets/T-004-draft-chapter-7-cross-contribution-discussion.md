---
id: T-004
title: Draft Chapter 7 Cross-Contribution Discussion
status: review
priority: P1
chapter: 7
owner: codex
depends_on: []
blocks: []
tags: [writing]
created: 2026-09-10
updated: 2026-09-20
---

## Goal

Revise Chapter 7 as a contribution-led synthesis in at most four pages. Under D-003, replace
the earlier seven sections with four connected discussions of contextual representations,
observation requirements and analysis cost, evaluation principles, and Android implications.
Remove repeated limitations and incidental detail while retaining brief qualifications
needed to interpret the evidence. The Hybroid/HGANN-Mal comparison remains conceptual.

## Why it matters

Chapter 7 is the only place where the four research streams are set against one another.
Chapter 1 promises it in Sections 1.2, 1.4 and 1.6, the Chapter 3 summary names it as a
consequence of the missing transfer evidence, and Chapter 5 promises it in Sections 5.1, 5.3
and 5.15. Section 5.3 cites Section 7.3 by label for a direct comparison of acquisition cost.
On 10 September 2026 the thesis stood at 145 pages against a 150-page ceiling with Chapters 7
and 8 as stubs, and the author fixed the length of this chapter at four pages. The earlier
ticket for this chapter (old T-023, created 13 August 2026) was lost in the tracker reset; its
three acceptance criteria are carried over below.

On 20 September 2026 the author approved the T-017 proposal and requested a constructive
dissertation voice. The revision should explain the scientific contribution before its
scope, and should not reproduce the earlier review as a catalogue of criticism. D-003
supersedes the seven-section requirement. Detailed limitations remain in Chapters 3 to 6.

## Acceptance criteria

- [x] Four contribution-led sections under D-003; the plan matches the text and the
      acquisition cross-reference `sec:discussion:3` remains valid.
- [x] At most four pages, with less main text than the previous 1,414-word draft. Remove
      Table 7.1 and the repeated limitations inventory.
- [x] Explain the joint significance of the studies, including the SWaT representation
      comparison and the reusable NADICS/SAFAIR interfaces, without implying a common experiment.
- [x] State the conceptual comparison; preserve the distinction between whole-system
      results and attribution to attention, and between predictive and adversarial evidence.
- [x] No numerical ranking between Hybroid and HGANN-Mal, no claim that one corrects the
      other's limitations, and no historical progression from IoT to Android.
- [x] Introduce no new empirical number or claim of confirmed SWaT selection independence.
      Retain the existing empirical results and detailed limitations in contribution chapters.
- [x] Only use keys already cited in the dissertation, with full-text/claim records below;
      pass strict audits for all changed chapter files.
- [x] Compile with latexmk, inspect new warnings and confirm that the tracked PDF is updated
      and the root symlink is intact. Leave visual review to the author.
- [x] Use concise academic English with varied paragraphs, British spelling and no em dashes;
      pass the workflow check and leave changes unstaged.

## Evidence and sources

### Pre-draft claim-to-source record, 20 September 2026

T-017 records the full cross-chapter review and primary metadata checks of 19 September.
The revision uses the same verified sources, with the IoT and TUM framework passages read
again for their positive design contributions. All core cited sources below are already
in `references/MANIFEST.tsv` with status `have` and a positive title check. A strict audit of
Chapters 3 to 7 passed before drafting: 113 cited keys, 104 PDFs and no unresolved entries
(the remaining keys have documented non-PDF status). The audit is saved locally in
`tmp/chapter7-revision-2026-09-20/pre-draft-reference-audit.txt`.

| Section | Core citekeys / evidence | Supported claim and verification status |
| --- | --- | --- |
| Contextual representations | `aubet2018graph` | Observed service relations and operator-approved updates. Full two-page primary text inspected; venue metadata recorded in the bibliography and the false template DOI is excluded. Vault PDF present. |
| Contextual representations | `norouzian2021hybroid` | Static and traffic observation, matched modality comparisons and task-dependent reported performance. Original method/evaluation text inspected in T-017; current Table 4.6 and its figure-provenance account checked. DOI metadata verified against Crossref on 19 September; vault PDF present. No new numerical claim is planned. |
| Contextual representations and cost | `norouzian2025hgannmal` | Static inputs, hyperedge construction and complete-system comparison. Original method and numerical tables inspected in T-017; DOI metadata verified through the DOI resolver. The additional operator and complexity statements come from the explicit derivations in current Sections 5.8 and 5.13, inspected before this revision. Vault PDF present. |
| Process representation | Current Chapter 3, Table 3.6; T-001 and structure v0.3 D-054/D-055 account | Qualitative comparison of the full-input and PCA configurations' reported recall/false-positive profiles. The later author-approved chapter account governs; the older supplied report describes a different evaluation. This paragraph will not identify a best configuration, assert test-independent selection, add numerical results or cite the unpublished report as a published source. |
| Observation requirements and cohort | `mahdavifar2020dynamic`; current Chapter 4 and T-012 | CICMalDroid's dynamic-analysis acquisition history versus HGANN-Mal's static inference; Hybroid's matched retained cohort. Dataset full-text Sections IV--V inspected and DOI metadata verified in T-017; vault PDF present. T-012 records the author's confirmation of the common Hybroid cohort. |
| Reusable learning framework | `iuno_ap4`; current Section 3.4 | TUM protocol-feature extraction and interchangeable learning methods. Full-text TUM account on printed pp. 12--13 inspected; document metadata verified against its primary cover/author record in the existing bibliography. Vault PDF present. The later partner LDA/Spark account is not attributed to NADICS. |
| Reusable evaluation and metric analysis | `sparta2022d76`; current Sections 6.6 and 6.8 | Shared execution with task-specific interfaces and the partner benchmark application. Full-text Sections 3.1.1--3.1.3 inspected; public deliverable metadata previously verified against its primary record. Mathematical claims refer to the current Chapter 6 derivations, not to new empirical findings. Vault PDF present. |
| Evaluation scope and Android implications | `pendlebury2019tesseract`, `carlini2019evaluating` | Time-aware evaluation as distinct from random corpus comparison; explicit valid perturbations and attacks against the complete defence. Relevant full-text arguments inspected in T-017; USENIX and arXiv primary metadata checked on 19 September. Both PDFs present. |

### Limits retained outside the main discussion

The missing source-publication defect ledger and old source-record directories remain as
recorded in T-017; current limitations and surviving tickets supply the available record.
The author's editorial approval does not resolve the SWaT configuration-selection wording
conflict in Chapter 3. The new Chapter 7 will omit the disputed assurance and will use only
the reported configuration profiles. No experimental fact will be supplied by assumption.

### Follow-up source record: Vicomtech citation and Chapter 6 framing

On 20 September the author asked whether Chapter 6 needs a stronger connection through the
distinction between AI for security and security of AI, and whether the Vicomtech reuse
sentence should carry a direct citation. The present edit adds that citation only; the
broader framing remains a recommendation for the author.

- Core key `sparta2022d76`: full-text Section 3.1.3.1, printed p. 28, explicitly records
  Vicomtech's benchmark evaluation of defences for a VGG16-based breast-cancer image
  classifier. It supports the application and reuse claim. The source is already in the
  vault with status `have`, title verified, and primary deliverable metadata recorded.
- `sparta2020d72`, Section 2.3.2, supplies the underlying histopathology/IDC setting and
  partner defence descriptions. Its full-text dataset passage was checked as supporting
  context, without adding another citation to the short reuse sentence.
- The proposed framing uses the existing RQ1--RQ4 distinction and Chapter 6's documented
  contest/framework contribution. `carlini2019evaluating` supports the explicit adversary
  and complete-defence evaluation requirements. Its full text and primary metadata were
  checked in T-017. This connection must describe evaluation methodology, not claim that
  Chapter 6 experimentally established robustness of the Chapter 3--5 detectors.
- Strict Chapter 7 audit passed before this citation edit: eight keys, eight PDFs and no
  unresolved entries.

Follow-up acceptance criteria:

- [x] Cite the Vicomtech sentence directly to D7.6 Section 3.1.3.1.
- [x] Pass the strict audit and rebuild; inspect the log without visual review.
- [x] Keep the broader framing recommendation separate from the applied citation change.

The citation-only follow-up compiles at 155 pages, with Chapter 7 still on pp. 113--115.
Its strict audit passes with eight cited sources. The final log has no undefined citations
or references and no overfull boxes; existing warning counts are unchanged. No visual
review was performed. The proposed next step is a short opening paragraph in Section 7.3
that distinguishes learning-based security analysis from the security of the learning system
itself, followed by a clearer conceptual link to the Android application in Section 7.4.
The paragraph should foreground the evaluation contribution, without implying that the
Chapter 3--5 detectors underwent Chapter 6's experiments.

## Revision outcome, 20 September 2026

### Approved Section 7.3 opening paragraph

The author requested insertion of the proposed short paragraph at the beginning of Section
7.3. The change is limited to that paragraph; Section 7.4 and the Vicomtech citation remain
unchanged. The evidence is the existing claim-to-source record for `carlini2019evaluating`
(explicit adversary assumptions and evaluation) and `sparta2022d76` (the SAFAIR contest and
benchmark), together with the current Chapter 6 contribution statement. Their full text
and primary metadata have been checked as recorded above, and both sources are in the
reference vault with status `have`. The strict Chapter 7 audit passed before insertion:
eight cited keys, eight PDFs and no unresolved entries. No new empirical claim or citekey
is introduced, and the paragraph does not imply that the Android detectors were tested in
the SAFAIR experiments.

- [x] Insert the approved paragraph once, immediately after the Section 7.3 labels.
- [x] Preserve the remainder of Chapter 7 and its contribution-led tone.
- [x] Pass the citation audit and compile; inspect the log and retain the root PDF symlink.
- [x] Leave visual review to the author and pass the workflow consistency check.

Inserted the approved paragraph with an explicit cross-reference to Chapter 6. The strict
audit passes with eight cited keys, and `latexmk thesis.tex` completes successfully at
155 pages. Chapter 7 remains on printed pages 113--115. The final log contains no undefined
citations/references or overfull boxes; existing template, end-group and underfull-page
warnings remain. The root PDF symlink is intact. No visual review was performed.

### Four-section revision and citation follow-up

- Replaced the seven-section limitations-heavy discussion with four contribution-led
  sections. Removed Table 7.1, repeated extraction-failure counts and peripheral hardware
  detail. The text now relates additional observations to relational encoding, identifies
  the distinct acquisition and computation requirements, and connects the reusable
  frameworks to controlled evaluation and the Chapter 6 analytical results.
- Retained brief qualifications for point estimates, attention attribution and the scope
  of Android robustness claims. Detailed contribution-chapter limitations and empirical
  values are unchanged. The Chapter 3 selection-language question remains recorded in
  T-017; this revision supplies no answer by inference.
- Applied narrow Chapter 5 consistency edits: distinguish conceptual from numerical
  comparison and separate static acquisition requirements from measured computation.
  Corrected the same cost conflation at the end of the efficiency discussion. The legacy
  acquisition label now resolves to Section 7.2. No other contribution chapter was edited.
- TeXcount: 1,414 to 956 main-text words, a reduction of 458 (32.4%). Chapter 7 occupies
  printed pages 113--115, with the recto-opening blank on page 116. Chapter 8 begins on
  page 117. The complete thesis has 155 pages, previously 157.
- Strict Chapter 7 audit passes with eight cited keys and eight PDFs. The combined strict
  audit of the changed chapters passes with 41 keys and no unresolved entries. No
  bibliography or reference-vault modification was needed.
- The first build used a prepended TeX Live PATH and reached the native biber launcher's
  obsolete `lipo -extract_family` call. The existing `~/.local/bin/biber` shim already
  handles this local toolchain issue. Preserving the configured PATH and running
  `latexmk -g thesis.tex` cleared the cached failure and completed successfully. No
  toolchain or build configuration was changed.
- Read the final LaTeX and biber logs. Undefined citations/references and overfull boxes
  remain at zero; template warnings and the pre-existing end-group warning remain.
  Underfull vbox notices decrease from 41 to 39. Biber reports no warning or error. The
  root `thesis.pdf` symlink resolves to the updated tracked PDF. No visual review was
  performed.
- 2026-09-20 review -> in-progress (Apply the approved four-section revision with a contribution-led tone and concise claim qualifications)
- 2026-09-20 in-progress -> review (Contribution-led four-section revision complete; three pages, strict audits and build pass)
- 2026-09-20 review -> in-progress (Add the direct Vicomtech case-study citation; assess stronger AI-for-security versus security-of-AI framing without expanding the text yet)
- 2026-09-20 in-progress -> review (Vicomtech citation added and rebuilt; stronger Chapter 6 connection proposed separately)
- 2026-09-20 review -> in-progress (Insert the approved short paragraph at the beginning of Section 7.3)
- 2026-09-20 in-progress -> review (Approved Section 7.3 opening paragraph added; citation audit and build pass)
