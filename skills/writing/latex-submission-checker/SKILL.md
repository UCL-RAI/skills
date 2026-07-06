---
name: latex-submission-checker
description: Checks LaTeX paper source packages for venue formatting, anonymity, buildability, references, figures, arXiv readiness, and submission hygiene. Use before conference submission, arXiv upload, camera-ready, or when LaTeX build/source problems may block a paper.
---

# LaTeX Submission Checker

Use this as a final packaging gate, not as a writing-quality review.

## Inputs

- LaTeX source folder, main `.tex`, bibliography files, figures, style files, and build logs if available.
- Target venue and current official author/submission instructions.
- Submission mode: anonymous review, camera-ready, arXiv, workshop, or internal report.

Read `references/submission-checks.md` for package checks and arXiv-specific risks.

## Workflow

1. Identify the main `.tex` file, build system, bibliography tool, figure formats, and output PDF.
2. Check current venue requirements from official instructions when the venue matters.
3. Check anonymity: author names, acknowledgements, repo links, dataset links, PDF metadata, comments, and self-citation wording.
4. Check format compliance: page limit, template, font, margins, line numbers, appendix handling, figure/table placement, and supplementary material.
5. Check buildability: missing files, broken references, undefined citations, overfull boxes that affect readability, and stale generated artifacts.
6. Check bibliography and citation hygiene without inventing missing metadata.
7. Check arXiv/source packaging rules when relevant.
8. Produce a blocking checklist and exact commands or files to inspect.

## Output

```markdown
## LaTeX Submission Check

## Package Inventory
| Item | Status | Notes |
| --- | --- | --- |

## Blocking Issues

## Venue Compliance Risks

## Build / Reference Warnings

## Anonymity Risks

## arXiv / Camera-Ready Notes
```

## Rules

- Do not assume a venue rule from memory; verify current official instructions when the rule affects submission.
- Do not edit scientific claims while doing package checks.
- Do not remove author-identifying content for camera-ready unless the mode is anonymous review.
- Do not ignore LaTeX warnings that change references, citations, figures, or page count.
- Do not upload or expose private source files.

## Validation

- The checker identifies the intended submission mode.
- Blocking issues are separated from warnings.
- Venue-specific claims are marked verified or need current official confirmation.
- The package can be built or the build blocker is explicit.

## Completion

Done means the user knows whether the source package is buildable, compliant enough to submit, and free of obvious anonymity or packaging failures.
