#!/usr/bin/env python3
"""wf - the dissertation work tracker.

One unit of work is one ticket, and one ticket is one file. Around the tickets
sit an append-only worklog and a decision register, so that a later session can
reconstruct what was done and why without re-reading the whole conversation.
Standard library only.

    ./wf.py board                       rebuild BOARD.md from tickets/
    ./wf.py new "Draft 1.1" -c 1 -p P1  create the next ticket
    ./wf.py list [--status s] [-c 1]    one line per ticket
    ./wf.py show T-004                  print a ticket
    ./wf.py status T-004 done -m "..."  move a ticket, log the move
    ./wf.py log "message" [-t T-004]    add a worklog line
    ./wf.py decide "title" -w "..."     add a decision record
    ./wf.py recent [-n 40]              tail of the worklog
    ./wf.py check                       validate the board

Every command that changes state also rebuilds BOARD.md, so the board is never
stale.
"""
import argparse
import datetime as dt
import os
import re
import sys
import textwrap
from pathlib import Path

HERE = Path(__file__).resolve().parent
TICKETS = HERE / "tickets"
BOARD = HERE / "BOARD.md"
WORKLOG = HERE / "WORKLOG.md"
DECISIONS = HERE / "DECISIONS.md"

STATUSES = ["in-progress", "review", "blocked", "ready", "backlog", "done", "dropped"]
OPEN_STATUSES = ["in-progress", "review", "blocked", "ready", "backlog"]
PRIORITIES = ["P0", "P1", "P2", "P3"]
FIELD_ORDER = ["id", "title", "status", "priority", "chapter", "owner",
               "depends_on", "blocks", "tags", "created", "updated"]


def today():
    return dt.date.today().isoformat()


def now_hm():
    return dt.datetime.now().strftime("%H:%M")


# ------------------------------------------------------------------ tickets --

def parse_ticket(path):
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---"):
        raise ValueError(f"{path.name}: no frontmatter")
    _, front, body = text.split("---", 2)
    meta = {}
    for line in front.strip().splitlines():
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        key, value = key.strip(), value.strip()
        if value.startswith("[") and value.endswith("]"):
            value = [v.strip() for v in value[1:-1].split(",") if v.strip()]
        meta[key] = value
    return meta, body.lstrip("\n")


def write_ticket(path, meta, body):
    lines = ["---"]
    for key in FIELD_ORDER:
        if key not in meta:
            continue
        value = meta[key]
        if isinstance(value, list):
            value = "[" + ", ".join(value) + "]"
        lines.append(f"{key}: {value}")
    for key in sorted(set(meta) - set(FIELD_ORDER)):
        lines.append(f"{key}: {meta[key]}")
    lines += ["---", "", body.rstrip() + "\n"]
    path.write_text("\n".join(lines), encoding="utf-8")


def load_all():
    out = []
    for path in sorted(TICKETS.glob("T-*.md")):
        meta, body = parse_ticket(path)
        meta["_path"] = path
        meta["_body"] = body
        out.append(meta)
    return out


def by_id(tickets):
    return {t["id"]: t for t in tickets}


def find(tickets, ticket_id):
    ticket_id = ticket_id.upper()
    if not ticket_id.startswith("T-"):
        ticket_id = "T-" + ticket_id.zfill(3)
    index = by_id(tickets)
    if ticket_id not in index:
        sys.exit(f"no such ticket: {ticket_id}")
    return index[ticket_id]


def slug(title):
    s = re.sub(r"[^a-z0-9]+", "-", title.lower()).strip("-")
    return s[:52].rstrip("-")


def next_id(tickets):
    highest = 0
    for t in tickets:
        m = re.match(r"T-(\d+)$", t["id"])
        if m:
            highest = max(highest, int(m.group(1)))
    return f"T-{highest + 1:03d}"


TEMPLATE = """\
## Goal

{goal}

## Why it matters

To be written.

## Acceptance criteria

- [ ] To be written.

## Evidence and sources

- To be written.

## Log

- {date} created
"""


# ------------------------------------------------------------------ worklog --

def worklog_add(line):
    """Prepend under today's heading. The newest work stays at the top so that
    reading the first page of the file is enough to pick up the thread."""
    header = ("# Worklog\n\n"
              "Append-only. Newest first. Written by `wf.py`; hand edits are fine "
              "but keep the shape.\n")
    text = WORKLOG.read_text(encoding="utf-8") if WORKLOG.exists() else header + "\n"
    marker = f"## {today()}\n"
    if marker in text:
        head, rest = text.split(marker, 1)
        text = head + marker + "\n" + line + "\n" + rest.lstrip("\n")
    else:
        split_at = text.index("\n## ") if "\n## " in text else len(text)
        text = (text[:split_at].rstrip("\n") + "\n\n" + marker + "\n" + line + "\n"
                + text[split_at:])
    WORKLOG.write_text(text, encoding="utf-8")


# -------------------------------------------------------------------- board --

def build_board(tickets):
    lines = ["# Board", "",
             "Generated by `wf.py board`. Do not edit by hand; edit the ticket files in",
             "`tickets/` and rebuild.", ""]
    counts = {s: sum(1 for t in tickets if t.get("status") == s) for s in STATUSES}
    total_open = sum(counts[s] for s in OPEN_STATUSES)
    lines += [f"{len(tickets)} tickets, {total_open} open, {counts['done']} done, "
              f"{counts['dropped']} dropped. Rebuilt {today()}.", ""]

    for status in STATUSES:
        group = [t for t in tickets if t.get("status") == status]
        if not group:
            continue
        group.sort(key=lambda t: (PRIORITIES.index(t.get("priority", "P2"))
                                  if t.get("priority") in PRIORITIES else 9,
                                  t["id"]))
        lines += [f"## {status} ({len(group)})", ""]
        lines += ["| id | pri | ch | title | depends on |", "| --- | --- | --- | --- | --- |"]
        for t in group:
            deps = t.get("depends_on") or []
            deps = ", ".join(deps) if isinstance(deps, list) else str(deps)
            name = t["_path"].name
            lines.append(f"| [{t['id']}](tickets/{name}) | {t.get('priority','')} | "
                         f"{t.get('chapter','-')} | {t.get('title','')} | {deps or '-'} |")
        lines.append("")

    BOARD.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")


# ----------------------------------------------------------------- commands --

def cmd_new(args):
    tickets = load_all()
    tid = next_id(tickets)
    meta = {
        "id": tid,
        "title": args.title,
        "status": args.status,
        "priority": args.priority,
        "chapter": args.chapter or "-",
        "owner": args.owner,
        "depends_on": args.depends or [],
        "blocks": [],
        "tags": args.tags or [],
        "created": today(),
        "updated": today(),
    }
    path = TICKETS / f"{tid}-{slug(args.title)}.md"
    write_ticket(path, meta, TEMPLATE.format(goal=args.goal or args.title, date=today()))
    worklog_add(f"- `{now_hm()}` **{tid}** created: {args.title}")
    build_board(load_all())
    print(path)


def cmd_status(args):
    tickets = load_all()
    ticket = find(tickets, args.id)
    if args.new_status not in STATUSES:
        sys.exit(f"status must be one of: {', '.join(STATUSES)}")
    old = ticket.get("status")
    meta, body = parse_ticket(ticket["_path"])
    meta["status"] = args.new_status
    meta["updated"] = today()
    note = f" ({args.message})" if args.message else ""
    body = body.rstrip() + f"\n- {today()} {old} -> {args.new_status}{note}\n"
    write_ticket(ticket["_path"], meta, body)
    worklog_add(f"- `{now_hm()}` **{ticket['id']}** {old} -> {args.new_status}"
                + (f" - {args.message}" if args.message else ""))
    build_board(load_all())
    print(f"{ticket['id']}: {old} -> {args.new_status}")


def cmd_log(args):
    prefix = f"**{args.ticket.upper()}** " if args.ticket else ""
    worklog_add(f"- `{now_hm()}` {prefix}{args.message}")
    print("logged")


def cmd_list(args):
    tickets = load_all()
    if args.status:
        tickets = [t for t in tickets if t.get("status") == args.status]
    if args.open:
        tickets = [t for t in tickets if t.get("status") in OPEN_STATUSES]
    if args.chapter:
        tickets = [t for t in tickets if str(t.get("chapter")) == str(args.chapter)]
    tickets.sort(key=lambda t: (STATUSES.index(t.get("status", "backlog"))
                                if t.get("status") in STATUSES else 9, t["id"]))
    for t in tickets:
        print(f"{t['id']}  {t.get('status',''):<12} {t.get('priority',''):<3} "
              f"ch{t.get('chapter','-'):<3} {t.get('title','')}")
    if not tickets:
        print("(none)")


def cmd_show(args):
    ticket = find(load_all(), args.id)
    print(ticket["_path"].read_text(encoding="utf-8"))


def cmd_board(args):
    build_board(load_all())
    print(BOARD)


def cmd_recent(args):
    if not WORKLOG.exists():
        sys.exit("no worklog yet")
    print("\n".join(WORKLOG.read_text(encoding="utf-8").splitlines()[:args.n]))


def cmd_decide(args):
    text = DECISIONS.read_text(encoding="utf-8") if DECISIONS.exists() else \
        "# Decision register\n\nNewest first. A decision recorded here is not reopened " \
        "without a superseding entry.\n"
    highest = max([int(m) for m in re.findall(r"^### D-(\d+)", text, re.M)] or [0])
    did = f"D-{highest + 1:03d}"
    block = textwrap.dedent(f"""\
        ### {did} {args.title}

        - **Date:** {today()}
        - **Status:** {args.status}
        - **Context:** {args.context or 'To be written.'}
        - **Decision:** {args.what}
        - **Consequence:** {args.consequence or 'To be written.'}
        """)
    split_at = text.index("\n### ") if "\n### " in text else len(text)
    text = text[:split_at].rstrip("\n") + "\n\n" + block + text[split_at:]
    DECISIONS.write_text(text, encoding="utf-8")
    worklog_add(f"- `{now_hm()}` decision **{did}**: {args.title}")
    print(did)


def cmd_check(args):
    tickets = load_all()
    index = by_id(tickets)
    problems = []
    for t in tickets:
        tid = t["id"]
        if t.get("status") not in STATUSES:
            problems.append(f"{tid}: unknown status {t.get('status')!r}")
        if t.get("priority") not in PRIORITIES:
            problems.append(f"{tid}: unknown priority {t.get('priority')!r}")
        deps = t.get("depends_on") or []
        deps = deps if isinstance(deps, list) else [deps]
        for d in deps:
            if d not in index:
                problems.append(f"{tid}: depends on missing ticket {d}")
            elif t.get("status") == "done" and index[d].get("status") != "done":
                problems.append(f"{tid} is done but its dependency {d} is not")
        body = t["_body"]
        section = re.search(r"##\s*Acceptance criteria\n(.*?)(?=\n## |\Z)", body, re.S)
        if section:
            unchecked = len(re.findall(r"^\s*- \[ \]", section.group(1), re.M))
            if t.get("status") == "done" and unchecked:
                problems.append(f"{tid} is done with {unchecked} unchecked criteria")
        elif t.get("status") != "dropped":
            problems.append(f"{tid}: no acceptance criteria section")
    if problems:
        print("\n".join(problems))
        sys.exit(1)
    print(f"{len(tickets)} tickets, no problems")


def main():
    TICKETS.mkdir(parents=True, exist_ok=True)
    p = argparse.ArgumentParser(prog="wf", description=__doc__,
                                formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = p.add_subparsers(dest="cmd", required=True)

    n = sub.add_parser("new")
    n.add_argument("title")
    n.add_argument("-c", "--chapter")
    n.add_argument("-p", "--priority", default="P2", choices=PRIORITIES)
    n.add_argument("-s", "--status", default="backlog", choices=STATUSES)
    n.add_argument("-o", "--owner", default="claude")
    n.add_argument("-d", "--depends", nargs="*")
    n.add_argument("--tags", nargs="*")
    n.add_argument("-g", "--goal")
    n.set_defaults(func=cmd_new)

    s = sub.add_parser("status")
    s.add_argument("id")
    s.add_argument("new_status")
    s.add_argument("-m", "--message")
    s.set_defaults(func=cmd_status)

    lg = sub.add_parser("log")
    lg.add_argument("message")
    lg.add_argument("-t", "--ticket")
    lg.set_defaults(func=cmd_log)

    ls = sub.add_parser("list")
    ls.add_argument("--status", choices=STATUSES)
    ls.add_argument("--open", action="store_true")
    ls.add_argument("-c", "--chapter")
    ls.set_defaults(func=cmd_list)

    sh = sub.add_parser("show")
    sh.add_argument("id")
    sh.set_defaults(func=cmd_show)

    b = sub.add_parser("board")
    b.set_defaults(func=cmd_board)

    r = sub.add_parser("recent")
    r.add_argument("-n", type=int, default=40)
    r.set_defaults(func=cmd_recent)

    d = sub.add_parser("decide")
    d.add_argument("title")
    d.add_argument("-w", "--what", required=True)
    d.add_argument("--context")
    d.add_argument("--consequence")
    d.add_argument("--status", default="accepted")
    d.set_defaults(func=cmd_decide)

    c = sub.add_parser("check")
    c.set_defaults(func=cmd_check)

    args = p.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
