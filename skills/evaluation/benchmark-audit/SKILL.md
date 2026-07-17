---
name: benchmark-audit
description: Audits benchmark design, baselines, metrics, ablations, statistical reporting, leakage risk, and claim-result alignment for Robotics and AI papers. Use when the user asks whether experiments are convincing, fair, reproducible, or sufficient for paper claims.
---

# Benchmark Audit

Use this before polishing experimental claims or submitting a paper.

## Inputs

- Paper draft, experiment section, tables, plots, appendix, or result summary.
- Claimed contributions and target venue if known.
- Benchmark details: datasets, simulators, robot setups, tasks, metrics, splits, baselines, ablations, seeds, and compute.
- Optional artifacts: code, configs, logs, `evidence-matrix-builder` output, and prior papers.
- Desired depth: `quick`, `standard`, or `deep`; default to `quick` unless the user asks for a full experiment audit.

Read `references/benchmark-checks.md` for standard or deep audits, or when reviewing more than one table or benchmark. Skip it for quick triage unless benchmark validity is the main blocker.

## Workflow

For quick triage, prioritize the top rejection risks: unsupported main claim, unfair baseline, missing variance, weak ablation, leakage risk, or overbroad real-world/generalization wording.

1. Extract the paper's claims that depend on benchmark evidence.
2. Map each claim to the exact table, figure, metric, baseline, ablation, or qualitative result that supports it.
3. Check task and dataset fit: whether the benchmark measures the stated capability and whether the setup matches the paper's problem.
4. Check baseline fairness: implementation source, tuning budget, data access, architecture size, compute, and reporting symmetry.
5. Check metric validity: definition, direction, confidence intervals or variance, failure cases, and robotics-specific units or success criteria.
6. Check ablations and controls: remove each proposed component, isolate confounders, and test simple alternatives.
7. Check leakage and contamination risks: train/test splits, pretraining data, simulator overlap, prompt leakage, human demonstration reuse, and benchmark overfitting.
8. Classify each issue by severity and state the smallest evidence needed to repair it.

## Output

For quick triage:

```markdown
## Top Experiment Risks
| Risk | Evidence location | Why it matters | Smallest repair |
| --- | --- | --- | --- |

## Claims to Narrow Now
```

For standard or deep audits:

```markdown
## Benchmark Audit

## Claim-Result Map
| Claim | Evidence location | Support level | Missing evidence |
| --- | --- | --- | --- |

## Blocking Issues
| Issue | Evidence | Why it matters | Repair |
| --- | --- | --- | --- |

## Major Issues

## Minor Issues

## Required Additional Experiments
| Need | Minimum experiment | Expected decision value |
| --- | --- | --- |

## Claims to Narrow
```

## Rules

- Do not accept a benchmark because it is popular; check whether it tests the paper's claimed capability.
- Do not compare against weak, stale, or under-tuned baselines without labeling the limitation.
- Do not treat qualitative demos as benchmark evidence unless the claim is explicitly qualitative.
- Do not turn non-significant or high-variance results into strong superiority claims.
- Do not invent missing baselines, scores, confidence intervals, or implementation details.

## Validation

- In quick triage, the largest visible experiment risks are ranked and the unchecked scope is explicit.
- In standard or deep audits, every strong experimental claim maps to at least one concrete result.
- Every baseline criticism identifies the fairness dimension being violated.
- Every requested experiment has a decision value, not just "more experiments".
- Unsupported claims are narrowed or flagged instead of polished.

## Completion

Done means the chosen audit depth is explicit, weak or unfair comparisons are visible, and each reported experimental gap has a concrete repair path.
