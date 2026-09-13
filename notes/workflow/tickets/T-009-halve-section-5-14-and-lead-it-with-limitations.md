---
id: T-009
title: Halve Section 5.14 and lead it with limitations
status: review
priority: P1
chapter: 5
owner: claude
depends_on: []
blocks: []
tags: []
created: 2026-09-13
updated: 2026-09-13
---

## Goal

Remove the CICMalDroid binary-row consistency paragraph and cut Section 5.14 to about half, keeping limitations and a very short threats-to-validity paragraph

## Why it matters

The author asked on 13 September 2026 for the CICMalDroid binary HGANN-Mal row analysis to be
removed and for Section 5.14 to be halved, with limitations as the main content and threats to
validity removed or kept very short.

## Acceptance criteria

- [x] The CICMalDroid binary-row paragraph and the paragraph that only supported it are removed.
- [x] Section 5.14 is at most about half its former length (1,857 words before, 804 after).
- [x] Limitation paragraphs lead; threats to validity form one short closing paragraph.
- [x] Every forward reference to Section 5.14 from Sections 5.1 to 5.12 is still satisfied.
- [x] D-059 recorded; source record `sec-5.10-5.15.md` marks the removed statements.
- [x] Strict audit passes; thesis compiles with identical PDFs; log read.
