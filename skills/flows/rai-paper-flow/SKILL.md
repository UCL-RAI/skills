---
name: rai-paper-flow
description: Routes Robotics & AI conference paper writing for ICRA, RSS, CoRL, ICML, ICLR, and NeurIPS style submissions. Use when the user asks to outline, draft, revise, audit, or prepare a research paper for Robotics or AI venues.
disable-model-invocation: true
---

# RAI Paper Flow

Use this as the user-facing router for paper writing and revision.

## Intake

Before routing, identify:

- target venue family and page/format constraints if known;
- paper state: idea, outline, partial draft, full draft, camera-ready package, or review response;
- evidence state: experiments planned, running, complete, or missing;
- risky zones: novelty, baselines, ablations, citations, figures, limitations, or writing clarity.

If the user asks for "make this paper better", first classify the paper state and choose one blocking artifact.

## Route by State

| Paper state | Route | Do not proceed until |
| --- | --- | --- |
| No clear contribution | `research-idea-rubric` | The thesis, novelty claim, baselines, and falsification test are stated. |
| Contribution exists but paper shape is unclear | `venue-paper-outline` | Each contribution maps to evidence and a paper section. |
| Draft exists with citations | `citation-integrity-auditor` | High-risk citation issues are marked before polishing. |
| Figures or diagrams are missing or weak | `scientific-figure-director` | Each figure has a claim, section role, and audit result. |
| Draft is ready for attack | `paper-red-team-review` | Blocking and major issues have repair paths or evidence gaps. |

## Venue Stance

Target Robotics & AI conference norms, not Nature-style journal prose by default. Prioritize:

- problem formulation and contribution clarity;
- method reproducibility;
- baselines and ablations;
- benchmark or robot setup validity;
- limitations and failure cases;
- concise related-work positioning.

## Paper Gates

- Do not strengthen novelty language until related work and baselines support it.
- Do not hide weak experiments with writing edits; label missing baselines, metrics, ablations, or failure cases.
- Do not generate citations or bibliographic details from memory.
- Do not accept figures that imply mechanisms, causal arrows, or system behavior not supported by the text.
- Do not optimize for one venue's style if the target venue is unknown; state venue assumptions.

## Handoff Artifacts

Use or create these artifacts when useful:

```text
paper/
|-- outline.md
|-- claim-evidence-map.md
|-- citation-audit.md
|-- figure-plan.md
`-- red-team-review.md
```

## Completion

Finish with a paper status table:

```markdown
| Area | Status | Blocking issue |
| --- | --- | --- |
| Contribution | | |
| Method | | |
| Experiments | | |
| Figures | | |
| Citations | | |
| Writing | | |
```

Done means the route is explicit, the next blocking paper artifact is identified, and unsupported claims are not silently rewritten.
