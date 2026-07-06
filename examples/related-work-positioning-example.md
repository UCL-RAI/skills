# Related Work Positioning Example

## User Prompt

> Help position our paper against prior work on diffusion policies and hierarchical imitation learning.

## Example Input

```markdown
Our claim: We improve long-horizon manipulation by combining subgoal planning with diffusion-based low-level policies.

Sources:
- Source A: diffusion policy for visuomotor control.
- Source B: hierarchical imitation learning for long-horizon tasks.
- Source C: task-and-motion planning with learned skills.
```

## Expected Skill Behavior

The agent should use `related-work-positioning`, cluster sources, define novelty boundaries, and avoid unsupported "first" claims.

## Example Output Shape

```markdown
## Prior-Work Clusters
| Cluster | Representative sources | What they solve | Boundary for this paper |
| --- | --- | --- | --- |
| diffusion policies | Source A | low-level visuomotor control | long-horizon subgoal structure must be distinguished |
| hierarchical imitation | Source B | temporal abstraction | low-level diffusion controller is the claimed difference |

## Safer Wording
Rather than claiming to be first, state the precise combination and evaluation setting, then verify whether that combination is absent from closest work.
```

## Quality Checks

- Uses clusters instead of a chronological list.
- Flags missing must-cite papers.
- Does not assert novelty without coverage.
