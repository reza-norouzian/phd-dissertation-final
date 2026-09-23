# Chapter 2 source records

Re-established on 20 September 2026 under T-025 after the author approved the full Chapter 2
review. The earlier section records referenced by the LaTeX comments were absent from the
available repository history. This index records the current evidence; it does not reproduce
those missing records.

## Current records

The ticket system was removed on 23 September 2026. Tickets T-023 and T-025 remain in git
history (for example, `git show d3288fa:notes/workflow/tickets/`).

- **Scientific and readability revision:**
  T-025
  contains the pre-drafting claim-to-source table for all seven sections, source versions and
  verification limits. It also records the scope of the read-only review and the subsequent
  author approval.
- **Shared performance measures:**
  T-023
  records the metric inventory, source passages and checks for the 18 equations retained in
  the revision.
- **Physical source inventory:** [reference manifest](../../references/MANIFEST.tsv).
  Existing entries remain discovery/availability records; the writing tickets state which
  claims the inspected passages support.

## Version and interpretation safeguards

- `pierazzi2020intriguing` uses arXiv:1911.02142v2, dated 16 March 2020, with the four authors
  of the cited S&P paper. The previously filed six-author 2024 extension is preserved in the
  T-025 scratch evidence, not used as the canonical copy for the 2020 citation.
- `wang2024graphs` is **Hypergraph Projection and Its Remediation**, matching the paper and
  primary arXiv record. Its projection is an unweighted graph on the original vertex set.
- Fang et al.'s Table 2 has higher reported GAT means than the non-attentive baselines on
  some node-classification datasets. The contradictory categorical prose is not repeated.
- PScout's count of over 75 permissions is not a count of undocumented permission mappings.
- Wolsing et al. reviewed 70 publications; their empirical comparison did not rerun all 70.
- Maali et al. evaluated device identification. Its transfer results are identified as
  evidence about that task, not relabelled as anomaly-detection results.

The revision's metadata responses, source extractions and preservation checks are in
`tmp/background-revision-2026-09-20/`. The primary PDFs remain in the reference vault.
