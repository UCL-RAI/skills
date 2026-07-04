# Scientific Figure Director Example

## User Prompt

> I need a figure for a CoRL-style paper that explains a robot learning pipeline combining offline demonstrations, simulation rollout, and real-robot evaluation. Help me specify the figure and audit it.

## Expected Skill Behavior

The agent should use `scientific-figure-director`, define the scientific job, specify panels and arrow semantics, and reject unsupported visual claims.

## Example Figure Spec

```markdown
## Figure job
Explain the method pipeline and make the sim/real boundary explicit.

## Scientific claim
The method trains from offline demonstrations, improves policy behavior in simulation, and evaluates the final policy on a real robot.

## Paper section
Method overview.

## Figure type
Three-panel pipeline diagram.

## Panels
| Panel | Content | Claim | Required labels |
| --- | --- | --- | --- |
| A | Offline demonstrations -> dataset preprocessing | Training data source | "offline demos", "dataset", "state/action pairs" |
| B | Policy training and simulation rollout loop | Simulation is used for training/validation, not final deployment evidence | "simulation", "rollout", "policy update" |
| C | Real-robot evaluation | Evaluation happens after training | "real robot", "held-out tasks", "metrics" |

## Entities and relationships
- Data arrows: offline demos -> dataset -> policy training.
- Training loop arrows: policy -> simulation rollout -> loss/update -> policy.
- Evaluation arrow: trained policy -> real robot evaluation.

## Forbidden ambiguities
- Do not show real-robot data flowing back into training unless that experiment exists.
- Do not invent numeric metrics or success rates.
- Do not blur training and inference stages.

## Style constraints
Clean black/gray scientific diagram, readable labels, no decorative background, panel labels A-C.
```

## Audit Checklist

- Every arrow has an explicit meaning.
- Simulation and real-robot stages are visually separated.
- The figure does not imply online real-robot training unless the paper supports it.
- Labels remain readable at paper-column scale.
