---
id: T-026
title: Apply the approved Chapter 1 scientific and readability revision
status: review
priority: P1
chapter: 1
owner: codex
depends_on: []
blocks: []
tags: []
created: 2026-09-20
updated: 2026-09-20
---

## Goal

Revise the Introduction within its six sections, align its research promises and attribution with the current dissertation, refine novelty and source claims, reduce repetition, update reference provenance and rebuild the tracked PDF without changing research-question wording or empirical results.

## Why it matters

The author approved the complete read-only Chapter 1 review with "do it". The
Introduction predates several revisions to the contribution chapters. Its attention-only
question and empirical-scope wording exceed the available evidence, while repeated
disclosures obscure the scientific contribution. D-006 records the approved revision.
The six sections and all research-question macros remain unchanged.

## Acceptance criteria

- [x] Define contextual representations and establish the Android focus early.
- [x] Position G1-G4 against the existing literature and current contribution evidence.
- [x] Distinguish complete-system comparison from attention-specific attribution, and
      reusable evaluation software from reproduction of historical experiments.
- [x] State the industrial and image-task scope explicitly; make no Android robustness claim.
- [x] Strengthen the supported findings and the dissertation's analytical contributions.
- [x] Correct citation interpretations, companion-paper authorship and evidence provenance.
- [x] Consolidate repeated disclosures and give the two tables different purposes.
- [x] Preserve settled individual contributions, including partial Hybroid graph work and
      the concept/measurement-design role in the service-graph study.
- [x] Update the software citation and publication map from primary records; retain the
      distinction between public deliverables and internal/confidential records.
- [x] Update the relevant planning/source records; pass strict audits and preservation checks.
- [x] Rebuild the tracked PDF, inspect the log, preserve the root symlink and leave changes
      unstaged. Visual review of the thesis stays with the author.

## Evidence and sources

### Review and preservation baseline

The preceding review read the complete Introduction, Chapters 2 to 8 and both abstracts.
All 41 cited sources were checked at claim level against relevant full-text passages and
source records. The strict audit passed with 39 PDFs and two web/software sources. This
was not a cover-to-cover reading of every cited publication or an experimental replication.
The review is recorded in the current Codex task, immediately before the author's approval.

Temporary primary-record responses and full-text extractions from that review are in
`/tmp/chapter1-review-hi7vwmgj/`. The revision baseline and additional source checks are in
`/tmp/chapter1-revision-hm0tb2ae/`. Durable claim and software records are provided here and
in `references/source-records/chapter1-software.md`; the temporary paths are not required
for subsequent citation audits.

The working tree already contains T-025 changes to Chapter 2 and narrow Chapter 5 passages,
with their bibliography, planning and PDF updates. Preserve them. The baseline records
tracked-file hashes, the original Introduction and bibliography, and the build log.
TeXcount reports 2,823 main-text words before question-macro expansion. The compiled PDF
has 153 pages; the log contains 47 underfull vertical boxes and no overfull horizontal boxes.

### Claim-to-source record, before drafting

| Section / claim | Core citekeys | Full-text, metadata and reference-vault status |
| --- | --- | --- |
| 1.1: Android observation and representation choices | `arp2014drebin`, `onwuzurike2019mamadroid`, `liu2023deeplearning`, `bilot2024survey` | Original feature/method descriptions and review scope inspected. DREBIN uses manifest and bytecode features; MaMaDroid uses statically recovered abstracted call sequences. Liu identifies 132 studies from 2014-2021. The graph-learning survey supports program-graph applications; GCN/GAT foundation papers alone do not establish deployment. DOI/publisher records and existing PDFs checked. |
| 1.1: time and population dependence of predictive results | `jordaney2017transcend`, `pendlebury2019tesseract`, `arp2022dos` | Full-text motivation, protocol and prevalence passages inspected against the USENIX originals. Arp's result concerns 30 selected papers and ten pitfalls, not all security research. Distribution shift is not unique to security. Existing primary PDFs and metadata checked. |
| 1.1: related samples and scoped duplication effects | `irolla2018duplication`, `zhao2021impact` | Irolla's opcode-duplication analysis and Zhao's supervised/unsupervised comparison inspected. Retain the distinction between tested supervised binary detectors and unsupervised family clustering. Publisher/DOI records and PDFs checked; Zhao's original carries DOI 10.1145/3446905. |
| 1.1: robustness evaluation and chronology | `athalye2018obfuscated`, `carlini2019evaluating`, `tramer2020adaptive` | Athalye's case study concerns nine non-certified white-box defences: seven used obfuscated gradients, six were circumvented completely and one partially. Carlini's February 2019 checklist precedes Tramer's 2020 study. Tramer's introduction says almost all of the 13 defences attempted adaptive evaluation. Full-text passages, first-page metadata and vault copies checked. |
| 1.1-1.2: valid malware transformations | `pierazzi2020intriguing` | Four-author March 2020 manuscript, arXiv v2, and DOI record inspected. Problem-space constraints include semantic preservation; a valid modified application must retain malicious functionality. Existing corrected vault version from T-025 is retained. |
| 1.2: observation limits and prior hybrid comparison | `moser2007limits`, `enck2014taintdroid`, `onwuzurike2018family` | Full-text analysis assumptions and static/dynamic comparison inspected; DOI records checked. Moser's construction concerns x86 obfuscation, not a Dalvik-specific empirical guarantee. TaintDroid provides an example of runtime observation. Hybrid benefits depend on the observation pair and task. PDFs available and checked. |
| 1.2: group membership, projection and prior hypergraph methods | `zhou2006learning`, `agarwal2006higherorder`, `zhang2023android`, `bai2021hypergraphattention` | Zhou's example/definition, Agarwal Section 5.2, Zhang's construction and Bai's attention formulation inspected. Typed star/incidence encodings preserve memberships; a clique projection may lose them. Android hypergraphs and hypergraph attention predate HGANN-Mal. New live DOI checks on 20 September confirm Agarwal, Zhang and Bai metadata; PDFs available and title-checked. |
| 1.2: existing evaluation infrastructure | `rauber2017foolbox`, `kurakin2018competition`, `carlini2019evaluating` | Foolbox interfaces and robustness criteria, the NIPS 2017 competition design and independent-team rationale, and Carlini's threat-model/reproducibility criteria inspected. Original arXiv/publisher records checked; Kurakin's DOI metadata rechecked live. The gap concerns reusable protocols and interpretable measurements, not the absence of libraries or competitions. |
| 1.2-1.4: service and process observation settings | `aubet2018graph`, `mathur2016swat`, `iuno_ap4`, `iuno_ap7` | Two-page service-graph source, SWaT testbed description and relevant IUNO tool passages inspected. Service changes motivate operator-approved graph updates; process measurements differ from traffic. The framework and SWaT empirical account remain those of Chapter 3 and the candidate's internal records. Existing PDFs checked. |
| 1.3-1.4: Hybroid's method and modality findings | `norouzian2021hybroid` | Original LaTeX and publication pp. 271-274 inspected; the published Figure 8/9 page was viewed to verify the data, not to review thesis layout. Fusion leads the detection F1 bars; category F1 improves for the ensembles and is lower for the decision tree. The results are descriptive fold means on the retained cohort, with T-012/T-021 qualifications preserved. DOI and original PDF checked. |
| 1.3-1.4: HGANN-Mal comparisons and operator analysis | `norouzian2025hgannmal` | Original LaTeX result tables and publisher PDF inspected. Hypergraph configurations exceed pairwise baselines; HGANN-Mal exceeds the best non-attentive accuracy in three of four combinations and scores 97.6 vs 97.7 in the fourth. No attention-only ablation is inferred. The operator-capacity statement is the analysis in Chapter 5.8, distinct from an empirical explanation. DOI metadata verifies online publication in 2025 and the ISC 2025 volume with a 2026 imprint. |
| 1.2-1.4: SAFAIR scope, reusable interfaces and scoring analysis | `sparta2020d72`, `sparta2021d73`, `sparta2021d75`, `sparta2022d76`, `norouzian2021adversarialbenchmark`, `norouzian2021safairtoolkit` | Contest and benchmark passages, original D7.6 Table 2 and D7.2 Section 2.3.2.1 inspected. The partner dataset is histopathology; there is no Android robustness experiment. Constant-predictor and binary-response identities are the analyses in Chapter 6. Original report covers verify metadata; public software README/guide and primary commit records checked. D7.2/D7.3 vault files were missing despite `have` rows and were restored from byte-identical copies in `publications/SPARTA/`, matching the existing manifest hashes. |
| 1.5: publication identities and individual roles | `aubet2018graph`, `pahl2018all`, `pahl2018graphbased`, `iuno_ap4`, `iuno_ap7`, `iuno2017d42`, `norouzian2021hybroid`, `norouzian2025hgannmal`, `sparta2021d71`, `sparta2020d72`, `sparta2021d73`, `sparta2021d75`, `sparta2022d76` | Original author/editor lists inspected. All Eyes on You has Pahl/Aubet; the NOMS companion has Pahl/Aubet/Liebald. Hybroid records shared first authorship. IUNO/SPARTA lists generally operate at document level. Individual work allocations follow the existing author-confirmed accounts in Chapters 3, 4, 5 and 6, not inference from author order. Public D7.2/D7.3 are added to the publication map; confidential D7.4 and unpublished IUNO/SWaT records remain outside it. |
| 1.5: contest software identity and persistent access | `norouzian2021safairtoolkit`, `norouzian2021adversarialbenchmark` | Live GitHub commit and directory APIs verify the toolkit tree at f44ba8c4ea13ab4b2439f47fb5ea5e625e25a8f4, authored on 8 November 2021. Full startup guide inspected; bibliography will use the public pinned path. This is separate from benchmark revision 2fac62b947ed. Both are registered `no-pdf` software resources. Metadata proves source identity, not reproduction of the historical experiments or sole authorship of every repository file. |

Core-source audit before drafting:
\cite{arp2014drebin,onwuzurike2019mamadroid,liu2023deeplearning,bilot2024survey,jordaney2017transcend,pendlebury2019tesseract,arp2022dos,irolla2018duplication,zhao2021impact,athalye2018obfuscated,carlini2019evaluating,tramer2020adaptive,pierazzi2020intriguing,moser2007limits,enck2014taintdroid,onwuzurike2018family,zhou2006learning,agarwal2006higherorder,zhang2023android,bai2021hypergraphattention,rauber2017foolbox,kurakin2018competition,aubet2018graph,mathur2016swat,iuno_ap4,iuno_ap7,iuno2017d42,pahl2018all,pahl2018graphbased,norouzian2021hybroid,norouzian2025hgannmal,sparta2021d71,sparta2020d72,sparta2021d73,sparta2021d75,sparta2022d76,norouzian2021adversarialbenchmark,norouzian2021safairtoolkit}.

### Constraints on the revision

- Preserve the six section titles, existing labels and research-question calls/macros.
- Keep all contribution-chapter sources, equations, empirical tables and figure assets unchanged.
- Keep the Hybroid partial graph contribution and the IoT concept/measurement-design role.
- Treat project partners' defence methods and experiments as their work, even where the
  candidate authored the reporting deliverable.
- Leave SW-01 and the HGANN-Mal preprocessing/slicing questions unresolved. No empirical
  issue is marked corrected merely because introductory wording changes.
- Avoid a universal claim of protocol compliance, prospective performance or adversarial
  robustness. The studies retain their original evidentiary limits.

## Log

### Implementation and verification

- Rewrote the research context and problem statement around contextual representations,
  prior methods and the actual evaluation domains. Removed the unsupported adoption/volume
  claims and the broad attention-expressivity statement; the latter's scoped theory remains
  in Chapters 2 and 5. Corrected the robustness-paper chronology and quantifiers, the
  problem-space validity requirement and the clique/incidence distinction.
- Retained all six section titles, all nine labels and the six research-question calls
  exactly. Research-question macros are byte-identical. The contribution list now leads
  with the Android studies and states the principal supported findings and analytical work.
- Consolidated individual contributions in Section 1.5. The candidate's service-graph role
  is concept and measurement design; both companion papers have the correct author lists.
  Hybroid's shared first authorship and partial graph contribution remain explicit.
  The public-source table retains its earlier entries and adds D7.2, D7.3 and the separate
  benchmark software. The RQ table now maps questions to scientific evidence, without a
  repeated role/publication inventory.
- Updated only the toolkit bibliography entry relative to the inherited bibliography.
  Its public pinned source replaces the TUM-login URL. Updated its manifest row and the
  D7.2/D7.3 restoration records, with durable software provenance and the guide checksum.
- Updated the Chapter 1 outline record and the literature map's context remit. No empirical
  defect was marked resolved. Other chapter sources and all method/result/figure assets
  remain unchanged; 691 protected paths passed the hash-preservation check.
- TeXcount main-text words fall from **2,823 to 2,019**, a reduction of **28.48%**, before
  question-macro expansion. All six question boxes remain. The rebuilt Introduction
  text and tables occupy printed pages **1-7**, followed by the recto-opening blank on
  page 8; Chapter 2 still begins on page 9. The complete PDF remains **153 pages**.
- Strict reference audits pass for **38 Introduction keys** and **177 whole-thesis keys**.
  The Introduction's 36 PDFs physically exist and match the manifest hashes; its two
  software resources have documented source revisions. The chapter cites only sources in
  the pre-drafting gate. `git diff --check` passes.
- Compilation succeeds with the user's existing Biber shim and the normal inherited PATH.
  The first attempt prepended `/Library/TeX/texbin` and bypassed that shim, exposing the
  packaged universal Biber launcher's obsolete `lipo -extract_family` call. The cached
  failure required `latexmk -g thesis.tex`; a subsequent plain `latexmk thesis.tex` succeeds
  and reports up-to-date targets. No tool installation or global configuration was changed.
- The final log has no undefined references/citations, Biber warnings or overfull boxes.
  Existing template/end-group notices remain. Underfull vertical boxes increase from
  **47 to 49**, with no underfull horizontal boxes. These layout notices are left for the
  author's review. No visual review of the rebuilt thesis was performed; the primary
  Hybroid source figure was inspected only to verify its reported values.
- The root `thesis.pdf` remains a symlink to `output/pdf/thesis.pdf`. No second compiled
  thesis PDF, staging, commit or push was created.

- 2026-09-20 created
- 2026-09-20 in-progress -> review (Approved Chapter 1 revision complete; source gates, preservation checks, strict audits and PDF rebuild pass)
