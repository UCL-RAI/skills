---
name: paper-search-protocol
description: Builds reproducible Robotics & AI search logs across papers, projects, datasets, benchmarks, and code. Use when the user asks for literature search, project search, survey source collection, related work discovery, or field onboarding.
---

# Paper Search Protocol

Use this skill to search broadly without losing provenance.

## Inputs

- Research question or topic.
- Desired output: source list, survey seed set, related work map, project/code scan, dataset/benchmark scan, or field onboarding.
- Scope constraints: venue families, time window, Robotics domain, AI method family, language, hardware/simulator, and available databases.
- Stopping budget: target number of sources, time budget, or confidence threshold.

If the user asks for "all papers", narrow the scope before searching. If the scope cannot be narrowed, split the search into query families and report coverage limits.

## Workflow

1. Define the search question, target communities, time window, and required source types.
2. Create query families, not one query. Include synonyms, method names, benchmark names, dataset names, robot/task terms, and negative controls.
3. Search by source tier:
   - primary papers: venue pages, arXiv, OpenReview, IEEE, ACM, PMLR;
   - projects and code: GitHub, official project pages, benchmark leaderboards;
   - datasets and simulators: dataset pages, benchmark docs, simulator docs;
   - citation graph: Semantic Scholar, Crossref, Google Scholar if available to the user.
4. Record exact queries, filters, dates, hit counts, and inclusion/exclusion decisions.
5. Deduplicate by title, DOI, arXiv ID, OpenReview forum, and project URL.
6. Label each included item with why it matters: foundational, recent SOTA, direct baseline, dataset/benchmark, negative result, survey, or implementation reference.
7. Hand selected papers to `paper-reading-card` and broader sets to `evidence-matrix-builder`.

For broad field onboarding or survey work, read `references/search-strategy.md` before finalizing the search plan.

## Search Log Format

```markdown
## Search question

## Scope
- Time window:
- Venue/source families:
- Inclusion criteria:
- Exclusion criteria:

## Query families
| Family | Query strings | Source | Filters | Date searched | Notes |
| --- | --- | --- | --- | --- | --- |

## Sources searched

## Included items
| Item | Type | Identifier/URL | Why included | Next action |
| --- | --- | --- | --- | --- |

## Excluded items
| Item | Reason | Source |
| --- | --- | --- |

## Gaps and follow-up queries
```

## Quality Gates

- Do not treat search results as exhaustive unless the searched sources, query families, and date are recorded.
- Do not include papers only because titles sound relevant; record the reason for inclusion.
- Do not collapse project pages, papers, datasets, and benchmark leaderboards into one undifferentiated source list.
- Do not infer venue, year, DOI, code availability, or benchmark status when the source does not state it.

## Validation

Check that another person can rerun the search from the log, recover the included sources, and understand why each item was kept or rejected.

## Completion

Done means the search log can be rerun by another person, every included item has a source URL or identifier, and every unresolved gap has a follow-up query or a clear statement that the source was unavailable.
