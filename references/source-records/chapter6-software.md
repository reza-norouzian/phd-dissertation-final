# Chapter 6 software references

Verified and full source read on 10 September 2026 for writing ticket T-003.
These are versioned software resources, so the reference-vault status is `no-pdf`.
They support an inspection of published source code, not a reconstruction of the
historical experiments in SPARTA D7.6 Table 2. No downloaded code was executed.

## `norouzian2021adversarialbenchmark`

- Title: *Adversarial Machine Learning Benchmark Tool*, exactly as headed by the
  repository README.
- Author: Mohammad Reza Norouzian, verified from the primary commit record.
- Revision: `2fac62b947ed77a509f397a9cc316937291395f5`.
- Commit date: `2021-11-08T15:00:24Z` (committer date). The public GitHub repository
  was created on `2021-11-09T11:26:35Z`; repository creation and commit dates are
  different metadata fields.
- Primary commit record:
  https://api.github.com/repos/reza-norouzian/Adversarial-Benchmark-Tool/commits/2fac62b947ed77a509f397a9cc316937291395f5
- Permanent source tree:
  https://github.com/reza-norouzian/Adversarial-Benchmark-Tool/tree/2fac62b947ed77a509f397a9cc316937291395f5

Full `README.md`, `main.py` and `requirements.txt` were read. The README describes
five modules and expects pretrained model weights. The dependency file pins
`foolbox==3.3.1`. In `main.py`, line 18 defines `FIXED_EPSILON = 8. / 255`;
lines 134–135 receive separate raw and clipped outputs but pass the raw tensor
to the dataset accuracy function. The returned attack-success indicator is not
used by that scoring line. Lines 40–41 and 131–132 replace labels with a supplied
target label, so targeted label agreement requires interpretation distinct from
true-label accuracy.

The code demonstrates a possible budget-validation problem. It does not prove
that a particular historical attack exceeded its budget, and no run manifest or
result provenance connects this revision to D7.6 Table 2. This repository is
separate from the contest toolkit cited by `norouzian2021safairtoolkit`.

## `foolbox2021api`

- Resource: *Foolbox: Attack Base Classes, Version 3.3.1*. This is a descriptive
  title for the software component `foolbox/attacks/base.py`, not a paper title.
- Package author: Jonas Rauber, exactly as declared in version 3.3.1 `setup.py`.
- Release: Version 3.3.1, published `2021-02-23T07:09:34Z`.
- Tag: `v3.3.1`, resolved to commit
  `92af8673ee957e5af1f9ad5f3abb474c63f93397`.
- Official release record:
  https://api.github.com/repos/bethgelab/foolbox/releases/tags/v3.3.1
- Official tag record:
  https://api.github.com/repos/bethgelab/foolbox/git/ref/tags/v3.3.1
- Versioned source:
  https://github.com/bethgelab/foolbox/blob/v3.3.1/foolbox/attacks/base.py

Full `foolbox/attacks/base.py`, `README.rst` and `setup.py` were read. In
`MinimizationAttack.__call__`, line 410 computes the raw candidate. Lines
414–419 clip it to a finite requested distance budget and test the clipped
candidate. Line 434 returns the raw candidate, the clipped candidate and the
clipped candidate's success indicator separately for scalar epsilon. The
raw result need not satisfy that budget. `FixedEpsilonAttack.__call__` also
clips its result (line 284), so callers should not assume the raw return
has been validated. The distance is attack-specific; a fixed numerical epsilon
alone does not establish a shared norm or shared physical perturbation scale.

## Source checksums

Raw files were retrieved over HTTPS from `raw.githubusercontent.com` using the
revision or tag above. SHA-256 hashes apply to the downloaded bytes. Temporary
inspection copies reside in `/tmp/ch6-reference-gate/`; retrieval URLs and hashes
below allow the record to remain checkable when those temporary files expire.

| Inspection filename | Original path | SHA-256 |
| --- | --- | --- |
| `benchmark-main.py.txt` | `main.py` | `af1b43c97c5d4df4eb0f10f54ba1c25f2fdfcbe0565fe2121478047770c4caf8` |
| `benchmark-README.md` | `README.md` | `024b4effd8d151a5d31fb9a811d40b544660aa922d4d8950f805494f7d812550` |
| `benchmark-requirements.txt` | `requirements.txt` | `16c29021caeb74f79d5dfa340f16cb280814cc479e7c90d5db4a710cca732661` |
| `foolbox-base.py.txt` | `foolbox/attacks/base.py` | `867c37ecdec730147da637b427d566d95bfb8bc431d1fee7d49330d9b2b17505` |
| `foolbox-README.rst` | `README.rst` | `0ec50adfe2ad3678d3921b7c498e56a0ef0f99ecb6c032a1ab49a28ee7d48c7b` |
| `foolbox-setup.py.txt` | `setup.py` | `0ad3c17a2f0be8a8921c1c66f8c0d4060ed412bfe5b705afcbf9fec9e421bfe0` |

Benchmark raw URL prefix:
`https://raw.githubusercontent.com/reza-norouzian/Adversarial-Benchmark-Tool/2fac62b947ed77a509f397a9cc316937291395f5/`

Foolbox raw URL prefix:
`https://raw.githubusercontent.com/bethgelab/foolbox/v3.3.1/`

## Reference gate

The two bibliography entries preserve the existing contest-toolkit and Foolbox
paper entries. Each new key is separately registered in `references/MANIFEST.tsv`
with status `no-pdf`, primary source URL, inspection date and this record's path.
A scratch LaTeX citation audit is performed before the chapter uses these keys.

## Typesetting follow-up, 11 September 2026

The bibliography uses the twelve-character revision URL ending in
`/tree/2fac62b947ed` to avoid an overfull line. The primary GitHub page was
opened and resolved to the full revision recorded above. The full SHA remains
in this record and the manifest. The Foolbox source-file note uses
`\nolinkurl` so that its path can break at separators.
