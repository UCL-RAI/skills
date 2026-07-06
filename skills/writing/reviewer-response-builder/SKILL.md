---
name: reviewer-response-builder
description: Builds evidence-grounded, point-by-point reviewer responses and rebuttal plans for Robotics and AI papers. Use when the user has reviews, meta-review, AC comments, or rebuttal constraints and needs a concise, non-defensive response strategy.
---

# Reviewer Response Builder

Use this after reviews arrive and before editing the manuscript or rebuttal.

## Inputs

- Reviewer comments, scores, confidence, meta-review, AC comments, or decision letter.
- Current paper draft and any allowed rebuttal format, word limit, deadline, and anonymity rule.
- Evidence artifacts: experiments, citations, appendix material, figures, logs, and planned revisions.

Read `references/response-patterns.md` before drafting a full response or revision plan.

## Workflow

1. Parse every reviewer point into an issue ledger; split bundled comments into separate actionable items.
2. Classify each issue: misunderstanding, missing evidence, valid weakness, writing clarity, citation gap, experiment gap, or out-of-scope request.
3. Rank response priority by decision impact, reviewer confidence, and whether the issue affects the main claim.
4. Choose a response action: clarify, concede and fix, provide existing evidence, add experiment, narrow claim, or respectfully decline with reason.
5. Draft concise point-by-point responses with location references and concrete manuscript changes.
6. Flag any promise that cannot be completed before camera-ready or revision.
7. End with a response-to-action map for the paper edit.

## Output

```markdown
## Reviewer Response Plan

## Issue Ledger
| Reviewer | Comment | Classification | Priority | Response action |
| --- | --- | --- | --- | --- |

## Draft Responses

## Promised Manuscript Changes
| Change | Paper location | Evidence needed | Risk |
| --- | --- | --- | --- |

## Do Not Promise
```

## Rules

- Do not argue tone before resolving substance.
- Do not claim a change, experiment, or citation exists unless it can be verified.
- Do not over-concede by weakening the main contribution beyond the evidence.
- Do not dismiss a reviewer as wrong without explaining the source of the misunderstanding.
- Do not include private author identity if the rebuttal or review process is anonymous.

## Validation

- Every reviewer point is represented or explicitly grouped.
- Every high-priority issue has a direct response and paper-change decision.
- The response is polite, specific, and evidence-grounded.
- Promises are feasible within the allowed response or revision window.

## Completion

Done means the user has a prioritized rebuttal ledger, draft responses for decision-critical points, and a concrete manuscript edit plan.
