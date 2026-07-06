# Forward Test: Limitations Failure Case Auditor

## Skill

`limitations-failure-case-auditor`

## Prompt

Use `limitations-failure-case-auditor` to audit this draft limitation and claim.

```markdown
Claim: Our method enables robust real-world manipulation.
Evidence: simulation-only benchmark, 20 tasks, one robot embodiment, one seed.
Known failures: transparent objects fail frequently; long-horizon rollouts fail after perception drift.
Draft limitation: Future work will extend to more robots and objects.
```

## Expected Artifact Checklist

- Includes an assumption map.
- Includes a failure-case table or equivalent.
- Flags robust real-world manipulation as unsupported.
- Connects transparent-object and perception-drift failures to interpretation.
- Suggests concrete limitations text.
- Recommends claim narrowing or additional analysis.

## Pass Conditions

- The limitations are specific to the paper, not generic caveats.
- The response does not invent additional failures.
- The output narrows unsupported claims without discarding supported simulation findings.

## Fail Conditions

- The response leaves the deployment claim intact.
- The response turns limitations into vague future work.
- The response over-apologizes in a way that undermines supported evidence.
