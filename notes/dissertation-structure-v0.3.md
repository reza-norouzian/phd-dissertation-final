# Dissertation structure, version 0.3

Date: 2026-08-12

This planning document incorporates the author's second answer set. It does not alter the
compiled LaTeX thesis.

## Decisions fixed in this version

- The dissertation is an integrated monograph.
- Android malware analysis forms the scientific centre.
- The anomaly-detection work is an early original contribution and receives a research
  question, although its chapter remains short.
- RQ1 uses one umbrella question and two subquestions. RQ1.1 concerns communication graphs
  for IoT services. RQ1.2 concerns the modular NADICS/IUNO learning framework for industrial
  control systems.
- The graph and framework studies provide complementary answers to RQ1. The dissertation
  will not claim that they were integrated or compared in one experiment.
- The IoT microservice graph work did not influence Hybroid. The dissertation will not
  present a historical progression between them.
- Hybroid and HGANN-Mal will be compared as two approaches to contextual Android malware
  analysis. The comparison is conceptual unless the author later establishes a direct
  developmental link.
- The Drebin multiclass task is malware-family classification.
- The CICMalDroid multiclass task is malware-category classification, with Benign as one
  category.
- The 120-170 page limit includes front matter, references, appendices, and blank pages.
  170 pages is the maximum (D-045); the planning target below is unchanged.
- The broader title direction has been selected.

## Working title

**Learning-Based Security Analysis: Contextual Representations and Adversarial Evaluation**

The title remains a working title until the research questions and contribution statements
are approved by the supervisor.

## Dissertation argument

The dissertation examines the representation and evaluation of context in learning-based
security analysis. The early anomaly-detection work represents communication behaviour in
IoT and industrial networks. The Android chapters form the main contribution. Hybroid
combines program structure with observed network behaviour, whereas HGANN-Mal represents
higher-order relations within static program structure. The SPARTA work addresses the
assessment of ML defences under adversarial input.

Two research themes organise these contributions. RQ1-RQ3 concern representations of
security-relevant behaviour. RQ4 concerns evaluation under explicit adversary assumptions.
The themes meet in the cross-contribution discussion, where representation quality and
evaluation validity are examined together.

The dissertation will compare the graph-based IoT work with the later Android
representations at a methodological level. It will state that the IoT study did not motivate
Hybroid. This distinction prevents a retrospective narrative from being presented as
research chronology.

## Research questions

### RQ1: Behaviour in networked and industrial systems

**How can behaviour in networked and industrial systems be represented to support anomaly
detection?**

#### RQ1.1: Communication graphs

**How can service relationships be represented as communication graphs to identify
unexpected interactions?**

The graph-based study answers RQ1.1 through its relation model, graph-update process, and
overhead measurements. It does not report detection accuracy against a labelled attack set.

#### RQ1.2: Modular industrial anomaly detection

**How can a modular learning framework analyse network and process features for anomaly
detection in industrial control systems?**

NADICS and IUNO answer RQ1.2 through packet and flow processing, feature representation,
and modular learning components. The chapter must document the candidate's design,
implementation, and evaluation roles before it assigns originality to individual elements.

### RQ2: Multimodal Android malware analysis

**To what extent does fusing static code-graph representations with dynamic network-flow
features improve Android malware detection and category classification compared with either
modality alone?**

Chapter 4 answers RQ2 through Hybroid. It uses corrected dataset counts and precise graph
terminology, and it bases the answer on the reported within-system modality comparison.

### RQ3: Higher-order Android malware analysis

**To what extent do attention-weighted hypergraph representations of static Android program
structure improve binary malware detection and malware classification over pairwise graph
models and non-attentive hypergraph models?**

Chapter 5 will report the multiclass tasks with dataset-specific terminology:

- Drebin: malware-family classification.
- CICMalDroid: malware-category classification, including Benign.

Binary detection remains a separate evaluation task. Chapter 5 now documents the AndroZoo
benign cohort used for Drebin binary detection. Its remaining label-curation and temporal
qualifications are stated in that chapter.

### RQ4: Adversarial robustness evaluation

**How can an explicit adversary model be translated into a reproducible benchmark for
adversarial attacks and defences, and what does such a benchmark reveal about the relation
between clean predictive performance and adversarial robustness?**

Reworded on 15 August 2026 under D-030. The earlier wording asked "what trade-off does the
benchmark reveal", which presupposes a trade-off that D7.6 Table 1 does not show. See the
decision for the reasoning and for the four files the change touches.

Chapter 6 will answer RQ4 through the SPARTA threat analysis, SAFAIR contest, and modular
benchmark. The answer must account for the unrealised attack track, metric weaknesses, and
conflicting values across the deliverables.

## Relationship between Hybroid and HGANN-Mal

The dissertation should relate the two chapters because they address Android malware
analysis through different observation models:

- Hybroid combines static program information with runtime network evidence.
- HGANN-Mal uses static analysis and represents relations between several functions in one
  hyperedge.

This comparison supports the dissertation-level discussion of observability, representation
scope, data-acquisition cost, and model complexity. Numerical results from the two papers
cannot be compared directly because their datasets, task definitions, and validation
protocols differ.

The dissertation should not state that HGANN-Mal corrects a Hybroid limitation unless the
author confirms that motivation and the research record supports it. A defensible transition
is: Hybroid studies context across evidence sources, while HGANN-Mal studies richer context
within the program when the analysis relies on static information.

## Chapter and page plan

The full PDF should remain between 120 and 170 pages; 170 is a maximum, set by D-045 on
11 September 2026 (150 before). The planning target is 139 pages since D-051 (142 under D-044,
146 before), including blank pages caused by recto chapter openings.

| Component | Target pages |
| --- | ---: |
| Front matter | 10 |
| 1. Introduction | 9 |
| 2. Background | 15 |
| 3. Anomaly Detection in IoT and Industrial Control Systems | 15 |
| 4. Multimodal Android Malware Analysis with Hybroid | 23 |
| 5. Higher-Order Android Malware Analysis with HGANN-Mal | 27 |
| 6. Evaluating Adversarial Robustness: Benchmark Design and Metric Analysis | 15 |
| 7. Cross-Contribution Discussion | 4 |
| 8. Conclusion and Future Work | 2 |
| References | 13 |
| Appendices | 2 |
| Recto-page reserve | 4 |
| **Planning total** | **139** |

Revised on 10 September 2026 under D-044: Chapter 7 is four pages, so the planning total
falls from 146 to 142. The build of that date is 147 pages, because Chapter 3 (22 pages),
Chapter 6 (20 pages), the references (16 pages) and the front matter (18 pages) exceed their
targets. Chapter 8 must therefore stay at four pages or fewer to keep the thesis within 150
pages.

Revised on 11 September 2026 under D-045: the ceiling rises from 150 to 170 pages. The
planning total and the chapter targets are unchanged, so Chapter 8 keeps its five-page target
and the four-page restriction above no longer applies. The build of that date is 149 pages,
with Chapter 7 one page over its D-044 limit.

Revised on 11 September 2026 under D-046: the T-005 mathematical revision of Chapter 5 adds the
restored construction algorithm, the operator analysis, a worked example with one table, and
complexity and metric-consistency sections. Chapter 5 now runs pp. 63-91 with a recto blank on
p. 92, 30 pages against its 27-page target, and the build is 155 pages. The chapter targets are
unchanged; the author accepted the Chapter 5 overrun on 11 September 2026.

Revised on 13 September 2026 under D-060: the constructed six-method example, its equation and its
table are removed. Section 5.8 retains the representational conclusion in two sentences within the
operator analysis, without a separate heading. After the D-059 and D-060 cuts, Chapter 5 occupies
pp. 63--92, Chapter 6 begins on p. 93, and the full build is 157 pages.

Revised on 11 September 2026 under D-047: the two TikZ diagrams of Chapter 5 give way to the
author's five figures, three of them on landscape pages. Chapter 5 now runs pp. 63-96, 34 pages
against its 27-page target, Chapter 6 begins on p. 97, and the build is 159 pages. Cutting the two
dataset tables under D-048 shortened the chapter by less than a page and left that range unchanged.
Removing most pending markers at the author's instruction (12 September 2026) brings Chapter 5 to
pp. 63-94, 32 pages; Chapter 6 begins on p. 95 and the build is 157 pages.

Revised on 12 September 2026 under D-051: Chapter 8 is limited to two pages at the author's
request, so the planning total falls from 142 to 139. The chapter keeps its four sections and
typesets the research questions from their macros as run-in paragraphs. The build of that date is
157 pages, with Chapter 8 on pp. 121-122 and the references from p. 123.

The two Android chapters receive 50 pages, the largest share assigned to any research
stream. Chapter 2 holds the common foundations only. Each contribution chapter keeps a
section on the work specific to its method, and that is where competing systems are compared.

## Chapter outline

### 1. Introduction

1.1 Research Context

1.2 Problem Statement and Scope

1.3 Research Questions

1.4 Contributions

1.5 Publications, Projects, and Individual Contributions

1.6 Dissertation Structure

Revised on 20 September 2026 under T-026 and D-006 after the author approved the complete
Chapter 1 review. The six sections and all research-question macros are retained. The
Introduction defines contextual representations and gives the Android contributions
priority, with separate scope for the industrial studies and the image-based adversarial
evaluations. Its problem statements acknowledge existing hybrid, hypergraph and evaluation
methods. The RQ3 explanation concerns complete configurations; attention-only attribution
remains open. The RQ4 explanation distinguishes reusable interfaces from reproduction of
historical experiments and retains the limited clean-performance/robustness conclusion.

The contribution statements now include the dissertation's operator and scoring analyses.
Authorship is consolidated in Section 1.5, with the service-graph concept/measurement-design
role and partial Hybroid graph contribution preserved. The dissemination table includes
public SPARTA D7.2/D7.3 and the separate benchmark repository; the RQ map instead identifies
scientific evidence. The contest toolkit uses a verified public source revision. Other
chapter sources, empirical results and figures are unchanged. The nine-page planning
allowance is retained; build results are recorded in T-026.

The rebuilt Introduction's text and tables occupy printed pages 1-7, followed by the
recto-opening blank on page 8; the complete PDF has 153 pages.
Main-text prose decreases from 2,823 to 2,019 words before question-macro expansion
(28.48%), while all question boxes and the two tables are retained.

### 2. Background

Revised on 13 August 2026. The chapter is titled Background and carries seven sections, with
an original 15-page allocation before the D-004 metric expansion. Android material opens the chapter because Android malware analysis
is the scientific centre; the representation and learning sections follow it, so that a reader
meets hypergraphs only after function-call graphs have been defined.

2.1 Android Applications and Their Analysis

- Dalvik bytecode, component lifecycles, manifest and permission grants
- Static, dynamic, and hybrid analysis
- Obfuscation, packing, repackaging

2.2 Graph Representations of Programs

- Control-flow and function-call graphs; program dependence and backward slicing
- Hypergraphs, typed incidence representations and clique projection

2.3 Learning over Graphs

- Message passing, graph-level readout and permutation properties
- Attention
- Hypergraph convolution

2.4 Detection in Networked and Cyber-Physical Systems

- Flow and other observation units; supervised, normal-only and unlabelled learning
- Reconstruction and relational methods; industrial observations and measurement limits

2.5 Adversarial Machine Learning

- Goals, knowledge and capability constraints; feature-space and problem-space attacks
- Adaptive evaluation and existing attack-library/competition infrastructure

2.6 Performance Measures and Evaluation Methodology

  Expanded on 20 September 2026 under D-004 and T-023. The section defines the measures used
  across the contribution chapters, with the following subsections:

  - 2.6.1 Observation Units and Confusion Counts
  - 2.6.2 Binary Detection Measures and Class Prevalence
  - 2.6.3 Multiclass and Multilabel Aggregation
  - 2.6.4 ROC Curves and Area under the Curve
  - 2.6.5 Performance under Adversarial Input
  - 2.6.6 Aggregation and Operational Reporting
  - 2.6.7 Experimental Protocol and Bias

  The seven main sections and the existing evaluation label are retained. Mathematical
  definitions do not resolve unreported averaging conventions in the source studies, and no
  contribution-chapter results are changed. The addition introduces 18 numbered equations and
  three verified references. The first rebuild has 155 pages, with Chapter 2 occupying printed
  pages 9-26, above its original 15-page planning allowance. The original allocation below is
  retained as a planning reference; the overall 170-page maximum is unchanged.

  The author requested a shorter version later that day. T-023 reduces Section 2.6 prose from
  1,857 to 1,460 words while preserving all 18 equations and the subsection structure. The
  section now occupies pages 18-23. The thesis remains 155 pages because the shorter background
  is followed by a recto-opening blank before Chapter 3.

2.7 Summary and Research Gaps

A concise chapter synthesis precedes four numbered gaps, G1 to G4. Each identifies the
remaining design or empirical question and names the research question that addresses it.
Gaps acknowledge existing approaches rather than asserting an unsupported field-wide absence.

Revised on 20 September 2026 under T-025 and D-005 after the author approved the complete
Chapter 2 review. G1 concerns observation-specific representations and their maintenance,
without presupposing cross-site transfer. G2 retains the matched-modality comparison.
G3 distinguishes alternative hyperedge construction from learned weighting and their
component-specific attribution. G4 acknowledges existing evaluation infrastructure and
concerns reproducible protocols and interpretable clean/attacked measurements. The
research-question macros and gap labels remain unchanged.

The revision adds a compact decision-unit/target table in Section 2.6 and preserves its 18
equation blocks. Operator-specific derivations and empirical table bodies remain in the
contribution chapters. Only two related Chapter 5 passages are corrected: approximate
call-graph recovery and the task-dependent attention results in Fang et al. The two
background figure assets remain unchanged; Figure 2.1's caption no longer promises complete
static coverage.

The rebuilt chapter occupies printed pages 9-24, with Chapter 3 beginning on page 25. Main
prose decreases from 5,947 to 4,495 words (24.42%). The complete thesis has 153 pages, down
from 155; the overall 170-page maximum is unchanged. The 18 numbered metric equations are
preserved, and the existing degree definitions use one unnumbered display for line fitting.

#### Page budget for Chapter 2

| Section | Target pages |
| --- | ---: |
| 2.1 Android Applications and Their Analysis | 3.5 |
| 2.2 Graph Representations of Programs | 2.5 |
| 2.3 Learning over Graphs | 2.5 |
| 2.4 Detection in Networked and Cyber-Physical Systems | 2.0 |
| 2.5 Adversarial Machine Learning | 1.5 |
| 2.6 Performance Measures and Evaluation Methodology (original allocation before D-004) | 1.5 |
| 2.7 Summary and Research Gaps | 1.5 |
| **Total** | **15.0** |

#### Consequences of the revision

- The Research Gaps section is merged into the summary rather than dropped. Section 2.7
  states the gaps as numbered items G1 to G4, so that Chapter 1 can point at them and
  Chapter 8 can close them. An implicit gap statement, carried only by the wording of the
  research questions, would leave the questions looking chosen rather than derived.
- The chapter is background rather than a survey. Comparison against competing systems stays
  in the contribution chapters (4.2, 5.2, and the related-work passages of Chapters 3 and 6).
  Section 2.4 and Section 2.5 therefore describe method families and their measurement
  problems; they do not rank published systems.
- The old Learning-Based Security Analysis section is dissolved. Its framing material (the
  observation-to-decision procedure and the assumptions needed to interpret an evaluation)
  sits in the chapter preamble and Section 2.6.
- Network-flow representation, previously grouped with program graphs, now sits in Section 2.4
  next to the detection methods that consume it. Chapter 4 needs both flow features and program
  graphs, so Section 4.7 must state the flow feature set itself rather than rely on Chapter 2.
- Section ordering differs from contribution-chapter ordering: Chapter 3 draws on Section 2.4,
  which appears after the Android sections but still precedes Chapter 3. The Chapter 2
  preamble and decision-unit table provide the navigation; Section 3.3 retains its direct
  background reference.

#### Alignment with `notes/literature-map.md`

The Chapter 2 source plan in `notes/literature-map.md` uses the current section numbers and
routes each section to one or more thematic candidate pools. The pools retain the earlier
harvest counts because several topics contribute to more than one section. Section 2.7 adds
no new literature; it derives G1-G4 from sources already discussed in Sections 2.1-2.6.

### 3. Anomaly Detection in IoT and Industrial Control Systems

3.1 Scope, Research Question, and Contributions

3.2 Observation Models and Datasets

3.3 Communication Graphs for IoT Services

3.4 The NADICS Framework and IUNO Integration

3.5 A GAN-Based Multivariate Detector for SWaT

    3.5.1 Model and Training
    3.5.2 Input Representations and Settings
    3.5.3 Detection Results
    3.5.4 Interpretation and Evaluation Scope

3.6 Limitations, Validity, and Individual Contribution

3.7 Chapter Summary

Chapter 3 reports IoT and industrial evidence only. Under D-040 (10 September 2026) the former
Section 3.6, Framework Generality on Non-Industrial Corpora (UNSW-NB15 and CICAndMal2017), and
the former Section 3.7, Clean-Data Results, including its classical SWaT column, are removed.
RQ1.2 rests on the S7-300 evaluation in IUNO and on the SWaT GAN study. CICAndMal2017 remains
the evaluation corpus of Chapter 4.

Under D-050 (12 September 2026) the chapter is titled Anomaly Detection in IoT and Industrial
Control Systems. RQ1, gap G1 and the rqOneText macro keep the D-034 wording.

Under D-054 (12 September 2026) Section 3.5 reports the author's empirical GAN evaluation on
SWaT, and Section 3.5.4 is Interpretation and Evaluation Scope. The earlier result recorded in
D-039 no longer appears in the thesis.

Under D-055 (12 September 2026) the GAN study uses all 449,919 attack-period timestamps. The
first 56,240 support training and validation, while the later 393,679 form the test set.

### 4. Multimodal Android Malware Analysis with Hybroid

4.1 Research Problem and Contribution

4.2 Related Work

4.3 Observation and Threat Model

4.4 Dataset and Experimental Protocol

4.5 Opcode and Basic-Block Representation

4.6 Program-Graph Representation

4.7 Network-Flow Representation

4.8 Multimodal Fusion and Classification

4.9 Binary Detection Results

4.10 Malware-Category Classification

4.11 Modality Comparison

4.12 Limitations and Threats to Validity

4.13 Chapter Summary

Revised on 20 September 2026 under T-021 after approval of the T-019 review. The thirteen-section
structure is retained, with the Section 4.5 title aligned to the outline above. The chapter now
defines the skip-gram objective, CFG readout and flow preprocessing, and formalises the fusion
contrast. The scientific explanations and citation placement are corrected; repeated source
commentary is consolidated. Empirical table values and figure assets are unchanged, and the
undocumented weighting/composition steps remain qualified. Chapter 2 receives only the related
operand and G2 consistency corrections. Main prose decreases from 6,226 to 3,838 words, with
nine displayed equations instead of three. The rebuilt chapter occupies pp. 45-60, Chapter 5
starts on p. 61, and the complete thesis has 151 pages. The 23-page planning allowance is unchanged.

### 5. Higher-Order Android Malware Analysis with HGANN-Mal

5.1 Research Problem and Relation to Hybroid

5.2 Related Work

5.3 Observation and Threat Model

5.4 APK Processing and Function-Call Graph Extraction

5.5 Security-Sensitive API Identification and Program Slicing

5.6 Node Features

5.7 Hyperedge Construction

5.8 Hypergraph Attention Model

5.9 Datasets, Tasks, and Split Policy

5.10 Binary Detection Results

5.11 Malware-Family Classification on Drebin

5.12 Malware-Category Classification on CICMalDroid

5.13 Ablation, Efficiency, and Interpretability Analysis

5.14 Limitations and Threats to Validity

5.15 Chapter Summary

### 6. Evaluating Adversarial Robustness: Benchmark Design and Metric Analysis

6.1 Research Problem and Contribution

6.2 Threat Analysis and Evaluation Scope

6.3 Evaluation Requirements and Threat Models

6.4 Tasks and Evaluation Protocol

6.5 Data and Evaluation Measures

  On 19 September 2026, the author approved merging the residual Biometric Data and Data
  Protection subsection into the corpus discussion. Attribute imbalance and the limits of
  demographic inference remain in Section 6.5.1; no separate subsection is retained.

6.6 Benchmark Architecture and Reproducibility

6.7 Defence Mechanisms and Integration

6.8 Results and Metric Analysis

6.9 Threats to Validity

6.10 Individual Contribution and Project Attribution

6.11 Chapter Summary

  Revised on 19 September 2026 under T-003 to clarify the framework's design contribution
  around reference attack implementations and distinguish the contest evidence from the
  histopathology application. The PDF-malware comparison is shortened, with its original
  figure and partner attribution retained. The summary answers RQ4 through these two
  evaluation mechanisms; the available aggregates do not establish a general relation
  between clean performance and robustness. Chapter 8 and both abstracts use that wording.
  The rebuild has 157 pages (159 before this revision); Chapter 6 occupies pp. 95--112
  (18 pages, previously 20). Its main text is 227 words shorter by TeXcount. The six
  figures, four tables and sixteen numbered equations are retained.

  Revised under T-003 and D-041, with D-042/D-043 diagram redraws. The chapter
  contains six figures, four tables and sixteen numbered equations. It separates
  reported observations from mathematical deductions and unresolved mechanisms.
  The short PDF-malware comparison is attributed to the partner study. The final
  build occupies printed pages 87-106 (20 pages), above the proposed 15-16-page
  target; the whole dissertation remains 147 pages. Further expansion must account
  for the existing total-page limit and the D-044 Chapter 7/8 allocation.

### 7. Cross-Contribution Discussion

7.1 Contributions of Contextual Representations

7.2 Observation Requirements and Analysis Cost

7.3 Evaluation Principles Across the Contributions

7.4 Implications for Android Malware Analysis

Revised on 20 September 2026 under D-003 and T-004 after the author approved the T-017
review and requested a contribution-led tone. The four sections connect the scientific
contributions; brief qualifications remain beside the claims they bound, and detailed
limitations stay in Chapters 3 to 6. The earlier evaluation-condition table and repeated
defect inventory are removed. The chapter keeps its four-page ceiling and its conceptual
comparison of the Android systems. Original section labels remain as aliases, so Chapter 5's
acquisition reference resolves to the new Section 7.2. No common experiment or historical
progression from IoT to Android is implied.

The revision compiles to three content pages (113--115), followed by the recto-opening blank
on page 116; Chapter 8 starts on page 117. Main text decreases from 1,414 to 956 words by
TeXcount, and the full PDF decreases from 157 to 155 pages. The planning allowance remains
four pages.

### 8. Conclusion and Future Work

8.1 Answers to the Research Questions

8.2 Summary of Contributions

8.3 Future Work

Revised on 12 September 2026 under D-052: the Limitations section is removed at the author's
instruction, so Future Work becomes Section 8.3. The limits of each study remain in the
Limitations sections of Chapters 3 to 6.

Revised on 20 September 2026 under T-007 after the author approved the T-018 review.
The three-section structure and two-page limit are retained. The conclusion now gives the
Android contributions greater prominence, scopes the RQ3 and RQ4 answers to the evidence,
identifies the partner histopathology benchmark, and connects controlled ablation to temporal
and adversarial evaluation. Chapter 8 occupies pp. 117-118, with references from p. 119;
the thesis remains 155 pages. Main text decreases from 712 to 591 words before question-macro
expansion. The SWaT description refers to later test data; configuration-selection history in
Chapter 3 remains a separate unresolved question.

## Structure status

The author accepted the RQ1 hierarchy on 12 August 2026. The Chapter 2 section list was
replaced on 13 August 2026 by the seven-section Background outline recorded above; the
15-page budget was kept. The main chapter architecture is stable. RQ2-RQ4 and the chapter titles remain working formulations until the author and
supervisor approve their exact wording. Detailed subchapter design can continue later.
Authorship and experimental questions remain assigned to their contribution chapters in
`notes/known-issues-to-fix.md`.
