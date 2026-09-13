# Clean TUM dissertation template

This workspace contains a clean dissertation skeleton based on the existing Clean CAMP Thesis style and KOMA-Script. It is an unofficial template, so the title-page wording and formal requirements must be checked against the current TUM doctoral regulations before submission.

## Start writing

1. Replace the placeholder metadata in `thesissetup.tex`.
2. Write the dissertation chapters in `content/`.
3. Add BibTeX records to `bib/references.bib` and cite them with `\cite{key}`.
4. Put figures in `figures/` and include them with `\includegraphics`.
5. Compile from the repository root with:

   ```sh
   latexmk thesis.tex
   ```

The generated PDF is written to `output/pdf/thesis.pdf`.

## Main files

- `thesis.tex`: document structure, packages, and chapter order
- `thesissetup.tex`: title, author, reviewers, dates, and university metadata
- `cleancampthesis.sty`: typography, colors, headings, margins, and page styles
- `content/titlepages.tex`: TUM-style title page
- `content/*.tex`: dissertation chapters and front matter
- `bib/references.bib`: bibliography database
- `assets/`: reusable TUM logo assets

## Useful commands

```sh
latexmk thesis.tex
latexmk -c thesis.tex
```

The first command builds the PDF. The second removes intermediate build files while preserving the PDF.
