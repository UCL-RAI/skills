# Forward Tests

Forward tests are lightweight prompts and pass criteria for checking whether a skill behaves usefully on realistic tasks.

These are not automated benchmark scores. They are review fixtures for forward-testing skills in fresh agent contexts without leaking the intended answer.

## How to Use

1. Open one test file.
2. Start a fresh agent context.
3. Ask the agent to use the named skill on the prompt.
4. Compare the result against the expected artifact checklist and pass conditions.

## Current Tests

| Skill | Test |
| --- | --- |
| `knowledge-base-onboarding` | [`knowledge-base-onboarding.md`](./knowledge-base-onboarding.md) |
| `paper-search-protocol` | [`paper-search-protocol.md`](./paper-search-protocol.md) |
| `evidence-matrix-builder` | [`evidence-matrix-builder.md`](./evidence-matrix-builder.md) |
| `related-work-positioning` | [`related-work-positioning.md`](./related-work-positioning.md) |
| `abstract-introduction-builder` | [`abstract-introduction-builder.md`](./abstract-introduction-builder.md) |
| `manuscript-structure-auditor` | [`manuscript-structure-auditor.md`](./manuscript-structure-auditor.md) |
| `scientific-writing-editor` | [`scientific-writing-editor.md`](./scientific-writing-editor.md) |
| `benchmark-audit` | [`benchmark-audit.md`](./benchmark-audit.md) |
| `experiment-provenance-auditor` | [`experiment-provenance-auditor.md`](./experiment-provenance-auditor.md) |
| `limitations-failure-case-auditor` | [`limitations-failure-case-auditor.md`](./limitations-failure-case-auditor.md) |
| `scientific-figure-director` | [`scientific-figure-director.md`](./scientific-figure-director.md) |
| `paper-red-team-review` | [`paper-red-team-review.md`](./paper-red-team-review.md) |
| `reviewer-response-builder` | [`reviewer-response-builder.md`](./reviewer-response-builder.md) |
| `latex-submission-checker` | [`latex-submission-checker.md`](./latex-submission-checker.md) |
