# Experiment Provenance Auditor Example

## User Prompt

> Check whether these paper results are traceable enough for submission.

## Example Input

```markdown
Table 2 reports:
- Ours: 82.4 success
- No-memory ablation: 76.1

Known files:
- runs/final/ours.log
- configs/policy.yaml
- plots/table2.ipynb

Unknown: commit hash, seed list, dataset version, exact command, and baseline config.
```

## Expected Skill Behavior

The agent should use `experiment-provenance-auditor`, create a result ledger, and mark missing provenance instead of assuming traceability.

## Example Output Shape

```markdown
## Result Ledger
| Paper result | Source run | Commit/config/data | Status | Gap |
| --- | --- | --- | --- | --- |
| Ours 82.4 | runs/final/ours.log | config present, commit/data missing | ambiguous | cannot tie log to code/data version |
| No-memory 76.1 | not found | missing | missing | baseline source run unavailable |

## Blocking Gaps
- Missing commit hash and dataset version for headline result.
- Missing source run and config for ablation.
```

## Quality Checks

- Separates `verified`, `ambiguous`, and `missing`.
- Does not create fake run ids.
- Names minimum artifacts needed to repair traceability.
