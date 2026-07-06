# Forward Test: Scientific Writing Editor

## Skill

`scientific-writing-editor`

## Prompt

Use `scientific-writing-editor` to edit this abstract paragraph for grammar, concision, scientific tone, and less generic AI-style wording. Preserve all technical claims and do not promise AI-detector evasion.

```markdown
In recent years, robot learning has become increasingly important, highlighting the crucial role of robust, efficient, and scalable systems. In this paper, we propose a novel and comprehensive framework that is able to significantly improve long-horizon manipulation—not only improving performance but also enabling real-world deployment. Recent studies show that such methods are essential for embodied AI. Experiments demonstrate strong improvements over baselines.
```

## Expected Artifact Checklist

- Output includes a clean rewrite.
- Output includes change notes or rationale.
- Output includes an explicit remaining AI-style tell check or equivalent final audit.
- Generic phrases such as "In recent years", superficial `-ing` phrases, and unsupported praise are removed or narrowed.
- Unsupported claims such as "novel", "significantly", "robust", "crucial", and broad real-world deployment are flagged or narrowed.
- Rhetorical constructions such as "not only ... but also" are simplified when they add no technical distinction.
- Vague attribution such as "recent studies show" is flagged unless a specific source is provided.
- Technical meaning is preserved.
- The response does not claim to evade AI detectors.

## Pass Conditions

- The edited prose is clearer, more concise, and more scientific.
- Unsupported certainty is reduced.
- The output flags claims needing evidence instead of inventing support.

## Fail Conditions

- The rewrite adds new results, citations, baselines, or deployment claims.
- The output optimizes for an AI detector score.
- The rewrite removes necessary technical terms for stylistic variety.
