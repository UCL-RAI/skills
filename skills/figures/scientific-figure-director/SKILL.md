---
name: scientific-figure-director
description: Plans, prompts, and audits scientific figures, diagrams, and GPT Image outputs for Robotics & AI papers. Use when the user asks where figures are needed, what figure to draw, how to prompt image generation, or whether a returned figure is scientifically valid.
---

# Scientific Figure Director

Use this for scientific visual planning and review, not decorative illustration.

## Inputs

- Manuscript section, method notes, result table, experiment setup, or draft figure.
- Desired figure role: explain, compare, diagnose, summarize, or persuade.
- Target output: figure plan, diagram spec, GPT Image prompt, plotting brief, or returned-figure audit.

If the scientific claim is unclear, define it before choosing a visual style.

## Workflow

1. Identify the figure's scientific job: method explanation, experimental setup, result comparison, failure case, taxonomy, or system pipeline.
2. Define the figure claim in one sentence.
3. Choose figure type:
   - pipeline or architecture diagram;
   - robot/system setup;
   - flowchart or decision process;
   - comparison table or matrix;
   - quantitative plot;
   - conceptual taxonomy.
4. Decide whether the figure should be generated, drawn as a diagram, plotted from data, or specified for a human designer.
5. Write a prompt or diagram spec that includes entities, relationships, arrow semantics, panel labels, constraints, and forbidden ambiguities.
6. Audit the generated figure against `references/figure-contract.md`.

## Figure Spec

```markdown
## Figure job
## Scientific claim
## Paper section
## Figure type
## Panels
| Panel | Content | Claim | Required labels |
| --- | --- | --- | --- |
## Entities and relationships
## Arrow semantics
## Data source or evidence
## Forbidden ambiguities
## Style constraints
```

## Prompt Contract

Every prompt should specify:

- target venue or paper context;
- exact entities and labels;
- arrow meaning;
- left-to-right or top-to-bottom logic;
- what must not appear;
- expected panel structure;
- style constraints appropriate for a scientific paper.

Do not ask an image model to invent exact plots, numeric values, paper-specific results, citations, robot hardware, or benchmark details. For quantitative results, request a plot specification or use real data.

## Returned Figure Audit

When the user returns an image, inspect:

- factual correctness;
- arrow direction and causal logic;
- label accuracy and spelling;
- visual hierarchy;
- overlap and readability;
- whether the figure supports the paper claim.

## Validation

- The figure claim matches a manuscript claim.
- Every visual element has a scientific role.
- Arrows distinguish data flow, control flow, causality, training, and inference.
- Labels are readable and technically accurate.
- The figure does not introduce unsupported mechanisms, results, or entities.

## Completion

Done means the figure plan or audit states whether the figure is acceptable, what must change, and why.
