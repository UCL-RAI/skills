# Scientific Writing Editor Example

## User Prompt

> Edit this abstract paragraph for grammar, concision, scientific tone, and less generic AI-style wording. Do not change technical claims or invent stronger evidence.

## Example Input

```markdown
In recent years, robot learning has become a very important topic, highlighting the need for robust, efficient, and scalable systems. We propose a novel and comprehensive framework that is able to significantly improve long-horizon manipulation—not only improving performance but also enabling real-world deployment. Recent studies show that such methods are crucial for embodied AI. Experiments demonstrate strong improvements over baselines.
```

## Expected Skill Behavior

The agent should use `scientific-writing-editor`, preserve technical claim scope, remove unsupported confidence, and avoid promising AI-detector evasion.

## Example Output Shape

```markdown
## Clean Rewrite

Robot learning for long-horizon manipulation requires policies that can complete multi-step tasks reliably. We propose a framework for decomposing manipulation tasks into subgoals and evaluating policy performance against baseline methods. Experiments show improvements on the tested tasks; broader real-world deployment remains to be established.

## Remaining AI-Style Tells Checked
- Removed generic opening and inflated significance language.
- Removed unsupported deployment and novelty language.
- Removed rhetorical "not only ... but also" construction.
- Flagged vague attribution instead of turning it into an unsupported citation claim.

## Change Notes
| Issue | Original cue | Edit rationale |
| --- | --- | --- |
| generic opening | "In recent years" | removed because no time trend is used |
| superficial `-ing` phrase | "highlighting the need" | removed because it adds no evidence |
| unsupported novelty/intensity | "novel and comprehensive", "significantly" | narrowed unless citation/statistical support is provided |
| deployment overclaim | "enabling real-world deployment" | changed to explicit remaining evidence need |
| vague attribution | "Recent studies show" | flagged because no specific source is provided |

## Claims Not Edited Because Evidence Is Needed
- Whether the method is novel.
- Whether improvements are statistically significant.
- Whether the system is robust in real-world deployment.
- Which studies support the embodied AI motivation claim.
```

## Quality Checks

- Numbers, citations, baselines, and technical terms are preserved or explicitly flagged.
- The rewrite is more concise and scientific.
- Unsupported claims are narrowed or flagged, not made smoother.
