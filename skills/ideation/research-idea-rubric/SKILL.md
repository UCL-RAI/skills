---
name: research-idea-rubric
description: Scores and refines Robotics & AI project ideas for novelty, feasibility, baselines, evaluation, risk, and publishability. Use when brainstorming, ranking, stress-testing, or improving research ideas with or without the user.
---

# Research Idea Rubric

Use this to turn vague ideas into testable project candidates.

## Inputs

- One or more ideas, research directions, paper gaps, project constraints, or user goals.
- Available resources: time, compute, robot hardware, simulators, datasets, team expertise, and venue target if known.
- Evidence state: prior literature matrix, reading cards, rough intuition, or no evidence.

If evidence is missing, label the evaluation as assumption-based and recommend the fastest evidence-gathering step.

## Idea Card

```markdown
# Idea: <name>

## One-sentence thesis

## Motivation

## Novelty claim

## Why now

## Method sketch

## Baselines

## Evaluation plan
- Tasks:
- Metrics:
- Datasets/simulators/robots:
- Ablations:

## Required resources

## Risks

## Fastest falsification test

## Likely venue fit

## Decision
- Keep, revise, park, or reject:
- Reason:
```

## Workflow

1. Restate the idea as a falsifiable thesis.
2. Identify the smallest empirical claim that would make the idea worth pursuing.
3. Name the closest baselines and what would count as a fair comparison.
4. Score the idea using the rubric below.
5. Stress-test the idea against novelty, feasibility, evaluation, and reviewer objections.
6. Recommend keep, revise, park, or reject, with a next action.

Read `references/idea-stress-tests.md` when ranking multiple ideas or making a go/no-go recommendation.

## Score Each Idea

Use 1-5 scores, with short evidence.

| Dimension | Question |
| --- | --- |
| Novelty | Is this more than a recombination of obvious components? |
| Feasibility | Can a student team test the core claim with available compute, hardware, and time? |
| Evaluation | Are baselines, metrics, and tasks clear enough to falsify the idea? |
| Robotics relevance | Does it matter for embodied systems, control, perception, planning, or robot learning? |
| Publishability | Could it plausibly fit ICRA, RSS, CoRL, ICML, ICLR, or NeurIPS after execution? |
| Risk | What could make the result unpublishable? |

## Output

For multiple ideas, include:

```markdown
| Idea | Novelty | Feasibility | Evaluation | Robotics relevance | Publishability | Risk | Decision |
| --- | --- | --- | --- | --- | --- | --- | --- |
```

For one idea, include the idea card plus the top three risks and the fastest falsification test.

## Quality Gates

- Do not recommend an idea solely because it sounds novel; state what prior work must be checked.
- Do not treat "we can implement it" as publishability.
- Do not accept evaluation plans without baselines, metrics, and a failure criterion.
- Do not hide hardware, compute, dataset, or time constraints.

## Completion

Done means each idea has a decision, scores with evidence or assumptions, a fair evaluation path, and either a fastest falsification test or a reason to reject/park it.
