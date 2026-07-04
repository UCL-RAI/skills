# Paper Search Protocol Example

## User Prompt

> Build a reproducible search log for recent Robotics papers on tactile in-hand manipulation. I care about methods, datasets, simulators, and available code. Do not summarize papers yet.

## Expected Skill Behavior

The agent should use `paper-search-protocol`, narrow the scope before searching, and produce a rerunnable search log.

## Example Artifact Shape

```markdown
## Search question

What recent Robotics work studies tactile in-hand manipulation, and which papers/projects/datasets are relevant for methods, benchmarks, simulators, and code reuse?

## Scope
- Time window: 2020-present unless the user changes it
- Venue/source families: ICRA, RSS, CoRL, RA-L, arXiv, OpenReview when relevant, official project pages, dataset pages, GitHub
- Inclusion criteria: tactile sensing + dexterous or in-hand manipulation; source has traceable paper/project/dataset identity
- Exclusion criteria: generic grasping without tactile feedback; untraceable demos; secondary summaries when primary source is available

## Query families
| Family | Query strings | Source | Filters | Date searched | Notes |
| --- | --- | --- | --- | --- | --- |
| Method terms | "tactile in-hand manipulation robot learning" | <source> | 2020-present | <date> | Seed query |
| Robotics terms | "dexterous manipulation tactile sensor robot" | <source> | 2020-present | <date> | Platform/task query |
| Dataset/code terms | "tactile manipulation dataset code" | <source> | none | <date> | Dataset/project query |

## Included items
| Item | Type | Identifier/URL | Why included | Next action |
| --- | --- | --- | --- | --- |
| <verified paper title> | paper | <verified source URL> | Directly studies tactile in-hand manipulation | Read with `paper-reading-card` |
| <verified dataset/project> | dataset/project | <verified source URL> | Provides reusable benchmark or code | Add to matrix |

## Excluded items
| Item | Reason | Source |
| --- | --- | --- |
| <item> | Does not use tactile feedback | <source URL> |

## Gaps and follow-up queries
- Check citation graph for recent baselines.
- Search official project pages for code and dataset links.
```

## Quality Checks

- Exact query strings and dates are recorded.
- Included items have verified identifiers or URLs.
- No paper title, venue, code link, or benchmark status is invented.
