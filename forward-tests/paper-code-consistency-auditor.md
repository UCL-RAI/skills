# Forward Test: Paper Code Consistency Auditor

## Skill

`paper-code-consistency-auditor`

## Prompt

Use `paper-code-consistency-auditor` in standard depth on this manuscript and
implementation snapshot.

```markdown
Manuscript:
- Section 3 says LayerNorm is applied independently before visual-language
  fusion.
- Appendix A says dropout defaults to 0.1.
- Table 2 caption says success is averaged over all evaluation episodes.

Code at commit abc123:
- model/fusion.py applies one LayerNorm after concatenation.
- configs/eval.yaml sets dropout: 0.0 and the CLI does not override it.
- eval/metrics.py removes episodes with status == "timeout" before averaging.
- README repeats the manuscript description, but no test covers these paths.
```

## Expected Artifact Checklist

- Records the manuscript and code version contract.
- Creates separate discrepancy rows for normalization placement, dropout, and
  timeout filtering.
- Uses active implementation/config evidence rather than treating the README
  as executed behavior.
- Distinguishes scientific consequences from wording differences.
- Does not decide automatically that paper or code is the intended truth.
- Recommends runtime or regression checks where static inspection is
  insufficient.

## Pass Conditions

- Every manuscript statement maps to exact code/config evidence and a valid
  consistency status.
- Timeout filtering is treated as a result-interpretation risk.
- Repair paths identify whether paper, code, config, or evidence must change.

## Fail Conditions

- The response calls the implementation consistent because README and paper
  agree.
- It ignores effective defaults or filtering behavior.
- It rewrites code before establishing intended behavior and provenance.
