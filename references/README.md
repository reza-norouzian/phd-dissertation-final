# The reference vault

Every reference cited in this dissertation must be a document that exists and that someone
has opened. This directory holds the evidence.

The concern is specific. A language model can produce a citation that is well formed,
plausibly titled, attributed to real authors who work in the right field, and entirely
fictitious. Bibliographic metadata alone does not settle the question, because metadata is
exactly what is easy to invent. An original PDF on disk, whose first pages contain the title
the bibliography claims, settles it.

## Layout

| Path | Contents | In git |
| --- | --- | --- |
| `pdf/<citekey>.pdf` | The original document, one file per bibliography key. | no |
| `MANIFEST.tsv` | One row per key: status, page count, size, hash, title check, where it came from. | yes |
| `refcheck.py` | The tool. | yes |

The PDFs are not committed. They are large, and many carry publisher licences that permit
personal use and nothing further. `MANIFEST.tsv` is committed, so the record of what was
checked survives even where the file itself cannot be shared.

## Status values

- `have` The PDF is on disk and was opened successfully.
- `no-pdf` No PDF exists or none should be expected. A poster, a book, a standard behind a
  purchase wall, a live web resource. The `note` column says which.
- `paywall` The document exists and was located, but the full text needs a subscription or a
  purchase that the fetch agent cannot make. **The author must supply these.**
- `notfound` No copy was located. Treat as a red flag until resolved.
- `pending` Not yet attempted.

## The title check

`refcheck.py` extracts the text of the first two pages of each PDF and measures how much of
the bibliography title appears there, ignoring short words. The `title_ok` column reports
`yes` above 70 per cent, `partial` above 40 per cent, and `no` below that. A `?` means the
PDF carries no extractable text, which usually indicates a scanned document, and those need
a human glance.

A `no` is the case that matters. It has three common causes: the download returned a login
page or an error page rather than the paper, the file is a different paper than the key
claims, or the bibliography title is wrong. Each is worth catching.

## Usage

```
./refcheck.py audit content/introduction.tex          the table that matters
./refcheck.py audit content/*.tex --strict            non-zero exit if anything is unresolved
./refcheck.py todo content/introduction.tex --json    work list for a fetch agent
./refcheck.py missing content/introduction.tex        keys still needing a PDF
./refcheck.py add KEY --status have --source arxiv --url https://...
./refcheck.py verify                                  re-hash and re-check the whole vault
```

`add` takes a file lock before touching `MANIFEST.tsv`, so several fetch agents may run at
once without losing each other's rows.

## Where to look for a PDF

In roughly this order, because the earlier sources are both legal and stable: arXiv,
the ACM Digital Library open-access items, IEEE Xplore open-access items, USENIX (all papers
are free), the Network and Distributed System Security Symposium, PMLR, OpenReview, JMLR,
the publisher's own page when the venue is gold open access, then the author's institutional
page. Sci-Hub and similar mirrors are not used.

## What to do when a PDF cannot be obtained

Record it as `paywall` with the URL of the landing page, and say so in the session report.
The author has institutional access through TUM and can retrieve those. Do not silently
downgrade the entry to `no-pdf`, and never remove the citation to make the audit pass.
