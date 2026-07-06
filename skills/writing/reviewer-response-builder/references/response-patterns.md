# Response Patterns

Use this reference to turn reviews into rebuttal actions.

## Source Patterns

- ACL Rolling Review author guidance distinguishes review, author response, action editor recommendation, and revision stages: https://aclrollingreview.org/authors
- OpenReview-based venues often constrain rebuttals by anonymity, length, and discussion rules; verify the current venue page before drafting.
- Conference author guidelines can change yearly. Treat venue policy as live information and check official instructions before submission.

## Issue Classes

| Class | Response stance |
| --- | --- |
| Misunderstanding | Clarify the intended claim and state the manuscript change that prevents repeat confusion. |
| Missing evidence | Provide existing evidence or state the new experiment/analysis; do not hand-wave. |
| Valid weakness | Concede, narrow the claim, and say how the paper will be corrected. |
| Citation gap | Add or correct specific citations only after verification. |
| Writing clarity | Acknowledge and give the exact section or wording change. |
| Out of scope | Explain why it is outside scope and offer a limitation or future-work note. |
| Incorrect premise | Correct politely with evidence and line/table references. |

## Response Template

```markdown
R{reviewer}-{point}: [short issue title]
Thank you for raising this. [One-sentence answer.]
Evidence: [paper location, result, citation, or planned analysis].
Revision: We will [specific manuscript change].
Boundary: [if needed, what is not claimed or cannot be added].
```

## Priority Heuristics

Handle first:

- novelty rejection risks;
- missing baseline or ablation requests;
- reproducibility concerns;
- claims contradicted by evidence;
- reviewer misunderstandings shared by multiple reviewers;
- issues raised by high-confidence reviewers or the meta-review.

Handle later:

- minor wording preferences;
- optional future-work requests;
- formatting comments unless they block compliance.

## Risky Phrases

- "We believe" without evidence.
- "Clearly" or "obviously" when the reviewer missed it.
- "Due to space" when the issue is central.
- "We will add" for work that is not feasible.
- "This is beyond scope" without explaining the paper's actual scope.
