# Onboarding Map

Use this reference to structure a research knowledge base.

## Source Patterns

- FAIR principles emphasize that data and metadata should be findable, accessible, interoperable, and reusable: https://www.go-fair.org/fair-principles/
- The Turing Way emphasizes reproducible research practices, project organization, documentation, and reusable research artifacts: https://the-turing-way.netlify.app/
- ACM Artifact Review and Badging provides useful language for artifact availability, functionality, reusability, and result support: https://www.acm.org/publications/policies/artifact-review-and-badging-current

## Source Types

| Type | Examples | Trust question |
| --- | --- | --- |
| Paper | PDF, arXiv page, DOI, proceedings page | Was the actual paper read or only metadata? |
| Code | Git repo, scripts, notebooks, ROS package | Is the version tied to a result or paper? |
| Dataset | download page, split files, preprocessing scripts | Are version, license, and splits clear? |
| Experiment | logs, configs, checkpoints, tracker runs | Can a claim be traced to this run? |
| Note | lab notes, meeting notes, chat exports | Is it observation, decision, or speculation? |
| Figure | plots, diagrams, source files | Does it map to a claim and data source? |

## Trust Labels

- `verified`: source was opened or inspected and supports the stated fact.
- `metadata-only`: title, abstract, README, or citation metadata only.
- `user-claim`: supplied by the user but not independently checked.
- `stale`: may be outdated because code, data, or venue rules changed.
- `unknown`: source exists but has not been inspected.

## Minimum Onboarding Artifact

```markdown
## Goal

## Source Inventory

## Key Terms

## Methods / Systems

## Benchmarks / Datasets

## Known Claims

## Open Questions

## Next Actions
```
