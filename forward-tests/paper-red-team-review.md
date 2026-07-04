# Forward Test: Paper Red-Team Review

## Skill

`paper-red-team-review`

## Prompt

Use `paper-red-team-review` to critique this abstract for an ICRA-style paper:

```markdown
We introduce a novel robot learning system that solves long-horizon manipulation. Our method is simple and scalable, outperforming previous approaches in simulation. The approach generalizes to unseen objects and is suitable for real-world deployment. Experiments show significant improvements over baselines.
```

## Expected Artifact Checklist

- Output starts with findings, not praise.
- Findings are grouped by `Blocking`, `Major`, `Minor`, `Nits`, `Rewrite Suggestions`, and `Residual Risk`.
- Blocking or major issues include overbroad novelty/capability claims, unspecified baselines/metrics, and simulation-to-real overclaim.
- Every blocking/major issue has evidence, why it matters, and repair path.
- Rewrite suggestions narrow claims rather than making unsupported claims smoother.

## Pass Conditions

- The review is blunt, specific, and evidence-grounded.
- The agent does not request cosmetic polish before scientific issues.
- Residual risk separates not-checked items from known failures.

## Fail Conditions

- The output mainly rewrites the abstract without severity-ranked findings.
- The review accepts "solves long-horizon manipulation" without scope.
- The review treats simulation results as deployment evidence.
