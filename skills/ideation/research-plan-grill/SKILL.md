---
name: research-plan-grill
description: Interrogates a Robotics or AI research, paper, experiment, survey, or engineering plan one decision at a time until its objective, evidence, scope, evaluation, risks, and next artifact are explicit. Use when the user asks to be grilled, wants a plan stress-tested through questions, or has an ambiguous design that should be resolved before implementation or writing.
---

# Research Plan Grill

Use a focused interview to turn an ambiguous plan into an agreed decision
brief. Resolve the highest-dependency decision first rather than presenting a
questionnaire.

## Inputs

Identify the available artifact: idea note, research plan, paper draft,
experiment design, repository, issue, specification, or verbal proposal.

Before asking a question:

1. Inspect the available repository, documents, sources, and prior decisions.
2. Answer factual questions from evidence when possible.
3. Separate facts that can be discovered from decisions only the user can
   authorize.

Do not ask the user for information that is already available in scope.

## Workflow

1. Build a private decision tree covering only relevant dimensions:
   objective, audience, scope, evidence, contribution, method, interfaces,
   evaluation, constraints, failure criteria, risks, and deliverable.
2. Select the unresolved decision that blocks the most downstream choices.
3. Ask exactly one concise question.
4. Include a recommended answer and the reason it best fits known evidence and
   constraints. Name alternatives only when they represent a real trade-off.
5. After the user answers, record the decision as `accepted`, `modified`,
   `deferred`, or `rejected`, then choose the next dependent question.
6. Challenge contradictions, hidden assumptions, weak evidence, undefined
   terms, and plans that cannot be falsified or evaluated.
7. Stop when the next artifact can be produced without guessing a blocking
   decision. Do not continue merely to exhaust every possible question.

Use this turn shape:

```markdown
## Question
<one question>

## Recommendation
<recommended answer>

## Why This Matters
<downstream decision or risk affected>
```

## Depth

- `quick`: resolve one immediate blocker, usually within 3-5 questions.
- `standard`: resolve enough of the decision tree to produce the next research
  or engineering artifact.
- `deep`: stress-test a high-cost plan before experiments, implementation,
  submission, or hardware deployment.

Default to `standard`. Let the user stop or change depth at any point.

## Domain Priorities

For research and survey plans, prioritize research question, inclusion scope,
evidence standard, taxonomy or contribution boundary, and synthesis method.

For experiment plans, prioritize hypothesis, baselines, metrics, data splits,
seeds or trials, ablations, failure criteria, compute/hardware, and the claim
each result can support.

For paper plans, prioritize audience, thesis, contribution-evidence mapping,
venue constraints, missing experiments, and overclaim risk.

For engineering plans, inspect the codebase first, then prioritize ownership
boundaries, interfaces, verification loop, migration risk, and Robotics safety
assumptions.

## Rules

- Ask one question at a time; never send a batch questionnaire.
- Recommend rather than remain neutral, but state uncertainty and let the user
  reject the recommendation.
- Do not reopen settled decisions without new evidence or a contradiction.
- Do not confuse a missing fact with a user preference.
- Do not turn speculative ideas into established claims.
- Do not begin writing or implementation while a blocking decision remains,
  unless the user explicitly accepts the risk.
- Keep a visible interview concise; store detail in the final decision brief.

## Output

When the interview converges, produce:

```markdown
# Decision Brief

## Objective and Deliverable

## Constraints

## Agreed Decisions
| Decision | Choice | Rationale | Status |
| --- | --- | --- | --- |

## Evidence and Assumptions
| Item | Evidence/status | Consequence |
| --- | --- | --- |

## Rejected Alternatives

## Open Risks and Deferred Decisions

## Next Artifact and Recommended Skill
```

## Validation

- Every asked question changes or protects a downstream decision.
- Discoverable facts were inspected rather than delegated to the user.
- Recommendations distinguish evidence from judgment.
- The brief preserves rejected alternatives and unresolved risks.
- The next artifact can proceed without hidden blocking assumptions.

## Completion

Done means the user and agent share an explicit decision brief, the next
artifact and skill are named, and any remaining uncertainty is consciously
accepted rather than silently guessed.
