# LaTeX Submission Checker Example

## User Prompt

> Check this LaTeX package for anonymous conference submission readiness.

## Example Input

```text
paper/
|-- main.tex
|-- refs.bib
|-- figures/overview.pdf
|-- neurips_2025.sty
`-- build.log
```

Known risks:

- `main.tex` contains an acknowledgements section.
- A GitHub link points to the authors' personal organization.
- Build log contains undefined citations.

## Expected Skill Behavior

The agent should use `latex-submission-checker`, identify submission mode, separate blocking issues from warnings, and require current venue confirmation for specific rules.

## Example Output Shape

```markdown
## Blocking Issues
- Anonymous mode risk: acknowledgements and author GitHub organization reveal identity.
- Build risk: undefined citations remain in build log.

## Venue Compliance Risks
- Confirm current NeurIPS 2025 instructions for style file, page limit, and supplementary rules.

## Build / Reference Warnings
- Rebuild from a clean checkout after removing identity leaks.
```

## Quality Checks

- Does not apply anonymous rules to camera-ready mode.
- Does not assume venue rules from memory.
- Keeps package checks separate from paper-content editing.
