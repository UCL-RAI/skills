# Skill Catalog

The catalog contains 28 reusable skills across the Robotics & AI research lifecycle. Machine-readable metadata and dependencies live in [`catalog.json`](../catalog.json).

All current skills are `draft`. See the [quality rubric](./quality-rubric.md) for maturity definitions and promotion evidence.

## Core Routers

| Skill | Purpose |
| --- | --- |
| `rai-research-flow` | Route research onboarding, surveys, ideation, writing, figures, and audits. |
| `rai-paper-flow` | Route conference-paper writing, review, rebuttal, and submission preparation. |
| `rai-coding-flow` | Route Robotics & AI coding, debugging, testing, review, and reproducibility work. |

## Discover and Map

| Skill | Purpose |
| --- | --- |
| `knowledge-base-onboarding` | Build a source inventory, concept map, artifact map, and next-action plan. |
| `paper-search-protocol` | Build reproducible search logs. |
| `paper-reading-card` | Create source-grounded single-paper cards. |
| `evidence-matrix-builder` | Build comparison matrices and gap maps. |
| `research-plan-grill` | Resolve an ambiguous research or engineering plan one decision at a time. |
| `research-idea-rubric` | Score and refine project ideas. |

## Write and Position

| Skill | Purpose |
| --- | --- |
| `venue-paper-outline` | Plan ICRA/RSS/CoRL/ICML/ICLR/NeurIPS-style papers. |
| `related-work-positioning` | Build source-grounded prior-work clusters and novelty boundaries. |
| `abstract-introduction-builder` | Draft abstracts and introductions from verified problem, gap, method, evidence, and scope. |
| `paper-draft-builder` | Turn an experiment dossier and verified literature into a coherent story brief and conference-paper draft. |
| `survey-synthesis-builder` | Turn verified literature into a defensible taxonomy, claim-evidence structure, and survey draft. |
| `scientific-writing-editor` | Edit grammar, clarity, concision, scientific tone, and generic AI-style prose patterns without changing technical claims. |
| `scientific-figure-director` | Plan, prompt, and audit scientific figures. |

## Audit and Review

| Skill | Purpose |
| --- | --- |
| `citation-integrity-auditor` | Check whether citations support claims. |
| `manuscript-structure-auditor` | Audit coherence, section flow, repetition, contradictions, and claim threading. |
| `benchmark-audit` | Audit benchmark fit, baselines, metrics, ablations, leakage risk, and claim-result alignment. |
| `experiment-provenance-auditor` | Trace paper results to code, configs, data, seeds, logs, hardware, and generated artifacts. |
| `experiment-dossier-builder` | Summarize a remote project, results, failures, and provenance into a portable Markdown handoff. |
| `paper-code-consistency-auditor` | Check whether manuscript descriptions, configs, evaluation, tables, and figures match the implementation. |
| `limitations-failure-case-auditor` | Audit limitations, assumptions, failure cases, negative results, and deployment risks. |
| `paper-red-team-review` | Perform a harsh, evidence-grounded paper review. |

## Package and Code

| Skill | Purpose |
| --- | --- |
| `reviewer-response-builder` | Build point-by-point reviewer responses and revision plans. |
| `latex-submission-checker` | Check LaTeX source packages for build, venue, anonymity, arXiv, and submission hygiene. |
| `slide-talk-builder` | Build timed, source-grounded research talks with a rendered deck, speaker notes, and visual QA. |
| `robotics-ai-coding-flow` | Apply Robotics & AI code quality checks. |

## Choosing a Skill

Start with a router when the task spans several lifecycle stages. Invoke an atomic skill directly when the required artifact is already clear. Use `quick` mode for routine paper work and expand to `standard` or `deep` only when risk or scope requires it.
