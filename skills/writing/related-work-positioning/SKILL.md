---
name: related-work-positioning
description: Positions a paper against prior work by building source-grounded clusters, contribution boundaries, novelty claims, and comparison language. Use when writing related work, introduction positioning, survey paragraphs, or responses about novelty and differentiation.
---

# Related Work Positioning

Use this after at least a minimal source set exists.

## Inputs

- Target paper claim, abstract, introduction, related-work draft, or contribution list.
- Verified sources, reading cards, evidence matrix, search log, or citation audit.
- Target venue and intended scope if known.

Read `references/positioning-checks.md` before drafting or rewriting a related-work section.

## Workflow

1. Identify the paper's exact contribution claims and what must be distinguished from prior work.
2. Group prior work into method, task, benchmark, dataset, system, theory, or application clusters.
3. For each cluster, state what prior work already solves and what remains different.
4. Map every novelty or gap claim to verified sources.
5. Draft positioning language that is specific, fair, and non-dismissive.
6. Flag missing must-cite papers and claims that require citation-integrity audit.
7. Produce a related-work outline or rewrite with claim boundaries.

## Output

```markdown
## Related Work Positioning

## Prior-Work Clusters
| Cluster | Representative sources | What they solve | Boundary for this paper |
| --- | --- | --- | --- |

## Novelty Claim Map
| Claim | Supporting sources | Risk | Safer wording |
| --- | --- | --- | --- |

## Draft / Rewrite

## Missing Sources
```

## Rules

- Do not claim "first", "novel", or "unlike prior work" without source coverage.
- Do not attack prior work with vague weakness language.
- Do not cite papers that were not checked for the stated claim.
- Do not turn a literature survey into a chronological list unless chronology is the argument.
- Do not hide overlap with prior work; define the boundary precisely.

## Validation

- Every cluster has representative sources or is marked as missing coverage.
- Every differentiation claim has a cited basis or is narrowed.
- The draft explains why the current paper is needed after prior work.
- Missing citations and weak novelty claims are explicit.

## Completion

Done means the related-work position is fair, source-grounded, and strong enough to guide writing, rebuttal, or further search.
