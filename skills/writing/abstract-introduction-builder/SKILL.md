---
name: abstract-introduction-builder
description: Builds or revises paper abstracts and introductions from verified problem, gap, method, evidence, contribution, and limitation material. Use when the user needs a conference-paper abstract, introduction, contribution paragraph, or opening narrative without overstating evidence.
---

# Abstract Introduction Builder

Use this when the paper has enough substance to state a problem, gap, approach, and evidence.

## Inputs

- Paper idea, contribution list, outline, draft abstract, introduction, or claim-evidence map.
- Verified results, baselines, limitations, related-work positioning, and target venue if known.
- Desired length constraints, such as abstract word limit or page budget.

Read `references/abstract-intro-patterns.md` before writing a full abstract or introduction.

## Workflow

1. Extract the problem, practical or scientific stakes, gap, method, evidence, and contribution.
2. Check which elements are verified, speculative, or missing.
3. Build an abstract skeleton before prose: context, gap, approach, evidence, contribution, and limitation boundary.
4. Build an introduction skeleton: motivation, gap, why hard, core idea, evidence preview, contributions, and scope.
5. Draft only claims supported by available evidence; mark missing results or citations instead of inventing them.
6. Align wording with `related-work-positioning`, `benchmark-audit`, and `limitations-failure-case-auditor` outputs when available.
7. Provide a clean draft plus a claim-risk table.

## Output

```markdown
## Abstract / Introduction Draft

## Claim-Risk Table
| Sentence or claim | Evidence | Risk | Fix |
| --- | --- | --- | --- |

## Missing Inputs

## Optional Stronger Version After Evidence
```

## Rules

- Do not write a confident abstract before evidence status is known.
- Do not use "first", "novel", "significant", or "state-of-the-art" unless source and benchmark checks support it.
- Do not make the introduction broader than the paper can evaluate.
- Do not bury the actual contribution behind generic motivation.
- Do not add citations, numbers, or benchmarks from memory.

## Validation

- The abstract states what was done and what was found without unsupported inflation.
- The introduction explains why the problem is hard and why this paper is needed.
- Contributions match the method, experiments, and limitations.
- Missing evidence is visible rather than smoothed over.

## Completion

Done means the user has a draft or skeleton whose claims, evidence needs, and paper scope are explicit.
