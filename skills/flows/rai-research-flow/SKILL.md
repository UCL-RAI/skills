---
name: rai-research-flow
description: Routes Robotics & AI research work across search, reading, evidence mapping, ideation, paper writing, figure planning, and audits. Use when the user asks to enter a field, build a literature base, brainstorm a project, write a survey or paper, or coordinate multiple research skills.
disable-model-invocation: true
---

# RAI Research Flow

Use this as the user-facing router for Robotics & AI research work.

## Intake

Before routing, identify:

- research goal: onboarding, survey, ideation, experiment design, writing, figure work, or audit;
- domain and constraints: Robotics subfield, AI method family, hardware/simulator, timeline, venue, and available sources;
- evidence state: no sources, source list only, reading cards, matrix, draft, figures, or code/results;
- required artifact: onboarding map, search log, reading cards, matrix, idea cards, outline, figure plan, provenance audit, or review report.

If the user asks for "research help" without a concrete artifact, propose the smallest useful next artifact instead of starting a broad open-ended workflow.

## Route by Intent

| User intent | Route | Gate |
| --- | --- | --- |
| Inherit a folder, notes, paper list, or lab knowledge base | `knowledge-base-onboarding` | Source inventory and trust labels exist before synthesis. |
| Enter a new area | `paper-search-protocol` -> `paper-reading-card` -> `evidence-matrix-builder` | At least one reproducible search log before synthesis. |
| Build a survey | `evidence-matrix-builder` | Reading cards or source-grounded notes must exist, or missing coverage must be explicit. |
| Brainstorm a project | `research-idea-rubric` | Either an evidence matrix exists or the output must be labeled speculative. |
| Write a conference paper | `rai-paper-flow` | Contributions, evidence, and venue assumptions must be stated. |
| Position related work | `related-work-positioning` | Prior-work clusters and novelty boundaries use verified sources. |
| Audit experiments or results | `benchmark-audit` -> `experiment-provenance-auditor` | Claims map to result evidence and traceable runs. |
| Plan or audit figures | `scientific-figure-director` | Each figure needs a one-sentence scientific claim. |
| Review a draft | `citation-integrity-auditor` when citations are present, then `paper-red-team-review` | Do not style-polish unsupported claims. |

## Phase Gates

- **Discover before map**: do not build taxonomy from a thin or unlogged search.
- **Inventory before onboarding claims**: do not summarize a project folder or source set until source trust labels are explicit.
- **Map before ideate**: do not recommend projects from an unmapped field unless the user explicitly accepts speculative brainstorming.
- **Evidence before writing**: do not draft survey conclusions until the evidence matrix exists or missing evidence is stated.
- **Support before polish**: do not polish claims that lack support; mark them as unsupported and ask for evidence.
- **Trace before claim**: do not strengthen benchmark claims until result provenance and baseline fairness are checked.
- **Contract before figure**: do not treat a figure as valid until its scientific claim, entities, arrows, and labels pass review.

## Handoff Rules

- When switching skills, pass the current artifact paths or pasted content, not only the user's broad goal.
- Preserve uncertainty. If a source, result, or citation is unverified, carry that status into the next skill.
- Prefer one clear next artifact over multiple partial artifacts.
- Ask the user before starting a large search, full-paper review, or multi-skill survey if the scope is not bounded.

## Default Artifacts

Use these names unless the repo already has a convention:

```text
research/
|-- onboarding-map.md
|-- search-log.md
|-- reading-cards/
|-- evidence-matrix.csv
|-- idea-cards.md
|-- benchmark-audit.md
|-- provenance-audit.md
|-- figure-plan.md
`-- audit-report.md
```

## Completion

Finish with:

```markdown
## Research Flow Status
| Phase | Artifact | Status | Blocker |
| --- | --- | --- | --- |

## Subskills Used

## Next Best Step
```

Done means the chosen subskills were routed in a defensible order, every produced artifact is named, and any blocked gate is explicit.
