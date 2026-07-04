# Support Grades Reference

Use this reference for full-section audits or claim rewrites.

## Support Grades

| Grade | Meaning | Acceptable use |
| --- | --- | --- |
| `direct` | The source explicitly supports the exact claim. | Use for core claims, benchmark facts, dataset details, and novelty positioning. |
| `partial` | The source supports a narrower, adjacent, or weaker version. | Rewrite the claim to match the evidence. |
| `background` | The source is relevant context but not evidence for the statement. | Keep only for general framing, not proof. |
| `unsupported` | The source does not support the claim or contradicts it. | Remove, replace, or rewrite. |
| `unverified` | The source could not be checked. | Do not rely on it for important claims. |

## Issue Types

| Issue | Description | Fix |
| --- | --- | --- |
| `overclaim` | Claim is broader or stronger than source evidence. | Narrow the claim. |
| `wrong-source` | Cited paper is real but supports a different point. | Replace or add the correct source. |
| `missing-citation` | Claim needs evidence but has no citation. | Add primary source or mark unsupported. |
| `fabricated-looking` | Metadata is incomplete, inconsistent, or not findable. | Verify identity before use. |
| `stale-baseline` | Claim ignores newer or stronger baselines. | Search and update related work. |
| `secondary-source` | Claim relies on a survey/blog when primary source is needed. | Cite the original paper, dataset, or benchmark. |

## Rewrite Rules

- Convert universal claims to scoped claims when evidence is limited.
- Replace "first", "state-of-the-art", or "widely" unless the source directly supports that strength.
- Use "has been used for" instead of "is the standard" unless standard status is verified.
- Separate method claims from benchmark claims.
- Keep uncertainty visible when support is partial or unverified.
