# Figures 2.1 and 2.2: temporary redesigns

Prepared on 13 September 2026 under T-014 using the built-in image_gen tool. This directory preserves the four design previews and generation records.

The author subsequently selected **2.1 A and 2.2 B** for insertion. Identical copies are now used by `content/background.tex` as `figures/background-apk-analysis.png` and `figures/background-hypergraph-projection.png`. LaTeX clips the temporary A/B labels at the top and scales each figure to the text width. The Figure 2.2 caption and its introductory sentence were aligned with the selected panel layout. The source PNGs remain unchanged.

| Figure | Variant A | Variant B |
| --- | --- | --- |
| 2.1 | [Parallel branches with convergence](figure-2-1-variant-a.png). The APK feeds static and dynamic observation, which combine in the hybrid panel. | [Analysis-mode comparison](figure-2-1-variant-b.png). Package contents appear above equally weighted static and dynamic panels; hybrid appears below. |
| 2.2 | [Projection and ambiguity](figure-2-2-variant-a.png). The six-method hypergraph and its projection occupy the main panels. An inset shows two distinct inputs that yield the same triangle. | [Explicit incidence matrix](figure-2-2-variant-b.png). The same memberships are shown in a matrix between the hypergraph and its pairwise projection. |

## Recommendation

Use A for Figure 2.1: the arrows make the meaning of hybrid analysis explicit. A is also the more direct choice for Figure 2.2 because the ambiguity is drawn as an example. Choose B for Figure 2.2 if the figure should also help readers interpret the incidence matrix introduced in Section 2.2.2. The matrix adds an explicit encoding of the existing example, rather than a new relation or result.

The approved PNGs have been inserted as requested. A later typesetting refinement could reproduce them as vector figures with the thesis font sizes, thinner strokes and flat fills. No vector redraw has been performed.

## Publication references inspected

- `publications/Hybroid/Hybroid.pdf`, Figure 1 on PDF page 3 (printed page 261), and the corresponding System Design text in `Hybroid.tex`: separate static and dynamic feature branches converge at feature combination. The redesign borrows that relationship without importing the paper's classifier or learning pipeline into a background figure.
- `references/pdf/zhou2006learning.pdf`, Figure 1 on PDF page 2: overlapping hyperedge contours are compared with a simple graph and an incidence table. The eight-page text was inspected. The redesign retains the dissertation's six methods and three hyperedges, not the source's article example.
- `publications/HGANN‑Mal/HGANN‑Mal.tex` and the original 21-page PDF: hyperedge generation is presented as Algorithm 1. The detailed diagram already in `figures/hgann-mal/hgann-mal-hyperedge-generation.pdf` belongs to the thesis assets and is not an original figure from that publication. It was inspected as a local style reference only.

## Content and checks

The APK filenames and the original observation claims were retained. Hybrid was reworded as the union of static and dynamic observations, with the original no-new-primitive note retained.

Both Figure 2.2 variants use e1={m1,m2,m3}, e2={m3,m4,m5}, and e3={m5,m6}. Their clique expansion contains exactly seven undirected edges. The incidence matrix in B has rows 100, 100, 110, 010, 011, 001, in the order m1 through m6. These entries, node labels and contours were inspected visually. Targeted image edits removed an extraneous m4-to-m5 line from both hypergraph panels and repaired the inset arrows in A. Figure 2.1 B received a small refinement to the hybrid icon's union shading.

Before final integration, the existing phrase "all shipped code" should receive a scientific wording review. It is an absolute statement beside an exception for packed code. This preview task preserves that source wording; it does not resolve the underlying qualification. A possible replacement is "Statically recoverable package contents", subject to agreement with the surrounding paragraph and caption. Any final wording change must be supported through the chapter's source workflow.

Integration corrected Figure 2.2's (a)/(b)/(c) caption mapping and replaced the surrounding sentence's description of "lifting" with hyperedge membership and pairwise projection. Neither variant depicts a call graph being lifted into a hypergraph.

The strict Chapter 2 citation audit passed after integration (110 sources, zero needing attention). `latexmk thesis.tex` succeeded, and `cmp thesis.pdf output/pdf/thesis.pdf` confirmed identical PDF copies. The build has no overfull boxes, undefined-reference warnings or citation warnings. Existing template and end-group warnings remain; Chapter 2's underfull vertical-box warnings changed with the new float sizes. No rendered-page visual review was performed, in accordance with the repository instructions.

## Generation record

The complete initial prompts are in [prompts.md](prompts.md); local correction prompts are in [refinement-prompts.md](refinement-prompts.md). [provenance.json](provenance.json) records the selected generated output paths. Original generated files remain in the Codex image directory. No CLI fallback or API key was used.
