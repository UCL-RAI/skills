---
name: limitations-failure-case-auditor
description: Audits limitations, assumptions, failure cases, negative results, boundary conditions, and ethical or deployment risks in Robotics and AI papers. Use when the user needs a limitations section, failure analysis, responsible research check, or pre-review overclaim audit.
---

# Limitations Failure Case Auditor

Use this before final paper review, rebuttal, or camera-ready submission.

## Inputs

- Draft paper, abstract, introduction, experiments, conclusion, or limitations section.
- Benchmark results, failed runs, qualitative examples, logs, safety notes, and deployment constraints.
- Target venue or responsible research checklist if known.

Read `references/limitations-checks.md` when auditing a full paper or claims with deployment risk.

## Workflow

1. Extract claims that imply generality, safety, robustness, deployment, fairness, or real-world readiness.
2. Identify assumptions: data, robot platform, sensors, simulator, tasks, metrics, compute, user population, and operating conditions.
3. Map observed failures and missing evaluations to the claims they weaken.
4. Separate limitations from excuses: a limitation must tell readers how to interpret the result.
5. Draft limitation and failure-case language that is specific, honest, and not self-sabotaging.
6. Recommend minimal additional analysis when a limitation can be quantified.
7. Flag claims that must be narrowed before review.

## Output

```markdown
## Limitations and Failure Case Audit

## Assumption Map
| Claim | Assumption | Evidence | Risk |
| --- | --- | --- | --- |

## Failure Cases
| Failure | Where observed | Interpretation | Paper action |
| --- | --- | --- | --- |

## Suggested Limitations Text

## Claims to Narrow

## Additional Analysis Needed
```

## Rules

- Do not hide major limitations in vague future-work language.
- Do not invent failure cases that were not observed or plausibly implied by evidence.
- Do not over-apologize for normal scope boundaries.
- Do not make safety, robustness, or deployment claims without matching evaluation.
- Do not treat limitations as optional if the venue explicitly asks for them.

## Validation

- Each limitation connects to a claim, assumption, result, or missing evaluation.
- Failure cases explain what readers should infer.
- Strong claims are narrowed when evidence is absent.
- Responsible research concerns are checked when humans, robots, safety, or societal deployment are in scope.

## Completion

Done means the paper's scope boundaries are explicit, failure cases are interpretable, and overclaims are either supported or narrowed.
