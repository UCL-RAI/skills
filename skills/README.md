# Skills

Published skills live in this directory.

## Entry Points

Use these router skills first when the user goal spans several steps:

| Router | Use for |
| --- | --- |
| `flows/rai-research-flow` | Field onboarding, knowledge-base mapping, literature bases, survey planning, ideation, and research coordination. |
| `flows/rai-paper-flow` | Robotics & AI conference paper outlining, related-work positioning, experiment audit, revision, response, and submission checks. |
| `flows/rai-coding-flow` | Research code implementation, debugging, testing, review, and reproducibility checks. |

Use atomic, reference, or tool skills directly when the user asks for one clear artifact, such as a search log, reading card, evidence matrix, benchmark audit, provenance ledger, figure plan, citation audit, reviewer response, or submission check.

## Lifecycle Map

| Phase | Skills |
| --- | --- |
| `DISCOVER` | `research/knowledge-base-onboarding`, `research/paper-search-protocol` |
| `MAP` | `research/paper-reading-card`, `research/evidence-matrix-builder` |
| `IDEATE` | `ideation/research-idea-rubric` |
| `DESIGN` | `figures/scientific-figure-director`, `engineering/robotics-ai-coding-flow` |
| `WRITE` | `writing/venue-paper-outline`, `writing/related-work-positioning`, `writing/abstract-introduction-builder`, `writing/scientific-writing-editor` |
| `AUDIT` | `writing/citation-integrity-auditor`, `writing/manuscript-structure-auditor`, `writing/limitations-failure-case-auditor`, `evaluation/benchmark-audit`, `evaluation/experiment-provenance-auditor`, `review/paper-red-team-review` |
| `PACKAGE` | `writing/reviewer-response-builder`, `writing/latex-submission-checker` |

Current layout:

```text
skills/
|-- flows/
|   |-- rai-research-flow/
|   |-- rai-paper-flow/
|   `-- rai-coding-flow/
|-- research/
|   |-- knowledge-base-onboarding/
|   |-- paper-search-protocol/
|   |-- paper-reading-card/
|   `-- evidence-matrix-builder/
|-- ideation/
|   `-- research-idea-rubric/
|-- writing/
|   |-- venue-paper-outline/
|   |-- related-work-positioning/
|   |-- abstract-introduction-builder/
|   |-- citation-integrity-auditor/
|   |-- manuscript-structure-auditor/
|   |-- scientific-writing-editor/
|   |-- limitations-failure-case-auditor/
|   |-- reviewer-response-builder/
|   `-- latex-submission-checker/
|-- evaluation/
|   |-- benchmark-audit/
|   `-- experiment-provenance-auditor/
|-- figures/
|   `-- scientific-figure-director/
|-- review/
|   `-- paper-red-team-review/
`-- engineering/
    `-- robotics-ai-coding-flow/
```

Each published skill must have a matching entry in `../catalog.json`.

The preferred skill shape is:

```text
skill-name/
|-- SKILL.md
|-- references/
|   `-- optional-reference.md
|-- scripts/
|   `-- optional-helper.py
`-- assets/
    `-- optional-template.ext
```

Do not add per-skill README files unless there is a strong reason. The skill itself should be the agent-facing entry point.
