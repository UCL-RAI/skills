# Benchmark Checks

Use this checklist for full experiment-section audits.

## Source Patterns

- NeurIPS Paper Checklist asks authors to state assumptions, limitations, experiment details, compute, error bars, and whether code/data support reproducibility: https://neurips.cc/public/guides/PaperChecklist
- NeurIPS Code and Data Submission Policy emphasizes submitting code, data, environments, scripts, and instructions when applicable: https://neurips.cc/public/guides/CodeSubmissionPolicy
- Papers with Code's ML Code Completeness Checklist emphasizes dependencies, training/evaluation code, pretrained models, data processing, and result reproduction: https://github.com/paperswithcode/releasing-research-code
- ACM Artifact Review and Badging separates availability, functionality, reusability, and result reproduction/replication claims: https://www.acm.org/publications/policies/artifact-review-and-badging-current

Use these as structure inspiration, not as copied venue rules. Always verify the current target venue instructions.

## Claim Types

| Claim type | Evidence expected |
| --- | --- |
| State-of-the-art | Current strong baselines, same benchmark protocol, statistical uncertainty, and citation trail. |
| Better generalization | Held-out tasks, domains, robots, objects, scenes, seeds, or datasets. |
| Robustness | Stress conditions, perturbations, sensor noise, failures, and negative cases. |
| Sample efficiency | Matched data budgets, learning curves, and fixed stopping criteria. |
| Real-world deployment | Hardware setup, safety constraints, trial counts, failure rates, and sim-to-real boundary. |
| Efficiency | Wall-clock, compute, memory, model size, and hardware. |

## Fairness Questions

- Were baselines selected because they are competitive for this task?
- Were baselines implemented from official code, faithful reimplementation, or a weak custom version?
- Were hyperparameters and training budgets comparable?
- Did all methods receive the same data, pretraining, demonstrations, prompts, or privileged state?
- Are failed runs, seeds, or tasks excluded? If yes, is the exclusion rule pre-specified?
- Are metrics reported with uncertainty where randomness matters?
- Are results robust to simple controls such as random policy, heuristic planner, no-memory variant, or no-vision variant?

## Robotics-Specific Risks

- Simulator benchmark does not match real robot constraints.
- Success metric hides unsafe contacts, retries, human intervention, or reset costs.
- Evaluation tasks overlap with demonstrations, teleoperation scripts, or scripted policies.
- Visual domain randomization or scene assets leak from train to test.
- Small trial counts make success-rate claims unstable.
- Hardware failures are silently excluded.

## Severity Guide

- `blocking`: main claim depends on missing or unfair benchmark evidence.
- `major`: benchmark is useful but leaves a serious alternate explanation.
- `minor`: reporting gap or local clarity issue.
- `nit`: formatting, label, or wording issue that does not change interpretation.
