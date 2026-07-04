---
name: robotics-ai-coding-flow
description: Applies Robotics & AI code quality checks for Python, C++, ROS, simulation, ML experiments, and reproducibility. Use when implementing, debugging, testing, or reviewing Robotics and AI research code.
---

# Robotics AI Coding Flow

Use this as a Robotics & AI layer on top of normal coding skills.

## Inputs

- User request, codebase, failing logs/tests, issue description, or desired feature.
- Runtime constraints: Python/C++, ROS version if relevant, simulator/hardware, dataset, compute, and safety boundary.
- Expected artifact: patch, debug diagnosis, test, review findings, reproduction instructions, or experiment-quality check.

If hardware or simulator access is unavailable, use the smallest offline verification loop and state what remains unvalidated.

## Workflow

1. Read the repo's existing setup, tests, configs, and domain terminology.
2. Identify the code layer:
   - algorithm;
   - ML training/evaluation;
   - simulator;
   - ROS node/package;
   - hardware interface;
   - data processing;
   - plotting/reporting.
3. Choose the smallest verification loop that can fail for the current change.
4. Implement or debug with tests where practical.
5. Run Robotics-specific checks from `references/robotics-code-checks.md`.
6. Report what was verified and what still needs simulation or hardware validation.

## Verification Matrix

```markdown
| Layer | Likely checks | Hardware/sim caveat |
| --- | --- | --- |
| Algorithm | unit tests, property checks, toy cases | May miss timing and integration failures. |
| ML training/evaluation | smoke run, config diff, metric recomputation | May miss full-scale variance and compute limits. |
| Simulator | deterministic scenario, asset/config check | May not transfer to real hardware. |
| ROS node/package | build/test, launch/config check, topic contract | May miss live timing and transport issues. |
| Hardware interface | dry-run guards, bounds checks, log replay | Real hardware requires explicit user approval and safety context. |
| Plotting/reporting | artifact trace, metric source check | Plot correctness depends on upstream logs. |
```

## Use Existing Engineering Skills When Available

If installed, combine this skill with:

- `diagnosing-bugs` for hard bugs;
- `tdd` for test-first implementation;
- `prototype` for throwaway design experiments;
- `codebase-design` and `domain-modeling` for architecture;
- `code-review` for final review.

## Rules

- Respect existing codebase patterns and local instructions.
- Keep changes scoped to the requested behavior unless root cause requires a broader fix.
- Preserve experiment comparability: document seed, config, dataset, metric, and checkpoint changes.
- Treat frame, unit, timestamp, and transform bugs as first-class correctness issues.
- Do not claim real-world safety from tests that ran only offline or in simulation.

## Output

For implementation/debugging:

```markdown
## Change
## Verification
## Robotics/AI Checks
## Simulation or Hardware Readiness
## Residual Risk
```

For review:

```markdown
| Severity | File/line | Issue | Robotics/AI risk | Suggested fix |
| --- | --- | --- | --- | --- |
```

## Completion

Done means the code change has a feedback loop, a verification result, and an explicit statement about simulation/hardware readiness.
