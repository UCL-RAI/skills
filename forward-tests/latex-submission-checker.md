# Forward Test: LaTeX Submission Checker

## Skill

`latex-submission-checker`

## Prompt

Use `latex-submission-checker` for an anonymous conference submission package with this inventory and risk log.

```text
paper/
|-- main.tex
|-- refs.bib
|-- style.sty
|-- figures/overview.pdf
|-- figures/results.png
`-- build.log
```

Known risks:
- `main.tex` has acknowledgements.
- The paper links to a personal GitHub repository.
- `build.log` contains "Citation `smith2024` undefined".
- The current PDF is one page over the stated limit.
- The target venue is not specified.

## Expected Artifact Checklist

- Identifies anonymous review mode and asks for or flags missing target venue.
- Separates blocking issues from warnings.
- Flags acknowledgements, personal repository link, undefined citation, and page limit.
- States that current venue rules must be verified from official instructions.
- Keeps content editing out of scope.

## Pass Conditions

- The checker does not assume a specific venue template.
- The checker identifies build/reference and anonymity problems as blocking for anonymous submission.
- The output includes concrete files or commands to inspect when local files exist.

## Fail Conditions

- The response ignores anonymity risks.
- The response treats page limit rules as known without a target venue.
- The response rewrites scientific content instead of checking package readiness.
