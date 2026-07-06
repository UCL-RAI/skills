# Forward Test: Manuscript Structure Auditor

## Skill

`manuscript-structure-auditor`

## Prompt

Use `manuscript-structure-auditor` to audit this introduction for coherence, repetition, and claim threading. Do not do sentence-level grammar polishing yet.

```markdown
Long-horizon robot manipulation is important because robots need to complete many steps. Recent robot learning methods have achieved strong performance on manipulation tasks. However, long-horizon manipulation remains challenging. We propose a hierarchical policy that decomposes tasks into subgoals. Existing methods often struggle with long-horizon manipulation because they cannot reason across stages. Our method is simple and robust. We evaluate in simulation and on a robot. Long-horizon manipulation is a key challenge for real-world robots.
```

## Expected Artifact Checklist

- Output includes `Claim Thread`.
- Output includes `Structure Findings` with severity, location, issue, why it matters, and repair action.
- Output includes a `Repetition Map`.
- Repeated problem statements are identified.
- Unsupported "simple and robust" claim is flagged as structure/claim-thread risk or evidence risk.
- The agent recommends structural repairs before grammar edits.

## Pass Conditions

- The audit separates coherence/repetition from sentence-level grammar.
- Every major issue has a repair action.
- The suggested order preserves scientific meaning.

## Fail Conditions

- The output only rewrites the paragraph.
- Repetition is described vaguely without locations.
- The audit strengthens claims without evidence.
