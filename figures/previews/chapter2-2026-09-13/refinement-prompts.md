# Targeted refinement prompts

Built-in image_gen edit mode; each target is its first generated preview.

## figure-2-2-variant-a

```text
Use case: scientific-educational. Edit the supplied Figure 2.2 variant A preview. Preserve all text, style, upper-panel layout, all six-node memberships, and the upper-right projected graph, which is already correct. Make ONLY these two corrections:
1. In upper-left panel (a), REMOVE the single vertical black line between nodes m₄ and m₅. Those two nodes are members of the grey hyperedge e₂; there should be NO pairwise line inside any upper-left hyperedge. Preserve the white node circles, labels and all three hyperedge enclosures.
2. Redesign ONLY the lower inset (c) so the two distinct input diagrams each have their own visibly connected arrow to the same output triangle. Use TWO input rows on the lower left: top row "One hyperedge" with one pale blue enclosure around m₁,m₂,m₃ and no internal edges; bottom row "Three pairwise relations" with m₁,m₂,m₃ joined by exactly three black edges and no enclosure. Position one output triangle at lower right centered vertically between the two rows, labelled "Same projected triangle". Draw one arrow from the right boundary of the top hyperedge diagram to the output triangle, and one arrow from the right boundary of the bottom pairwise triangle to the output triangle. Each arrow must start visibly next to its OWN input diagram and stop before the output; no floating arrows. Keep "(c) Lost information" and "Group membership is lost". Use enough vertical room, shrink the diagrams slightly rather than text if necessary. No other edits.
```

## figure-2-2-variant-b

```text
Use case: scientific-educational. Edit the supplied Figure 2.2 variant B preview with ONE exact local correction. In the leftmost panel "(a) Hypergraph", remove the single black vertical line connecting m₄ to m₅ inside the grey dashed hyperedge e₂. Restore the same pale grey fill where that line was. Do not remove or alter either node circle, mathematical label, dashed enclosure, blue enclosure, dotted capsule or any text. The left hypergraph must have zero pairwise connector lines inside its enclosures. Preserve EVERYTHING ELSE pixel-for-pixel if possible, especially the incidence matrix values, rightmost clique expansion (which must retain its m₄–m₅ edge), bottom triangle and all arrows. No layout, color, font or content changes.
```

## figure-2-1-variant-b

```text
Use case: scientific-educational. Edit this Figure 2.1 variant B preview with one small correction to the Hybrid icon only. The two overlapping blue circles at bottom left should depict the UNION, so give both circles AND their overlap exactly the SAME uniform pale-blue fill. Remove the darker lens-shaped overlap emphasis, keep both blue circular outlines and the icon position. Keep ALL text, box geometry, colors, arrows, and every other element unchanged. Do not add or remove anything.
```

