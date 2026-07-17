---
name: citation-integrity-auditor
description: Audits whether citations are real, traceable, and actually support manuscript claims. Use when the user asks to verify references, check citation truthfulness, map claims to papers, detect hallucinated citations, or audit related work.
---

# Citation Integrity Auditor

Use this before polishing cited academic writing.

## Inputs

- Manuscript text, section, paragraph, claim list, or related-work draft.
- Bibliography, BibTeX, DOI/arXiv/OpenReview links, or source PDFs if available.
- Audit depth: quick triage, claim-by-claim audit, bibliography sanity check, or rewrite support.

If sources are unavailable, mark support as `unverified`; do not infer support from title, abstract memory, or citation popularity.

## Workflow

For quick triage, inspect only high-risk claims first: novelty, state-of-the-art, benchmark comparisons, dataset facts, historical claims, and citations that look fabricated or mismatched.

1. Split text into atomic claims.
2. Extract cited sources for each claim.
3. Verify source identity: title, authors, venue/year, DOI/arXiv/OpenReview when available.
4. Check support strength:
   - `direct`: source explicitly supports the claim;
   - `partial`: source supports a narrower or related claim;
   - `background`: source is relevant but not evidence for the statement;
   - `unsupported`: source does not support the claim;
   - `unverified`: source could not be checked.
5. Flag overclaiming, miscitation, missing citation, and fabricated-looking references.
6. Suggest conservative rewrites when support is partial.

Read `references/support-grades.md` when auditing a full section, defining issue types, or rewriting claims. Skip it for quick triage unless support grades are ambiguous.

## Output

For quick triage:

```markdown
## High-Risk Citation Issues
| Claim | Citation | Risk | Fix |
| --- | --- | --- | --- |

## Not Checked
```

For claim-by-claim or deep audits:

```markdown
| Claim | Citation | Source status | Support grade | Issue type | Fix |
| --- | --- | --- | --- | --- | --- |
```

Use these source statuses:

- `verified`: identity and cited content were checked;
- `metadata-only`: identity was checked, but full support was not;
- `missing-source`: citation cannot be found from supplied info;
- `mismatch`: citation metadata points to a different source;
- `unavailable`: source may exist but is not accessible in the current context.

## Rules

- Do not invent missing bibliographic details.
- Do not assume a citation supports a claim because the title sounds relevant.
- For high-stakes claims, prefer primary papers, official benchmarks, or original dataset/project pages.
- Treat survey papers as background unless they directly support the exact historical or taxonomic claim.
- Prefer conservative rewrites that narrow the claim to the evidence actually checked.

## Validation

- In quick triage, high-risk checked claims have a risk status and the unchecked scope is listed.
- In claim-by-claim or deep audits, every non-obvious factual, historical, novelty, benchmark, or comparative claim has a support grade.
- Every `direct` support grade is tied to source content, not metadata alone.
- Every weak support issue has a fix: remove, narrow, replace citation, add source, or mark as unsupported.
- Bibliographic identity is not silently repaired without noting the correction.

## Completion

Done means the chosen audit depth is explicit, weak or missing citation support has a concrete fix path, and unverified or unchecked claims are not presented as verified.
