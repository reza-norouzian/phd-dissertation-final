---
id: T-027
title: Fix nine bibliography defects found by the reference validation pass
status: review
priority: P1
chapter: -
owner: claude
depends_on: []
blocks: []
tags: [references, bib]
created: 2026-09-21
updated: 2026-09-21
---

## Goal

Repair the defects that the 21 September 2026 reference validation pass found in the 177
cited entries. The pass checked every cited key against Crossref, DataCite, arXiv, OpenAlex
and the live publisher pages, independently of `refcheck.py` and of the vault manifest. No
fabricated reference was found; the nine items below are the defects that were.

## Why it matters

Five cited URLs did not open at all, which a reader or an examiner would hit directly. The
rest are metadata defects that do not change which document a reader finds, but they weaken
the record the vault exists to keep.

## Acceptance criteria

- [x] The five SPARTA deliverable URLs resolve and return a PDF.
- [x] The two arXiv entries follow the house `eprint`/`archiveprefix` pattern.
- [x] No cited entry carries fields belonging to a different publication.
- [x] The uncited Argus duplicates are gone and the cited key carries what they held.
- [x] The `chen2018android` and `vassilev2025adversarial` findings are recorded in the manifest.
- [x] `refcheck.py audit content/*.tex --strict` passes.
- [x] `latexmk thesis.tex` runs clean and the log carries no new warning.

## Evidence and sources

Each repair was confirmed against a primary record before it was made.

| Item | Repair | Evidence |
| --- | --- | --- |
| 1 | `sparta2020d72`, `sparta2021d71`, `sparta2021d73`, `sparta2021d75`, `sparta2022d76`: URL host changed from `www.sparta.eu` to `sparta.eu` | The www host serves a TLS certificate that does not cover it (curl error 60). All five apex URLs return HTTP 200, `application/pdf`, at the byte sizes the manifest records |
| 2 | `chen2018android`: manifest note added | Crossref API returns 404 for `10.3966/199115992018122906024`; doi.org resolves it to an ERICDATA page carrying the title; the vault PDF prints the same DOI on page 243 |
| 3 | `kan2024tesseract`, `chow2025beyond`: `journal = {arXiv preprint ...}` replaced by `eprint`, `archiveprefix`, `primaryclass` and the arXiv DOI; type changed to `@misc` | DataCite holds both DOIs with matching titles and creator counts (eight and seven); primary classes cs.LG and cs.CR read off the arXiv abstract pages |
| 4 | `chow2025beyond`: kept as a preprint, with the open question recorded in the entry | arXiv shows no journal reference, Semantic Scholar reports no venue, and the UCL Discovery page that OpenAlex derives its 2026 conference classification from is behind a bot challenge |
| 5 | `paxson1999bro`: `booktitle` and `publisher` removed | Both named the USENIX Security 1998 version; the entry, its DOI and the vault PDF are the 1999 Computer Networks article. Biblatex ignored them in an `@article`, so the printed entry is unchanged |
| 6 | `cicandmal2017dataset`: `year = {2026}` added | The dataset page carries no publication date. 2026 is the year of consultation, the convention the other live web resources in the file already use |
| 7 | `feng2019hypergraph`: duplicate `booktitle` removed | Crossref returns the AAAI proceedings as a journal for `10.1609/aaai.v33i01.33013558`, which the `journal` field already held |
| 8 | `argus` and `argus2020argus` removed | Both described the same openargus.org documentation as the cited `qosient2026argus`, and neither was cited. The UNSW-NB15 note that `argus` carried was moved onto the cited key. `vassilev2024adversarial` was kept: it is the 2023 edition of the NIST report, a different document with its own DOI, not a duplicate |
| 9 | `vassilev2025adversarial`: cover-page author check recorded | The cover of the vault PDF names Vassilev, Oprea, Fordyce, Anderson, Davies and Hamin, in the order the entry gives. The Crossref record names Vassilev alone |

## Log

- 2026-09-21 created
- 2026-09-21 All nine items applied. `refcheck.py audit content/*.tex --strict` exits 0 over
  177 cited keys. `latexmk thesis.tex` rebuilds to 153 pages with 177 bibliography entries,
  no undefined citation and no biber warning. The five repaired URLs were fetched again from
  the edited entries and all returned a PDF.
- 2026-09-21 INCIDENT, and the reason this ticket also touches `references/MANIFEST.tsv`:
  `refcheck.py verify` rewrites the `note` column of every row whose PDF it re-reads, which
  destroys curated text. It was run early in this session and overwrote the uncommitted notes
  in the working tree. 39 rows were rebuilt afterwards from three independent sources: the
  20:09 snapshot in `tmp/background-revision-2026-09-20/MANIFEST.tsv`, the saved audit outputs
  under `tmp/`, and the audit printed at the start of this session, which had captured the
  final pre-loss state of the alphabetical tail. Every manifest blob in the git object store
  was also checked and held nothing richer. The file now carries 54 substantive notes, more
  than any earlier version of it. A note that existed only in the working tree and in none of
  those sources cannot be recovered. `refcheck.py verify` should preserve the note column;
  until it does, do not run it on this repository.
- 2026-09-21 in-progress -> review (Nine bibliography defects repaired; strict audit and rebuild pass)
