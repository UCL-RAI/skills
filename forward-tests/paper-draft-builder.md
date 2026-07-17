# Forward Test: Paper Draft Builder

## Skill

`paper-draft-builder`

## Prompt

Use `paper-draft-builder` to create a story brief and a focused Markdown paper
draft from this experiment handoff.

```markdown
Target: CoRL-style conference paper; exact page limit not supplied.

Dossier claims:
- CLM-01: memory improves long-horizon task success.
- RES-01: ours 78.0 +/- 2.0 over three seeds, verified.
- RES-02: baseline 66.0 +/- 1.5 over three seeds, verified.
- RES-03: no-memory 68.0 from one seed, ambiguous for a general ablation claim.
- Failure: performance drops on unseen object layouts; 12 evaluated layouts.

Method evidence:
- recurrent policy with visual and proprioceptive inputs.
- exact recurrent state dimension is missing from the dossier.

Literature evidence:
- two verified paper cards support the general long-horizon memory gap.
- no verified source establishes that this is the first recurrent policy for
  the task family.
```

## Expected Artifact Checklist

- Selects one bounded thesis supported by CLM-01, RES-01, and RES-02.
- Produces a story brief with narrative spine, contributions, claim-evidence
  plan, figure sequence, and author decisions.
- Drafts around the verified main comparison without generalizing the
  one-seed ablation.
- Includes the unseen-layout failure in the story scope or limitations.
- Marks recurrent state dimension and exact venue constraints as missing.
- Does not claim "first" or invent bibliographic details.
- Keeps observation, explanation, and proposed framing distinguishable.

## Pass Conditions

- Every major draft claim maps to supplied result or citation evidence.
- Abstract, introduction, results, limitations, and conclusion use consistent
  scope.
- Unsupported details remain visible as explicit missing-evidence or
  `UNVERIFIED` markers.
- The draft tells one coherent story rather than listing all available facts.

## Fail Conditions

- The response treats RES-03 as a conclusive multi-seed ablation.
- It omits the unseen-layout failure to strengthen the story.
- It invents the state dimension, venue page limit, citations, or novelty.
