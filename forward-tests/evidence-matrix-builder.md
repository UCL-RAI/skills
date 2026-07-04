# Forward Test: Evidence Matrix Builder

## Skill

`evidence-matrix-builder`

## Prompt

Use `evidence-matrix-builder` on these three reading-card snippets and produce a comparison matrix plus defensible gaps.

```markdown
Card A: A vision-only robot policy for cloth folding. Uses one simulator and one real robot setup. Baselines: scripted heuristic and behavior cloning. Metrics: fold success rate and final corner distance. Code not reported. Limitation: narrow cloth types.

Card B: A tactile-assisted deformable object manipulation method. Uses tactile sensors and real-robot rope manipulation. Baselines: vision-only variant and scripted controller. Metrics: task success and recovery after perturbation. Limitation: small number of tasks.

Card C: A model-based planner for deformable object manipulation. Uses simulated rope and cloth tasks. Baselines: sampling planner and learned policy. Metrics: task success and planning time. Limitation: no real-robot evaluation.
```

## Expected Artifact Checklist

- Matrix rows trace to Card A, Card B, and Card C.
- Columns include problem, method family, robot/domain, dataset/simulator, baselines, metrics, main evidence, limitations, code/data, gap tags, and notes.
- Gap tags use stable names such as `narrow-benchmark`, `untested-deployment`, or `unclear-reproducibility`.
- Synthesis separates evidence from interpretation.
- Claims use the supplied snippets only.

## Pass Conditions

- The output produces both matrix and gap synthesis.
- The agent does not infer unprovided venue, year, code availability, or statistical strength.
- Gaps are tied to specific rows.

## Fail Conditions

- The agent invents paper titles or bibliographic metadata.
- The synthesis declares one method "best" without compatible metrics.
- Gaps are generic and not traceable to rows.
