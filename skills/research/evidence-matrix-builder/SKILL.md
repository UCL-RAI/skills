---
name: evidence-matrix-builder
description: Builds comparison matrices, taxonomies, and gap maps from paper cards, projects, datasets, or benchmark notes. Use when the user asks to synthesize a literature base, write a survey, compare methods, or find research gaps.
---

# Evidence Matrix Builder

Use this after several paper or project cards exist.

## Inputs

- Reading cards, project notes, benchmark notes, dataset docs, or a source list with identifiers.
- Research question and intended use: survey section, related work, method comparison, project gap analysis, or reviewer-risk analysis.
- Minimum comparison unit: paper, method, dataset, benchmark, robot task, or project.

If fewer than three comparable sources exist, produce a coverage note first and avoid overclaiming taxonomy.

## Workflow

1. Inventory available cards and mark missing coverage.
2. Choose matrix axes that match the research question.
3. Fill cells with source-grounded facts, not generic summaries.
4. Separate evidence from interpretation.
5. Derive taxonomy only after the matrix is populated.
6. Mark gaps using stable tags such as `missing-evaluation`, `weak-baseline`, `unrealistic-assumption`, `narrow-benchmark`, `untested-deployment`, or `unclear-reproducibility`.
7. Produce synthesis only after the rows are traceable.

Read `references/matrix-design.md` when choosing axes, gap tags, or survey synthesis structure.

## Default Columns

```csv
id,title,year,venue,problem,method_family,robot_or_domain,dataset_or_simulator,baselines,metrics,main_result,limitations,code_or_data,gap_tags,notes
```

## Survey Output

When asked for survey synthesis, produce:

- taxonomy;
- timeline or method evolution;
- comparison matrix;
- unresolved gaps;
- promising directions;
- claims that require more evidence.

## Quality Gates

- Do not compare methods across incompatible tasks or metrics without labeling the mismatch.
- Do not infer "best" from one benchmark unless the benchmark and baselines are aligned.
- Do not turn absent evidence into negative evidence; distinguish `not reported` from `reported weak`.
- Do not derive a taxonomy before the matrix has enough rows to justify the categories.

## Validation

- Every row traces to a reading card or source URL.
- Every non-empty result cell states the metric, task, and comparison target when available.
- Every gap tag ties to a specific missing or weak evidence pattern.
- Every synthesis claim can be traced back to one or more matrix rows.

## Completion

Done means every row traces back to a reading card or source, and every claimed gap is tied to a specific missing or weak evidence pattern.
