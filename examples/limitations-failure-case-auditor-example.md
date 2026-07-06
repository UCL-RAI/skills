# Limitations Failure Case Auditor Example

## User Prompt

> Audit our limitations section before submission.

## Example Input

```markdown
Claim: The method enables robust real-world manipulation.
Evidence: simulation benchmark on 20 tasks, one robot embodiment, one seed.
Known failures: transparent objects fail often; long-horizon tasks fail after perception drift.
Draft limitation: Future work will explore more objects and robots.
```

## Expected Skill Behavior

The agent should use `limitations-failure-case-auditor`, connect limitations to claims, and narrow unsupported deployment language.

## Example Output Shape

```markdown
## Assumption Map
| Claim | Assumption | Evidence | Risk |
| --- | --- | --- | --- |
| robust real-world manipulation | sim transfers to real robot | no real robot evidence | blocking overclaim |

## Suggested Limitations Text
The current evaluation is limited to simulation with one robot embodiment. Transparent objects and perception drift remain failure modes, which limits claims about robust real-world deployment.

## Claims to Narrow
- Replace "enables robust real-world manipulation" with a simulation-scoped claim.
```

## Quality Checks

- Does not hide limitations as vague future work.
- Does not invent unobserved failures.
- Keeps supported claims intact while narrowing overclaims.
