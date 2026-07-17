# Survey Synthesis Contract

Use these schemas for standard and deep synthesis.

For systematic or scoping reviews, use the official
[PRISMA 2020 statement](https://www.prisma-statement.org/prisma-2020) when its
reporting model fits the review. Do not label a narrative survey systematic
unless its search, screening, and inclusion process supports that claim.

## Synthesis Contract

```markdown
# Survey Synthesis Contract

## Reader and Decision Supported

## Central Question and Thesis

## Coverage Promise
- Included:
- Excluded:
- Date cutoff:
- Search/evidence limitations:

## Organizing Principle

## Claims the Survey Will Not Make
```

## Taxonomy Ledger

```markdown
| Category | Definition | Membership rule | Representative source ids | Edge cases | Limitation |
| --- | --- | --- | --- | --- | --- |
```

Prefer categories that explain meaningful differences in assumptions,
mechanisms, interfaces, evidence, or deployment. Reject categories created
only because papers use different names.

## Claim-Evidence Map

```markdown
| Claim ID | Synthesis claim | Supporting source ids | Counterevidence | Scope/status | Planned location |
| --- | --- | --- | --- | --- | --- |
```

Use separate rows for observed field patterns, interpretation, and author
proposals. A source may support several claims, but repeated use must not make
the evidence base appear broader than it is.

## Section Contract

```markdown
| Section | Question answered | Synthesis takeaway | Evidence ids | Table/figure | Transition | Coverage risk |
| --- | --- | --- | --- | --- | --- | --- |
```

## Coverage Checks

- Method-family and historical coverage reflects the stated scope.
- Recent papers do not crowd out foundational work without justification.
- Papers with missing code or weak evaluation are not excluded silently.
- Survey and benchmark papers are used as maps, not substitutes for primary
  evidence where primary claims matter.
- Open problems distinguish missing literature coverage, missing reporting,
  and genuinely missing research evidence.
