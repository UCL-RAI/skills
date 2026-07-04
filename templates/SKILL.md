---
name: example-skill
description: Use this skill when an agent needs to perform one concrete, reusable workflow.
---

# Example Skill

## When to Use

Use this skill when:

- The task matches a narrow, repeatable workflow.
- The required inputs are available or can be requested safely.
- The output can be checked with concrete validation steps.

Do not use this skill when:

- The task needs private credentials that have not been provided.
- The workflow depends on facts that must be verified but no reliable source is available.
- A smaller existing skill already covers the task.

## Workflow

1. Confirm the user goal and required inputs.
2. Inspect the relevant local context before proposing changes.
3. Execute the smallest practical workflow that solves the root problem.
4. Validate the result with commands, tests, examples, or manual checks.
5. Report assumptions, changes made, and remaining risks.

## Inputs

- Required: Describe the minimum required input.
- Optional: Describe useful optional context.

## Outputs

- Describe the expected final artifact, patch, command output, or decision.

## Validation

Run or describe checks that prove the workflow worked.

```bash
# Example:
python scripts/validate_catalog.py
```

## Completion

State the artifact or condition that proves the skill is done. Avoid vague criteria such as "make it useful."

## Notes

Keep this section short. Add links to primary documentation or papers if the skill depends on external knowledge.
