# Paper Red-Team Review Example

## User Prompt

> Red-team this abstract for an ICRA submission. Be harsh and focus on rejection risks.

## Example Input

```markdown
We present a novel robot learning framework that solves long-horizon manipulation. Our approach outperforms prior work in simulation and demonstrates strong generalization. Experiments show significant gains over baselines. The method is simple, scalable, and suitable for real-world deployment.
```

## Expected Skill Behavior

The agent should use `paper-red-team-review`, lead with findings, and avoid rewriting away unsupported claims.

## Example Output Shape

```markdown
## Blocking
| Issue | Evidence | Why it matters | Repair path |
| --- | --- | --- | --- |
| Overbroad capability claim | "solves long-horizon manipulation" | Reviewers will reject unsupported universal claims. | Scope the claim to the exact tasks and horizons tested. |
| Deployment overclaim | "suitable for real-world deployment" but only simulation is mentioned | Simulation-only evidence does not establish hardware readiness. | Add real-robot evidence or rewrite as simulation-only. |

## Major
| Issue | Evidence | Why it matters | Repair path |
| --- | --- | --- | --- |
| Baselines are unspecified | "significant gains over baselines" | The claim cannot be evaluated without baseline names and metrics. | Name baselines, metrics, tasks, and statistical evidence. |
| Novelty is unsupported | "novel robot learning framework" | Novelty must be positioned against closest related work. | State what is new relative to specific prior methods. |

## Rewrite Suggestions
- Replace "solves long-horizon manipulation" with a task-scoped claim.
- Replace "suitable for real-world deployment" with the actual evaluation boundary.

## Residual Risk
The abstract still needs experiment details, baseline names, and citation support before style polishing.
```

## Quality Checks

- Findings are severity-ranked.
- Every blocking/major issue has a repair path.
- Unsupported claims are narrowed rather than made more fluent.
