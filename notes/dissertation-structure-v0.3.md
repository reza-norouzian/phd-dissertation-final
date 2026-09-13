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

**Context-Aware Learning for Security Analysis: Android Malware Detection and Adversarial
Robustness Evaluation**

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

Binary detection remains a separate evaluation task. The source and count of benign
applications in the Drebin binary experiment remain unresolved.

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
| 6. Threat-Guided Evaluation of Adversarial Defences | 15 |
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

### 2. Background

Revised on 13 August 2026. The chapter is now titled Background, carries seven sections, and
keeps its 15-page budget. Android material opens the chapter because Android malware analysis
is the scientific centre; the representation and learning sections follow it, so that a reader
meets hypergraphs only after function-call graphs have been defined.

2.1 Android Applications and Their Analysis

- Dalvik bytecode, manifest, permissions
- Static, dynamic, and hybrid analysis
- Obfuscation, packing, repackaging

2.2 Graph Representations of Programs

- Control-flow and function-call graphs
- Hypergraphs and higher-order relations

2.3 Learning over Graphs

- Message passing
- Attention
- Hypergraph convolution

2.4 Detection in Networked and Cyber-Physical Systems

2.5 Adversarial Machine Learning

2.6 Evaluation Methodology and Experimental Bias

2.7 Summary and Research Gaps

Half a page of chapter summary, then four numbered gaps, G1 to G4. Each gap states what the
literature leaves unsettled and names the research question that takes it up. A gap is written
as an open question in the field, not as a description of the method used to close it.

#### Page budget for Chapter 2

| Section | Target pages |
| --- | ---: |
| 2.1 Android Applications and Their Analysis | 3.5 |
| 2.2 Graph Representations of Programs | 2.5 |
| 2.3 Learning over Graphs | 2.5 |
| 2.4 Detection in Networked and Cyber-Physical Systems | 2.0 |
| 2.5 Adversarial Machine Learning | 1.5 |
| 2.6 Evaluation Methodology and Experimental Bias | 1.5 |
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
- The old Learning-Based Security Analysis section is dissolved. Its framing material (what a
  learning pipeline for security looks like, which of its assumptions the security setting
  breaks) moves to the chapter preamble and to Section 2.6.
- Network-flow representation, previously grouped with program graphs, now sits in Section 2.4
  next to the detection methods that consume it. Chapter 4 needs both flow features and program
  graphs, so Section 4.7 must state the flow feature set itself rather than rely on Chapter 2.
- Section ordering no longer follows chapter order: Chapter 3 draws on Section 2.4, which
  appears after the Android sections. This is deliberate and should be signalled in the chapter
  preamble and in Section 3.1.

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

### 6. Threat-Guided Evaluation of Adversarial Defences

6.1 Research Problem and Contribution

6.2 AI-System Threat Analysis

6.3 Evaluation Requirements and Threat Models

6.4 Tasks and Evaluation Protocol

6.5 Data and Evaluation Measures

  6.5.1 Biometric Data and Data Protection

  Added 15 August 2026 on the author's decision under T-035 Q9. The benchmark performs face
  re-identification and facial-attribute prediction over CelebA and LFW, and no SPARTA
  deliverable treats biometric data protection, the GDPR position, or dataset bias beyond one
  sentence. The subsection sits here because 6.5 is where the reader meets the data. It cites
  D7.1's own data-protection chapter, to which the candidate contributed.

6.6 Benchmark Architecture and Reproducibility

6.7 Defence Mechanisms and Integration

6.8 Results and Metric Analysis

6.9 Threats to Validity

6.10 Individual Contribution and Project Attribution

6.11 Chapter Summary

  Revised under T-003 and D-041, with D-042/D-043 diagram redraws. The chapter
  contains six figures, four tables and sixteen numbered equations. It separates
  reported observations from mathematical deductions and unresolved mechanisms.
  The short PDF-malware comparison is attributed to the partner study. The final
  build occupies printed pages 87-106 (20 pages), above the proposed 15-16-page
  target; the whole dissertation remains 147 pages. Further expansion must account
  for the existing total-page limit and the D-044 Chapter 7/8 allocation.

### 7. Cross-Contribution Discussion

7.1 Communication Context and Program Context

7.2 Multimodal and Higher-Order Representations

7.3 Observation Requirements and Data-Acquisition Cost

7.4 Predictive Evaluation and Adversarial Evaluation

7.5 Dataset Limitations and Extraction Failures

7.6 Scope of Generalisation

7.7 Implications for Android Malware Analysis

### 8. Conclusion and Future Work

8.1 Answers to the Research Questions

8.2 Summary of Contributions

8.3 Future Work

Revised on 12 September 2026 under D-052: the Limitations section is removed at the author's
instruction, so Future Work becomes Section 8.3. The limits of each study remain in the
Limitations sections of Chapters 3 to 6.

## Structure status

The author accepted the RQ1 hierarchy on 12 August 2026. The Chapter 2 section list was
replaced on 13 August 2026 by the seven-section Background outline recorded above; the
15-page budget was kept. The main chapter architecture is stable. RQ2-RQ4 and the chapter titles remain working formulations until the author and
supervisor approve their exact wording. Detailed subchapter design can continue later.
Authorship and experimental questions remain assigned to their contribution chapters in
`notes/known-issues-to-fix.md`.
