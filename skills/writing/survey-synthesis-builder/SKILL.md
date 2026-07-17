---
name: survey-synthesis-builder
description: Builds a source-grounded Robotics or AI survey from verified reading cards, search logs, evidence matrices, and bibliography records. Use when defining a survey thesis or taxonomy, synthesizing literature across method families, designing section logic and comparison artifacts, revising an existing survey, or drafting survey prose without forcing an empirical-paper structure.
---

# Survey Synthesis Builder

Turn a verified literature base into an argument about a field. Do not produce
an annotated bibliography or impose a Method/Experiments template.

Read `references/survey-contract.md` before a `standard` or `deep` synthesis.

## Inputs

- Survey question, intended audience, scope boundary, date cutoff, and target
  format or venue when known.
- Reproducible search log and inclusion/exclusion criteria.
- Verified reading cards and bibliography records.
- Evidence matrix with traceable rows and explicit missing coverage.
- Optional taxonomy notes, competing surveys, existing outline, tables,
  figures, or draft.

If the evidence base is thin or unverified, produce a coverage gate instead of
drafting conclusions.

## Workflow

1. Validate source trust, search coverage, time cutoff, and inclusion scope.
   Distinguish full-text evidence from metadata-only sources.
2. Define a synthesis contract: reader, central question, one survey thesis,
   promised coverage, excluded territory, and claims the evidence cannot make.
3. Generate at least two plausible organizing structures when taxonomy is not
   locked. Compare their explanatory value, coverage balance, overlap, and
   stability under new papers before selecting one.
4. Build taxonomy categories from evidence-matrix patterns. Define membership,
   edge cases, multi-label handling, and category limitations.
5. Build a claim-evidence map for field evolution, agreements, disagreements,
   trade-offs, benchmark limitations, and open problems. Preserve conflicting
   evidence rather than averaging it away.
6. Assign each section one question, synthesis claim, evidence set, comparison
   artifact, and transition. Remove sections that only list papers.
7. Plan tables and figures that expose comparison structure, coverage, or
   evolution. Do not duplicate prose in visual form.
8. Draft in dependency order: taxonomy and technical synthesis first, then
   evaluation/gaps, introduction, conclusion, and abstract. Use supplied
   citation keys and visible missing-evidence markers.
9. Audit coverage balance, repeated paper descriptions, unsupported trends,
   taxonomy circularity, recency bias, and confusion between absence of
   reporting and negative evidence.
10. End with bounded open problems derived from evidence gaps, not generic
    future-work language.

## Depth

- `quick`: resolve one taxonomy, claim thread, or section synthesis problem.
- `standard`: produce the synthesis contract, taxonomy, claim-evidence map,
  section contracts, and focused draft.
- `deep`: produce or revise the full survey and run coverage, structure, and
  citation-risk checks.

Default to `standard`. Use `deep` only after the source base is stable enough
that full-draft work will not be discarded immediately.

## Outputs

```text
survey/
|-- synthesis-contract.md
|-- taxonomy.md
|-- claim-evidence-map.md
|-- section-contracts.md
`-- survey-draft.md          # or user-supplied LaTeX structure
```

In `quick` mode, update only the requested artifact.

## Rules

- Do not fabricate papers, citations, bibliographic fields, historical trends,
  benchmark facts, or category membership.
- Do not call an uncovered combination a research gap without checking whether
  it lies inside the search and inclusion scope.
- Do not treat `not reported` as `shown ineffective`.
- Do not count citations or papers as evidence of scientific quality.
- Do not make taxonomy categories mutually exclusive unless the evidence and
  definitions justify that constraint.
- Do not reuse claims from an abandoned draft until they trace to verified
  sources.
- Keep author proposals visibly separate from surveyed findings.

## Validation

- Every synthesis claim traces to evidence-matrix rows and reading cards.
- Every taxonomy category has a definition, membership rule, evidence, and
  known edge cases.
- Section transitions advance one central thesis rather than chronology alone.
- Competing or negative evidence is represented fairly.
- Open problems are tied to demonstrated limitations or coverage gaps.
- Citation-bearing prose uses verified sources or explicit markers.

## Completion

Done means the survey has a defensible synthesis contract, evidence-derived
organization, traceable claims, balanced coverage, and visible uncertainty.
