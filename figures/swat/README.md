# SWaT figures supplied for Section 3.5

Copied on 10 September 2026 at the author's request. All supplied PDFs and screenshots are
preserved byte for byte. `MANIFEST.tsv` records their source paths, sizes, and SHA-256 hashes.
The supplied files remain unchanged. Corrected context diagrams, a thesis-native pipeline
diagram, and two extracted report images are used in the revised Section 3.5.

- `SWAT_ICS_Architecture.pdf`: proposed testbed context figure.
- `SWaT_Attack_Taxonomy.pdf`: proposed attack-scope figure.
- `SWaT_collection_campaign.pdf`: proposed collection and preprocessing figure.
- `screenshots/`: the six author-supplied screenshots, numbered in their supplied order.
- `report-originals/`: eight PNGs extracted from the report at their native resolution,
  covering all six screenshots. Its own manifest maps the images to report pages and figures.
- `thesis/`: four vector diagrams built from `figures/src/swat-*.tex`. Three are the corrected
  context diagrams; `swat-gan-pipeline.pdf` is the GAN pipeline of Figure 3.8, drawn for the
  thesis from the report's method chapters and the accompanying code, and redrawn on
  12 September 2026 to match Section 3.5 (window fixed at 60, validation set, later 393,679
  test timestamps; D-055).

The supplied PDFs required scientific and caption corrections. In particular, the
campaign figure misidentifies 51,453 anomalous timestamps as the entire evaluation trace.
The taxonomy contains unsupported statements about detection difficulty and the necessity
of observing all 51 variables. The architecture mixes network-level and hierarchy-level
numbering. All three have embedded figure numbers from another document. The versions in
`thesis/` resolve these issues with native LaTeX captions supplied by the chapter. The
attack counts 26/4/2/4 were verified against Table 1 of the full SWaT dataset paper.

The complete assessment and proposed placements are in
`notes/chapter3-source-records/sec-3.5-figures-results-preparation.md`, relative to the
repository root. That note also maps each screenshot to its original report page.
Use the extracted images in `report-originals/`, or verified numerical outputs, for eventual
thesis figures. The screenshots serve as selection references.

Under the candidate's clarification D-038, the campaign bars describe collection phases
rather than the final train/test split. The pipeline's training and testing sets both
contain normal and attack observations, with unseen observations in testing. The pipeline
now shows 5 or 24 PCA components; its caption states that scaling and PCA were fitted on
training data and reused for testing. The functional network diagram does not assert
unrecovered layer counts or widths.

D-055 supplies the chronological partition. The revised campaign diagram shows the full
449,919-timestamp attack-period recording, with its first 56,240 timestamps assigned to training
and validation and its later 393,679 timestamps assigned to testing. Separate normal-operation
portions also support training and validation.

Rebuild the four diagrams with `sh build.sh` from `figures/src/`. The build copies their
PDFs to `figures/swat/thesis/`. The numerical curves remain the extracted original PNGs; no
plot values have been redrawn or estimated.
