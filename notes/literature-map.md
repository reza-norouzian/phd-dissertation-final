# Literature map

Generated from `bib/references.bib` (1,368 pooled entries). The Chapter 2 source plan follows
the current seven-section outline. The thematic candidate pools preserve the results of the
earlier literature harvest and may serve more than one section.

Column `n` is the number of independent harvests that found the entry (1-10). Column `v` is
the metadata-verification tier: `doi`, `publisher`, `dblp`, `arxiv` and similar are
independent; `src` means it was copied from a colleague's bibliography and still needs
checking; `no` means existence could not be confirmed at all. A verified metadata record does
not replace reading the source. Before drafting a section, record its core sources and the
claims they support in the writing ticket, inspect the full text where available, and add each
cited key to the reference vault.

## Chapter 2 source plan

| Section | Material to support | Candidate pools below |
| --- | --- | --- |
| 2.1 Android Applications and Their Analysis | APK and Dalvik artefacts, manifests and permissions, analysis modes, obfuscation, packing, and repackaging | Android Applications and Malware Analysis; Static, Dynamic, and Hybrid Observation |
| 2.2 Graph Representations of Programs | control-flow graphs, function-call graphs, hypergraphs, and the information lost by pairwise projection | Network Flows, Program Graphs, and Hypergraphs; Android Applications and Malware Analysis |
| 2.3 Learning over Graphs | message passing, graph attention, hypergraph convolution, and their limits | Network Flows, Program Graphs, and Hypergraphs; Learning-Based Security Analysis |
| 2.4 Detection in Networked and Cyber-Physical Systems | flow representation, anomaly-detection families, industrial and IoT settings, datasets, and measurement limits | Network Anomaly and Intrusion Detection; Ch.3 Anomaly Detection in IoT and Industrial Control Systems; Network Flows, Program Graphs, and Hypergraphs |
| 2.5 Adversarial Machine Learning | attack and defence classes, threat models, adaptive attacks, and failure modes | Adversarial Machine Learning; Ch.6 Threat-Guided Evaluation |
| 2.6 Performance Measures and Evaluation Methodology | confusion counts; binary and class-averaged metrics; ROC AUC; prevalence sensitivity; adversarial and operational measures; temporal/spatial bias, leakage and evaluation protocols | Verified performance-measures sources below; Evaluation Methodology and Threats to Validity; Ch.3 Anomaly Detection in IoT and Industrial Control Systems; Ch.6 Threat-Guided Evaluation |
| 2.7 Summary and Research Gaps | a short synthesis followed by G1-G4, using sources already cited in Sections 2.1-2.6 | no new source pool |

### Verified performance-measures sources (T-023, 20 September 2026)

These entries were added or inspected for the D-004 expansion. Their full texts and reference
vault records were checked before drafting; the detailed claim-to-source record is in T-023.

| Key | Role in Section 2.6 | Scope |
| --- | --- | --- |
| `fawcett2006roc` | Binary rates, ROC construction, ties and AUC ranking interpretation | DOI-registry metadata and publisher full text verified |
| `grandini2020metrics` | Ordinary balanced accuracy and micro-averaging identities | arXiv white paper; use Sections 3 and 4.3, not its weighted-balanced-accuracy or printed macro-F1 formula |
| `opitz2019macrof1` | Averaged class F1 versus F1 of macro precision/recall, including their inequality | arXiv version 3; first submitted 2019 and revised 2021; source zero-fill is not assigned to historical experiments |
| `axelsson2000base` | Precision under changes in prevalence with fixed conditional rates | Existing verified primary source; Equation (7) inspected |
| `sorbo2024navigating` | Timestamp versus event-based counting | Existing verified full text; the observation unit must be specified |
| `carlini2019evaluating`, `sparta2022d76` | Threat-conditioned performance, task-specific accuracy and accuracy loss | Existing verified full texts; distinguish analytical ASR definitions from reported contest outcomes |

The author-provided colleague screenshot is a structural reference, not a bibliographic source.
Definitions in the background do not establish missing aggregation conventions or generate
new scores for any contribution chapter.

## Coverage at a glance

| Candidate pool | Candidates | Landmarks (n>=2) | Unverified | Newest |
| --- | ---: | ---: | ---: | ---: |
| 1.1 Research Context | 205 | 70 | 9 | 2026 |
| Learning-Based Security Analysis | 168 | 68 | 10 | 2026 |
| Network Anomaly and Intrusion Detection | 505 | 60 | 102 | 2026 |
| Android Applications and Malware Analysis | 275 | 51 | 42 | 2026 |
| Static, Dynamic, and Hybrid Observation | 171 | 34 | 37 | 2026 |
| Network Flows, Program Graphs, and Hypergraphs | 277 | 58 | 8 | 2026 |
| Adversarial Machine Learning | 314 | 86 | 95 | 2026 |
| Evaluation Methodology and Threats to Validity | 317 | 54 | 56 | 2026 |
| 3.x Ch.3 Anomaly Detection in IoT and Industrial Control Systems | 253 | 32 | 30 | 2026 |
| 4.2 Ch.4 Hybroid related work | 95 | 20 | 1 | 2026 |
| 5.2 Ch.5 HGANN-Mal related work | 93 | 22 | 0 | 2026 |
| 6.x Ch.6 Threat-guided evaluation | 387 | 103 | 117 | 2026 |

## 1.1 Research Context

**Must support:** Learning-based security analysis is now standard practice, and its published results are systematically optimistic. Sets up the whole thesis.

| n | v | year | key | title |
| ---: | --- | ---: | --- | --- |
| 5 | openreview | 2017 | `kipf2017semi` | Semi-Supervised Classification with Graph Convolutional Networks |
| 5 | dblp | 2015 | `goodfellow2015explaining` | Explaining and Harnessing Adversarial Examples |
| 4 | doi | 2018 | `biggio2018wildpatterns` | Wild Patterns: Ten Years After the Rise of Adversarial Machine Learning |
| 4 | doi | 2016 | `grover2016node2vec` | node2vec: Scalable Feature Learning for Networks |
| 4 | doi | 2014 | `perozzi2014deepwalk` | {DeepWalk}: Online Learning of Social Representations |
| 4 | doi | 2009 | `chandola2009anomaly` | Anomaly Detection: A Survey |
| 4 | doi | 2000 | `breunig2000lof` | {LOF}: Identifying Density-Based Local Outliers |
| 4 | openreview | 2018 | `velickovic2018graph` | Graph Attention Networks |
| 4 | publisher | 2017 | `vaswani2017attention` | Attention Is All You Need |
| 4 | arxiv | 2014 | `szegedy2014intriguing` | Intriguing Properties of Neural Networks |
| 3 | doi | 2023 | `gao2023hgnn` | {HGNN}$^{+}$: General Hypergraph Neural Networks |
| 3 | doi | 2021 | `bai2021hypergraphattention` | Hypergraph Convolution and Hypergraph Attention |
| 3 | doi | 2019 | `feng2019hypergraph` | Hypergraph Neural Networks |
| 3 | doi | 2019 | `li2019madgan` | {MAD-GAN}: Multivariate Anomaly Detection for Time Series Data with Generative Adv |
| 3 | doi | 2019 | `onwuzurike2019mamadroid` | {MaMaDroid}: Detecting {Android} Malware by Building {Markov} Chains of Behavioral |
| 3 | doi | 2018 | `kravchik2018detecting` | Detecting Cyber Attacks in Industrial Control Systems Using Convolutional Neural N |
| 3 | doi | 2018 | `lashkari2018toward` | Toward Developing a Systematic Approach to Generate Benchmark {Android} Malware Da |
| 3 | doi | 2017 | `grosse2017adversarial` | Adversarial Examples for Malware Detection |
| 3 | doi | 2014 | `arp2014drebin` | {DREBIN}: Effective and Explainable Detection of {Android} Malware in Your Pocket |
| 3 | doi | 2013 | `biggio2013evasion` | Evasion Attacks against Machine Learning at Test Time |
| 3 | doi | 2011 | `huang2011adversarial` | Adversarial Machine Learning |
| 3 | doi | 2006 | `agarwal2006higherorder` | Higher Order Learning with Graphs |
| 3 | doi | 2006 | `zhou2006learning` | Learning with Hypergraphs: Clustering, Classification, and Embedding |
| 3 | doi | 2004 | `dalvi2004adversarial` | Adversarial Classification |
| 3 | doi | 1999 | `paxson1999bro` | Bro: A System for Detecting Network Intruders in Real-Time |
| 3 | doi | 2021 | `pang2021deep` | Deep Learning for Anomaly Detection: A Review |
| 3 | doi | 2021 | `ruff2021unifying` | A Unifying Review of Deep and Shallow Anomaly Detection |
| 3 | doi | 2018 | `kolosnjaji2018adversarial` | Adversarial Malware Binaries: Evading Deep Learning for Malware Detection in Execu |

Plus 177 further candidates in the pool at `keywords` matching this section.

## Candidate pool: Learning-Based Security Analysis

**Must support:** What a learning pipeline for security looks like, and which of its assumptions the security setting breaks.

| n | v | year | key | title |
| ---: | --- | ---: | --- | --- |
| 5 | openreview | 2017 | `kipf2017semi` | Semi-Supervised Classification with Graph Convolutional Networks |
| 5 | dblp | 2015 | `goodfellow2015explaining` | Explaining and Harnessing Adversarial Examples |
| 4 | doi | 2018 | `biggio2018wildpatterns` | Wild Patterns: Ten Years After the Rise of Adversarial Machine Learning |
| 4 | doi | 2016 | `grover2016node2vec` | node2vec: Scalable Feature Learning for Networks |
| 4 | doi | 2014 | `perozzi2014deepwalk` | {DeepWalk}: Online Learning of Social Representations |
| 4 | doi | 2009 | `chandola2009anomaly` | Anomaly Detection: A Survey |
| 4 | doi | 2000 | `breunig2000lof` | {LOF}: Identifying Density-Based Local Outliers |
| 4 | openreview | 2018 | `velickovic2018graph` | Graph Attention Networks |
| 4 | publisher | 2017 | `vaswani2017attention` | Attention Is All You Need |
| 3 | doi | 2023 | `gao2023hgnn` | {HGNN}$^{+}$: General Hypergraph Neural Networks |
| 3 | doi | 2021 | `bai2021hypergraphattention` | Hypergraph Convolution and Hypergraph Attention |
| 3 | doi | 2021 | `chakraborty2021survey` | A Survey on Adversarial Attacks and Defences |
| 3 | doi | 2019 | `devlin2019bert` | {BERT}: Pre-Training of Deep Bidirectional Transformers for Language Understanding |
| 3 | doi | 2019 | `feng2019hypergraph` | Hypergraph Neural Networks |
| 3 | doi | 2019 | `li2019madgan` | {MAD-GAN}: Multivariate Anomaly Detection for Time Series Data with Generative Adv |
| 3 | doi | 2018 | `jagielski2018manipulating` | Manipulating Machine Learning: Poisoning Attacks and Countermeasures for Regressio |
| 3 | doi | 2018 | `kravchik2018detecting` | Detecting Cyber Attacks in Industrial Control Systems Using Convolutional Neural N |
| 3 | doi | 2018 | `zugner2018adversarial` | Adversarial Attacks on Neural Networks for Graph Data |
| 3 | doi | 2016 | `ribeiro2016why` | ``Why Should I Trust You?'': Explaining the Predictions of Any Classifier |
| 3 | doi | 2015 | `xiao2015support` | Support Vector Machines Under Adversarial Label Contamination |
| 3 | doi | 2011 | `huang2011adversarial` | Adversarial Machine Learning |
| 3 | doi | 2006 | `agarwal2006higherorder` | Higher Order Learning with Graphs |
| 3 | doi | 2006 | `globerson2006nightmare` | Nightmare at Test Time: Robust Learning by Feature Deletion |
| 3 | doi | 2006 | `zhou2006learning` | Learning with Hypergraphs: Clustering, Classification, and Embedding |
| 3 | doi | 2005 | `lowd2005adversarial` | Adversarial Learning |
| 3 | doi | 2004 | `dalvi2004adversarial` | Adversarial Classification |
| 3 | doi | 2021 | `pang2021deep` | Deep Learning for Anomaly Detection: A Review |
| 3 | doi | 2021 | `ruff2021unifying` | A Unifying Review of Deep and Shallow Anomaly Detection |

Plus 140 further candidates in the pool at `keywords` matching this section.

## Candidate pool: Network Anomaly and Intrusion Detection

**Must support:** Anomaly detection in network and industrial settings: the method families, the datasets, and the measurement problems. Feeds Chapter 3.

| n | v | year | key | title |
| ---: | --- | ---: | --- | --- |
| 4 | doi | 2009 | `chandola2009anomaly` | Anomaly Detection: A Survey |
| 4 | doi | 2000 | `breunig2000lof` | {LOF}: Identifying Density-Based Local Outliers |
| 3 | doi | 2019 | `li2019madgan` | {MAD-GAN}: Multivariate Anomaly Detection for Time Series Data with Generative Adv |
| 3 | doi | 2018 | `kravchik2018detecting` | Detecting Cyber Attacks in Industrial Control Systems Using Convolutional Neural N |
| 3 | doi | 1999 | `paxson1999bro` | Bro: A System for Detecting Network Intruders in Real-Time |
| 3 | doi | 2021 | `pang2021deep` | Deep Learning for Anomaly Detection: A Review |
| 3 | doi | 2021 | `ruff2021unifying` | A Unifying Review of Deep and Shallow Anomaly Detection |
| 3 | doi | 2018 | `pahl2018graphbased` | Graph-based {IoT} Microservice Security |
| 3 | doi | 2015 | `akoglu2015graph` | Graph Based Anomaly Detection and Description: A Survey |
| 3 | doi | 2010 | `sommer2010outside` | Outside the Closed World: On Using Machine Learning for Network Intrusion Detectio |
| 3 | doi | 2009 | `tavallaee2009nslkdd` | A Detailed Analysis of the {KDD CUP 99} Data Set |
| 3 | doi | 2008 | `liu2008isolation` | Isolation Forest |
| 3 | doi | 2001 | `scholkopf2001estimating` | Estimating the Support of a High-Dimensional Distribution |
| 3 | dblp | 2022 | `arp2022dos` | Dos and Don'ts of Machine Learning in Computer Security |
| 3 | openalex | 2008 | `nelson2008exploiting` | Exploiting Machine Learning to Subvert Your Spam Filter |
| 2 | doi | 2021 | `alhajjar2021advmlnids` | Adversarial Machine Learning in Network Intrusion Detection Systems |
| 2 | doi | 2020 | `perales2020madics` | {MADICS}: A Methodology for Anomaly Detection in Industrial Control Systems |
| 2 | doi | 2020 | `zizzo2020advics` | Adversarial Attacks on Time-Series Intrusion Detection for Industrial Control Syst |
| 2 | doi | 2019 | `ngo2019fencegan` | Fence {GAN}: Towards Better Anomaly Detection |
| 2 | doi | 2018 | `pahl2018securing` | Securing {IoT} Microservices with Certificates |
| 2 | doi | 2018 | `schneider2018highperf` | High-Performance Unsupervised Anomaly Detection for Cyber-Physical System Networks |
| 2 | doi | 2018 | `zenati2018alad` | Adversarially Learned Anomaly Detection |
| 2 | doi | 2017 | `du2017deeplog` | {DeepLog}: Anomaly Detection and Diagnosis from System Logs through Deep Learning |
| 2 | doi | 2017 | `feng2017multi` | Multi-Level Anomaly Detection in Industrial Control Systems via Package Signatures |
| 2 | doi | 2017 | `goh2016swatdataset` | A Dataset to Support Research in the Design of Secure Water Treatment Systems |
| 2 | doi | 2017 | `goh2017anomaly` | Anomaly Detection in Cyber Physical Systems Using Recurrent Neural Networks |
| 2 | doi | 2017 | `inoue2017anomaly` | Anomaly Detection for a Water Treatment System Using Unsupervised Machine Learning |
| 2 | doi | 2017 | `wang2017malware` | Malware Traffic Classification Using Convolutional Neural Network for Representati |

Plus 477 further candidates in the pool at `keywords` matching this section.

## Candidate pool: Android Applications and Malware Analysis

**Must support:** The Android platform, the threat, and the detection literature Chapters 4 and 5 sit in.

| n | v | year | key | title |
| ---: | --- | ---: | --- | --- |
| 3 | doi | 2019 | `onwuzurike2019mamadroid` | {MaMaDroid}: Detecting {Android} Malware by Building {Markov} Chains of Behavioral |
| 3 | doi | 2018 | `lashkari2018toward` | Toward Developing a Systematic Approach to Generate Benchmark {Android} Malware Da |
| 3 | doi | 2017 | `grosse2017adversarial` | Adversarial Examples for Malware Detection |
| 3 | doi | 2014 | `arp2014drebin` | {DREBIN}: Effective and Explainable Detection of {Android} Malware in Your Pocket |
| 3 | doi | 2013 | `biggio2013evasion` | Evasion Attacks against Machine Learning at Test Time |
| 3 | doi | 2018 | `kolosnjaji2018adversarial` | Adversarial Malware Binaries: Evading Deep Learning for Malware Detection in Execu |
| 3 | publisher | 2019 | `pendlebury2019tesseract` | {TESSERACT}: Eliminating Experimental Bias in Malware Classification Across Space  |
| 3 | dblp | 2018 | `raff2018malware` | Malware Detection by Eating a Whole {EXE} |
| 3 | dblp | 2022 | `arp2022dos` | Dos and Don'ts of Machine Learning in Computer Security |
| 2 | doi | 2025 | `guo2025malhapgnn` | {MalHAPGNN}: An Enhanced Call Graph-Based Malware Detection Framework Using Hierar |
| 2 | doi | 2025 | `qian2025lamd` | {LAMD}: Context-Driven {Android} Malware Detection and Classification with {LLMs} |
| 2 | doi | 2024 | `bilot2024survey` | A Survey on Malware Detection with Graph Representation Learning |
| 2 | doi | 2024 | `lu2024sndgcn` | {SNDGCN}: Robust {Android} Malware Detection Based on Subgraph Network and Denoisi |
| 2 | doi | 2024 | `soi2024enhancing` | Enhancing {Android} Malware Detection Explainability Through Function Call Graph { |
| 2 | doi | 2024 | `zheng2024maskdroid` | {MaskDroid}: Robust {Android} Malware Detection with Masked Graph Representations |
| 2 | doi | 2023 | `yumlembam2023iot` | {IoT}-Based {Android} Malware Detection Using Graph Neural Network with Adversaria |
| 2 | doi | 2023 | `zhang2023android` | {Android} Malware Detection Based on Hypergraph Neural Networks |
| 2 | doi | 2020 | `mahdavifar2020dynamic` | Dynamic {Android} Malware Category Classification Using Semi-Supervised Deep Learn |
| 2 | doi | 2020 | `xu2020manis` | {MANIS}: Evading Malware Detection System on Graph Structure |
| 2 | doi | 2019 | `taheri2019extensible` | Extensible {Android} Malware Detection and Family Classification Using Network-Flo |
| 2 | doi | 2018 | `narayanan2018apk2vec` | {apk2vec}: Semi-Supervised Multi-View Representation Learning for Profiling {Andro |
| 2 | doi | 2017 | `mclaughlin2017deep` | Deep {Android} Malware Detection |
| 2 | doi | 2017 | `wang2017malware` | Malware Traffic Classification Using Convolutional Neural Network for Representati |
| 2 | doi | 2016 | `kang2016ngram` | N-gram Opcode Analysis for {Android} Malware Detection |
| 2 | doi | 2013 | `aafer2013droidapiminer` | {DroidAPIMiner}: Mining {API}-Level Features for Robust Malware Detection in {Andr |
| 2 | doi | 2013 | `gascon2013structural` | Structural Detection of {Android} Malware Using Embedded Call Graphs |
| 2 | doi | 2012 | `wu2012droidmat` | {DroidMat}: {Android} Malware Detection Through Manifest and {API} Calls Tracing |
| 2 | doi | 2024 | `ceschin2024machine` | Machine Learning (In) Security: A Stream of Problems |

Plus 247 further candidates in the pool at `keywords` matching this section.

## Candidate pool: Static, Dynamic, and Hybrid Observation

**Must support:** The observation trade-off: coverage against evasion resistance against cost. This is the axis Hybroid moves along.

| n | v | year | key | title |
| ---: | --- | ---: | --- | --- |
| 3 | doi | 2019 | `onwuzurike2019mamadroid` | {MaMaDroid}: Detecting {Android} Malware by Building {Markov} Chains of Behavioral |
| 3 | doi | 2018 | `lashkari2018toward` | Toward Developing a Systematic Approach to Generate Benchmark {Android} Malware Da |
| 3 | doi | 2017 | `xu2017neural` | Neural Network-Based Graph Embedding for Cross-Platform Binary Code Similarity Det |
| 3 | doi | 2014 | `arp2014drebin` | {DREBIN}: Effective and Explainable Detection of {Android} Malware in Your Pocket |
| 3 | dblp | 2018 | `raff2018malware` | Malware Detection by Eating a Whole {EXE} |
| 2 | doi | 2025 | `guo2025malhapgnn` | {MalHAPGNN}: An Enhanced Call Graph-Based Malware Detection Framework Using Hierar |
| 2 | doi | 2025 | `qian2025lamd` | {LAMD}: Context-Driven {Android} Malware Detection and Classification with {LLMs} |
| 2 | doi | 2024 | `lu2024sndgcn` | {SNDGCN}: Robust {Android} Malware Detection Based on Subgraph Network and Denoisi |
| 2 | doi | 2024 | `soi2024enhancing` | Enhancing {Android} Malware Detection Explainability Through Function Call Graph { |
| 2 | doi | 2024 | `zheng2024maskdroid` | {MaskDroid}: Robust {Android} Malware Detection with Masked Graph Representations |
| 2 | doi | 2020 | `mahdavifar2020dynamic` | Dynamic {Android} Malware Category Classification Using Semi-Supervised Deep Learn |
| 2 | doi | 2019 | `taheri2019extensible` | Extensible {Android} Malware Detection and Family Classification Using Network-Flo |
| 2 | doi | 2017 | `mclaughlin2017deep` | Deep {Android} Malware Detection |
| 2 | doi | 2016 | `kang2016ngram` | N-gram Opcode Analysis for {Android} Malware Detection |
| 2 | doi | 2014 | `biggio2014poisoning` | Poisoning Behavioral Malware Clustering |
| 2 | doi | 2013 | `aafer2013droidapiminer` | {DroidAPIMiner}: Mining {API}-Level Features for Robust Malware Detection in {Andr |
| 2 | doi | 2013 | `gascon2013structural` | Structural Detection of {Android} Malware Using Embedded Call Graphs |
| 2 | doi | 2012 | `wu2012droidmat` | {DroidMat}: {Android} Malware Detection Through Manifest and {API} Calls Tracing |
| 2 | doi | 2024 | `wang2024fagnet` | {FAGnet}: Family-Aware-Based Android Malware Analysis Using Graph Neural Network |
| 2 | doi | 2019 | `ding2019asm2vec` | {Asm2Vec}: Boosting Static Representation Robustness for Binary Clone Search Again |
| 2 | doi | 2019 | `massarelli2019safe` | {SAFE}: Self-Attentive Function Embeddings for Binary Similarity |
| 2 | doi | 2017 | `hou2017hindroid` | {HinDroid}: An Intelligent Android Malware Detection System Based on Structured He |
| 2 | doi | 2017 | `kolosnjaji2017empowering` | Empowering Convolutional Networks for Malware Classification and Analysis |
| 2 | doi | 2016 | `kolosnjaji2016adaptive` | Adaptive Semantics-Aware Malware Classification |
| 2 | doi | 2016 | `kolosnjaji2016deep` | Deep Learning for Classification of Malware System Call Sequences |
| 2 | doi | 2015 | `lindorfer2015marvin` | {MARVIN}: Efficient and Comprehensive Mobile App Classification through Static and |
| 2 | doi | 2015 | `shoshitaishvili2015firmalice` | {Firmalice} -- Automatic Detection of Authentication Bypass Vulnerabilities in Bin |
| 2 | doi | 2011 | `anderson2011graph` | Graph-Based Malware Detection Using Dynamic Analysis |

Plus 143 further candidates in the pool at `keywords` matching this section.

## Candidate pool: Network Flows, Program Graphs, and Hypergraphs

**Must support:** How structure gets represented and learned, from flows through pairwise graphs to hypergraphs. The formal spine of RQ1-RQ3.

| n | v | year | key | title |
| ---: | --- | ---: | --- | --- |
| 5 | openreview | 2017 | `kipf2017semi` | Semi-Supervised Classification with Graph Convolutional Networks |
| 4 | doi | 2016 | `grover2016node2vec` | node2vec: Scalable Feature Learning for Networks |
| 4 | doi | 2014 | `perozzi2014deepwalk` | {DeepWalk}: Online Learning of Social Representations |
| 4 | openreview | 2018 | `velickovic2018graph` | Graph Attention Networks |
| 3 | doi | 2023 | `gao2023hgnn` | {HGNN}$^{+}$: General Hypergraph Neural Networks |
| 3 | doi | 2021 | `bai2021hypergraphattention` | Hypergraph Convolution and Hypergraph Attention |
| 3 | doi | 2019 | `feng2019hypergraph` | Hypergraph Neural Networks |
| 3 | doi | 2019 | `onwuzurike2019mamadroid` | {MaMaDroid}: Detecting {Android} Malware by Building {Markov} Chains of Behavioral |
| 3 | doi | 2018 | `zugner2018adversarial` | Adversarial Attacks on Neural Networks for Graph Data |
| 3 | doi | 2017 | `xu2017neural` | Neural Network-Based Graph Embedding for Cross-Platform Binary Code Similarity Det |
| 3 | doi | 2006 | `agarwal2006higherorder` | Higher Order Learning with Graphs |
| 3 | doi | 2006 | `zhou2006learning` | Learning with Hypergraphs: Clustering, Classification, and Embedding |
| 3 | doi | 2018 | `pahl2018graphbased` | Graph-based {IoT} Microservice Security |
| 3 | doi | 2015 | `akoglu2015graph` | Graph Based Anomaly Detection and Description: A Survey |
| 2 | doi | 2025 | `guo2025malhapgnn` | {MalHAPGNN}: An Enhanced Call Graph-Based Malware Detection Framework Using Hierar |
| 2 | doi | 2024 | `bilot2024survey` | A Survey on Malware Detection with Graph Representation Learning |
| 2 | doi | 2024 | `lu2024sndgcn` | {SNDGCN}: Robust {Android} Malware Detection Based on Subgraph Network and Denoisi |
| 2 | doi | 2024 | `soi2024enhancing` | Enhancing {Android} Malware Detection Explainability Through Function Call Graph { |
| 2 | doi | 2024 | `zheng2024maskdroid` | {MaskDroid}: Robust {Android} Malware Detection with Masked Graph Representations |
| 2 | doi | 2023 | `yumlembam2023iot` | {IoT}-Based {Android} Malware Detection Using Graph Neural Network with Adversaria |
| 2 | doi | 2023 | `zhang2023android` | {Android} Malware Detection Based on Hypergraph Neural Networks |
| 2 | doi | 2022 | `gao2022hypergraph` | Hypergraph Learning: Methods and Practices |
| 2 | doi | 2020 | `xu2020manis` | {MANIS}: Evading Malware Detection System on Graph Structure |
| 2 | doi | 2019 | `alon2019code2vec` | code2vec: Learning Distributed Representations of Code |
| 2 | doi | 2018 | `narayanan2018apk2vec` | {apk2vec}: Semi-Supervised Multi-View Representation Learning for Profiling {Andro |
| 2 | doi | 2013 | `gascon2013structural` | Structural Detection of {Android} Malware Using Embedded Call Graphs |
| 2 | doi | 2024 | `wang2024fagnet` | {FAGnet}: Family-Aware-Based Android Malware Analysis Using Graph Neural Network |
| 2 | doi | 2023 | `antelmi2023hypergraphsurvey` | A Survey on Hypergraph Representation Learning |

Plus 249 further candidates in the pool at `keywords` matching this section.

## Candidate pool: Adversarial Machine Learning

**Must support:** Attacks, defences, and why most published defences did not hold. Feeds Chapter 6.

| n | v | year | key | title |
| ---: | --- | ---: | --- | --- |
| 5 | dblp | 2015 | `goodfellow2015explaining` | Explaining and Harnessing Adversarial Examples |
| 4 | doi | 2018 | `biggio2018wildpatterns` | Wild Patterns: Ten Years After the Rise of Adversarial Machine Learning |
| 4 | doi | 2017 | `carlini2017robustness` | Towards Evaluating the Robustness of Neural Networks |
| 4 | arxiv | 2018 | `madry2018pgd` | Towards Deep Learning Models Resistant to Adversarial Attacks |
| 4 | arxiv | 2017 | `kurakin2017bim` | Adversarial Examples in the Physical World |
| 4 | arxiv | 2014 | `szegedy2014intriguing` | Intriguing Properties of Neural Networks |
| 3 | doi | 2021 | `chakraborty2021survey` | A Survey on Adversarial Attacks and Defences |
| 3 | doi | 2018 | `jagielski2018manipulating` | Manipulating Machine Learning: Poisoning Attacks and Countermeasures for Regressio |
| 3 | doi | 2018 | `xu2018featuresqueezing` | Feature Squeezing: Detecting Adversarial Examples in Deep Neural Networks |
| 3 | doi | 2018 | `zugner2018adversarial` | Adversarial Attacks on Neural Networks for Graph Data |
| 3 | doi | 2017 | `grosse2017adversarial` | Adversarial Examples for Malware Detection |
| 3 | doi | 2017 | `papernot2017practical` | Practical Black-Box Attacks against Machine Learning |
| 3 | doi | 2016 | `papernot2016distillation` | Distillation as a Defense to Adversarial Perturbations against Deep Neural Network |
| 3 | doi | 2016 | `papernot2016jsma` | The Limitations of Deep Learning in Adversarial Settings |
| 3 | doi | 2015 | `xiao2015support` | Support Vector Machines Under Adversarial Label Contamination |
| 3 | doi | 2014 | `biggio2014security` | Security Evaluation of Pattern Classifiers under Attack |
| 3 | doi | 2013 | `biggio2013evasion` | Evasion Attacks against Machine Learning at Test Time |
| 3 | doi | 2012 | `xiao2012adversarial` | Adversarial Label Flips Attack on Support Vector Machines |
| 3 | doi | 2011 | `huang2011adversarial` | Adversarial Machine Learning |
| 3 | doi | 2006 | `globerson2006nightmare` | Nightmare at Test Time: Robust Learning by Feature Deletion |
| 3 | doi | 2005 | `lowd2005adversarial` | Adversarial Learning |
| 3 | doi | 2004 | `dalvi2004adversarial` | Adversarial Classification |
| 3 | doi | 2018 | `kolosnjaji2018adversarial` | Adversarial Malware Binaries: Evading Deep Learning for Malware Detection in Execu |
| 3 | doi | 2016 | `moosavi2016deepfool` | {DeepFool}: A Simple and Accurate Method to Fool Deep Neural Networks |
| 3 | doi | 2010 | `barreno2010security` | The Security of Machine Learning |
| 3 | doi | 2006 | `barreno2006can` | Can Machine Learning Be Secure? |
| 3 | pmlr | 2018 | `athalye2018obfuscated` | Obfuscated Gradients Give a False Sense of Security: Circumventing Defenses to Adv |
| 3 | nips | 2018 | `shafahi2018poison` | Poison Frogs! Targeted Clean-Label Poisoning Attacks on Neural Networks |

Plus 286 further candidates in the pool at `keywords` matching this section.

## Candidate pool: Evaluation Methodology and Threats to Validity

**Must support:** Spatial and temporal bias, point adjustment, adaptive evaluation. The methodological argument the thesis makes twice.

| n | v | year | key | title |
| ---: | --- | ---: | --- | --- |
| 4 | doi | 2018 | `biggio2018wildpatterns` | Wild Patterns: Ten Years After the Rise of Adversarial Machine Learning |
| 4 | doi | 2017 | `carlini2017robustness` | Towards Evaluating the Robustness of Neural Networks |
| 3 | doi | 2019 | `onwuzurike2019mamadroid` | {MaMaDroid}: Detecting {Android} Malware by Building {Markov} Chains of Behavioral |
| 3 | doi | 2018 | `lashkari2018toward` | Toward Developing a Systematic Approach to Generate Benchmark {Android} Malware Da |
| 3 | doi | 2016 | `ribeiro2016why` | ``Why Should I Trust You?'': Explaining the Predictions of Any Classifier |
| 3 | doi | 2015 | `xiao2015support` | Support Vector Machines Under Adversarial Label Contamination |
| 3 | doi | 2014 | `arp2014drebin` | {DREBIN}: Effective and Explainable Detection of {Android} Malware in Your Pocket |
| 3 | doi | 2014 | `biggio2014security` | Security Evaluation of Pattern Classifiers under Attack |
| 3 | doi | 2011 | `huang2011adversarial` | Adversarial Machine Learning |
| 3 | doi | 2010 | `barreno2010security` | The Security of Machine Learning |
| 3 | doi | 2010 | `sommer2010outside` | Outside the Closed World: On Using Machine Learning for Network Intrusion Detectio |
| 3 | doi | 2009 | `tavallaee2009nslkdd` | A Detailed Analysis of the {KDD CUP 99} Data Set |
| 3 | doi | 2006 | `barreno2006can` | Can Machine Learning Be Secure? |
| 3 | publisher | 2019 | `pendlebury2019tesseract` | {TESSERACT}: Eliminating Experimental Bias in Malware Classification Across Space  |
| 3 | pmlr | 2018 | `athalye2018obfuscated` | Obfuscated Gradients Give a False Sense of Security: Circumventing Defenses to Adv |
| 3 | pmlr | 2015 | `xiao2015feature` | Is Feature Selection Secure against Training Data Poisoning? |
| 3 | dblp | 2022 | `arp2022dos` | Dos and Don'ts of Machine Learning in Computer Security |
| 3 | dblp | 2019 | `carlini2019evaluating` | On Evaluating Adversarial Robustness |
| 2 | doi | 2021 | `alhajjar2021advmlnids` | Adversarial Machine Learning in Network Intrusion Detection Systems |
| 2 | doi | 2021 | `bai2021recent` | Recent Advances in Adversarial Training for Adversarial Robustness |
| 2 | doi | 2020 | `mahdavifar2020dynamic` | Dynamic {Android} Malware Category Classification Using Semi-Supervised Deep Learn |
| 2 | doi | 2020 | `perales2020madics` | {MADICS}: A Methodology for Anomaly Detection in Industrial Control Systems |
| 2 | doi | 2019 | `taheri2019extensible` | Extensible {Android} Malware Detection and Family Classification Using Network-Flo |
| 2 | doi | 2018 | `kurakin2018competition` | Adversarial Attacks and Defences Competition |
| 2 | doi | 2018 | `papernot2018sok` | SoK: Security and Privacy in Machine Learning |
| 2 | doi | 2017 | `carlini2017adversarial` | Adversarial Examples Are Not Easily Detected: Bypassing Ten Detection Methods |
| 2 | doi | 2017 | `goh2016swatdataset` | A Dataset to Support Research in the Design of Secure Water Treatment Systems |
| 2 | doi | 2002 | `chawla2002smote` | {SMOTE}: Synthetic Minority Over-sampling Technique |

Plus 289 further candidates in the pool at `keywords` matching this section.

## 3.x Ch.3 Anomaly Detection in IoT and Industrial Control Systems

**Must support:** Chapter 3 related work. Must include the prior art that anticipates the service-graph approach and the measurement work that contradicts the reported scores.

| n | v | year | key | title |
| ---: | --- | ---: | --- | --- |
| 3 | doi | 2019 | `li2019madgan` | {MAD-GAN}: Multivariate Anomaly Detection for Time Series Data with Generative Adv |
| 3 | doi | 2018 | `kravchik2018detecting` | Detecting Cyber Attacks in Industrial Control Systems Using Convolutional Neural N |
| 3 | doi | 1999 | `paxson1999bro` | Bro: A System for Detecting Network Intruders in Real-Time |
| 3 | doi | 2018 | `pahl2018graphbased` | Graph-based {IoT} Microservice Security |
| 3 | doi | 2010 | `sommer2010outside` | Outside the Closed World: On Using Machine Learning for Network Intrusion Detectio |
| 3 | doi | 2009 | `tavallaee2009nslkdd` | A Detailed Analysis of the {KDD CUP 99} Data Set |
| 2 | doi | 2023 | `yumlembam2023iot` | {IoT}-Based {Android} Malware Detection Using Graph Neural Network with Adversaria |
| 2 | doi | 2021 | `alhajjar2021advmlnids` | Adversarial Machine Learning in Network Intrusion Detection Systems |
| 2 | doi | 2020 | `perales2020madics` | {MADICS}: A Methodology for Anomaly Detection in Industrial Control Systems |
| 2 | doi | 2020 | `zizzo2020advics` | Adversarial Attacks on Time-Series Intrusion Detection for Industrial Control Syst |
| 2 | doi | 2018 | `pahl2018securing` | Securing {IoT} Microservices with Certificates |
| 2 | doi | 2018 | `schneider2018highperf` | High-Performance Unsupervised Anomaly Detection for Cyber-Physical System Networks |
| 2 | doi | 2017 | `du2017deeplog` | {DeepLog}: Anomaly Detection and Diagnosis from System Logs through Deep Learning |
| 2 | doi | 2017 | `feng2017multi` | Multi-Level Anomaly Detection in Industrial Control Systems via Package Signatures |
| 2 | doi | 2017 | `goh2016swatdataset` | A Dataset to Support Research in the Design of Secure Water Treatment Systems |
| 2 | doi | 2017 | `goh2017anomaly` | Anomaly Detection in Cyber Physical Systems Using Recurrent Neural Networks |
| 2 | doi | 2017 | `inoue2017anomaly` | Anomaly Detection for a Water Treatment System Using Unsupervised Machine Learning |
| 2 | doi | 2013 | `barbosa2013flow` | Flow Whitelisting in {SCADA} Networks |
| 2 | doi | 2022 | `zhang2022deeptralog` | {DeepTraLog}: Trace-Log Combined Microservice Anomaly Detection through Graph-Base |
| 2 | doi | 2020 | `erba2020constrained` | Constrained Concealment Attacks against Reconstruction-Based Anomaly Detectors in  |
| 2 | doi | 2019 | `milajerdi2019holmes` | HOLMES: Real-Time APT Detection through Correlation of Suspicious Information Flow |
| 2 | doi | 2019 | `nguyen2019diot` | D{\"I}oT: A Federated Self-Learning Anomaly Detection System for IoT |
| 2 | doi | 2017 | `ahmed2017wadi` | {WADI}: A Water Distribution Testbed for Research in the Design of Secure Cyber Ph |
| 2 | doi | 2016 | `manzoor2016fast` | Fast Memory-Efficient Anomaly Detection in Streaming Heterogeneous Graphs |
| 2 | doi | 2015 | `moustafa2015unsw` | {UNSW-NB15}: A Comprehensive Data Set for Network Intrusion Detection Systems ({UN |
| 2 | doi | 2015 | `shoshitaishvili2015firmalice` | {Firmalice} -- Automatic Detection of Authentication Bypass Vulnerabilities in Bin |
| 2 | doi | 2012 | `ding2012intrusion` | Intrusion as (Anti)social Communication: Characterization and Detection |
| 2 | doi | 2009 | `garcia2009anomaly` | Anomaly-Based Network Intrusion Detection: Techniques, Systems and Challenges |

Plus 225 further candidates in the pool at `keywords` matching this section.

## 4.2 Ch.4 Hybroid related work

**Must support:** Multimodal and hybrid Android detection: what fusing code with traffic was already known to buy.

| n | v | year | key | title |
| ---: | --- | ---: | --- | --- |
| 3 | doi | 2019 | `onwuzurike2019mamadroid` | {MaMaDroid}: Detecting {Android} Malware by Building {Markov} Chains of Behavioral |
| 3 | doi | 2018 | `lashkari2018toward` | Toward Developing a Systematic Approach to Generate Benchmark {Android} Malware Da |
| 3 | doi | 2014 | `arp2014drebin` | {DREBIN}: Effective and Explainable Detection of {Android} Malware in Your Pocket |
| 2 | doi | 2025 | `qian2025lamd` | {LAMD}: Context-Driven {Android} Malware Detection and Classification with {LLMs} |
| 2 | doi | 2024 | `lu2024sndgcn` | {SNDGCN}: Robust {Android} Malware Detection Based on Subgraph Network and Denoisi |
| 2 | doi | 2024 | `soi2024enhancing` | Enhancing {Android} Malware Detection Explainability Through Function Call Graph { |
| 2 | doi | 2024 | `zheng2024maskdroid` | {MaskDroid}: Robust {Android} Malware Detection with Masked Graph Representations |
| 2 | doi | 2023 | `zhang2023android` | {Android} Malware Detection Based on Hypergraph Neural Networks |
| 2 | doi | 2020 | `mahdavifar2020dynamic` | Dynamic {Android} Malware Category Classification Using Semi-Supervised Deep Learn |
| 2 | doi | 2019 | `taheri2019extensible` | Extensible {Android} Malware Detection and Family Classification Using Network-Flo |
| 2 | doi | 2018 | `narayanan2018apk2vec` | {apk2vec}: Semi-Supervised Multi-View Representation Learning for Profiling {Andro |
| 2 | doi | 2017 | `mclaughlin2017deep` | Deep {Android} Malware Detection |
| 2 | doi | 2016 | `kang2016ngram` | N-gram Opcode Analysis for {Android} Malware Detection |
| 2 | doi | 2013 | `aafer2013droidapiminer` | {DroidAPIMiner}: Mining {API}-Level Features for Robust Malware Detection in {Andr |
| 2 | doi | 2013 | `gascon2013structural` | Structural Detection of {Android} Malware Using Embedded Call Graphs |
| 2 | doi | 2012 | `wu2012droidmat` | {DroidMat}: {Android} Malware Detection Through Manifest and {API} Calls Tracing |
| 2 | doi | 2024 | `wang2024fagnet` | {FAGnet}: Family-Aware-Based Android Malware Analysis Using Graph Neural Network |
| 2 | doi | 2017 | `hou2017hindroid` | {HinDroid}: An Intelligent Android Malware Detection System Based on Structured He |
| 2 | doi | 2015 | `lindorfer2015marvin` | {MARVIN}: Efficient and Comprehensive Mobile App Classification through Static and |
| 2 | dblp | 2014 | `arzt2014flowdroid` | {FlowDroid}: Precise Context, Flow, Field, Object-Sensitive and Lifecycle-Aware Ta |

Plus 75 further candidates in the pool at `keywords` matching this section.

## 5.2 Ch.5 HGANN-Mal related work

**Must support:** Graph and hypergraph learning on program structure, and attention. Must confront the GAT static-attention result and clique-expansion lossiness.

| n | v | year | key | title |
| ---: | --- | ---: | --- | --- |
| 3 | doi | 2023 | `gao2023hgnn` | {HGNN}$^{+}$: General Hypergraph Neural Networks |
| 3 | doi | 2021 | `bai2021hypergraphattention` | Hypergraph Convolution and Hypergraph Attention |
| 3 | doi | 2019 | `feng2019hypergraph` | Hypergraph Neural Networks |
| 3 | doi | 2019 | `onwuzurike2019mamadroid` | {MaMaDroid}: Detecting {Android} Malware by Building {Markov} Chains of Behavioral |
| 3 | doi | 2006 | `agarwal2006higherorder` | Higher Order Learning with Graphs |
| 3 | doi | 2006 | `zhou2006learning` | Learning with Hypergraphs: Clustering, Classification, and Embedding |
| 2 | doi | 2024 | `lu2024sndgcn` | {SNDGCN}: Robust {Android} Malware Detection Based on Subgraph Network and Denoisi |
| 2 | doi | 2024 | `soi2024enhancing` | Enhancing {Android} Malware Detection Explainability Through Function Call Graph { |
| 2 | doi | 2024 | `zheng2024maskdroid` | {MaskDroid}: Robust {Android} Malware Detection with Masked Graph Representations |
| 2 | doi | 2023 | `yumlembam2023iot` | {IoT}-Based {Android} Malware Detection Using Graph Neural Network with Adversaria |
| 2 | doi | 2023 | `zhang2023android` | {Android} Malware Detection Based on Hypergraph Neural Networks |
| 2 | doi | 2022 | `gao2022hypergraph` | Hypergraph Learning: Methods and Practices |
| 2 | doi | 2020 | `xu2020manis` | {MANIS}: Evading Malware Detection System on Graph Structure |
| 2 | doi | 2018 | `narayanan2018apk2vec` | {apk2vec}: Semi-Supervised Multi-View Representation Learning for Profiling {Andro |
| 2 | doi | 2013 | `gascon2013structural` | Structural Detection of {Android} Malware Using Embedded Call Graphs |
| 2 | doi | 2024 | `wang2024fagnet` | {FAGnet}: Family-Aware-Based Android Malware Analysis Using Graph Neural Network |
| 2 | doi | 2023 | `antelmi2023hypergraphsurvey` | A Survey on Hypergraph Representation Learning |
| 2 | doi | 2017 | `hou2017hindroid` | {HinDroid}: An Intelligent Android Malware Detection System Based on Structured He |
| 2 | publisher | 2022 | `chien2022allset` | You Are {AllSet}: A Multiset Function Framework for Hypergraph Neural Networks |
| 2 | publisher | 2019 | `yadati2019hypergcn` | {HyperGCN}: A New Method for Training Graph Convolutional Networks on Hypergraphs |
| 2 | dblp | 2014 | `arzt2014flowdroid` | {FlowDroid}: Precise Context, Flow, Field, Object-Sensitive and Lifecycle-Aware Ta |
| 2 | arxiv | 2025 | `shokouhinejad2025recent` | Recent Advances in Malware Detection: Graph Learning and Explainability |

Plus 71 further candidates in the pool at `keywords` matching this section.

## 6.x Ch.6 Threat-guided evaluation

**Must support:** Threat modelling for AI systems, contest and benchmark design, robustness measurement.

| n | v | year | key | title |
| ---: | --- | ---: | --- | --- |
| 5 | dblp | 2015 | `goodfellow2015explaining` | Explaining and Harnessing Adversarial Examples |
| 4 | doi | 2018 | `biggio2018wildpatterns` | Wild Patterns: Ten Years After the Rise of Adversarial Machine Learning |
| 4 | doi | 2017 | `carlini2017robustness` | Towards Evaluating the Robustness of Neural Networks |
| 4 | doi | 2000 | `breunig2000lof` | {LOF}: Identifying Density-Based Local Outliers |
| 4 | publisher | 2017 | `vaswani2017attention` | Attention Is All You Need |
| 4 | arxiv | 2018 | `madry2018pgd` | Towards Deep Learning Models Resistant to Adversarial Attacks |
| 4 | arxiv | 2017 | `kurakin2017bim` | Adversarial Examples in the Physical World |
| 4 | arxiv | 2014 | `szegedy2014intriguing` | Intriguing Properties of Neural Networks |
| 3 | doi | 2021 | `chakraborty2021survey` | A Survey on Adversarial Attacks and Defences |
| 3 | doi | 2018 | `jagielski2018manipulating` | Manipulating Machine Learning: Poisoning Attacks and Countermeasures for Regressio |
| 3 | doi | 2018 | `xu2018featuresqueezing` | Feature Squeezing: Detecting Adversarial Examples in Deep Neural Networks |
| 3 | doi | 2018 | `zugner2018adversarial` | Adversarial Attacks on Neural Networks for Graph Data |
| 3 | doi | 2017 | `grosse2017adversarial` | Adversarial Examples for Malware Detection |
| 3 | doi | 2017 | `papernot2017practical` | Practical Black-Box Attacks against Machine Learning |
| 3 | doi | 2016 | `papernot2016distillation` | Distillation as a Defense to Adversarial Perturbations against Deep Neural Network |
| 3 | doi | 2016 | `papernot2016jsma` | The Limitations of Deep Learning in Adversarial Settings |
| 3 | doi | 2015 | `xiao2015support` | Support Vector Machines Under Adversarial Label Contamination |
| 3 | doi | 2014 | `biggio2014security` | Security Evaluation of Pattern Classifiers under Attack |
| 3 | doi | 2013 | `biggio2013evasion` | Evasion Attacks against Machine Learning at Test Time |
| 3 | doi | 2012 | `xiao2012adversarial` | Adversarial Label Flips Attack on Support Vector Machines |
| 3 | doi | 2011 | `huang2011adversarial` | Adversarial Machine Learning |
| 3 | doi | 2006 | `globerson2006nightmare` | Nightmare at Test Time: Robust Learning by Feature Deletion |
| 3 | doi | 2005 | `lowd2005adversarial` | Adversarial Learning |
| 3 | doi | 2004 | `dalvi2004adversarial` | Adversarial Classification |
| 3 | doi | 2018 | `kolosnjaji2018adversarial` | Adversarial Malware Binaries: Evading Deep Learning for Malware Detection in Execu |
| 3 | doi | 2016 | `moosavi2016deepfool` | {DeepFool}: A Simple and Accurate Method to Fool Deep Neural Networks |
| 3 | doi | 2010 | `barreno2010security` | The Security of Machine Learning |
| 3 | doi | 2008 | `liu2008isolation` | Isolation Forest |

Plus 359 further candidates in the pool at `keywords` matching this section.


---

# State of the pool

1,659 harvested records across fourteen files, folding to **1,361 unique entries**. The file
compiles under biber with zero warnings and zero LaTeX errors.

## Recency

The pool originally stopped in 2023, holding 25 entries from 2024 or later. After a targeted
2024-2026 top-up it holds **141 from 2024 onward and 175 from 2023 onward**, and every section
of the map reaches 2026. The distribution still peaks at 2015-2019, which is correct: that is
when the underlying work was done, and the contribution chapters should read as of then.
Chapter 2 is what needed the recent layer.

The top-up ran as four parallel searches covering Android malware detection, hypergraph
learning, anomaly and intrusion detection, and adversarial robustness evaluation. 121 entries
were added, each confirmed against a resolved DOI, a DBLP record, a publisher page, arXiv,
PMLR, OpenReview or a USENIX proceedings page. Nothing was included on recall alone.
Candidates that could not be confirmed were dropped, among them ETSI TS 104 223 and the
CISA/NSA AI deployment guidance, both unreachable.

## Verification

| Tier | Count | What it means |
| --- | ---: | --- |
| `doi` | 685 | DOI resolved through Crossref |
| `publisher`, `dblp`, `pmlr`, `usenix`, `openreview`, `jmlr`, and similar | 155 | record seen directly at the publisher or a scholarly index |
| `arxiv`, `openalex` | 90 | preprint or aggregator record seen |
| `url`, `web` | 35 | a web page was found, nothing stronger |
| `src` | 149 | copied from a colleague's bibliography, never checked |
| `no` | 166 | existence could not be confirmed at all |

**Roughly 1,010 of 1,361 are independently verified.** The 166 marked `no` are almost all
SPARTA deliverable citations, transcribed accurately but never confirmed externally; they are
incomplete rather than wrong. The 149 marked `src` inherit whatever errors the colleague
bibliographies contain. Since the thesis will cite roughly 200 entries, verification is best
done on demand, section by section, as each is drafted.

## Three cautions when using this file

**Off-topic residue.** SPARTA covered disinformation as well as adversarial ML, so the pool
carries a fake-news cluster (`allcott2017socialmedia`, `ahmed2018opinionspam`,
`ciampaglia2018fightingfakenews`, `conroy2015deception`, `jwa2019exbake`,
`quandt2019fakenews`, `tandoc2018definingfakenews`, `zhang2019fakenewsanalytics`,
`goldman2016nyt`) plus a few translation and recommender records. They cost nothing, because
biblatex prints only what is cited, but they are not coverage. The face-recognition records
(`huang2007lfw`, `parkhi2015deepface`, `schroff2015facenet`) are **not** in this category: the
SAFAIR contest ran on CelebA, so face data is on topic for Chapter 6.

**Deduplication keeps distinct editions apart.** Entries cluster by DOI and by normalised
title with author agreement, but two records that each carry a DOI, and different DOIs, are
never folded together. Without that rule the NIST AI 100-2e2023 and e2025 editions merged into
one entry, which produces a wrong citation rather than a missing one. The same rule keeps
conference papers separate from their extended journal versions (MaMaDroid NDSS 2017 and TOPS
2019; TESSERACT USENIX 2019 and the 2024 extended version).

**Some entries carry scope limits in their notes. Read them before citing.** Two examples that
would otherwise support claims they do not reach: `fang2025kaa` treats pairwise graphs only and
says nothing about hyperedges, and `maali2025evaluating` covers IoT device identification only,
not relationship or service-graph modelling. In both cases the limit is recorded in the entry's
own comment block so it travels with the citation.

## Calibration

Nine colleague dissertations from the same chair cite between 59 and 332 references, median
about 150:

| Thesis | Pages | References |
| --- | ---: | ---: |
| Fabian | 109 | 59 |
| Kirsch | 128 | 70 |
| Marius | 151 | 117 |
| Kolosnjaji | 135 | 139 |
| Xiao | 153 | 150 |
| Jan-Philipp | 132 | 188 |
| Kunz | 267 | 315 |
| Salfer | 260 | 332 |

At the planned 140 pages, this dissertation should cite between 180 and 250. The pool is a
selection pool, roughly six times larger than the bibliography it will produce.
