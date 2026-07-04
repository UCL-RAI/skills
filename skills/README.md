# Skills

Published skills live in this directory.

## Entry Points

Use these router skills first when the user goal spans several steps:

| Router | Use for |
| --- | --- |
| `flows/rai-research-flow` | Field onboarding, literature bases, survey planning, ideation, and research coordination. |
| `flows/rai-paper-flow` | Robotics & AI conference paper outlining, revision, figure planning, citation audit, and red-team review. |
| `flows/rai-coding-flow` | Research code implementation, debugging, testing, review, and reproducibility checks. |

Use atomic, reference, or tool skills directly when the user asks for one clear artifact, such as a search log, reading card, evidence matrix, figure plan, or citation audit.

## Lifecycle Map

| Phase | Skills |
| --- | --- |
| `DISCOVER` | `research/paper-search-protocol` |
| `MAP` | `research/paper-reading-card`, `research/evidence-matrix-builder` |
| `IDEATE` | `ideation/research-idea-rubric` |
| `DESIGN` | `figures/scientific-figure-director`, `engineering/robotics-ai-coding-flow` |
| `WRITE` | `writing/venue-paper-outline` |
| `AUDIT` | `writing/citation-integrity-auditor`, `review/paper-red-team-review` |
| `PACKAGE` | Planned for later release skills such as reviewer responses, slide decks, and reproducibility bundles. |

Current layout:

```text
skills/
|-- flows/
|   |-- rai-research-flow/
|   |-- rai-paper-flow/
|   `-- rai-coding-flow/
|-- research/
|   |-- paper-search-protocol/
|   |-- paper-reading-card/
|   `-- evidence-matrix-builder/
|-- ideation/
|   `-- research-idea-rubric/
|-- writing/
|   |-- venue-paper-outline/
|   `-- citation-integrity-auditor/
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
