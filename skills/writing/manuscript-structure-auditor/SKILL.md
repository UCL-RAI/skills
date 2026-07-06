---
name: manuscript-structure-auditor
description: Audits manuscript coherence, section flow, paragraph logic, repetition, contradictions, and claim threading. Use when the user asks whether a paper draft, section, abstract, introduction, related work, or conclusion is logically connected, non-redundant, and easy for reviewers to follow.
---

# Manuscript Structure Auditor

Use this before detailed sentence-level polishing.

## Inputs

- Manuscript, section, abstract, outline, or pasted paragraphs.
- Target venue or audience if known.
- User concern: coherence, repetition, paragraph logic, section order, claim thread, contradiction, or reviewer readability.
- Optional artifacts: claim-evidence map, citation audit, figure plan, or red-team review.

If only a short passage is provided, audit local paragraph logic and state that full-paper coherence is not checked.

## Workflow

1. Identify the unit under review: full manuscript, section, subsection, paragraph cluster, or abstract.
2. Extract the intended claim thread: problem -> gap -> contribution -> method -> evidence -> limitation.
3. Check section and paragraph jobs against `references/structure-checks.md`.
4. Mark repeated, redundant, contradictory, misplaced, or unsupported material.
5. Propose structural moves before sentence rewrites.
6. Produce a concise audit with severity and repair actions.

Read `references/structure-checks.md` when auditing more than one paragraph or when the user asks about coherence, repetition, or flow.

## Output

```markdown
## Claim Thread

## Structure Findings
| Severity | Location | Issue | Why it hurts the paper | Repair action |
| --- | --- | --- | --- | --- |

## Repetition Map
| Repeated idea | Locations | Keep | Remove or merge |
| --- | --- | --- | --- |

## Suggested Order

## Residual Risk
```

## Severity

- `blocking`: the argument is internally inconsistent or reviewers cannot identify the contribution.
- `major`: flow, repetition, or missing transitions materially weakens the paper.
- `minor`: local paragraph order or phrasing slows the reader.
- `nit`: small structural polish.

## Rules

- Do not rewrite the science to make the structure smoother.
- Do not delete repeated material unless one location can preserve the needed claim.
- Do not move claims ahead of the evidence or definitions needed to understand them.
- Do not treat every repeated term as redundancy; technical consistency often requires repeated terms.

## Validation

- Every structural issue has a location or quoted cue.
- Every proposed deletion or merge preserves the scientific claim.
- The audit separates structure problems from grammar/style problems.
- The proposed order follows the paper's evidence state, not just a preferred template.

## Completion

Done means the manuscript unit has a clear claim thread, repeated material is mapped, major coherence breaks have repair actions, and sentence-level editing can proceed without hiding structural problems.
