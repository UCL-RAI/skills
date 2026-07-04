---
name: paper-reading-card
description: Turns one Robotics & AI paper into a structured, source-grounded reading card. Use when the user asks to read, summarize, compare, or extract claims, methods, experiments, limitations, and reusable ideas from a paper.
---

# Paper Reading Card

Use this skill for one paper at a time.

## Inputs

- Paper PDF, URL, DOI, arXiv ID, OpenReview page, or pasted text.
- User goal: quick triage, deep reading, comparison, citation support, implementation extraction, or project relevance.
- Optional project context, target method family, or claim to verify.

If the source is unavailable or only metadata is available, produce a metadata-only card and mark missing fields as `not found`.

## Workflow

1. Verify bibliographic identity before summarizing.
2. Extract the problem, core claim, method, and evaluation setup.
3. Separate claims from evidence. Record what the paper demonstrates, not what the abstract implies.
4. Capture experiment details needed for comparison: datasets, simulators, robot platforms, baselines, metrics, ablations, seeds if available, and code/data links.
5. Identify limitations, failure cases, assumptions, and threats to validity.
6. Record reusable ideas and questionable points for `evidence-matrix-builder`.
7. Add citation notes only for claims the paper can actually support.

## Card Fields

```markdown
# Reading Card: <paper title>

## Bibliographic identity
- Title:
- Authors:
- Venue/year:
- DOI/arXiv/OpenReview:
- Code/data/project:

## Problem

## Core idea

## Claimed contributions

## Method

## Experimental setup
- Datasets/simulators/robots:
- Baselines:
- Metrics:
- Ablations:
- Sim-only, real-robot, or mixed:

## Main evidence
- What the paper directly supports:
- What remains unsupported or weak:

## Limitations and failure cases

## What is reusable

## What is questionable

## Relation to our project

## Citation notes
- Safe claims this paper can support:
- Claims this paper should not be used to support:
```

## Rules

- Separate what the paper claims from what the evidence actually shows.
- Mark missing information explicitly as `not found`, not as an inferred fact.
- Preserve exact identifiers for later citation auditing.
- For Robotics papers, capture whether results are simulation-only, real-robot, or mixed.
- Do not fill in baseline strength, code availability, dataset split, or hardware details from memory.
- If using the paper for implementation, extract enough detail to know whether reproduction is possible.

## Validation

- Bibliographic fields match the source.
- Every experiment summary names the task, metric, and baseline if the paper provides them.
- Every limitation is tied to the paper's text, experiments, or an explicit missing detail.
- Every citation note states whether support is direct, partial, background, unsupported, or unverified.

## Completion

Done means every required field is filled or explicitly marked `not found`, claims and evidence are separated, and the card can feed `evidence-matrix-builder` without guessing.
