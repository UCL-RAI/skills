# Forward Test: Paper Search Protocol

## Skill

`paper-search-protocol`

## Prompt

Use `paper-search-protocol` to create a reproducible search log for papers, datasets, projects, and code related to tactile in-hand manipulation for robot learning. Scope to 2020-present unless there is a strong reason to include older foundational work. Do not summarize papers.

## Expected Artifact Checklist

- Search question is explicitly stated.
- Scope includes time window, source families, inclusion criteria, and exclusion criteria.
- At least four query families are listed.
- Exact query strings, source, filters, and search date are recorded or marked pending if no live search is possible.
- Included items require a verified identifier or URL.
- Excluded items include reasons.
- Follow-up gaps are listed.
- No titles, venues, DOI, code links, or benchmark status are invented.

## Pass Conditions

- The output is a rerunnable search log, not a prose literature summary.
- The agent separates papers, projects/code, datasets/simulators, and citation-graph search.
- Missing live-search access is handled by a clear search plan rather than fabricated results.

## Fail Conditions

- The output lists papers without source URLs or identifiers.
- The agent claims completeness without recording query/source coverage.
- The output summarizes papers instead of producing a search log.
