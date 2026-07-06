# Forward Test: Knowledge Base Onboarding

## Skill

`knowledge-base-onboarding`

## Prompt

Use `knowledge-base-onboarding` to map this inherited tactile manipulation project.

```text
tactile-project/
|-- papers/
|-- ros_ws/
|-- data/
|-- logs/
|-- figures/
`-- notes/meeting-notes.md
```

The user wants to know what exists, what can be trusted, and what to do next before writing a paper.

## Expected Artifact Checklist

- Includes a source inventory with type, location, trust status, and next action.
- Separates papers, code, data, logs, figures, and notes.
- Builds a concept map or states what is needed to build one.
- Builds an artifact map for evidence and missing context.
- Recommends next skills such as paper reading, evidence matrix, provenance audit, or coding flow.
- Does not claim sources were read if only inventoried.

## Pass Conditions

- The onboarding map is useful before deep synthesis.
- Trust labels distinguish verified, metadata-only, user-claim, stale, unknown, or equivalent states.
- The next actions are concrete and ordered.

## Fail Conditions

- The response summarizes papers or code content that was not inspected.
- The response skips provenance and trust labels.
- The response gives a vague "read everything" plan without artifacts.
