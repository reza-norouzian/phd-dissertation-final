# Original report images for Section 3.5

Eight images extracted from the original PDF on 10 September 2026, covering all six
supplied screenshots. Files retain the embedded pixel dimensions and transparency.
There was no resampling, upscaling, cropping, or redrawing. The images are raster assets
inside the report; placing them in a PDF wrapper would not turn them into vector graphics.

Source: `publications/Anomaly Detection/Anomaly Detection in Industrial Control Systems.pdf`
(relative to the repository root).

`MANIFEST.tsv` maps each image to its report figure, original screenshot, printed page,
PDF page and object number. It records native dimensions, output SHA-256, and source PDF
SHA-256. PDF page numbers are one-based. The two comparisons in screenshot 6 and the two
loss plots in screenshot 2 are saved separately, giving eight files from six screenshots.

Extraction used pypdf 6.10.0: selected `page.images` by PDF object number and
wrote the returned PNG bytes directly. Every saved image was reopened and checked for
identical dimensions, mode and decoded pixels, including its alpha channel.

These files replace screenshots as the source assets for later inclusion. Figure selection,
scientific qualifications and caption work remain as recorded in the preparation plan.
No dissertation source or compiled PDF was changed during extraction.
