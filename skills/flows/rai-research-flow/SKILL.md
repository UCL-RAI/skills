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
- required artifact: onboarding map, search log, reading cards, matrix, idea
  cards, experiment dossier, outline, paper draft, figure plan, provenance
  audit, or review report.

If the user asks for "research help" without a concrete artifact, propose the smallest useful next artifact instead of starting a broad open-ended workflow.

## Route by Intent

| User intent | Route | Gate |
| --- | --- | --- |
| Goal, scope, or deliverable remains ambiguous after inspecting available materials | `research-plan-grill` | A decision brief names the objective, constraints, evidence standard, and next artifact. |
| Inherit a folder, notes, paper list, or lab knowledge base | `knowledge-base-onboarding` | Source inventory and trust labels exist before synthesis. |
| Enter a new area | `paper-search-protocol` -> `paper-reading-card` -> `evidence-matrix-builder` | At least one reproducible search log before synthesis. |
| Build a survey | `evidence-matrix-builder` -> `survey-synthesis-builder` | Reading cards and traceable matrix rows exist before taxonomy or prose synthesis. |
| Brainstorm a project | `research-plan-grill` when key decisions are unresolved, then `research-idea-rubric` | Either an evidence matrix exists or the output must be labeled speculative. |
| Write a conference paper | `rai-paper-flow` | Contributions, evidence, and venue assumptions must be stated. |
| Position related work | `related-work-positioning` | Prior-work clusters and novelty boundaries use verified sources. |
| Audit experiments or results | `benchmark-audit` -> `experiment-provenance-auditor` | Claims map to result evidence and traceable runs. |
| Hand off a remote project for local writing | `experiment-dossier-builder` | The dossier records the inspected snapshot, result provenance, and missing evidence. |
| Turn a completed evidence handoff into a draft | `paper-draft-builder` | The story thesis and every major claim map to dossier results or verified literature. |
| Plan or audit figures | `scientific-figure-director` | Each figure needs a one-sentence scientific claim. |
| Build a lab, conference, journal-club, or project talk | `slide-talk-builder` | Audience, duration, takeaway, source package, and requested deck format are explicit. |
| Check whether a manuscript describes the implementation accurately | `paper-code-consistency-auditor` | Paper and code versions are identifiable and material discrepancies have repair owners. |
| Review a draft | `rai-paper-flow` in `quick` mode, then expand to citation or red-team checks only if needed | Do not style-polish unsupported claims. |

## Phase Gates

- **Discover before map**: do not build taxonomy from a thin or unlogged search.
- **Decide before execute**: do not start a costly search, experiment, or draft
  while its blocking scope or evaluation decisions remain implicit.
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
|-- survey-synthesis.md
|-- idea-cards.md
|-- benchmark-audit.md
|-- provenance-audit.md
|-- experiment-dossier.md
|-- story-brief.md
|-- paper-draft.md
|-- figure-plan.md
|-- paper-code-audit.md
|-- talk-storyboard.md
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
