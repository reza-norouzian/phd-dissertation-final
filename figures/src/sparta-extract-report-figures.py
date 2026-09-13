#!/usr/bin/env python3
"""Extract selected original SPARTA figure panels without resampling.

Run with the bundled Python (pypdf and Pillow). JPEG payloads remain byte
identical to their PDF streams; Flate image samples are losslessly saved as
PNG. The manifest records both file and decoded-pixel checksums.
"""

import csv
import hashlib
import io
from pathlib import Path

from PIL import Image
from pypdf import PdfReader

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "figures/sparta/report-originals"
SOURCES = {
    "D7.2": "publications/SPARTA/SPARTA-D7.2-preliminary-AI-security-mechanisms.pdf",
    "D7.5": "publications/SPARTA/SPARTA-D7.5-defensive_solutions_AI_contest_concept.pdf",
    "D7.6": "publications/SPARTA/SPARTA-D7.6-evaluation-and-validation.pdf",
}
# report, source figure, printed page, PDF page (one-based), PDF object,
# native width, native height, stable output basename
PANELS = [
    ("D7.6", "2", 22, 29, 261, 561, 332, "d76-fig02-benchmark-architecture"),
    ("D7.2", "13", 14, 21, 413, 380, 210, "d72-fig13-input-autoencoder"),
    ("D7.2", "11", 14, 21, 411, 407, 207, "d72-fig11-middle-autoencoder"),
    ("D7.2", "15", 16, 23, 420, 599, 205, "d72-fig15-prediction-similarity"),
    ("D7.2", "16", 16, 23, 421, 401, 228, "d72-fig16-activation-detector"),
    ("D7.5", "15-left", 23, 34, 724, 717, 478, "d75-fig15-iter-fgsm-left"),
    ("D7.5", "15-right", 23, 34, 725, 715, 477, "d75-fig15-iter-fgsm-right"),
]


def sha(data):
    return hashlib.sha256(data).hexdigest()


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    readers = {key: PdfReader(ROOT / value) for key, value in SOURCES.items()}
    source_sha = {key: sha((ROOT / value).read_bytes())
                  for key, value in SOURCES.items()}
    rows = []
    for report, figure, printed, pdf_page, object_id, width, height, name in PANELS:
        page = readers[report].pages[pdf_page - 1]
        extracted = next(im for im in page.images
                         if im.indirect_reference.idnum == object_id)
        original = extracted.image
        obj = extracted.indirect_reference.get_object()
        assert original.size == (width, height), (name, original.size)
        assert original.mode == "RGB", (name, original.mode)
        suffix = Path(extracted.name).suffix
        if suffix == ".jpg":
            # pypdf's convenience image.data may re-encode a JPEG. Preserve
            # the original DCT bytes directly, including their metadata.
            assert obj["/Filter"] == "/DCTDecode"
            payload = obj._data
            original = Image.open(io.BytesIO(payload))
            original.load()
            assert original.size == (width, height)
            assert original.mode == "RGB"
            method = "original-DCT-stream"
        elif suffix == ".png":
            assert obj.get_data() == original.tobytes(), "Flate samples differ"
            payload = extracted.data
            method = "lossless-PNG-from-original-RGB-samples"
        else:
            raise ValueError(f"Unexpected image format: {suffix}")
        restored = Image.open(io.BytesIO(payload))
        restored.load()
        assert restored.size == original.size
        assert restored.mode == original.mode
        assert restored.tobytes() == original.tobytes(), "Decoded pixels differ"
        target = OUT / (name + suffix)
        target.write_bytes(payload)
        rows.append({
            "asset": str(target.relative_to(ROOT)),
            "report": report,
            "source_pdf": SOURCES[report],
            "source_pdf_sha256": source_sha[report],
            "source_figure": figure,
            "printed_page": printed,
            "pdf_page_1_based": pdf_page,
            "object_id": object_id,
            "native_width_px": width,
            "native_height_px": height,
            "colour_mode": original.mode,
            "extraction": method,
            "extracted_file_sha256": sha(payload),
            "decoded_pixels_sha256": sha(original.tobytes()),
        })
        print(f"Verified {target.relative_to(ROOT)}: {width} x {height}, {method}")
    manifest = OUT / "MANIFEST.tsv"
    with manifest.open("w", newline="", encoding="utf-8") as stream:
        writer = csv.DictWriter(stream, fieldnames=rows[0].keys(), delimiter="\t",
                                lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)
    print(f"Wrote {manifest.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
