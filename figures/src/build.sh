#!/bin/sh
# Rebuild the thesis-native figures in this directory and install the PDFs one
# level up, where \graphicspath finds them. Run from figures/src.
set -e

# --- TikZ figures -----------------------------------------------------------
for f in hybroid-detection-classifiers hybroid-categorisation-classifiers; do
  pdflatex -interaction=nonstopmode -halt-on-error "$f.tex" >/dev/null
  cp "$f.pdf" ../
  echo "built $f.pdf"
done

# Corrected SWaT context diagrams and the thesis-native GAN pipeline (Figure 3.8);
# preserve the author-supplied PDFs separately.
mkdir -p ../swat/thesis
for f in swat-ics-architecture swat-attack-taxonomy swat-collection-campaign swat-gan-pipeline; do
  pdflatex -interaction=nonstopmode -halt-on-error "$f.tex" >/dev/null
  cp "$f.pdf" ../swat/thesis/
  echo "built swat/thesis/$f.pdf"
done

# SPARTA diagrams redrawn in the same style (Figures 6.1 to 6.3); the report
# originals stay in ../sparta/report-originals/.
mkdir -p ../sparta/thesis
for f in sparta-benchmark-architecture sparta-autoencoder-placement sparta-detector-mechanisms; do
  pdflatex -interaction=nonstopmode -halt-on-error "$f.tex" >/dev/null
  cp "$f.pdf" ../sparta/thesis/
  echo "built sparta/thesis/$f.pdf"
done
rm -f ./*.aux ./*.log

# --- matplotlib figures -----------------------------------------------------
# The Python figures need matplotlib, which is not part of the LaTeX toolchain.
# A local virtualenv is created here on first run and reused afterwards; it is
# git-ignored, so a fresh clone rebuilds it from requirements.txt.
if [ ! -x .venv/bin/python ]; then
  echo "creating figures/src/.venv"
  if command -v uv >/dev/null 2>&1; then
    uv venv .venv
    uv pip install --quiet --python .venv/bin/python -r requirements.txt
  else
    python3 -m venv .venv
    .venv/bin/pip install --quiet -r requirements.txt
  fi
fi

for f in nadics-feature-importance; do
  .venv/bin/python "$f.py" >/dev/null
  cp "$f.pdf" ../
  echo "built $f.pdf"
done

# Appendix A tables, generated from the same JSON as Figure 3.4. The script writes
# its two LaTeX fragments straight into figures/.
.venv/bin/python nadics-feature-importance-table.py

# SPARTA plots install themselves in figures/sparta/thesis/. Their shared JSON
# preserves the reported values and the scripts derive percentage-point changes.
for f in sparta-sd-comparison sparta-benchmark-deltas; do
  .venv/bin/python "$f.py"
  echo "built sparta/thesis/$f.pdf"
done
