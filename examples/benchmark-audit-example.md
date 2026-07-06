# Benchmark Audit Example

## User Prompt

> Audit whether this experiment table is enough to support our claim that our robot policy is more robust than prior work.

## Example Input

```markdown
Claim: Our method improves robust long-horizon manipulation.

Table 1 reports success rate on 20 simulation tasks:
- Ours: 78.2
- Baseline A: 73.5
- Baseline B: 71.0

We ran one seed. Baseline A uses the authors' reported score from a different paper. No real robot tests yet.
```

## Expected Skill Behavior

The agent should use `benchmark-audit`, map the claim to evidence, and flag unsupported robustness, baseline fairness, seed count, and sim-to-real limitations.

## Example Output Shape

```markdown
## Claim-Result Map
| Claim | Evidence location | Support level | Missing evidence |
| --- | --- | --- | --- |
| more robust long-horizon manipulation | Table 1 simulation success rate | weak | stress conditions, repeated seeds, fair baseline reruns, real robot boundary |

## Blocking Issues
- Robustness is not tested by a single aggregate simulation success score.
- Baseline A is not protocol-matched if it comes from another paper.

## Required Additional Experiments
- Rerun baselines under the same data, tasks, seeds, and metric.
- Add variance or confidence intervals over multiple seeds.
- Add stress/failure conditions if the claim remains "robust".
```

## Quality Checks

- Does not invent new scores.
- Narrows the claim instead of polishing it.
- States which experiment would change the decision.
