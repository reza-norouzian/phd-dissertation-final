# Figure 2.1 and Figure 2.2 temporary design prompts

Built-in image_gen mode. Four independent variants, preview only. No thesis integration.

## figure-2-1-variant-a

Reference images: thesis-29, hybroid-original-p3 (rendered from local PDFs).

```text
Use case: scientific-educational
Asset type: temporary redesign preview for Figure 2.1 in a TUM PhD dissertation.
Primary request: Redesign the supplied original diagram, preserving its scientific content and filenames. Render a crisp, flat, publication-quality scientific figure on pure white, with generous spacing and large readable text. No page screenshot, no caption paragraph, no decorative illustration, no shadows, no gradients, no texture, no logos or watermark. Landscape about 2:1. Black text, thin dark lines, restrained TUM-like blue accents with pale blue and pale grey fills. Sans-serif labels; monospace filenames. Arrows must have a clear origin and destination and must not cross text.
Input images: first image is the EDIT TARGET, the existing thesis page containing Figure 2.1; redesign only the figure, omit all surrounding page text. Second image is the STYLE/STRUCTURE REFERENCE, Hybroid's original publication architecture; borrow only the idea of parallel static/dynamic branches converging, never its classifiers, metrics, feature vectors, or pipeline details.
Preserve all these elements, with exact text in quotation marks:
Package title "APK"; subtitle "ZIP archive".
"AndroidManifest.xml"; "components, permissions,"; "filtered intents".
"classes*.dex"; "Dalvik bytecode: methods,"; "invocations, basic blocks".
"res/   assets/   lib/".
Analysis mode "Static"; main observation "All shipped code, run or not"; qualifier "Not reached: packed and runtime-loaded code".
Analysis mode "Dynamic"; main observation "Paths the harness triggers"; qualifier "Adds: runtime values, unpacked code, traffic".
Combined mode "Hybrid"; description "Union of static and dynamic observations"; smaller note "No new primitive".
Do not invent any scientific information, icons that imply extra processing, counts, percentages or capabilities. All qualifiers must remain readable. Hybrid combines both branches; no arrow from Static to Dynamic and no independent APK-to-Hybrid branch.
Composition: Variant A, compact journal layout. Three aligned columns: left 30% a single APK container with neatly spaced manifest, DEX and secondary files sections; centre 45% two equal analysis panels stacked vertically, Static above Dynamic; right 20% a Hybrid panel vertically centered. Thin connectors from the APK to each analysis panel; their two output arrows separately enter the Hybrid panel. Give each mode a small blue uppercase eyebrow and bold main heading, use exact specified mode names only once. Small unobtrusive top-left label "2.1 / A". No main title. Align outer edges and provide generous internal padding. The filenames are comfortably contained, and descriptions cannot overlap borders. Fit text by line breaks, not by tiny type.
```

## figure-2-1-variant-b

Reference images: thesis-29, hybroid-original-p3 (rendered from local PDFs).

```text
Use case: scientific-educational
Asset type: temporary redesign preview for Figure 2.1 in a TUM PhD dissertation.
Primary request: Redesign the supplied original diagram, preserving its scientific content and filenames. Render a crisp, flat, publication-quality scientific figure on pure white, with generous spacing and large readable text. No page screenshot, no caption paragraph, no decorative illustration, no shadows, no gradients, no texture, no logos or watermark. Landscape about 2:1. Black text, thin dark lines, restrained TUM-like blue accents with pale blue and pale grey fills. Sans-serif labels; monospace filenames. Arrows must have a clear origin and destination and must not cross text.
Input images: first image is the EDIT TARGET, the existing thesis page containing Figure 2.1; redesign only the figure, omit all surrounding page text. Second image is the STYLE/STRUCTURE REFERENCE, Hybroid's original publication architecture; borrow only the idea of parallel static/dynamic branches converging, never its classifiers, metrics, feature vectors, or pipeline details.
Preserve all these elements, with exact text in quotation marks:
Package title "APK"; subtitle "ZIP archive".
"AndroidManifest.xml"; "components, permissions,"; "filtered intents".
"classes*.dex"; "Dalvik bytecode: methods,"; "invocations, basic blocks".
"res/   assets/   lib/".
Analysis mode "Static"; main observation "All shipped code, run or not"; qualifier "Not reached: packed and runtime-loaded code".
Analysis mode "Dynamic"; main observation "Paths the harness triggers"; qualifier "Adds: runtime values, unpacked code, traffic".
Combined mode "Hybrid"; description "Union of static and dynamic observations"; smaller note "No new primitive".
Do not invent any scientific information, icons that imply extra processing, counts, percentages or capabilities. All qualifiers must remain readable. Hybrid combines both branches; no arrow from Static to Dynamic and no independent APK-to-Hybrid branch.
Composition: Variant B, explanatory two-column layout. Top full-width APK strip with the archive title at left and THREE distinct source-content cells for manifest, DEX, and secondary files. All text remains horizontal. Below it, two wide equal columns, Static left and Dynamic right, separated by open white space. Each analysis column has a small simple line icon, a clear heading, one main observation in larger type, and the exact qualifier underneath in readable smaller text. Connect the APK strip downward to each analysis column. At bottom, both columns feed one full-width blue-outlined Hybrid bar with its description and small note. No directional connection between the two columns. Small unobtrusive top-left label "2.1 / B". No main title. Precise grid and large readable typography.
```

## figure-2-2-variant-a

Reference images: thesis-31, zhou-original (rendered from local PDFs).

```text
Use case: scientific-educational
Asset type: temporary redesign preview for Figure 2.2 in a TUM PhD dissertation.
Primary request: Redesign the supplied original diagram as a precise, flat, publication-quality scientific illustration. Pure white background, clean crisp lines, large legible text, no photo effect, no shadows, no gradient, no decoration, no figure caption paragraph. Landscape canvas. Sans-serif headings and LaTeX-like italic mathematical labels.
Input images: first image is the EDIT TARGET, the thesis page containing Figure 2.2. Preserve its mathematical example and draw only the redesigned figure, no surrounding thesis page. Second image is the SUPPORTING STYLE REFERENCE, Zhou et al. Figure 1; borrow overlapping hyperedge contours and side-by-side representation comparison, but DO NOT copy its 7-vertex example. Our example has exactly SIX vertices.
Mathematical invariants: nodes m₁,m₂,m₃,m₄,m₅,m₆ exactly once in each complete six-node diagram. e₁={m₁,m₂,m₃}, e₂={m₃,m₄,m₅}, e₃={m₅,m₆}. Cardinalities 3,3,2. Draw e₁ as a smooth blue translucent enclosure with solid blue boundary containing exactly m₁,m₂,m₃; e₂ as pale warm grey enclosure with dashed dark grey boundary containing exactly m₃,m₄,m₅; e₃ as a narrow pale blue-grey capsule with dotted boundary containing exactly m₅,m₆. m₃ lies INSIDE both e₁ and e₂; m₅ lies INSIDE both e₂ and e₃. No other overlaps cause extra membership. Each circle has a white fill and a mathematical label.
Keep node coordinates identical in every full six-node diagram, arranged as two adjacent triangles sharing m₃ and a tail to m₆: m₁ upper left, m₂ lower left, m₃ centre, m₄ upper right, m₅ lower right, m₆ farther lower right. The projected graph has EXACTLY SEVEN undirected edges: m₁–m₂, m₁–m₃, m₂–m₃, m₃–m₄, m₃–m₅, m₄–m₅, m₅–m₆. Edges plain black, no edge labels or colors that retain hyperedge identity, no arrowheads on graph edges.
Core point: a single three-member hyperedge and three separate pairwise relations yield the same unweighted triangle. Label this "Group membership is lost". Do not imply loss of all connectivity or improved detection performance. e₃ remains a two-member hyperedge equivalent to an ordinary graph edge. No extra nodes, no invented edges.
Composition: Variant A, compact journal comparison, landscape about 2:1. Upper two-thirds: two equally sized spacious panels, "(a) Hypergraph" at left and "(b) Clique expansion" at right. Draw the full six-node example at the same scale in each. Place a single labelled arrow "Clique expansion" between panels. Below the hypergraph list "e₁ = {m₁, m₂, m₃}" and "e₂ = {m₃, m₄, m₅}" and "e₃ = {m₅, m₆}" on separate lines. Put the set list beside the graph if needed, never obscure nodes.
Bottom third is a narrow illustrative inset labelled "(c) Lost information". At its left draw a tiny triangular arrangement of m₁,m₂,m₃ enclosed together in ONE pale blue smooth boundary with NO edges inside, label "One hyperedge". Beside it draw another tiny arrangement of m₁,m₂,m₃ connected by exactly THREE black pairwise edges and NO enclosure, label "Three pairwise relations". Have both point with two separately routed arrows to ONE tiny triangle of m₁,m₂,m₃ at right labelled "Same projected triangle". Put "Group membership is lost" under the inset. Keep the two upper panels visually dominant, the inset compact and very clear. Small top-left label "2.2 / A". No global title.
```

## figure-2-2-variant-b

Reference images: thesis-31, zhou-original (rendered from local PDFs).

```text
Use case: scientific-educational
Asset type: temporary redesign preview for Figure 2.2 in a TUM PhD dissertation.
Primary request: Redesign the supplied original diagram as a precise, flat, publication-quality scientific illustration. Pure white background, clean crisp lines, large legible text, no photo effect, no shadows, no gradient, no decoration, no figure caption paragraph. Landscape canvas. Sans-serif headings and LaTeX-like italic mathematical labels.
Input images: first image is the EDIT TARGET, the thesis page containing Figure 2.2. Preserve its mathematical example and draw only the redesigned figure, no surrounding thesis page. Second image is the SUPPORTING STYLE REFERENCE, Zhou et al. Figure 1; borrow overlapping hyperedge contours and side-by-side representation comparison, but DO NOT copy its 7-vertex example. Our example has exactly SIX vertices.
Mathematical invariants: nodes m₁,m₂,m₃,m₄,m₅,m₆ exactly once in each complete six-node diagram. e₁={m₁,m₂,m₃}, e₂={m₃,m₄,m₅}, e₃={m₅,m₆}. Cardinalities 3,3,2. Draw e₁ as a smooth blue translucent enclosure with solid blue boundary containing exactly m₁,m₂,m₃; e₂ as pale warm grey enclosure with dashed dark grey boundary containing exactly m₃,m₄,m₅; e₃ as a narrow pale blue-grey capsule with dotted boundary containing exactly m₅,m₆. m₃ lies INSIDE both e₁ and e₂; m₅ lies INSIDE both e₂ and e₃. No other overlaps cause extra membership. Each circle has a white fill and a mathematical label.
Keep node coordinates identical in every full six-node diagram, arranged as two adjacent triangles sharing m₃ and a tail to m₆: m₁ upper left, m₂ lower left, m₃ centre, m₄ upper right, m₅ lower right, m₆ farther lower right. The projected graph has EXACTLY SEVEN undirected edges: m₁–m₂, m₁–m₃, m₂–m₃, m₃–m₄, m₃–m₅, m₄–m₅, m₅–m₆. Edges plain black, no edge labels or colors that retain hyperedge identity, no arrowheads on graph edges.
Core point: a single three-member hyperedge and three separate pairwise relations yield the same unweighted triangle. Label this "Group membership is lost". Do not imply loss of all connectivity or improved detection performance. e₃ remains a two-member hyperedge equivalent to an ordinary graph edge. No extra nodes, no invented edges.
Composition: Variant B, explicit membership comparison, landscape about 2:1. Three well separated columns with generous space: "(a) Hypergraph", "(b) Incidence matrix H", "(c) Clique expansion". Draw the six-node example in the left and right columns using exact matching positions. Middle is a typeset 6x3 incidence matrix with bracket edges and headers e₁,e₂,e₃, row labels m₁ through m₆. Matrix rows EXACTLY:
m₁: 1 0 0
m₂: 1 0 0
m₃: 1 1 0
m₄: 0 1 0
m₅: 0 1 1
m₆: 0 0 1.
Use pale blue cells for 1 and white cells for 0 with clear dark digits. Left-to-middle connector labelled "Membership", middle-to-right arrow labelled "Pairwise projection". Beneath the left column show e₁, e₂, e₃ set memberships in small readable mathematical text.
Under the entire three-column figure add a clean explanatory horizontal footer: "One hyperedge {m₁, m₂, m₃}" and "Three pairwise relations" on separate lines both pointing to ONE small black triangle with m₁,m₂,m₃ labelled "Same triangle". End with "Group membership is lost". Small top-left label "2.2 / B". White space throughout; avoid sprawling decorative boxes. This is the same example, the matrix merely exposes its existing membership.
```

