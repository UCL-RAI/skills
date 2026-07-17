---
name: paper-code-consistency-auditor
description: Audits whether a Robotics or AI manuscript accurately describes its implementation, configs, data pipeline, training and inference behavior, evaluation code, defaults, and generated tables or figures. Use when reconciling a paper with a codebase, preparing an artifact release, checking implementation drift, or verifying that equations, algorithms, hyperparameters, and system claims match the released code.
---

# Paper Code Consistency Auditor

Compare what the manuscript says with what the inspected implementation does.
Find semantic drift; do not substitute a code inventory or reproducibility
check for claim-level comparison.

Read `references/consistency-contract.md` before a `standard` or `deep` audit.

## Inputs

- Manuscript source or PDF with stable section, equation, table, and figure
  locations.
- Code repository and the commit or working-tree state intended to support the
  manuscript.
- Configs, CLI defaults, launch files, preprocessing, training, inference,
  evaluation, plotting code, and tests that are in scope.
- Optional artifact-release or camera-ready requirements.

If paper and code versions are not identifiable, record that as a blocking
ambiguity before judging consistency.

## Workflow

1. Record the manuscript version, code commit, branch, dirty state, generated
   files, and audit scope.
2. Inventory checkable manuscript statements about the method, equations,
   architecture, inputs/outputs, preprocessing, objectives, hyperparameters,
   defaults, training, inference, evaluation, and deployment behavior.
3. Locate the implementation evidence for each statement. Inspect the actual
   execution path and config precedence rather than relying on names, comments,
   or README prose.
4. Compare terminology and interfaces: tensor shapes, units, frames, action
   spaces, observation fields, model components, losses, update schedules,
   control frequency, and failure handling where relevant.
5. Compare data and training behavior: filtering, splits, normalization,
   augmentation, checkpoint selection, seeds, optimization, and overrides.
6. Compare evaluation and presentation paths: metric implementation, default
   flags, exclusions, aggregation, table generation, plotting transforms, and
   figure labels.
7. Classify every item as `match`, `paper-stale`, `code-stale`, `ambiguous`,
   `missing-implementation`, or `not-applicable`.
8. Assign severity based on scientific consequence: `blocking`, `major`, or
   `minor`. State whether to repair paper, code, config, or evidence.
9. Recheck changed items and report residual inconsistencies without silently
   choosing paper or code as ground truth.

## Depth

- `quick`: inspect one claim, section, table, figure, or config discrepancy.
- `standard`: audit the main method and evaluation path.
- `deep`: audit the full manuscript, release code, configs, generated results,
  Robotics interfaces, and artifact-facing commands.

Default to `standard`. Use `deep` before artifact release or camera-ready when
paper-code drift would alter scientific claims.

## Boundaries

- Use `experiment-provenance-auditor` to trace results to runs and artifacts.
- Use `benchmark-audit` to judge whether evaluation design is convincing.
- Use this skill to decide whether the paper's description matches the code.

Invoke those skills only when their separate question blocks this audit.

## Output

```markdown
# Paper-Code Consistency Audit

## Version Contract

## Discrepancy Ledger
| ID | Paper location/statement | Code evidence | Status | Severity | Scientific consequence | Repair |
| --- | --- | --- | --- | --- | --- | --- |

## Cross-Cutting Drift

## Blocking Repairs

## Residual Ambiguities
```

## Rules

- Do not infer behavior from symbol or filename similarity.
- Do not treat comments, docstrings, examples, or dead code as executed
  behavior without tracing the active path.
- Respect config inheritance, environment overrides, generated code, and
  launch-time parameters.
- Do not rewrite code to match the paper before establishing which behavior is
  intended and scientifically supported.
- Do not expose credentials, private paths, or unreleased data.
- Do not claim runtime or hardware consistency from static inspection alone;
  state the verification still required.

## Validation

- Every blocking manuscript statement in scope has implementation evidence or
  an explicit missing status.
- Every discrepancy identifies both paper and code locations.
- Severity reflects claim impact rather than cosmetic difference.
- Config defaults and overrides are compared using effective values.
- Suggested repairs preserve result provenance and experiment comparability.

## Completion

Done means the manuscript and implementation versions are explicit, material
drift has a source-grounded repair path, and runtime-only uncertainties remain
visible.
