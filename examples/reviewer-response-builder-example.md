# Reviewer Response Builder Example

## User Prompt

> Build a rebuttal plan for these reviews.

## Example Input

```markdown
R1: The method is interesting, but the paper lacks comparison to Diffusion Policy.
R2: The novelty over hierarchical imitation learning is unclear.
R3: The real-robot claim is too strong because all experiments are in simulation.
```

## Expected Skill Behavior

The agent should use `reviewer-response-builder`, split comments into an issue ledger, classify each issue, and draft evidence-grounded responses without overpromising.

## Example Output Shape

```markdown
## Issue Ledger
| Reviewer | Comment | Classification | Priority | Response action |
| --- | --- | --- | --- | --- |
| R1 | missing Diffusion Policy comparison | experiment/citation gap | high | add verified comparison or narrow claim |
| R2 | unclear novelty | positioning gap | high | clarify boundary against hierarchical imitation learning |
| R3 | real-robot claim too strong | valid weakness | high | narrow deployment claim and add limitation |

## Do Not Promise
- Do not promise real-robot experiments unless they can be completed.
```

## Quality Checks

- Polite and specific.
- Every reviewer point is represented.
- Promises map to feasible paper edits.
