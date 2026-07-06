---
name: knowledge-base-onboarding
description: Onboards a new Robotics or AI research area, project folder, or lab knowledge base into a structured source inventory, concept map, artifact map, and next-action plan. Use when the user starts a new area, inherits notes/code/papers, or needs a reusable research memory structure.
---

# Knowledge Base Onboarding

Use this before deep synthesis when the user has scattered papers, notes, code, links, or project folders.

## Inputs

- Research topic, project folder, paper list, notes directory, Zotero/BibTeX export, repository, or dataset links.
- User goal: field onboarding, project takeover, survey, paper writing, experiment reproduction, or code extension.
- Constraints: time budget, venue, course requirement, available tools, and private data boundaries.

Read `references/onboarding-map.md` when building a multi-source onboarding artifact.

## Workflow

1. Identify the user's immediate decision: what they need to understand, write, build, or debug.
2. Inventory available sources without assuming they are complete or trustworthy.
3. Classify sources into papers, code, datasets, experiments, notes, figures, decisions, and open questions.
4. Build a concept map: key terms, methods, benchmarks, claims, and recurring failure modes.
5. Build an artifact map: where evidence lives and what is missing.
6. Mark provenance and trust level for each source.
7. Route follow-up work to `paper-search-protocol`, `paper-reading-card`, `evidence-matrix-builder`, `related-work-positioning`, or coding skills.

## Output

```markdown
## Knowledge Base Onboarding Map

## Source Inventory
| Source | Type | Location | Trust | Next action |
| --- | --- | --- | --- | --- |

## Concept Map

## Artifact Map

## Missing Context

## Recommended Next Skills
```

## Rules

- Do not summarize a source as read if only its title, README, or abstract was inspected.
- Do not mix verified facts with the user's hypotheses.
- Do not copy private local paths into public artifacts.
- Do not build a taxonomy before the source inventory is explicit.
- Do not treat a knowledge base as complete without naming coverage gaps.

## Validation

- Every source has type, location, and trust status.
- The concept map separates definitions, methods, benchmarks, and claims.
- Missing sources and stale notes are visible.
- The next action is a concrete skill route, not a vague "learn more".

## Completion

Done means the user has a navigable map of what exists, what is reliable, what is missing, and which skill should run next.
