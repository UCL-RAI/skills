# Forward Test: Experiment Provenance Auditor

## Skill

`experiment-provenance-auditor`

## Prompt

Use `experiment-provenance-auditor` to audit traceability for these paper results.

```markdown
Paper results:
- Table 2, Ours: 84.0 success
- Table 2, No-vision ablation: 65.3 success
- Figure 4, learning curve over 200k steps

Available artifacts:
- runs/ours_final.log
- configs/ours.yaml
- plots/figure4.ipynb

Missing or unknown:
- commit hash
- dataset split
- exact command
- seed list
- ablation log
- environment file
```

## Expected Artifact Checklist

- Includes a result ledger.
- Marks the headline result as ambiguous rather than verified if commit/data/seed/command are missing.
- Marks the ablation as missing if no source run exists.
- Checks the raw-log to plot/table traceability chain.
- Separates reproducibility, availability, and reusability concerns.
- Does not create fake run ids or fake environment details.

## Pass Conditions

- Every paper result receives a provenance status.
- The repair plan prioritizes headline table and figure traceability.
- Private or missing artifacts are not treated as publishable.

## Fail Conditions

- The response assumes the available log proves the table value without checking transformations.
- The response ignores missing seed, data, and command information.
- The response promises reproducibility without enough artifacts.
