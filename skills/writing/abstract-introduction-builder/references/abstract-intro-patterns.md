# Abstract and Introduction Patterns

Use this reference to structure opening sections.

## Source Patterns

- UNC Writing Center guidance on introductions emphasizes moving from topic and context to a focused thesis or claim: https://writingcenter.unc.edu/tips-and-tools/introductions/
- UNC literature review guidance is useful for gap synthesis and source positioning: https://writingcenter.unc.edu/tips-and-tools/literature-reviews/
- NeurIPS Paper Checklist is useful for checking whether assumptions, limitations, experiments, and reproducibility details are not hidden by writing: https://neurips.cc/public/guides/PaperChecklist

## Abstract Skeleton

```text
Problem/context: What capability or scientific question matters?
Gap: What is missing in current methods, data, systems, or evaluation?
Approach: What does this paper do?
Evidence: What experiments or analysis support the claim?
Contribution: What should the reader remember?
Boundary: What scope or limitation prevents overclaiming?
```

## Introduction Skeleton

1. Establish the concrete problem and setting.
2. Explain why existing approaches leave a gap.
3. State why the gap is technically difficult.
4. Introduce the core idea without implementation clutter.
5. Preview evidence: datasets, robot tasks, benchmarks, or analysis.
6. List contributions with claim boundaries.
7. Signal limitations when they prevent overgeneralization.

## Sentence-Level Checks

- A motivation sentence should connect to the paper's actual task.
- A gap sentence should name the missing capability or evidence.
- A method sentence should use precise technical nouns.
- A result sentence should include metric context when available.
- A contribution bullet should be falsifiable.

## Red Flags

- Opening starts with "In recent years" but no time trend matters.
- Abstract is only motivation and promises.
- Contribution bullets repeat the same claim in three ways.
- Introduction claims broad real-world deployment from narrow benchmarks.
- Limitations appear only after submission review, not in the paper scope.
