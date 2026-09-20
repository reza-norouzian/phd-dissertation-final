---
id: T-025
title: Apply the approved Chapter 2 scientific and readability revision
status: review
priority: P1
chapter: 2
owner: codex
depends_on: []
blocks: []
tags: []
created: 2026-09-20
updated: 2026-09-20
---

## Goal

Correct source claims, add missing foundations, refine research gaps and reduce repetition while retaining seven sections and all 18 metric equations; repair reference records, reconcile planning context and rebuild the thesis PDF.

## Why it matters

The author approved the complete Chapter 2 review with "do them all". The review found
misreported source findings and overly broad analysis guarantees, as well as repeated
explanations and missing prerequisites for the contribution chapters. D-005 records the
approved scope. D-004's shared performance-measures treatment remains in force.

## Acceptance criteria

- [x] Correct the permission/PScout claims, static-analysis coverage and call-graph soundness.
- [x] Separate hypergraph encoding from operator expressivity; correct the attention and
      network-study interpretations and remove unsupported literature-absence claims.
- [x] Add concise component/lifecycle, dependence/slicing and graph-readout foundations;
      distinguish learning regimes and map observation units to prediction targets.
- [x] Refine G1 and G3-G4 against the research questions and current contribution evidence;
      retain the scoped G2 rationale and all existing question/gap labels.
- [x] Reduce repeated explanations and informal commentary while retaining seven sections,
      both figure assets and all 18 metric equation blocks.
- [x] Replace the universal protocol-compliance assertion with explicit evaluation criteria;
      preserve unreported settings as unresolved rather than supplying them.
- [x] Repair the Wang title and the Pierazzi source version; verify and vault new sources.
- [x] Re-establish the missing source-record index and a bounded current defect ledger;
      reconcile the relevant planning and literature-map passages.
- [x] Make only narrow related wording corrections outside Chapter 2; preserve contribution
      methods, empirical table bodies, equations and figures.
- [x] Pass strict citation, source-preservation and workflow checks; compile, read the log,
      preserve the root PDF symlink and leave the unstaged changes for author review.

## Evidence and sources

### Review and preservation baseline

The preceding read-only review covered the complete Chapter 2 and the other substantive
chapters. It audited 114 citations (110 PDFs and four live documentation references), checked
their bibliographic records, and inspected claim-bearing full-text passages. This was a
claim-focused audit, not a cover-to-cover reading of every publication or an exhaustive
literature search. Primary-record responses and full-text extractions were retained in
`/tmp/thesis-ch2-review-xoyvkk7s/`; the metadata inventory and records needed for this revision
are copied to `tmp/background-revision-2026-09-20/`.

The working tree was clean before this task. The baseline contains tracked-file hashes,
the complete original Chapter 2, its 18 equation blocks and all labels, and the existing
build warnings. TeXcount gives 5,947 main-text words, excluding headings and captions. The
compiled thesis has 155 pages. No second compiled thesis PDF is created.

### Claim-to-source record, before drafting

| Section / claim | Core citekeys | Full-text, metadata and vault status |
| --- | --- | --- |
| 2.1: APK contents, application sandbox, component entry points and lifecycle | `aosp2026appfundamentals`, `arzt2014flowdroid` | Live Android Developers article inspected, including App components and The manifest file; registered as a web resource. FlowDroid Sections 2-3 and its limitations inspected; DOI record and existing PDF/title check verified. |
| 2.1: DEX instructions, opcode/operand distinction and ART | `aosp2026dexformat`, `aosp2026dalvikbytecode`, `aosp2026art`, `arp2014drebin` | Official documentation inspected in the review, with current access dates retained. DREBIN feature-extraction passages inspected; original PDF and NDSS DOI record verified. The chapter does not infer operand values from the runtime. |
| 2.1: permission protection levels and permission/API mapping | `felt2011android`, `aosp2026permissions`, `au2012pscout`, `sabbah2026understanding` | Felt Section 2 explicitly assigns powerful operations to Signature/System permissions. Current Android documentation distinguishes runtime and signature permissions. PScout abstract and Sections 2-5 inspected: over 75 is the permission count, not the number of undocumented mappings. Sabbah's study concerns permission deprecation and drift. All papers have inspected full text and primary metadata; web documentation is registered. |
| 2.1: analysis coverage, hybrid observation and obfuscation | `moser2007limits`, `onwuzurike2018family`, `lindorfer2015marvin`, `duan2018things`, `gao2024comprehensive` | Relevant method/evaluation passages inspected against the primary records. Moser constructs difficult opaque constants for x86 binaries; no Dalvik-specific experimental result is inferred. The hybrid studies support setting-dependent modality comparisons. DroidUnpack supports concealed payloads and unpacking limits, not failure of every static feature. Existing PDFs/title checks pass. |
| 2.2: CFGs, FCGs and their approximate recovery | `bilot2024survey`, `gascon2013structural`, `arzt2014flowdroid` | Graph-type definitions and FlowDroid limitations inspected. Practical recovery can introduce infeasible edges and omit unresolved behaviour. DOI records and existing PDFs/title checks verified. |
| 2.2: dependence, backward slicing and interprocedural calling context | `horwitz1990interprocedural` | New source: DOI 10.1145/77606.77608 verifies authors, TOPLAS 12(1), 26-60, 1990. The definitions and calling-context discussion in Sections 1-2 of the University of Wisconsin author manuscript were inspected before drafting; further validation examined Sections 3-4. Vaulted and title-checked before drafting. The background definition does not establish the undocumented scope of the Chapter 5 slicer. |
| 2.2: incidence notation, clique projection and operator equivalence | `zhou2006learning`, `agarwal2006higherorder`, `chitra2019randomwalks`, `wang2024graphs` | Definitions and relevant theorems inspected. Chitra Theorems 3.1-3.2 concern their specified random walks; edge-dependent examples can fail equivalence. Wang Section 1 fixes an unweighted same-vertex-set clique projection. Typed incidence graphs retain memberships. Primary records and PDFs checked; Wang's title is corrected to Remediation. |
| 2.2: empirical expansion/embedding evaluation and expressivity | `kang2024low`, `jiang2026widthwall` | Full-text method and scope passages inspected. MILEAGE evaluates expansion, learned embeddings and reconstruction together. WidthWall is retained as a 2026 preprint, not described as settled evidence about every architecture. Existing vault entries and primary metadata checked. |
| 2.3: message passing, learned transforms, graph readout and expressivity limits | `gilmer2017neural`, `kipf2017semi`, `xu2019powerful`, `li2018deeper` | Original formulations, graph-level readout and permutation requirements inspected. The 1-WL bound is scoped to standard neighbourhood aggregation with corresponding initial features. Oversmoothing is a risk of repeated propagation, not an inevitable result for all GNNs. Existing PDFs and primary records verified. |
| 2.3: attention ranking and empirical comparisons | `velickovic2018graph`, `brody2022gatv2`, `fang2025kaa` | Original attention formulation, Brody's static-ranking argument and Fang Table 2 inspected. Fang reports GAT 82.76 vs GCN 81.99 on Cora, with the other non-attentive baselines lower, contradicting its own categorical prose. Use task-dependent reported means without claiming significance. Primary records/PDFs checked. |
| 2.3: hypergraph propagation, fixed support and later developments | `feng2019hypergraph`, `gao2023hgnn`, `bai2021hypergraphattention`, `chien2022allset`, `kim2022equivariant`, `kim2021transformers`, `li2026highpass`, `gao2026hgnnv2` | Architecture and theory-scope passages inspected in the review. Explain two-stage propagation and alternative architectures; identify the fixed support of HGANN-Mal through Chapter 5's documented operator. HGNNv2 is a later stability-oriented design, not proof that prior operators are obsolete. Existing PDFs/primary records checked. |
| 2.3 / G3: existing Android hypergraph work | `zhang2023android` | Publisher paper inspected, especially its introduction and construction sections; DOI record and existing 14-page PDF/title check verified. Supports prior Android hypergraph-level classification with call-neighbour and permission-based groups. No cross-paper numerical ranking is introduced. |
| 2.4: flow units, label regimes, reconstruction and relational anomalies | `sperotto2010overview`, `paxson1999bro`, `chandola2009anomaly`, `ruff2021unifying`, `pang2021deep`, `akoglu2015graph` | Definitions and relevant method-family passages inspected; existing full texts and DOI records checked. Conventional IP flow keys do not define every service message or layer-2 industrial record. Reconstruction discrepancies are anomaly scores, not direct proof of an attack. |
| 2.4 / G1: industrial observations and changing settings | `barbosa2013flow`, `yoon2014communication`, `goh2016swatdataset`, `mathur2016swat`, `maali2025evaluating` | Methods and observation settings inspected. Maali's experiment is IoT device identification, explicitly distinct from anomaly detection. G1 concerns suitable representations and update/interface requirements, not demonstrated cross-site transfer. Existing primary records and PDFs checked. |
| 2.4: benchmark and baseline evidence | `flood2024bad`, `kus2022false`, `wolsing2022simple` | Flood's construction-bias examples, Kus's unseen-attack comparisons and Wolsing Sections 3/5 inspected. Wolsing surveys 70 publications and evaluates four SIMPLE detectors against selected comparators; it does not rerun 70 systems. Existing PDFs and DOI records verified. |
| 2.5 / G4: attacker knowledge, capabilities, valid inputs and evaluation infrastructure | `biggio2014security`, `biggio2018wildpatterns`, `vassilev2025adversarial`, `pierazzi2020intriguing`, `carlini2019evaluating`, `rauber2017foolbox`, `kurakin2018competition` | Taxonomy and evaluation passages inspected. Grey-box knowledge is separated from the fixed-training constraint of the Chapter 6 evasion setting. Pierazzi's four-author March 2020 manuscript (arXiv v2) replaces the six-author 2024 extension. Foolbox Sections 1.1-1.2 and the competition's design/threat-model sections inspected; primary arXiv/DOI records checked. Existing infrastructure is acknowledged before G4. |
| 2.6: shared metrics and aggregation conventions | `fawcett2006roc`, `grandini2020metrics`, `opitz2019macrof1`, `axelsson2000base`, `sorbo2024navigating`, `sparta2022d76` | T-023's inspected full-text records remain applicable; all equations are preserved. The review independently checked micro/weighted identities, macro-F1 inequalities, prevalence identities and tied-score AUC. Grandini's problematic alternative formulas are not adopted. All cited sources remain vaulted/registered. |
| 2.6: leakage, target populations, temporal evaluation and event scoring | `arp2022dos`, `pendlebury2019tesseract`, `jordaney2017transcend`, `chow2025beyond`, `kan2024tesseract`, `zhao2021impact`, `irolla2018duplication`, `kim2022towards`, `liu2024elephant`, `bilot2025sometimes`, `daoudi2021lessons` | Claim-bearing full-text passages and primary records inspected in the review. Precision is conditional on the evaluated population; temporal splits target prospective performance. Zhao's supervised result concerns binary detection, distinct from its unsupervised clustering result. State reporting criteria without certifying compliance of historical experiments. Existing vault entries pass. |

The observation/target table is a map of the current contribution chapters, not a new
experiment. Its units are also supported by the original Hybroid/HGANN-Mal publications and
SPARTA D7.6, with the Chapter 3 internal-record distinctions retained from T-001/T-023.
It adds no counts, detection rates or implementation settings.

Weiser (1984) was considered as an additional source. Its DOI metadata resolved, but a full
text was not obtained in this task. It is not newly cited. Horwitz et al. provide the inspected
primary account used for dependence and slicing.

Core-source audit before drafting:
\cite{aosp2026appfundamentals,aosp2026dexformat,aosp2026dalvikbytecode,aosp2026art,aosp2026permissions,arp2014drebin,arzt2014flowdroid,felt2011android,au2012pscout,sabbah2026understanding,moser2007limits,lindorfer2015marvin,onwuzurike2018family,duan2018things,bilot2024survey,gascon2013structural,horwitz1990interprocedural,zhou2006learning,agarwal2006higherorder,chitra2019randomwalks,wang2024graphs,kang2024low,jiang2026widthwall,gilmer2017neural,kipf2017semi,xu2019powerful,li2018deeper,velickovic2018graph,brody2022gatv2,fang2025kaa,feng2019hypergraph,gao2023hgnn,bai2021hypergraphattention,chien2022allset,kim2022equivariant,kim2021transformers,li2026highpass,gao2026hgnnv2,zhang2023android,sperotto2010overview,chandola2009anomaly,ruff2021unifying,pang2021deep,akoglu2015graph,barbosa2013flow,yoon2014communication,goh2016swatdataset,maali2025evaluating,flood2024bad,kus2022false,wolsing2022simple,biggio2014security,biggio2018wildpatterns,vassilev2025adversarial,pierazzi2020intriguing,carlini2019evaluating,rauber2017foolbox,kurakin2018competition,fawcett2006roc,grandini2020metrics,opitz2019macrof1,axelsson2000base,sorbo2024navigating,sparta2022d76,arp2022dos,pendlebury2019tesseract,jordaney2017transcend,chow2025beyond,kan2024tesseract,zhao2021impact,irolla2018duplication,kim2022towards,liu2024elephant,bilot2025sometimes,daoudi2021lessons}.

### Scope limits and record repair

- Method-specific equations, experimental tables and figure assets outside Chapter 2 are
  preserved. Related wording corrections may qualify Chapter 5's recovered-call-graph and
  attention statements, without changing the method or treating missing ablations as completed.
- The original defect ledger and old chapter-source directories are absent from the available
  history. New indexes identify the surviving evidence and their reconstruction date; they do
  not recreate lost ticket numbers or claim complete historical coverage.
- Chapter 3's model-selection history and Chapter 5's preprocessing/slicing specifications
  remain unresolved. Definitions and editorial approval cannot establish those facts.

### Implementation and verification

- Revised the scientific explanations in Sections 2.1-2.5. Corrected the permission and
  PScout interpretation, bounded static coverage, and distinguished approximate call-graph
  recovery from sound over-approximation. Hypergraph projection and random-walk results now
  retain their stated scope. Attention comparisons follow Fang's Table 2 rather than its
  contradictory prose. Wolsing's review and Maali's identification task are identified correctly.
- Added component/lifecycle and dependence/slicing foundations, graph-level readout and
  permutation properties, and a distinction between label regimes and reconstruction scores.
  Table 2.1 maps decision units to prediction targets without supplying new empirical values.
- Replaced the universal protocol-compliance assertion with reporting criteria. G1 now concerns
  representation and maintenance, G3 distinguishes construction from aggregation, and G4
  acknowledges existing evaluation infrastructure. G2 is byte-identical to its approved wording.
- Retained all seven main sections, all subsection headings and all existing labels. All 18
  numbered metric equation blocks are byte-identical to the baseline. The existing vertex and
  hyperedge degree identities are formatted as one unnumbered display to avoid an overfull line;
  this adds no mathematical identity. Both figure assets are unchanged; Figure 2.1's caption
  now describes bounded static and dynamic coverage.
- Made two narrow Chapter 5 corrections concerning recovered call graphs and Fang's reported
  attention results. Its 23 equation blocks, construction algorithm, table bodies and figure
  blocks are unchanged. All other contribution chapters and the research-question macros are
  byte-identical to the baseline.
- Added two verified bibliography entries: Android application fundamentals and Horwitz et al.
  Added three existing verified references to Chapter 2 for prior Android hypergraph work and
  evaluation infrastructure. All original 114 Chapter 2 citations remain, giving 119 in total.
  Corrected Wang's title/author spelling and primary URL, and pinned Pierazzi's 2020 source
  version. The four existing Android documentation records have current access dates and URLs.
- Re-established the Chapter 2 source-record index and a bounded current defect ledger, with
  unresolved empirical specifications left open. Updated the relevant structure and literature
  plans. The missing historical records and their identifiers are not reconstructed.
- Main prose falls from 5,947 to 4,495 words by TeXcount, a reduction of 24.42%, excluding
  headings and captions. Chapter 2 occupies printed pages 9-24; Chapter 3 starts on page 25.
  The full PDF has 153 pages, down from 155.
- The strict Chapter 2 audit passes for 119 citations; the whole-thesis audit passes for 179.
  Read-only checks confirm that the 114 cited local PDFs have the recorded hashes and valid
  PDF headers. New and corrected sources have passed title checks.
- `latexmk thesis.tex` succeeds. The final log contains no undefined citations/references,
  biber warnings, LaTeX errors or overfull boxes. The 21 existing template-warning notices
  remain, as does the previously recorded end-group notice. Underfull vertical-box notices
  increase from 44 to 47. The two overfull lines introduced in the first build were corrected
  through paragraph/degree-definition formatting, without changing the template.
- Source-preservation checks pass. The PDF is newer than the changed LaTeX and bibliography,
  and the root PDF symlink still points to the sole compiled output. No visual review,
  staging or commit was performed.

Verification records: `tmp/background-revision-2026-09-20/final-verification.json`,
`preservation-checks.json`, `audit-chapter2.txt`, `audit-whole-thesis.txt` and `latexmk.log`.

## Log

- 2026-09-20 created
- 2026-09-20 in-progress -> review (Approved scientific/readability revision complete; source-preservation checks, strict citation audits and PDF rebuild pass)
