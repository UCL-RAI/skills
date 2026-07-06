# Forward Test: Benchmark Audit

## Skill

`benchmark-audit`

## Prompt

Use `benchmark-audit` to review whether this experiment evidence supports the claim "our method is a robust state-of-the-art long-horizon manipulation policy."

```markdown
Table 1 reports average simulated success rate on 12 tasks:
- Ours: 81.2
- Baseline A: 78.9 from the baseline paper
- Baseline B: 72.4 from our rerun

Only one seed was run. The method uses extra human demonstrations that Baseline B did not receive. No failure-case table is included. The paper draft says the method is "robust and deployment-ready."
```

## Expected Artifact Checklist

- Includes a claim-result map.
- Flags that state-of-the-art, robustness, and deployment-readiness are not all supported by the given evidence.
- Identifies baseline fairness risks for different protocol sources and unequal demonstration access.
- Identifies one-seed and missing variance as a reporting risk.
- Recommends specific additional experiments or claim narrowing.
- Does not invent new results, citations, or confidence intervals.

## Pass Conditions

- The audit separates blocking, major, and minor issues or equivalent severity.
- The response states the minimum evidence needed to support or narrow each risky claim.
- The response treats qualitative deployment language as unsupported without real-world evidence.

## Fail Conditions

- The response accepts the benchmark because the score is numerically highest.
- The response rewrites claims more smoothly without flagging benchmark weaknesses.
- The response fabricates missing baselines, seeds, or real-robot results.
