# Paper Draft Contract

Use this contract to keep narrative design evidence-grounded and to prevent a
full draft from becoming a polished list of unsupported claims.

## Story Brief

```markdown
# Story Brief

## Paper Identity
- Working title:
- Target venue and page budget:
- Intended reader:
- One-sentence thesis:

## Narrative Spine
| Beat | Content | Evidence ids | Risk |
| --- | --- | --- | --- |
| Problem | | | |
| Existing gap | | | |
| Technical insight | | | |
| Approach | | | |
| Main evidence | | | |
| Boundary/limitation | | | |
| Takeaway | | | |

## Contributions
| Contribution | Evidence ids | Novelty support | Destination | Status |
| --- | --- | --- | --- | --- |

## Claim-Evidence Plan
| Claim id | Claim | Dossier result ids | Citation ids | Planned location | Status |
| --- | --- | --- | --- | --- | --- |

## Figure Sequence
| Order | Figure/table | Question answered | Claim advanced | Source/status |
| --- | --- | --- | --- | --- |

## Evidence Gaps and Author Decisions
| Priority | Gap/decision | Affected text | Required action |
| --- | --- | --- | --- |
```

## Draft Section Contracts

- **Abstract**: problem, gap, approach, strongest quantified evidence,
  contribution, and scope in one consistent arc.
- **Introduction**: motivate the exact problem, establish a verified gap,
  explain the insight, preview evidence, and state bounded contributions.
- **Related Work**: organize by conceptual comparison, cite verified sources,
  and define the novelty boundary without straw-manning prior work.
- **Method**: define inputs/outputs, components, objectives, training/control
  procedure, inference, assumptions, and implementation details needed to
  understand or reproduce the approach.
- **Experiments**: state research questions, datasets/tasks, baselines,
  metrics, protocols, implementation details, statistical treatment, and
  selection rules before interpreting outcomes.
- **Results**: answer experiment questions in claim-evidence order; preserve
  conditions and uncertainty; distinguish observation from explanation.
- **Limitations**: report demonstrated failures, unsupported regimes,
  assumptions, and practical risks that bound the thesis.
- **Conclusion**: restate the supported answer and scope; introduce no new
  result, citation, or stronger claim.

## Story Selection Heuristics

Prefer the story that:

1. is supported by the strongest and most complete evidence chain;
2. explains why the method should work without claiming an untested mechanism;
3. differentiates from verified prior work on a meaningful axis;
4. remains true after including important failures and limitations;
5. can be communicated within the venue's page and figure budget.

Reject a framing that depends on omitted baselines, cherry-picked runs,
ambiguous provenance, or an unsupported universal claim.
