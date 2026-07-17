---
name: scientific-writing-editor
description: Edits academic paper prose for grammar, clarity, concision, scientific tone, reviewer readability, and removal of generic AI-style writing patterns while preserving technical claims. Use after claims, citations, and structure are checked, or when the user asks for grammar editing, human-sounding scientific prose, concise rewriting, or rigorous paper polishing.
---

# Scientific Writing Editor

Use this for sentence-level and paragraph-level editing after structure and evidence risks are visible.

## Inputs

- Text to edit: abstract, introduction, related work, method, experiments, conclusion, rebuttal, or cover letter.
- Target venue or style preference if known.
- Desired edit strength: minimal pass, light grammar pass, concision pass, scientific tone pass, or substantial rewrite.
- Optional writing sample from the user for voice calibration.
- Constraints: preserve terminology, equations, citations, numbers, baselines, limitations, and claim scope.

If the user asks to "lower AI rate", reframe the task as removing generic, inflated, or formulaic prose and improving authentic scientific voice. Do not promise AI-detector evasion.

## Workflow

1. Identify the edit mode and preserve non-negotiable technical content.
2. If the user provides a writing sample, calibrate sentence length, transition style, punctuation habits, and terminology level before editing.
3. Read `references/style-rules.md` for standard or deep edits; skip it for minimal local edits unless the text has obvious formulaic prose.
4. Mark or mentally separate facts, claims, citations, numbers, equations, and terminology before rewriting.
5. Edit for grammar, clarity, concision, and scientific tone.
6. Remove generic AI-style patterns: inflated transitions, repetitive framing, vague intensifiers, unsupported certainty, superficial `-ing` phrases, rule-of-three padding, and vague authority claims.
7. Do a final "AI-style tell" audit and revise remaining formulaic phrasing.
8. Provide either a clean rewrite, an edit table, or both, depending on user need.
9. Flag any claim that seems unsupported instead of silently polishing it.

## Output Modes

Use the mode that best fits the request:

Minimal output for daily editing:

```markdown
## Clean Rewrite

## Notes
- [only claim risks or wording changes the user must know]
```

Standard output when the user asks for rationale or a heavier edit:

```markdown
## Clean Rewrite

## Remaining AI-Style Tells Checked

## Change Notes
| Issue | Original cue | Edit rationale |
| --- | --- | --- |

## Claims Not Edited Because Evidence Is Needed
```

For grammar-only requests, keep the output minimal and avoid broad rewriting.

## Rules

- Do not change scientific meaning, claim strength, metric values, citations, equations, or terminology unless explicitly asked.
- Do not make the prose sound more confident than the evidence supports.
- Do not optimize for or guarantee AI-detector scores.
- Do not remove necessary technical repetition.
- Do not replace precise terms with vague synonyms for variety.
- Do not add casual personality, first person, humor, or rhetorical edge unless appropriate for the manuscript genre.
- Preserve British or American spelling if the draft already uses one consistently.

## Validation

- The edited text preserves all original technical claims unless changes are explicitly listed.
- Grammar and clarity improve without adding new facts.
- Redundant or generic phrasing is reduced.
- For minimal edits, only necessary claim risks or wording caveats are listed.
- For standard or deep edits, remaining AI-style tells are checked after the first rewrite.
- Scientific uncertainty remains visible.
- Any unsupported claim is flagged rather than polished.

## Completion

Done means the chosen edit depth is explicit, the prose is cleaner and technically faithful, and unsupported claims are flagged rather than polished.
