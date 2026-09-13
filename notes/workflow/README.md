# How work is tracked in this repository

Read this file before starting any dissertation task. It takes two minutes and it prevents
the two failures that cost the most: redoing work that was already done, and reopening a
question the author already settled.

## The four artefacts

| File | What it holds | Who writes it |
| --- | --- | --- |
| `BOARD.md` | Every ticket, grouped by status. The current state of the thesis. | `wf.py`, generated |
| `tickets/T-NNN-*.md` | One unit of work: goal, acceptance criteria, evidence, log. | agent and author |
| `WORKLOG.md` | Append-only diary, newest first. What happened, when. | `wf.py` |
| `DECISIONS.md` | Decisions that must not be relitigated, with their reasons. | `wf.py decide` |

Three further files outside this directory carry standing context and are not part of the
tracker: `notes/dissertation-structure-v0.3.md` (the plan), `notes/known-issues-to-fix.md`
(the defect ledger for the source publications), and `notes/literature-map.md` (which
reference serves which section).

## The protocol

At the **start** of a session:

1. `notes/workflow/wf.py recent -n 50` shows what the last session did.
2. `notes/workflow/wf.py list --open` shows what is outstanding.
3. Read `DECISIONS.md` in full if the task touches structure, scope, or attribution.

While **working**:

4. Move the ticket yourself: `wf.py status T-012 in-progress -m "reason"`. The board and the
   worklog update together, so no separate bookkeeping step is needed.
5. Before drafting a section, record its core citekeys, the claim supported by each source,
   and the full-text and vault status in the writing ticket. Verify the source before writing
   the claim. A bibliography entry or literature-map row is a lead, not evidence.
6. Record anything a later session would otherwise have to rediscover:
   `wf.py log "biber warns about X; the cause is Y" -t T-012`.
7. A decision that changes the shape of the dissertation goes in `DECISIONS.md`, not in a
   ticket comment. Tickets are closed and forgotten; decisions are not.

At the **end** of a piece of work:

8. Tick the acceptance criteria in the ticket file, then `wf.py status T-012 review`.
   Only the author moves a ticket to `done`.
9. `wf.py check` must pass before the session ends.

## Statuses

`backlog` not yet scoped. `ready` scoped and unblocked. `in-progress` being worked on now.
`review` finished and awaiting the author. `blocked` waiting on an answer or an artefact
that the agent cannot obtain. `done` accepted by the author. `dropped` abandoned, with the
reason in the ticket log.

A ticket that is `blocked` names in its body exactly what would unblock it, and who can
supply it. Most blocked tickets in this repository wait on the author, because they concern
experimental facts that only he knows.

## Rules that hold for every ticket

- No chapter text is written before the ticket's evidence section names its sources.
- A writing ticket records which claim each core source supports and whether its full text was
  inspected. Metadata verification alone is insufficient.
- Every citation added to a chapter passes `references/refcheck.py audit` before the ticket
  leaves `in-progress`. See `references/README.md` for what that checks and why.
- `latexmk thesis.tex` must run clean, and the log must be read, before a drafting ticket
  reaches `review`. A build that was not run is a build that failed.
- Numbers come from the files in `publications/`, never from memory or from an earlier
  summary of those files.

## Command reference

```
wf.py board                         rebuild BOARD.md
wf.py new "title" -c 4 -p P1 -g "goal"
wf.py list --open [-c 4]
wf.py show T-012
wf.py status T-012 review -m "drafted, compiles clean"
wf.py log "message" -t T-012
wf.py decide "title" -w "the decision" --context "..." --consequence "..."
wf.py recent -n 50
wf.py check
```
