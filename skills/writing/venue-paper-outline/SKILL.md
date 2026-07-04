---
name: venue-paper-outline
description: Plans Robotics & AI conference paper structure for ICRA, RSS, CoRL, ICML, ICLR, and NeurIPS style submissions. Use when the user asks for an outline, paper skeleton, section plan, contribution framing, or venue-aware writing strategy.
---

# Venue Paper Outline

Use this before drafting substantial paper prose.

## Inputs

- Target venue family if known.
- Project thesis, method sketch, experiments, results, figures, and limitations if available.
- Existing outline or draft, or a request to create one from notes.

If the target venue is unknown, state a default venue family assumption and avoid venue-specific claims that may be wrong.

## Workflow

1. Identify target venue family: Robotics, ML, robot learning, or systems-adjacent.
2. Extract the paper contract:
   - problem;
   - contribution;
   - method;
   - evidence;
   - baselines;
   - limitations.
3. Build a claim-evidence map before section prose.
4. Choose section allocation and argument order.
5. Draft outline bullets before prose.
6. Flag missing evidence instead of filling it with style.
7. Read `references/venue-rubric.md` when the user names a target venue or asks for venue fit.

## Claim-Evidence Map

```markdown
| Contribution claim | Evidence location | Required baseline/metric | Missing evidence |
| --- | --- | --- | --- |
```

## Default Section Contract

```markdown
## Title
## Abstract
## Introduction
## Related Work
## Method
## Experiments
## Results and Analysis
## Limitations
## Conclusion
```

## Outline Rules

- Keep the introduction as an argument, not a topic tour.
- Make each contribution falsifiable and tied to a result, theorem, ablation, or system evidence.
- Put implementation details where they support reproducibility, not where they interrupt the argument.
- Avoid writing related work as a list of summaries; use it to position the gap and baselines.
- Do not use style to hide missing experiments, weak baselines, or unclear limitations.

## Validation

- Every contribution has a planned evidence location.
- Every experiment has a stated task, metric, and baseline.
- Every figure or table has a section role and claim.
- Limitations are visible before the conclusion.
- Venue-specific advice is labeled as an orientation, not official instructions.

## Completion

Done means each claimed contribution has a planned evidence location, and each experiment has a stated baseline and metric.
