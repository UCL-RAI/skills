# Structure Checks

Use this reference for coherence, repetition, paragraph logic, and reviewer readability audits.

## Claim Thread

A paper should make the main argument traceable:

```text
problem -> gap -> contribution -> method -> evidence -> limitation
```

For each section, ask:

- What job does this section perform?
- Which claim does it advance?
- What evidence or setup does the next section need from it?
- What would break if this section were removed?

## Paragraph Jobs

| Paragraph job | Useful cue | Common failure |
| --- | --- | --- |
| Motivation | Why the problem matters | Generic importance without field-specific stakes |
| Gap | What prior work cannot do | Gap appears before prior work is scoped |
| Contribution | What this paper adds | Multiple claims mixed into one vague sentence |
| Method setup | What assumptions and objects exist | Terms appear before definition |
| Evidence | What experiment/result supports | Results stated without metric or baseline context |
| Limitation | What remains unproven | Limitation hidden as future work |

## Repetition Types

| Type | Keep or remove |
| --- | --- |
| Necessary term repetition | Keep for technical consistency. |
| Repeated motivation | Keep the strongest version; remove weaker restatements. |
| Repeated contribution claim | Keep in introduction and conclusion; merge duplicates elsewhere. |
| Repeated method description | Keep detailed version in method; keep only signposts elsewhere. |
| Repeated result claim | Keep where evidence is shown; use concise cross-reference elsewhere. |

## Coherence Failure Modes

- The contribution changes wording or scope across sections.
- A paragraph contains multiple unrelated jobs.
- A transition claims continuity but changes topic.
- A claim appears before definitions, setup, or evidence.
- A section repeats earlier text without narrowing, deepening, or supporting it.
- Limitations contradict claims made in the introduction or abstract.
- Related work summarizes papers but does not position the gap.

## Repair Actions

- `merge`: combine duplicate paragraphs or claims.
- `move`: relocate a claim after needed setup or evidence.
- `split`: separate overloaded paragraph jobs.
- `delete`: remove text that adds no new claim, evidence, or transition.
- `narrow`: reduce claim scope to match evidence.
- `add-transition`: make the logical dependency explicit.
- `rename-thread`: use one stable term for the same concept.
