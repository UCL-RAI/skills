# Forward Test: Related Work Positioning

## Skill

`related-work-positioning`

## Prompt

Use `related-work-positioning` to position this paper idea.

```markdown
Claim: We are the first to combine subgoal planning and diffusion policies for long-horizon manipulation.

Known sources:
- Paper A: diffusion policies for visuomotor control.
- Paper B: hierarchical imitation learning for long-horizon manipulation.
- Paper C: task-and-motion planning with learned skills.

No citation audit has been done yet.
```

## Expected Artifact Checklist

- Builds prior-work clusters.
- Flags the "first" claim as unsafe without stronger coverage and citation audit.
- States what each cluster appears to solve and what boundary the current paper might claim.
- Produces safer positioning language.
- Lists missing sources or audit needs.

## Pass Conditions

- The output synthesizes clusters instead of listing sources chronologically.
- Novelty language is narrowed or made conditional.
- The response avoids dismissive claims about prior work.

## Fail Conditions

- The response accepts the "first" claim from the user's wording.
- The response fabricates source details.
- The response writes polished related work without flagging missing evidence.
