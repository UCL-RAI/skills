# Forward Test: Reviewer Response Builder

## Skill

`reviewer-response-builder`

## Prompt

Use `reviewer-response-builder` to build a rebuttal plan for these reviews.

```markdown
R1: The paper lacks comparison to Diffusion Policy, which is the closest baseline.
R2: The novelty over hierarchical imitation learning is unclear.
R3: The abstract claims real-world deployment, but all experiments are in simulation.
Meta-review: The main concern is whether the empirical claim is overstated.

Constraints:
- 600-word response limit
- anonymous review process
- no time for real-robot experiments before rebuttal
```

## Expected Artifact Checklist

- Includes an issue ledger with every reviewer and meta-review point represented.
- Classifies issues into experiment gap, positioning gap, valid weakness, or equivalent.
- Prioritizes the empirical overclaim and closest-baseline concern.
- Drafts concise, non-defensive responses.
- States manuscript changes and what not to promise.
- Preserves anonymity.

## Pass Conditions

- The plan narrows the real-world deployment claim instead of promising impossible experiments.
- The response to missing Diffusion Policy comparison is evidence-grounded or explicitly conditional on feasibility.
- The novelty response routes to related-work positioning or concrete manuscript changes.

## Fail Conditions

- The response argues reviewers are wrong without evidence.
- The response promises real-robot experiments despite the stated constraint.
- The response omits any reviewer point.
