# Idea Stress Tests

Use this reference when ranking multiple ideas or making a go/no-go recommendation.

## Score Anchors

Use 1-5 scores consistently.

| Score | Anchor |
| --- | --- |
| 1 | Fails the dimension or lacks enough information to assess. |
| 2 | Plausible but weak, underspecified, or high-risk. |
| 3 | Workable with clear assumptions and moderate risk. |
| 4 | Strong, testable, and well matched to available resources. |
| 5 | Exceptional; clear novelty, feasibility, and evaluation path. |

## Reviewer Objection Prompts

Ask:

- What closest prior work would make this look incremental?
- What baseline could defeat the proposed method?
- What ablation would undermine the main mechanism claim?
- What dataset, robot, or simulator choice would make the result look narrow?
- What assumption would fail outside the lab setup?
- What evidence would be needed for a skeptical Robotics or ML reviewer?

## Fast Falsification Tests

Prefer tests that can be run before committing to a full project:

- reproduce a baseline on one task;
- run a minimal ablation that isolates the proposed mechanism;
- test one hard negative or failure case;
- verify dataset availability, license, and split compatibility;
- estimate compute/hardware time from a small pilot run;
- check whether the key idea already exists under different terminology.

## Decision Labels

- `keep`: strong enough to plan experiments now.
- `revise`: promising but needs narrowed claim, stronger baseline, or better evaluation.
- `park`: interesting but blocked by resources, missing evidence, or timing.
- `reject`: weak novelty, infeasible execution, invalid evaluation, or unacceptable risk.
