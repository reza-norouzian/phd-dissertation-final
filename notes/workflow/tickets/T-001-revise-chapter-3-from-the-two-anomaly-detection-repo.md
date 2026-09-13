---
id: T-001
title: Revise Chapter 3 from the two anomaly-detection reports
status: review
priority: P0
chapter: 3
owner: codex
depends_on: []
blocks: []
tags: [writing, evidence, attribution]
created: 2026-08-19
updated: 2026-09-12
---

## Goal

Revise Chapter 3 using the two supplied reports, with verified figures, explicit methods,
results, limitations, and candidate contribution. The original 9-16-page target predates
the author's later expansions. The September 2026 scope includes the completed industrial
evaluation and the Section 3.5 figure-and-results revision; actual length is recorded below.

## Why it matters

The chapter must explain the candidate's GAN-based SWaT study alongside the industrial
framework. D-036 removed the NADICS DNN and adversarial study from this scope, and D-040
removed the UNSW-NB15, CICAndMal2017 and classical SWaT experiments. Subsequent revisions must preserve the distinction between recorded
results and unresolved empirical claims.

## Acceptance criteria

- [x] the author confirms the contribution boundary and bibliographic identity of both reports
- [x] the claim-to-source record is complete before LaTeX drafting begins
- [x] Chapter 3 answers both parts of RQ1; actual page count and changes from the original budget are recorded
- [x] the chapter contains a checkable account of methods, datasets, results, and limitations
- [x] context diagrams are supplied as vector graphics; empirical plots preserve their native source resolution, and tables reproduce the reports with stated qualifications
- [x] Chapter 1 contribution and attribution statements match the revised chapter
- [x] every citation passes `references/refcheck.py audit content/anomaly-detection.tex --strict`
- [x] `latexmk thesis.tex` succeeds, the log has been read, and both thesis PDFs are identical
- [ ] the author has visually reviewed the latest compiled Section 3.5 (visual review is left to the author under AGENTS.md)

## Evidence and sources

- `notes/chapter3-source-records/sec-3-revision-reports.md`
- `publications/Anomaly Detection/Anomaly Detection in Industrial Control Systems.pdf`
- `publications/Anomaly Detection/Defending Network Intrusion Detection Systems against Adversarial Machine Learning Attacks.pdf`
- `publications/Anomaly Detection/anomaly_detection_in_indestrial_control_systems/`
- `publications/Anomaly Detection/NADICS_repo/`
- core external keys: `goh2016swatdataset`, `lashkari2018toward`, `li2019madgan`,
  `geiger2020tadgan`, `li2018ganad`, `kim2024rethinking`
