---
name: rai-paper-flow
description: Routes Robotics & AI conference paper writing for ICRA, RSS, CoRL, ICML, ICLR, and NeurIPS style submissions. Use when the user asks to outline, draft, revise, audit, rebut, package, or prepare a research paper for Robotics or AI venues.
disable-model-invocation: true
---

# RAI Paper Flow

Use this as the user-facing router for paper writing and revision.

Default to the smallest useful pass. Do not run a full paper audit unless the
user asks for it, the paper is near submission, or the next blocking issue
cannot be found with a lighter pass.

## Intake

Before routing, identify:

- mode: `quick`, `standard`, or `deep`; default to `quick` when unspecified;
- target venue family and page/format constraints if known;
- paper state: idea, remote project, experiment dossier, outline, partial draft,
  full draft, experiment package, camera-ready package, or review response;
- evidence state: experiments planned, running, complete, or missing;
- risky zones: novelty, related work, baselines, ablations, provenance, citations, figures, coherence, repetition, limitations, submission packaging, or writing clarity.

If the user asks for "make this paper better", first classify the paper state and choose one blocking artifact.

## Efficiency Modes

| Mode | Use when | Skill budget | Output |
| --- | --- | --- | --- |
| `quick` | Daily writing, section edits, "what should I fix next?", or early draft review. | 1-2 skills. Avoid detailed references unless needed. | Top blockers, direct edits, and one next action. |
| `standard` | Normal paper revision across structure, evidence, and prose. | 2-4 skills. Use references only for selected checks. | Focused audit tables plus repair plan. |
| `deep` | Pre-submission, rebuttal-critical, artifact release, or full-paper red team. | As many skills as needed. Load detailed references. | Full audit artifacts and residual-risk table. |

When mode is unclear, choose `quick` and say what a `standard` or `deep` pass would add.

## Daily Passes

Use these user-facing passes instead of exposing every atomic skill by default.

| Pass | Default route | Expand only when |
| --- | --- | --- |
| Draft pass | `venue-paper-outline` / `abstract-introduction-builder` / `related-work-positioning` / `manuscript-structure-auditor` / `scientific-writing-editor` | The draft lacks shape, positioning, coherence, or readable prose. |
| Survey pass | `evidence-matrix-builder` -> `survey-synthesis-builder` | The source base supports a taxonomy, synthesis claims, and section contracts. |
| Evidence handoff pass | `experiment-dossier-builder` -> `paper-draft-builder` | Results live on a remote machine or a completed dossier needs to become a story and draft. |
| Claim-evidence pass | `citation-integrity-auditor` / `benchmark-audit` / `limitations-failure-case-auditor` | Claims depend on citations, benchmark results, deployment scope, or limitations. |
| Reviewer-risk pass | `paper-red-team-review` | The user wants likely rejection risks or a harsh review. |
| Submission pass | `reviewer-response-builder` / `latex-submission-checker` | Reviews arrived, rebuttal is due, or source package is near submission. |

## Route by State

| Paper state | Route | Do not proceed until |
| --- | --- | --- |
| Goal, audience, scope, or deliverable is unresolved | `research-plan-grill` | The decision brief records the blocking choices and next paper artifact. |
| No clear contribution | `research-plan-grill` -> `research-idea-rubric` | The thesis, novelty claim, baselines, and falsification test are stated. |
| Code and results exist only in a remote project | `experiment-dossier-builder` on the remote machine | One portable dossier records the snapshot, method, result ledger, claims, failures, and evidence gaps. |
| Experiment dossier exists but no coherent draft exists | `paper-draft-builder` | The thesis, contributions, section plan, and major claims map to dossier evidence or visible TODOs. |
| Contribution exists but paper shape is unclear | `venue-paper-outline` | Each contribution maps to evidence and a paper section. |
| Abstract or introduction is weak, inflated, or missing | `abstract-introduction-builder` | Problem, gap, approach, evidence, contribution, and scope are explicit. |
| Related work does not defend novelty | `related-work-positioning` | Prior-work clusters and claim boundaries are source-grounded. |
| Experiment claims are central | `benchmark-audit` | Baselines, metrics, ablations, and result-claim support are audited. |
| Results must be reproducible or released | `experiment-provenance-auditor` | Paper numbers trace to code, configs, data, seeds, logs, and plots. |
| Method, configs, evaluation, or figures may disagree with code | `paper-code-consistency-auditor` | Material paper-code discrepancies have evidence, severity, and repair paths. |
| Draft exists with citations | `citation-integrity-auditor` | High-risk citation issues are marked before polishing. |
| Draft feels repetitive, disjointed, or hard to follow | `manuscript-structure-auditor` | The claim thread, repetition map, and structural repair actions are clear. |
| Draft needs grammar, concision, scientific tone, or less formulaic prose | `scientific-writing-editor` | Claims, citations, and structure have been checked or risk-labeled. |
| Figures or diagrams are missing or weak | `scientific-figure-director` | Each figure has a claim, section role, and audit result. |
| Limitations or failure cases are thin | `limitations-failure-case-auditor` | Assumptions, failures, and claims to narrow are explicit. |
| Draft is ready for attack | `paper-red-team-review` | Blocking and major issues have repair paths or evidence gaps. |
| Reviews or meta-review have arrived | `reviewer-response-builder` | Every reviewer point maps to a response action or manuscript change. |
| Source package is near submission | `latex-submission-checker` | Build, anonymity, venue, references, and packaging risks are checked. |
| Paper or project needs a talk | `slide-talk-builder` | The rendered deck fits audience, time, evidence, notes, and visual QA contracts. |

In `quick` mode, choose the first row that exposes a blocking issue and stop
after the smallest useful artifact. In `deep` mode, chain rows only when their
outputs are needed by the next check.

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

In `quick` mode, usually do not create files unless the user asks. In
`standard` or `deep` mode, use or create these artifacts when useful:

```text
paper/
|-- experiment-dossier.md
|-- story-brief.md
|-- paper-draft.md
|-- outline.md
|-- related-work-position.md
|-- abstract-intro-draft.md
|-- claim-evidence-map.md
|-- benchmark-audit.md
|-- provenance-audit.md
|-- paper-code-audit.md
|-- citation-audit.md
|-- structure-audit.md
|-- writing-edit.md
|-- figure-plan.md
|-- limitations-audit.md
|-- red-team-review.md
|-- reviewer-response-plan.md
|-- submission-check.md
`-- talk-storyboard.md
```

## Completion

For `quick` mode, finish with:

```markdown
## Top Fixes
1.
2.
3.

## Direct Edits or Repair Actions

## Next Best Pass
```

For `standard` or `deep` mode, finish with a paper status table:

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

Done means the mode and route are explicit, the next blocking paper artifact is identified, and unsupported claims are not silently rewritten.
