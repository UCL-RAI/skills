# Venue Rubric

Use this as a lightweight orientation, not as a substitute for current official author instructions.

| Venue family | Typical pressure points |
| --- | --- |
| ICRA | Robotics relevance, hardware or simulation validity, clear system details, practical evaluation. |
| RSS | Conceptual clarity, strong robotics contribution, careful experiments, concise argument. |
| CoRL | Robot learning contribution, benchmark realism, policy evaluation, sim-to-real or embodied evidence. |
| ICML / ICLR / NeurIPS | Method novelty, theoretical or empirical strength, baselines, ablations, reproducibility. |

## Section Emphasis

| Section | Robotics pressure | ML pressure |
| --- | --- | --- |
| Introduction | Why the robot/task setting matters and what capability improves. | Why the method problem matters and what general claim is tested. |
| Related Work | Position against systems, control, perception, planning, or robot learning baselines. | Position against method families, objectives, architectures, and theory/empirical baselines. |
| Method | Include assumptions, state/action spaces, sensors, control loops, and implementation details. | Specify objective, architecture, training/inference algorithm, complexity, and reproducibility details. |
| Experiments | Clarify robot/simulator setup, environments, safety limits, and sim-to-real boundaries. | Clarify datasets, splits, metrics, baselines, ablations, statistical reporting, and compute. |
| Limitations | Discuss deployment assumptions, hardware/sim constraints, failure cases, and safety. | Discuss scope of empirical evidence, scaling limits, assumptions, and negative results. |

## Common Rejection Risks

- Contribution is an engineering integration without a clear research claim.
- Baselines are weak or outdated.
- Evaluation is simulation-only without explaining why that is sufficient.
- Method is underspecified.
- Figures show a pipeline but not the actual scientific contribution.
- Related work is a list, not a positioning argument.

## Venue-Fit Questions

- What kind of reviewer would be most skeptical, and why?
- Does the contribution primarily improve embodied capability, learning method, system reliability, or evaluation methodology?
- Is the evidence strong enough for the claimed venue family?
- Are baselines recognizable to the venue community?
- Would the same paper make sense if the robot/system context were removed? If yes, the Robotics framing may be weak.
- Would the same paper make sense without a method novelty claim? If yes, the ML framing may be weak.
