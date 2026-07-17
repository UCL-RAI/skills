---
name: slide-talk-builder
description: Builds timed, source-grounded research talks and validated slide decks from papers, surveys, experiment dossiers, or project artifacts. Use when preparing a lab meeting, journal club, conference spotlight or oral, invited talk, project update, thesis presentation, or paper-to-slides conversion with speaker notes, visual assets, and delivery timing.
---

# Slide Talk Builder

Build a talk for an audience and time budget, not a paper pasted onto slides.
Produce the requested deck format when tooling is available and validate the
rendered slides before claiming completion.

Read `references/talk-contract.md` before generating a full deck.

## Inputs

- Source paper, survey, manuscript, experiment dossier, result artifacts, or
  project status package.
- Talk context: audience, purpose, duration, format, venue, room/online mode,
  and expected Q&A.
- Required template, aspect ratio, branding, author/affiliation details, output
  format, and available figures or media.
- Optional existing deck, speaker style, demo plan, and accessibility needs.

If duration or audience is unknown, resolve them before building the deck.

## Workflow

1. Verify the source thesis, contributions, evidence, figures, limitations,
   author details, and citation metadata. Mark unsupported material before it
   reaches a slide.
2. Define one audience takeaway and a talk contract: opening problem, narrative
   beats, evidence sequence, ending, duration, and Q&A/backup policy.
3. Allocate time by narrative beat, then set a slide budget. Prefer fewer
   readable slides over a fixed slides-per-minute formula.
4. Write a storyboard. Give every slide one job, one assertion-style headline,
   one primary visual or evidence object, timing, and transition.
5. Select or create assets from source-grounded figures, plots, diagrams,
   tables, demos, or photos. Redraw dense paper figures when necessary; do not
   misrepresent values, axes, mechanisms, or experimental conditions.
   Use `scientific-figure-director` when a new scientific diagram needs its
   own claim and visual contract.
6. Generate the deck in the requested format using available presentation
   tooling or the supplied template. Add speaker notes with the key point,
   evidence explanation, timing, and transition for every substantive slide.
7. Add backup slides for likely technical questions, additional results,
   limitations, and demo failure recovery when appropriate.
8. Render the deck and inspect every slide at presentation resolution. Fix
   overflow, clipping, unreadable plots, low contrast, inconsistent alignment,
   missing assets, citation omissions, and text-heavy layouts.
9. Rehearse against the timing budget using notes length and slide complexity.
   Cut content when the talk cannot fit; do not solve timing by speaking faster.
10. Deliver the deck, notes or script, asset manifest, timing table, and known
    residual risks.

## Talk Types

- `journal-club`: emphasize paper question, method, evidence, limitations, and
  discussion prompts.
- `project-update`: emphasize decisions, progress, failures, blockers, and next
  experiments.
- `spotlight`: communicate one problem, insight, method, result, and takeaway.
- `conference-oral`: build a complete contribution and evidence arc.
- `invited-or-thesis`: add field context, multiple evidence arcs, and deeper
  implications without losing the central thesis.

Treat these as narrative constraints, not rigid slide templates.

## Outputs

```text
talk/
|-- talk-contract.md
|-- storyboard.md
|-- deck.<pptx|pdf|html|key|tex>
|-- speaker-notes.md        # when notes are not embedded
|-- assets/
`-- render/                 # slide images or PDF used for QA
```

If deck-generation tooling is unavailable, produce the contract and storyboard
but state clearly that no validated deck was created.

## Rules

- Do not invent results, citations, affiliations, venue details, demos, links,
  or future commitments.
- Use `citation-integrity-auditor` when a slide claim cannot be verified from
  the supplied source package.
- Do not copy paper paragraphs or shrink dense paper figures until they fit.
- Do not show more precision, significance, or generality than the source
  evidence supports.
- Keep equations only when the audience needs them for the next idea.
- Label conceptual diagrams and author proposals as such.
- Preserve visual hierarchy, readable type, contrast, units, axes, legends,
  and source attribution.
- Never claim the deck is finished without render inspection.

## Validation

- The talk has one audience takeaway and a timed narrative arc.
- Every slide has a distinct job and supports the previous/next transition.
- Scientific claims and visuals trace to supplied sources.
- Rendered slides have no clipping, overlap, missing assets, or unreadable text.
- Notes fit the timing budget and identify high-risk transitions or demos.
- The ending states the supported takeaway and introduces no new claim.

## Completion

Done means the requested deck renders correctly, fits the talk contract, has
usable notes and source-grounded visuals, and records any unvalidated media,
timing, or environment risk.
