# Experiment Dossier Contract

Use this schema for the remote-to-local handoff. Remove empty optional rows,
but do not remove required sections or hide missing evidence.

## Required Structure

```markdown
# Experiment Dossier: <project>

## Handoff Summary
- Research question:
- Current answer:
- Strongest evidence:
- Largest evidence gap:
- Recommended paper scope:

## Snapshot
| Field | Value | Status/source |
| --- | --- | --- |
| Commit and dirty state | | |
| Run date range | | |
| Data/task version | | |
| Environment/hardware | | |
| Inspection scope | | |

## Method Map
### Problem and assumptions
### System or model components
### Training/control/inference pipeline
### Repository source map

## Experiment Matrix
| Exp ID | Question | Variant/baseline | Data/task | Seeds or N | Metric | Run/config locator | Status |
| --- | --- | --- | --- | --- | --- | --- | --- |

## Result Ledger
| Result ID | Exp ID | Value/trend | Aggregation and uncertainty | Raw source | Transformation | Status |
| --- | --- | --- | --- | --- | --- | --- |

## Claim-Evidence Candidates
| Claim ID | Candidate claim | Supporting result ids | Counterevidence/scope | Confidence |
| --- | --- | --- | --- | --- |

## Figures and Tables
| Artifact | Paper message | Source/generator | Supported result ids | Handoff action |
| --- | --- | --- | --- | --- |

## Failures and Negative Results
| Observation | Evidence | Likely explanation | Paper relevance | Follow-up |
| --- | --- | --- | --- | --- |

## Provenance and Reproducibility
### Traceability summary
### Environment summary
### Known nondeterminism

## Evidence Gaps
| Priority | Missing evidence | Claim at risk | Smallest repair |
| --- | --- | --- | --- |

## Source Index
| Source id | Repository-relative path or stable artifact id | What it supports | Status |
| --- | --- | --- | --- |

## Handoff Manifest
- Dossier file:
- Optional transferred assets:
- Deliberately excluded artifacts:
- Sensitive details removed:
```

## Granularity Rules

- Assign stable ids such as `EXP-01`, `RES-01`, `CLM-01`, and `SRC-01`.
- Keep interpretation out of numeric value cells; place it in candidate claims.
- Preserve the metric's direction and units.
- State whether uncertainty is standard deviation, standard error, confidence
  interval, bootstrap interval, or something else.
- Distinguish number of seeds, episodes, scenes, tasks, and physical trials.
- For Robotics results, record sim/real, robot platform, control frequency,
  success definition, reset policy, and safety interventions when relevant.
- For ML results, record split, checkpoint selection rule, evaluation protocol,
  and test-set access when relevant.

## Compression Rule

Prefer ledgers and source ids over pasted logs. Include enough context to
interpret a result, but keep raw evidence in its original artifact. If the
dossier becomes long, compress project narration before removing provenance,
negative results, or evidence gaps.
