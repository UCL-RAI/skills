# Paper-Code Consistency Contract

Use this contract for a standard or deep audit.

Primary process references:

- [ACM Artifact Review and Badging](https://www.acm.org/publications/policies/artifact-review-and-badging-current)
  distinguishes artifact availability, functionality, reusability, and result
  reproduction or replication claims.
- The [NeurIPS Paper Checklist](https://neurips.cc/public/guides/PaperChecklist)
  motivates explicit reporting of assumptions, experiment details, compute,
  limitations, code, and data.

## Comparison Dimensions

| Dimension | Paper evidence | Code evidence |
| --- | --- | --- |
| Problem/interface | notation, assumptions, input/output definitions | schemas, types, tensor shapes, messages, units |
| Method structure | equations, algorithm, architecture figure | active modules, call path, component wiring |
| Objective/optimization | loss definitions, weights, schedules | loss code, config values, optimizer/scheduler setup |
| Data | datasets, splits, filtering, preprocessing | loaders, manifests, transforms, split construction |
| Training | epochs/steps, batch, seeds, checkpoint rule | launch configs, defaults, resume and selection logic |
| Inference/control | decoding, action generation, frequency | inference path, controller loop, runtime parameters |
| Evaluation | baselines, metrics, exclusions, aggregation | metric code, flags, filters, reducers, seed handling |
| Tables/figures | values, labels, captions, conditions | source artifacts, analysis and plotting transforms |
| Release interface | commands, configs, model/data availability | executable entry points and packaged artifacts |

## Status Rules

- `match`: active implementation evidence supports the paper statement under
  the identified effective configuration.
- `paper-stale`: code behavior is intentionally newer but the paper still
  describes an older behavior.
- `code-stale`: paper records the intended behavior but release code has not
  implemented or restored it.
- `ambiguous`: multiple active paths or unresolved config precedence prevent a
  unique comparison.
- `missing-implementation`: no supporting active path was found.
- `not-applicable`: the statement does not make an implementation claim.

## Severity Rules

- `blocking`: changes a central method, result interpretation, safety claim,
  reproducibility path, or released command.
- `major`: changes a secondary claim, important hyperparameter, baseline,
  metric, ablation, or implementation detail needed to understand the result.
- `minor`: wording, naming, or packaging drift that does not change scientific
  meaning but should still be corrected.

## Robotics-Specific Checks

When relevant, compare coordinate frames, units, timestamps, transforms,
control frequency, action scaling, safety bounds, reset policy, simulator/real
mode, sensor preprocessing, and intervention handling. Mark hardware behavior
unverified unless runtime or log evidence is available.
