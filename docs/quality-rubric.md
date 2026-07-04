# Skill Quality Rubric

Use this rubric before moving a skill from `draft` to `beta` or `stable`.

| Criterion | Draft | Beta | Stable |
| --- | --- | --- | --- |
| Trigger | Clear enough for manual use. | Clear enough for model invocation. | Has been tested on realistic prompts without false positives. |
| Scope | One main workflow. | No hidden subworkflows. | Stable boundaries against adjacent skills. |
| Completion | Output artifact described. | Output artifact has required fields/checks. | Completion criteria catches premature completion. |
| Evidence | Mentions source needs. | Requires source grounding where claims matter. | Includes failure modes for unsupported claims. |
| Reuse | Project assumptions are documented. | No private paths or credentials. | Works across multiple Robotics & AI projects. |
| Validation | Manual review only. | Catalog validation passes. | Forward-tested or used in real work. |

## Review Questions

- Would this skill still make sense outside our current repo?
- Can the agent know when it is done?
- Is this skill doing one job, or hiding several jobs?
- Does the body contain information that belongs in `references/`?
- Does the description contain all trigger information needed for model invocation?
- Could any instruction cause fabricated citations, fake metrics, or unverified claims?

## Promotion Evidence

Before moving a skill beyond `draft`, maintainers should capture at least one of:

- a realistic example in `examples/`;
- a forward test in `forward-tests/`;
- a real task transcript or artifact showing the skill produced its required output.

Before moving a skill to `stable`, the skill should have repeated use across more than one project or user context, and any known false-trigger or false-completion behavior should be documented or fixed.
