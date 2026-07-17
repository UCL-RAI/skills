# Forward Test: Research Plan Grill

## Skill

`research-plan-grill`

## Prompt

Use `research-plan-grill` in standard depth on this proposal.

```markdown
I want to write a robot skills survey. I have about 100 PDFs, some reading
notes, an evidence matrix of uncertain quality, a current LaTeX manuscript,
and an abandoned draft. Possible emphases include classical robot skills,
language-guided skill selection, modular VLA experts, and WAM-based skill
arbitration. I have not fixed the target audience, inclusion criteria, or the
claim that should organize the survey. Grill me before we write anything.
```

## Expected Artifact Checklist

- Asks exactly one question in the first response.
- Starts with a high-dependency decision such as the central research question,
  audience, or scope boundary rather than prose style or file naming.
- Provides a concrete recommended answer and explains its downstream effect.
- Treats the existing matrix and abandoned draft as unverified inputs.
- Does not ask the user to recount files or facts that can be inspected.
- Does not start drafting the survey or emit the full decision brief before the
  interview has converged.

## Pass Conditions

- The first question materially constrains later inclusion, taxonomy, and
  evidence decisions.
- The recommendation is specific enough for the user to accept, modify, or
  reject.
- The response follows the one-question interaction contract.

## Fail Conditions

- The response sends a multi-question intake form.
- It remains neutral without recommending a direction.
- It asks the user to summarize available repository content before inspecting
  it.
- It treats a speculative WAM framing as an established survey conclusion.
