---
name: paper-red-team-review
description: Performs harsh but evidence-grounded review of Robotics & AI papers across factual accuracy, logic, novelty, experiments, citations, figures, writing, and reviewer risk. Use when the user asks for ruthless proofreading, red-team review, paper critique, or pre-submission audit.
---

# Paper Red-Team Review

Be blunt, but every criticism must be specific and defensible.

## Inputs

- Full paper, section, abstract, outline, figure, table, or rebuttal draft.
- Target venue family and review goal if known.
- Supporting artifacts when available: search log, reading cards, evidence matrix, citation audit, figure plan, experiment results.

If the user asks for a full-paper review, read `references/review-dimensions.md` before issuing the final review.

## Workflow

1. Identify the review mode: passage review, full-paper red team, experiment audit, citation/figure-focused review, or pre-submission gate.
2. Extract the paper's claimed contributions and evidence.
3. Attack the strongest rejection risks first: novelty, evidence, baselines, reproducibility, citations, figures, and clarity.
4. Assign severity using the scale below.
5. Provide concrete repair paths. If repair requires new experiments or sources, say so.

## Review Dimensions

For a short passage, still check:

- factual accuracy;
- claim-evidence match;
- coherence;
- scientific tone;
- grammar and spelling;
- figure/table references if present.

## Severity

Use:

- `blocking`: likely rejection or serious scientific error;
- `major`: weakens the paper materially;
- `minor`: local clarity or presentation problem;
- `nit`: small polish issue.

## Output

Lead with findings, not praise.

```markdown
## Blocking
| Issue | Evidence | Why it matters | Repair path |
| --- | --- | --- | --- |

## Major
| Issue | Evidence | Why it matters | Repair path |
| --- | --- | --- | --- |

## Minor

## Nits

## Rewrite Suggestions

## Residual Risk
```

## Rules

- Do not rewrite away scientific uncertainty.
- Do not accept unsupported novelty claims.
- Do not let fluent prose hide weak evidence.
- Do not mark something wrong without explaining the standard it violates.
- Do not recommend cosmetic rewrites before resolving blocking scientific issues.

## Validation

- Every `blocking` and `major` issue cites a location, claim, figure/table, experiment, or missing source.
- Every criticism explains the violated standard.
- Every suggested rewrite preserves scientific uncertainty.
- Residual risks separate "not checked" from "checked and failed".

## Completion

Done means every blocking and major issue has a concrete repair path or a clear statement that new evidence is needed.
