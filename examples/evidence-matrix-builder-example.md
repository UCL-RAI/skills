# Evidence Matrix Builder Example

## User Prompt

> I have six reading cards about robot learning for deformable object manipulation. Build a comparison matrix and tell me what research gaps are defensible.

## Expected Skill Behavior

The agent should use `evidence-matrix-builder`, inventory the cards, choose axes that match the research question, and separate source-grounded evidence from interpretation.

## Example Artifact Shape

```csv
id,title,year,venue,problem,method_family,robot_or_domain,dataset_or_simulator,baselines,metrics,main_result,limitations,code_or_data,gap_tags,notes
card-001,<title>,<year>,<venue>,cloth folding,<method family>,deformable object manipulation,<dataset/simulator>,<baselines>,<metrics>,<source-grounded result>,<reported limitation>,<code/data status>,weak-baseline;unclear-reproducibility,<trace to card section>
card-002,<title>,<year>,<venue>,rope manipulation,<method family>,deformable object manipulation,<dataset/simulator>,<baselines>,<metrics>,<source-grounded result>,<reported limitation>,<code/data status>,narrow-benchmark,<trace to card section>
```

## Example Synthesis Shape

```markdown
## Taxonomy
- Vision-only policy learning
- Tactile or force-aware manipulation
- Model-based planning for deformable objects

## Defensible gaps
| Gap | Evidence pattern | Affected rows | Confidence |
| --- | --- | --- | --- |
| Weak baseline coverage | Several cards compare only to simple heuristics or omit recent robot learning baselines | card-001, card-003 | medium |
| Narrow benchmark coverage | Most evidence uses one object family or simulator setup | card-002, card-004, card-006 | high |

## Claims requiring more evidence
- Whether any method transfers reliably across object categories.
- Whether real-robot latency or safety constraints were evaluated.
```

## Quality Checks

- Every row traces to a reading card or source.
- Gap tags describe missing or weak evidence, not personal preference.
- Cross-paper claims use row counts or explicit source references.
