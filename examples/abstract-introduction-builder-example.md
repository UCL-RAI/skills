# Abstract Introduction Builder Example

## User Prompt

> Draft an abstract from this claim-evidence map.

## Example Input

```markdown
Problem: long-horizon manipulation with sparse rewards.
Gap: low-level visuomotor policies struggle with task sequencing.
Method: subgoal graph plus diffusion low-level controller.
Evidence: simulation success improves over two baselines on 20 tasks; real robot not tested.
Limitation: benchmark is simulation-only and uses one robot embodiment.
```

## Expected Skill Behavior

The agent should use `abstract-introduction-builder`, produce a scoped abstract, and keep simulation-only limitations visible.

## Example Output Shape

```markdown
## Abstract Draft
Long-horizon manipulation requires policies that can both sequence subgoals and execute local visuomotor actions. We study a subgoal-graph controller paired with a diffusion-based low-level policy for sparse-reward manipulation tasks. In simulation, the method improves success rate over two baselines across 20 tasks. The current evaluation is limited to one simulated robot embodiment, so claims about real-world deployment remain outside scope.

## Claim-Risk Table
| Sentence or claim | Evidence | Risk | Fix |
| --- | --- | --- | --- |
| improves success rate | Table required | needs metric details | add exact metric and variance |
```

## Quality Checks

- Does not claim real-robot readiness.
- Makes missing evidence visible.
- Avoids generic opening prose.
