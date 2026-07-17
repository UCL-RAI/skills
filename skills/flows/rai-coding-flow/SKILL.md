---
name: rai-coding-flow
description: Routes Robotics & AI coding work through design, prototyping, debugging, testing, review, and reproducibility checks. Use when the user asks to build, debug, test, review, or restructure Python, C++, ROS, simulation, ML, or experiment code.
disable-model-invocation: true
---

# RAI Coding Flow

Use this as the user-facing router for Robotics & AI engineering work.

## Intake

Before choosing a workflow, identify:

- task type: implement, debug, test, review, refactor, reproduce, summarize,
  package, or explain;
- code layer: algorithm, ML training/evaluation, simulator, ROS node/package, hardware interface, data processing, plotting/reporting;
- safety boundary: offline-only, simulation, real hardware, or deployment;
- verification loop: unit test, integration test, replay log, benchmark script, simulator run, hardware test, or manual inspection.

Read the repo's local instructions, setup files, and existing tests before proposing changes.

## Route by Situation

| Situation | Route | Required check |
| --- | --- | --- |
| Ambiguous feature or system design | Inspect the codebase, then use `research-plan-grill` for unresolved user decisions before codebase design or implementation. | Produce a decision brief with assumptions, interfaces, verification, and risks before editing. |
| Hard bug or regression | Reproduce, minimize, instrument, fix, then add or update a regression check. | Show the failing loop before claiming a fix when feasible. |
| New feature | Prefer a test-first vertical slice when practical. | Verify the smallest behavior that exercises the new path. |
| Prototype question | Build throwaway code only to answer the question. | Preserve the conclusion and delete or isolate disposable code. |
| Review | Check standards, spec fit, reproducibility, and Robotics-specific failure modes. | Lead with findings and file/line evidence. |
| Reproducibility task | `experiment-provenance-auditor` for result traceability, then code-level fixes as needed. | Report what can and cannot be rerun. |
| Remote project is ready for local paper writing | `experiment-dossier-builder` | Produce one portable dossier with result ids, source locators, and explicit evidence gaps. |
| Paper and implementation may have drifted | `paper-code-consistency-auditor` | Compare identified manuscript and code versions before repairing either side. |

## Robotics & AI Checks

Always consider:

- coordinate frames, units, timestamps, and transforms;
- sim vs real assumptions;
- seeds, configs, datasets, logs, and result provenance;
- ROS package boundaries and launch/config behavior;
- Python/C++ interface contracts;
- latency, control-loop frequency, and safety assumptions;
- benchmark validity and statistical reporting.

## Engineering Gates

- Do not edit before understanding ownership boundaries and existing conventions.
- Do not claim hardware readiness from offline or simulation-only checks.
- Do not change benchmark code, metrics, or seeds without documenting the effect on comparability.
- Do not bypass safety checks, launch defaults, or hardware limits to make a demo pass.
- Do not rewrite large areas unless the existing structure makes the requested behavior impractical.

## Handoff Output

Finish substantial work with:

```markdown
## Coding Flow Status
| Area | Result |
| --- | --- |
| Task type | |
| Code layer | |
| Verification run | |
| Simulation readiness | |
| Hardware readiness | |
| Residual risk | |
```

## Completion

Done means the chosen engineering path is explicit, a concrete verification loop was run or blocked for a stated reason, and simulation/hardware readiness is not overstated.
