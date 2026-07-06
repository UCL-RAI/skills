---
name: rai-paper-flow
description: Routes Robotics & AI conference paper writing for ICRA, RSS, CoRL, ICML, ICLR, and NeurIPS style submissions. Use when the user asks to outline, draft, revise, audit, rebut, package, or prepare a research paper for Robotics or AI venues.
disable-model-invocation: true
---

# RAI Paper Flow

Use this as the user-facing router for paper writing and revision.

## Intake

Before routing, identify:

- target venue family and page/format constraints if known;
- paper state: idea, outline, partial draft, full draft, experiment package, camera-ready package, or review response;
- evidence state: experiments planned, running, complete, or missing;
- risky zones: novelty, related work, baselines, ablations, provenance, citations, figures, coherence, repetition, limitations, submission packaging, or writing clarity.

If the user asks for "make this paper better", first classify the paper state and choose one blocking artifact.

## Route by State

| Paper state | Route | Do not proceed until |
| --- | --- | --- |
| No clear contribution | `research-idea-rubric` | The thesis, novelty claim, baselines, and falsification test are stated. |
| Contribution exists but paper shape is unclear | `venue-paper-outline` | Each contribution maps to evidence and a paper section. |
| Abstract or introduction is weak, inflated, or missing | `abstract-introduction-builder` | Problem, gap, approach, evidence, contribution, and scope are explicit. |
| Related work does not defend novelty | `related-work-positioning` | Prior-work clusters and claim boundaries are source-grounded. |
| Experiment claims are central | `benchmark-audit` | Baselines, metrics, ablations, and result-claim support are audited. |
| Results must be reproducible or released | `experiment-provenance-auditor` | Paper numbers trace to code, configs, data, seeds, logs, and plots. |
| Draft exists with citations | `citation-integrity-auditor` | High-risk citation issues are marked before polishing. |
| Draft feels repetitive, disjointed, or hard to follow | `manuscript-structure-auditor` | The claim thread, repetition map, and structural repair actions are clear. |
| Draft needs grammar, concision, scientific tone, or less formulaic prose | `scientific-writing-editor` | Claims, citations, and structure have been checked or risk-labeled. |
| Figures or diagrams are missing or weak | `scientific-figure-director` | Each figure has a claim, section role, and audit result. |
| Limitations or failure cases are thin | `limitations-failure-case-auditor` | Assumptions, failures, and claims to narrow are explicit. |
| Draft is ready for attack | `paper-red-team-review` | Blocking and major issues have repair paths or evidence gaps. |
| Reviews or meta-review have arrived | `reviewer-response-builder` | Every reviewer point maps to a response action or manuscript change. |
| Source package is near submission | `latex-submission-checker` | Build, anonymity, venue, references, and packaging risks are checked. |

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
- Do not summarize benchmark wins before checking baseline fairness and provenance.
- Do not generate citations or bibliographic details from memory.
- Do not accept figures that imply mechanisms, causal arrows, or system behavior not supported by the text.
- Do not sentence-polish text before checking citation support, structure, and repeated claims when those are in scope.
- Do not promise AI-detector evasion; reduce generic, inflated, and formulaic prose while preserving scientific meaning.
- Do not promise rebuttal changes, camera-ready edits, or artifact releases that cannot be verified.
- Do not optimize for one venue's style if the target venue is unknown; state venue assumptions.

## Handoff Artifacts

Use or create these artifacts when useful:

```text
paper/
|-- outline.md
|-- related-work-position.md
|-- abstract-intro-draft.md
|-- claim-evidence-map.md
|-- benchmark-audit.md
|-- provenance-audit.md
|-- citation-audit.md
|-- structure-audit.md
|-- writing-edit.md
|-- figure-plan.md
|-- limitations-audit.md
|-- red-team-review.md
|-- reviewer-response-plan.md
`-- submission-check.md
```

## Completion

Finish with a paper status table:

```markdown
| Area | Status | Blocking issue |
| --- | --- | --- |
| Contribution | | |
| Method | | |
| Experiments | | |
| Provenance | | |
| Figures | | |
| Citations | | |
| Related Work | | |
| Limitations | | |
| Structure | | |
| Writing | | |
| Submission Package | | |
```

Done means the route is explicit, the next blocking paper artifact is identified, and unsupported claims are not silently rewritten.
