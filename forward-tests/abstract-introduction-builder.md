# Forward Test: Abstract Introduction Builder

## Skill

`abstract-introduction-builder`

## Prompt

Use `abstract-introduction-builder` to draft a scoped abstract from this material.

```markdown
Problem: long-horizon manipulation with sparse rewards.
Gap: low-level policies do not handle task sequencing well.
Method: subgoal graph plus diffusion low-level controller.
Evidence: simulation success improves over two baselines across 20 tasks.
Missing: variance, real-robot experiments, and citation audit.
Limitation: one simulated robot embodiment.
```

## Expected Artifact Checklist

- Includes a draft abstract or skeleton.
- Includes a claim-risk table or equivalent.
- States simulation-only and one-embodiment boundaries.
- Avoids unsupported "state-of-the-art", "first", "significant", or deployment claims.
- Marks missing variance, real-robot evidence, and citation audit as risks.

## Pass Conditions

- The abstract is specific and scoped to verified evidence.
- Missing evidence remains visible.
- The draft connects problem, gap, method, evidence, and limitation.

## Fail Conditions

- The response writes a broad confident abstract that hides missing evidence.
- The response invents citations, metrics, or real-world results.
- The response uses generic motivational filler instead of the provided technical content.
