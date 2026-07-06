# Knowledge Base Onboarding Example

## User Prompt

> I inherited a folder with papers, ROS code, experiment logs, and notes for tactile manipulation. Help me understand what is there.

## Example Input

```text
project/
|-- papers/
|-- ros_ws/
|-- logs/
|-- notes/meeting-notes.md
`-- figures/
```

## Expected Skill Behavior

The agent should use `knowledge-base-onboarding`, inventory sources, label trust, build a concept/artifact map, and route next actions.

## Example Output Shape

```markdown
## Source Inventory
| Source | Type | Location | Trust | Next action |
| --- | --- | --- | --- | --- |
| papers/ | paper set | local folder | unknown | run paper-search or reading-card pass |
| ros_ws/ | code | local folder | unknown | inspect package boundaries |
| logs/ | experiment | local folder | unknown | run provenance audit |

## Recommended Next Skills
- `paper-reading-card` for key papers.
- `experiment-provenance-auditor` for logs.
- `robotics-ai-coding-flow` for ROS package review.
```

## Quality Checks

- Does not claim papers were read when only inventoried.
- Separates verified facts from user-provided context.
- Produces concrete next actions.
