# Matrix Design Reference

Use this reference when choosing matrix axes, gap tags, or survey synthesis structure.

## Axis Selection

Choose axes that answer the research question.

| Question type | Useful axes |
| --- | --- |
| Method comparison | method family, input/output, training signal, assumptions, complexity |
| Robotics deployment | robot platform, sensors, control rate, environment, sim/real status |
| Benchmark survey | dataset, task, metric, split, baseline set, evaluation protocol |
| Reproducibility audit | code availability, config/logs, seeds, checkpoints, dependencies |
| Gap analysis | claimed contribution, missing evidence, assumption, untested setting |

Avoid axes that make every row unique without improving comparison.

## Gap Tags

Use stable tags so downstream synthesis can group patterns.

| Tag | Meaning |
| --- | --- |
| `missing-evaluation` | The paper claims capability without a relevant empirical test. |
| `weak-baseline` | Baselines are missing, outdated, unfair, or too narrow. |
| `unrealistic-assumption` | The setup assumes information, dynamics, labels, or conditions unlikely in deployment. |
| `narrow-benchmark` | Evidence covers only a small task, dataset, robot, or environment family. |
| `untested-deployment` | Sim-to-real, hardware, latency, safety, or robustness is not evaluated. |
| `unclear-reproducibility` | Code, data, configs, seeds, or implementation details are insufficient. |
| `metric-mismatch` | Reported metrics do not directly support the claim. |
| `citation-gap` | A key claim lacks primary-source support. |

## Synthesis Rules

- Start with what the matrix shows, then interpret why it matters.
- Use "most", "some", and "few" only when the row counts support them.
- Preserve minority patterns if they represent important baselines or failure cases.
- Separate taxonomy, evidence strength, and future directions.
- Mark unresolved questions as follow-up search tasks, not as conclusions.

## Minimum Useful Matrix

A matrix is useful when it has:

- a stated research question;
- at least three comparable rows, unless the field is genuinely sparse;
- stable identifiers for each source;
- enough columns to compare claims, methods, evidence, and limitations;
- gap tags that trace to source-specific evidence.
