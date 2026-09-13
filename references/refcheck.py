#!/usr/bin/env python3
"""refcheck - proof that every cited reference is a real document.

The rule this enforces: a citation may appear in the dissertation only if the
key exists in `bib/references.bib` and the reference vault holds either the
original PDF or an explicit, recorded reason why no PDF can be held. Nothing is
taken on trust.

    ./refcheck.py keys content/introduction.tex
    ./refcheck.py audit content/introduction.tex        the table that matters
    ./refcheck.py add KEY --status have --url ... --source arxiv
    ./refcheck.py verify                                re-hash and re-check every PDF
    ./refcheck.py missing content/introduction.tex      keys still needing a PDF
    ./refcheck.py todo content/introduction.tex --json  work list for a fetch agent

`add` takes a file lock, so several agents may write at once.
"""
import argparse
import datetime as dt
import fcntl
import hashlib
import json
import os
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
PDFS = HERE / "pdf"
MANIFEST = HERE / "MANIFEST.tsv"
LOCK = HERE / ".manifest.lock"
BIB = ROOT / "bib" / "references.bib"

COLUMNS = ["citekey", "status", "pages", "bytes", "sha256", "title_ok",
           "source", "url", "checked", "note"]
STATUSES = ["have", "paywall", "no-pdf", "notfound", "pending"]

STOP = set("a an and the of for with to in on at by from as is are be using via "
           "toward towards towards".split())


# ---------------------------------------------------------------------- bib --

def load_bib():
    """key -> {title, year, doi, verified, type}. Provenance sits in the comment
    lines above each entry, which biber ignores and we do not."""
    text = BIB.read_text(encoding="utf-8", errors="replace")
    out, comment = {}, []
    entry_key = None
    depth = 0
    buf = []
    for line in text.splitlines():
        if entry_key is None:
            if line.startswith("%"):
                comment.append(line[1:].strip())
                continue
            m = re.match(r"@(\w+)\s*\{\s*([^,]+),", line)
            if m:
                entry_key, etype = m.group(2).strip(), m.group(1).lower()
                depth = line.count("{") - line.count("}")
                buf = [line]
                continue
            if line.strip():
                comment = []
            continue
        buf.append(line)
        depth += line.count("{") - line.count("}")
        if depth <= 0:
            body = "\n".join(buf)
            prov = " ".join(comment)
            ver = re.search(r"verified:\s*([A-Za-z0-9_.-]+)", prov)
            out[entry_key] = {
                "type": etype,
                "title": field(body, "title"),
                "year": field(body, "year"),
                "doi": field(body, "doi"),
                "url": field(body, "url") or field(body, "howpublished"),
                "verified": (ver.group(1).lower() if ver else "no"),
            }
            entry_key, comment, buf = None, [], []
    return out


def field(entry, name):
    m = re.search(name + r"\s*=\s*", entry, re.I)
    if not m:
        return ""
    i = m.end()
    if i >= len(entry):
        return ""
    if entry[i] == '"':
        j = entry.index('"', i + 1)
        return clean(entry[i + 1:j])
    if entry[i] != "{":
        return clean(entry[i:].split(",")[0])
    depth, j = 0, i
    while j < len(entry):
        if entry[j] == "{":
            depth += 1
        elif entry[j] == "}":
            depth -= 1
            if depth == 0:
                break
        j += 1
    return clean(entry[i + 1:j])


def clean(s):
    s = re.sub(r"[{}]", "", s)
    s = re.sub(r"\\[a-zA-Z]+\s*", "", s)
    return " ".join(s.split())


# ----------------------------------------------------------------- manifest --

def read_manifest():
    if not MANIFEST.exists():
        return {}
    rows = {}
    for i, line in enumerate(MANIFEST.read_text(encoding="utf-8").splitlines()):
        if i == 0 or not line.strip():
            continue
        parts = line.split("\t")
        parts += [""] * (len(COLUMNS) - len(parts))
        rows[parts[0]] = dict(zip(COLUMNS, parts))
    return rows


def write_manifest(rows):
    lines = ["\t".join(COLUMNS)]
    for key in sorted(rows):
        r = rows[key]
        lines.append("\t".join(str(r.get(c, "")).replace("\t", " ") for c in COLUMNS))
    MANIFEST.write_text("\n".join(lines) + "\n", encoding="utf-8")


def locked_update(fn):
    LOCK.touch()
    with open(LOCK, "r+") as fh:
        fcntl.flock(fh, fcntl.LOCK_EX)
        try:
            rows = read_manifest()
            fn(rows)
            write_manifest(rows)
        finally:
            fcntl.flock(fh, fcntl.LOCK_UN)


# ---------------------------------------------------------------------- pdf --

def inspect_pdf(path, expect_title=""):
    """Return (pages, sha256, bytes, title_ok, note). A file that is not a PDF,
    or that carries a login page instead of the paper, has to be caught here
    rather than by a reader of the finished thesis."""
    data = path.read_bytes()
    sha = hashlib.sha256(data).hexdigest()[:16]
    if not data.startswith(b"%PDF"):
        return 0, sha, len(data), "no", "not a PDF"
    try:
        import pypdf
        reader = pypdf.PdfReader(str(path))
        pages = len(reader.pages)
        text = ""
        for p in reader.pages[:2]:
            try:
                text += p.extract_text() or ""
            except Exception:
                pass
    except Exception as e:
        return 0, sha, len(data), "no", f"unreadable: {type(e).__name__}"
    if not expect_title:
        return pages, sha, len(data), "?", ""
    want = [t for t in re.findall(r"[a-z0-9]+", expect_title.lower())
            if t not in STOP and len(t) > 2]
    if not want:
        return pages, sha, len(data), "?", ""
    got = set(re.findall(r"[a-z0-9]+", text.lower()))
    hit = sum(1 for t in want if t in got) / len(want)
    if not text.strip():
        return pages, sha, len(data), "?", "no extractable text (scan?)"
    ok = "yes" if hit >= 0.7 else ("partial" if hit >= 0.4 else "no")
    return pages, sha, len(data), ok, f"title match {hit:.0%}"


# --------------------------------------------------------------------- keys --

CITE = re.compile(r"\\(?:no|foot|auto|paren|text|super)?cite[a-zA-Z]*\*?"
                  r"(?:\[[^\]]*\])*\s*\{([^}]*)\}")


def cite_keys(paths):
    keys = []
    for p in paths:
        text = Path(p).read_text(encoding="utf-8", errors="replace")
        text = re.sub(r"(?<!\\)%.*", "", text)          # drop LaTeX comments
        for m in CITE.finditer(text):
            for k in m.group(1).split(","):
                k = k.strip()
                if k and k not in keys:
                    keys.append(k)
    return keys


# ----------------------------------------------------------------- commands --

def cmd_keys(args):
    for k in sorted(cite_keys(args.files)):
        print(k)


def cmd_audit(args):
    bib = load_bib()
    rows = read_manifest()
    keys = sorted(cite_keys(args.files))
    bad = 0
    print(f"{'citekey':<32} {'bib':<4} {'verified':<10} {'pdf':<9} {'title':<8} note")
    print("-" * 96)
    for k in keys:
        e = bib.get(k)
        r = rows.get(k, {})
        in_bib = "yes" if e else "NO"
        ver = (e or {}).get("verified", "-")
        st = r.get("status", "pending")
        tok = r.get("title_ok", "-")
        note = r.get("note", "")
        if not e or st in ("pending", "notfound") or tok == "no":
            bad += 1
        print(f"{k:<32} {in_bib:<4} {ver:<10} {st:<9} {tok:<8} {note}")
    print("-" * 96)
    have = sum(1 for k in keys if rows.get(k, {}).get("status") == "have")
    print(f"{len(keys)} cited, {have} with a PDF on disk, {bad} needing attention")
    if bad and args.strict:
        sys.exit(1)


def cmd_missing(args):
    bib = load_bib()
    rows = read_manifest()
    for k in sorted(cite_keys(args.files)):
        if rows.get(k, {}).get("status") not in ("have", "no-pdf"):
            e = bib.get(k, {})
            print(f"{k}\t{e.get('doi','')}\t{e.get('year','')}\t{e.get('title','')}")


def cmd_todo(args):
    bib = load_bib()
    rows = read_manifest()
    out = []
    for k in sorted(cite_keys(args.files)):
        if rows.get(k, {}).get("status") in ("have", "no-pdf"):
            continue
        e = bib.get(k)
        if not e:
            out.append({"citekey": k, "error": "not in bib"})
            continue
        out.append({"citekey": k, "title": e["title"], "year": e["year"],
                    "doi": e["doi"], "url": e["url"], "type": e["type"]})
    print(json.dumps(out, indent=1) if args.json else
          "\n".join(f"{o['citekey']}\t{o.get('doi','')}\t{o.get('title','')}" for o in out))


def cmd_add(args):
    bib = load_bib()
    key = args.citekey
    if key not in bib and not args.force:
        sys.exit(f"{key} is not in {BIB}. Add the entry first, or pass --force.")
    path = PDFS / f"{key}.pdf"
    pages = size = sha = ""
    title_ok = "-"
    note = args.note or ""
    status = args.status
    if path.exists():
        pages, sha, size, title_ok, auto = inspect_pdf(path, bib.get(key, {}).get("title", ""))
        note = note or auto
        if status == "pending":
            status = "have"
    elif status == "have":
        sys.exit(f"status 'have' but {path} does not exist")

    def upd(rows):
        rows[key] = {"citekey": key, "status": status, "pages": pages, "bytes": size,
                     "sha256": sha, "title_ok": title_ok, "source": args.source or "",
                     "url": args.url or "", "checked": dt.date.today().isoformat(),
                     "note": note}
    locked_update(upd)
    print(f"{key}\t{status}\t{title_ok}\t{note}")


def cmd_verify(args):
    bib = load_bib()
    changed = []

    def upd(rows):
        for path in sorted(PDFS.glob("*.pdf")):
            key = path.stem
            pages, sha, size, title_ok, note = inspect_pdf(path, bib.get(key, {}).get("title", ""))
            row = rows.get(key, {"citekey": key, "source": "", "url": ""})
            row.update({"citekey": key, "status": "have", "pages": pages, "bytes": size,
                        "sha256": sha, "title_ok": title_ok,
                        "checked": dt.date.today().isoformat(), "note": note})
            rows[key] = row
            if title_ok in ("no", "?"):
                changed.append(f"  {key}: {title_ok} ({note})")
    locked_update(upd)
    rows = read_manifest()
    n = sum(1 for r in rows.values() if r["status"] == "have")
    print(f"{n} PDFs in the vault")
    if changed:
        print("needing a look:")
        print("\n".join(changed))


def main():
    PDFS.mkdir(parents=True, exist_ok=True)
    p = argparse.ArgumentParser(prog="refcheck", description=__doc__,
                                formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = p.add_subparsers(dest="cmd", required=True)

    for name, fn in (("keys", cmd_keys), ("missing", cmd_missing)):
        s = sub.add_parser(name)
        s.add_argument("files", nargs="+")
        s.set_defaults(func=fn)

    a = sub.add_parser("audit")
    a.add_argument("files", nargs="+")
    a.add_argument("--strict", action="store_true")
    a.set_defaults(func=cmd_audit)

    t = sub.add_parser("todo")
    t.add_argument("files", nargs="+")
    t.add_argument("--json", action="store_true")
    t.set_defaults(func=cmd_todo)

    d = sub.add_parser("add")
    d.add_argument("citekey")
    d.add_argument("--status", default="pending", choices=STATUSES)
    d.add_argument("--url")
    d.add_argument("--source")
    d.add_argument("--note")
    d.add_argument("--force", action="store_true")
    d.set_defaults(func=cmd_add)

    v = sub.add_parser("verify")
    v.set_defaults(func=cmd_verify)

    args = p.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
