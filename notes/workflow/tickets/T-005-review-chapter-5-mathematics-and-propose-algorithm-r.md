---
id: T-005
title: Review Chapter 5 mathematics and propose algorithm restoration
status: review
priority: P1
chapter: 5
owner: codex
depends_on: []
blocks: []
tags: []
created: 2026-09-11
updated: 2026-09-11
---

## Goal

Read Chapter 5 and the complete HGANN-Mal source, identify scientifically defensible mathematical additions and corrections, and propose restoration of the original algorithm without editing dissertation LaTeX.

Extended on 11 September 2026: the author asked for the proposal to be applied to Chapter 5, which is recorded as D-046.

## Why it matters

The author requested a proposal for stronger mathematical exposition and restoration of the
paper's algorithm before any chapter changes. The chapter already has ten equations, but the
attention explanation contains algebraic errors and omits several deductions available from
the stated operator. A careful formalisation can expose those properties without inventing
historical implementation details or attributing performance gains to an unrun ablation.

## Acceptance criteria

- [x] Read the complete Chapter 5 and original HGANN-Mal LaTeX source, including the algorithm.
- [x] Check the related background, research questions, discussion and governing decisions.
- [x] Identify exact locations and scientific purposes for the proposed mathematical additions.
- [x] Distinguish derivations, conditional specifications and extensions requiring new evidence.
- [x] Locate the original algorithm and identify required clarifications before restoration.
- [x] Verify the worked example and key algebraic identities; record material contradictions.
- [x] Record the source evidence and pass the existing Chapter 5 strict reference audit.
- [x] Deliver a reviewable proposal without changing dissertation LaTeX, bibliography or PDFs.
- [x] Leave the working tree unstaged and pass the workflow consistency check.

Implementation, requested by the author on 11 September 2026 ("apply it to our dissertation in
Chapter 5"), recorded as D-046:

- [x] Restore the original algorithm as `alg:hgann:construction`, with the conventions of the
      proposal's table written in and stages 5 (post-processing) and 6 (sparse assembly) added.
- [x] Section 5.7: directed-distance convention, embedding `c_v` and similarity test, frozen `F_s`,
      candidate multiset with rejection and unrecorded duplicate policy, zero-degree methods.
- [x] Section 5.8: message derivation, effective coupling, fixed support, rank-one decomposition,
      binary-degree normalisation and uniform-attention scaling.
- [x] Section 5.8: six-method worked example with exact values (`tab:hgann:example`).
- [x] Section 5.8: conditional ranking result replacing the softmax-cancellation argument.
- [x] Section 5.8: energy identity with spectral damping, batch assembly, permutation invariance.
- [x] Section 5.8: masked objective stated as a conditional specification only.
- [x] Section 5.13: size and cost bounds; cap-as-evidence claim withdrawn.
- [x] Section 5.14 and both result captions: metric-convention inconsistencies disclosed.
- [x] Consistency corrections: Section 5.3 handset attribution, cross-sample semantic hyperedges
      (Section 5.11), transfer pointer in Section 2.3.2.
- [x] Strict audit passes for Chapters 5 and 2; build clean, PDFs identical, log read.
- [ ] Compiled-page visual review, left to the author under the project rules.
