# Search Strategy Reference

Use this reference for broad field onboarding, surveys, or project/code searches.

## Query Family Design

Build query families instead of relying on one phrase.

| Family | Examples to include |
| --- | --- |
| Problem terms | task name, domain name, failure mode, benchmark name |
| Method terms | algorithm family, architecture, training objective, control method |
| Robotics terms | robot platform, sensor, actuator, simulator, control setting |
| Evaluation terms | dataset, benchmark, metric, ablation, sim-to-real phrase |
| Community terms | venue, workshop, lab/project name, challenge name |
| Negative controls | adjacent methods that should not dominate the result set |

## Source Tiers

| Tier | Use for | Caution |
| --- | --- | --- |
| Primary venue pages | Accepted papers and official metadata | Search UI may be incomplete. |
| arXiv/OpenReview | Preprints, revisions, reviews, forum context | Venue status may be unclear. |
| IEEE/ACM/PMLR | Publisher metadata and proceedings | Access may be limited. |
| Official project pages | Code, demos, datasets, videos | Claims can be promotional. |
| GitHub | Implementation status and activity | Stars are not evidence of scientific validity. |
| Dataset/benchmark docs | Task definitions, splits, metrics, licenses | Leaderboards may change over time. |
| Citation graph tools | Snowballing related work | Citation count favors older work. |

## Inclusion Criteria

Prefer sources that are:

- directly aligned with the research question;
- foundational for the method or benchmark;
- recent enough to reflect current baselines;
- traceable to a paper, project page, dataset page, or official benchmark;
- useful as a baseline, limitation, dataset, tool, or negative example.

## Exclusion Criteria

Exclude or park sources when:

- the source cannot be identified or retrieved;
- it is only tangentially related;
- it lacks enough metadata to cite or compare;
- it duplicates a stronger version of the same work;
- it is a non-primary summary and the primary source is available.

## Snowballing

After seed papers are found:

1. Check references for foundational work.
2. Check citing papers for newer baselines and critiques.
3. Check project pages for code, datasets, and successor work.
4. Record snowballing queries separately from keyword search.

## Search Stop Conditions

Stop or pause when:

- new queries mostly return already included sources;
- the main method families, datasets, and baselines are represented;
- gaps are explicit enough to become follow-up searches;
- the user-provided budget is reached.
