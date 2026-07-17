---
name: paper-draft-builder
description: Turns an experiment dossier, verified literature, and venue constraints into a coherent source-grounded conference paper story and Markdown or LaTeX draft. Use when a local writing environment has research results but needs a defensible narrative, contribution structure, section drafting, or a first full paper draft without inventing evidence or citations.
---

# Paper Draft Builder

Use this after remote project evidence has been condensed into an experiment
dossier. Build the scientific story before drafting prose, and preserve all
uncertainty carried by the handoff.

Read `references/draft-contract.md` before producing a full draft.

## Inputs

- Required: experiment dossier or equivalent claim/result/provenance package.
- Required for citation-bearing prose: verified bibliography, paper cards, or
  evidence matrix. A title list alone is not enough to assert prior-work facts.
- Optional: target venue/template, page budget, existing manuscript, figure
  assets, author preferences, and requested output format.

Default to Markdown. Use LaTeX only when the user supplies a template or asks
for it. If the dossier is incomplete, draft around verified evidence and mark
gaps; do not reconstruct missing experiments from context.

## Workflow

1. Validate the handoff: identify snapshot, result ledger, claim-evidence
   links, provenance statuses, limitations, and missing evidence.
2. Separate three layers: observed evidence, defensible interpretation, and
   proposed paper framing. Never silently promote one layer into another.
3. Write a story brief with one central thesis, the reader's problem, the
   precise gap, the technical insight, contributions, evidence sequence, and
   scope boundary. Reject a story that needs unsupported novelty or results.
4. Build a claim-evidence plan. Every major contribution and conclusion must
   map to dossier result ids, verified citations, or an explicit evidence gap.
5. Select the paper structure and page budget with `venue-paper-outline` when
   venue constraints matter. Assign one job and one takeaway to each section.
6. Plan figures and tables as part of the argument. Introduce each result only
   after the question and evaluation protocol it answers are clear.
7. Draft in dependency order: method and experiments first, then results,
   limitations, introduction, related work, abstract, and conclusion. Adapt
   the order when revising an existing manuscript.
8. Use `related-work-positioning` for novelty boundaries and
   `citation-integrity-auditor` before presenting citation-bearing claims as
   verified. Never generate bibliographic facts from memory.
9. Use `benchmark-audit` or `limitations-failure-case-auditor` when the dossier
   exposes fairness, coverage, failure, or scope risks that affect the story.
10. Run a final consistency pass across thesis, contributions, terminology,
    result values, figure references, limitations, and conclusion.

## Missing-Evidence Syntax

Use explicit author-facing markers in drafts:

- `[TODO: evidence needed - ...]`
- `[TODO: citation needed - ...]`
- `[UNVERIFIED: dossier status ambiguous - ...]`
- `[AUTHOR DECISION: ...]`

Do not hide these markers with polished filler. Keep them out of text claimed
to be submission-ready.

## Efficiency Modes

- `quick`: produce or revise the story brief and one requested section.
- `standard`: produce the story brief, claim-evidence plan, and focused draft.
- `deep`: produce a full draft and run cross-section consistency checks.

Default to `standard` when the user asks for a paper draft, and `quick` for one
section. Do not invoke every dependent skill unless its gate is actually hit.

## Outputs

For a full drafting task, create:

```text
paper/
|-- story-brief.md
`-- paper-draft.md        # or the user-requested LaTeX source
```

Keep evidence gaps in the story brief and inline markers unless a separate
repair plan is requested. Avoid generating multiple overlapping audit files.

## Rules

- Do not invent results, experiment settings, mechanisms, citations, or venue
  requirements.
- Do not call a contribution novel until verified related work supports the
  boundary.
- Do not choose a story by headline score alone; account for robustness,
  ablations, failures, and scope.
- Do not erase negative results that materially qualify the central claim.
- Preserve exact values, units, uncertainty, and evaluation conditions from
  the dossier.
- Do not turn implementation details into contributions unless the paper's
  evidence demonstrates their scientific importance.
- Prefer one coherent thesis over a list of loosely related improvements.

## Validation

- The thesis is supported by the claim-evidence plan.
- Every contribution has evidence and a clear section/figure destination.
- Every reported result matches the dossier's value, condition, and status.
- Citation-bearing claims use supplied and verified sources or carry TODOs.
- Abstract, introduction, results, limitations, and conclusion express the
  same scope and do not contradict one another.
- Missing evidence remains visible to the author.

## Completion

Done means the story brief is defensible, the requested draft exists in the
chosen format, major claims trace to evidence, and unresolved gaps are visible
rather than fabricated away.
