---
name: experiment-provenance-auditor
description: Audits whether research results are traceable from paper claims back to configs, code versions, data versions, seeds, logs, hardware, and generated artifacts. Use when checking reproducibility, result provenance, experiment tracking, or paper appendix readiness.
---

# Experiment Provenance Auditor

Use this when results exist but their origin, reproducibility, or paper traceability is uncertain.

## Inputs

- Paper draft, experiment table, result spreadsheet, plots, or appendix.
- Repository, configs, scripts, logs, checkpoints, output folders, or experiment tracker exports.
- Data version, simulator version, robot setup, environment files, hardware, and run dates if available.
- Claimed result numbers and the exact manuscript locations where they appear.

Read `references/provenance-checks.md` for the detailed provenance ledger and source patterns.

## Workflow

1. Build a result inventory from the manuscript tables, figures, and numeric claims.
2. For each result, locate the run source: code commit, config, data split, seed, hardware, command, log, checkpoint, and plotting script.
3. Mark each field as `verified`, `missing`, `ambiguous`, or `not applicable`.
4. Check whether paper numbers can be regenerated or at least traced from raw logs to processed tables and figures.
5. Check environment capture: package versions, CUDA/driver, ROS/simulator, dataset preprocessing, random seed handling, and external services.
6. Check whether artifacts are publishable without private paths, credentials, or unreleased data.
7. Produce a blocking provenance gap list and a minimal repair plan.

## Output

```markdown
## Experiment Provenance Audit

## Result Ledger
| Paper result | Source run | Commit/config/data | Status | Gap |
| --- | --- | --- | --- | --- |

## Traceability Chain
| Raw artifact | Processing step | Paper artifact | Verified? |
| --- | --- | --- | --- |

## Blocking Gaps

## Reproducibility Package Fixes

## Claims Needing Provenance Caveats
```

## Rules

- Do not infer a run source from a similar filename; require explicit traceability or mark ambiguous.
- Do not rewrite results or create fake logs to make provenance look complete.
- Do not expose private paths, credentials, API keys, or unreleased participant data.
- Do not treat a random seed list as reproducibility if data, code, and environment are missing.
- Do not promise bitwise reproducibility unless the project actually supports it.

## Validation

- Every manuscript result has a provenance status.
- Every `verified` result has enough information for another researcher to locate or rerun it.
- Every missing artifact is tied to a concrete paper risk.
- The audit distinguishes reproducibility, availability, and reusability.

## Completion

Done means the manuscript's results have a traceability ledger and the user knows which provenance gaps must be fixed before submission or release.
