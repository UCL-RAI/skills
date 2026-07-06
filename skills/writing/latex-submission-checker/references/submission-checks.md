# Submission Checks

Use this reference for LaTeX package and submission hygiene.

## Source Patterns

- arXiv TeX help covers source submission expectations, supported formats, file inclusion, and common TeX upload problems: https://info.arxiv.org/help/submit_tex.html
- NeurIPS author guidance and checklist pages are useful examples of yearly venue requirements, but current-year rules must be checked directly: https://neurips.cc/Conferences/2025/CallForPapers
- Conference templates and style files are authoritative for formatting; do not rely on memory or old templates.

## Package Inventory

- Main `.tex` file.
- Bibliography files: `.bib`, `.bbl`, or venue-required format.
- Style files and class files permitted by the venue.
- Figures in accepted formats.
- Generated tables, plots, and externalized TikZ files.
- Supplementary files and appendix source.
- Build tool: `latexmk`, `pdflatex`, `xelatex`, `lualatex`, `bibtex`, or `biber`.

## Blocking Checks

- PDF does not build from a clean checkout.
- Required source file is missing.
- Page limit exceeded in the required mode.
- Wrong template, font, margin, line numbering, or appendix rule.
- Undefined references or citations remain in the final PDF.
- Figure/table files missing or rendered at unusable resolution.
- Anonymous submission contains author identity, acknowledgements, private links, or PDF metadata.

## arXiv Checks

- Include source files needed to compile the paper.
- Avoid local absolute paths and private packages.
- Ensure generated figures and bibliography files are included when required.
- Remove comments or files that reveal private review information.
- Confirm licensing and third-party figure permissions before public upload.

## Useful Local Commands

```bash
latexmk -pdf main.tex
grep -R "undefined references\\|undefined citations\\|Citation .* undefined" .
find . -name "*.tex" -o -name "*.bib" -o -name "*.sty" -o -name "*.cls"
pdfinfo paper.pdf
```

Run commands only when the files are available locally and the user wants an actual package check.
