# Figure Contract

Use this checklist for prompt generation and figure audit.

## Scientific Contract

- What claim does the figure support?
- Which paper section will use it?
- What evidence or mechanism does it reveal better than text?
- Does every arrow have an explicit meaning?
- Are visual groupings scientifically meaningful or merely aesthetic?

## Figure Types

| Type | Use when | Common failure |
| --- | --- | --- |
| Method pipeline | The paper needs to explain computation or data/control flow. | Arrows imply causality or temporal order incorrectly. |
| Robot/system setup | The paper needs to show hardware, sensors, environment, or task geometry. | Setup omits frame, sensor, or sim/real boundary. |
| Architecture diagram | The paper needs model/module structure. | Blocks are generic and do not reveal the actual contribution. |
| Result plot | The paper needs quantitative comparison. | Plot is generated without real data or uncertainty. |
| Failure case panel | The paper needs limitations or qualitative diagnosis. | Example is cherry-picked without context. |
| Taxonomy | The paper needs survey or design-space structure. | Categories overlap or are not exhaustive enough for the claim. |

## Diagram Logic

- Arrows should not imply causality unless causality is intended.
- Feedback loops need clear loop closure and update signal.
- Parallel branches need comparable semantics.
- Data flow, control flow, and training/inference flow should not be mixed without labels.
- If simulation and real robot stages both appear, the boundary must be explicit.
- Coordinate frames, sensors, actuators, or world/robot/object entities must be labeled when relevant.
- Training-only components must not appear in inference-time diagrams without clear separation.

## Visual QA

- No overlapping labels or shapes.
- Text is readable at paper-column scale.
- Panel labels are consistent.
- Colors do not carry undocumented meaning.
- The figure can be understood in grayscale unless color is essential.
- Captions do not claim more than the figure shows.

## Audit Verdicts

- `accept`: scientifically correct and readable; only polish remains.
- `revise`: useful structure but specific labels, arrows, panels, or hierarchy must change.
- `reject`: figure implies false science, invents evidence, or cannot be repaired without redesign.
