<div align="center">

<img src="./docs/assets/ucl-social-icon-square.jpg" alt="UCL social icon" width="120" />

# UCL-RAI Skills

**Reusable agent skills for research, robotics, AI, and engineering workflows.**

Built by UCL Robotics & AI students for people who want practical, inspectable, and reusable AI-assisted workflows.

[![License: MIT](https://img.shields.io/badge/license-MIT-0f766e.svg)](./LICENSE)
[![Catalog](https://img.shields.io/badge/catalog-json-2563eb.svg)](./catalog.json)
[![Contributions welcome](https://img.shields.io/badge/contributions-welcome-f59e0b.svg)](./CONTRIBUTING.md)

</div>

---

## What This Is

UCL-RAI Skills is a student-led open-source collection of reusable skills for AI coding agents, research assistants, and automation workflows.

The repository is intentionally small at the start. The current catalog contains 12 draft skills that establish the structure, contribution path, validation workflow, and review standards for the first public release.

The homepage style is inspired by clear, developer-facing open-source repositories such as [f/prompts.chat](https://github.com/f/prompts.chat), [DayuanJiang/next-ai-draw-io](https://github.com/DayuanJiang/next-ai-draw-io), and [mattpocock/skills](https://github.com/mattpocock/skills).

## At a Glance

| Area | What to expect |
| --- | --- |
| Research workflows | Literature review, experiment tracking, paper writing, reproducibility, and evaluation helpers. |
| Robotics workflows | Simulation, control, hardware bring-up, debugging, and deployment helpers. |
| AI engineering | Dataset preparation, model evaluation, agent workflows, prompt systems, and tooling. |
| Teaching and coursework | Practical templates that are easy to inspect, adapt, and cite. |

## How to Navigate

Start from one of the three router skills unless you already know the atomic skill you need:

| User goal | Start here |
| --- | --- |
| Enter a field, build a literature base, plan a survey, or brainstorm a Robotics & AI project. | `rai-research-flow` |
| Outline, revise, audit, or prepare a Robotics & AI conference paper. | `rai-paper-flow` |
| Build, debug, test, or review Robotics & AI research code. | `rai-coding-flow` |

Router skills stay thin: they select the right subskills, enforce gates, and name the expected artifacts. Detailed procedures live in focused atomic, reference, or tool skills.

## Skill System

The library is organized as a small research workflow system:

| Layer | Role | Examples |
| --- | --- | --- |
| `flow` | User-invoked orchestration across several skills. | `rai-research-flow`, `rai-paper-flow`, `rai-coding-flow` |
| `atomic` | One concrete repeatable task with a checkable artifact. | `paper-reading-card`, `citation-integrity-auditor` |
| `reference` | Shared rubric or vocabulary used by other skills. | `research-idea-rubric`, `venue-paper-outline` |
| `tool` | Tool-specific workflow or validation protocol. | `scientific-figure-director` |

See [docs/architecture.md](./docs/architecture.md) and [docs/skill-roadmap.md](./docs/skill-roadmap.md) for the design rationale.

## Current Catalog

The initial catalog contains draft skills for the Robotics & AI research lifecycle:

| Skill | Type | Purpose |
| --- | --- | --- |
| `rai-research-flow` | flow | Route research onboarding, surveys, ideation, writing, figures, and audits. |
| `rai-paper-flow` | flow | Route conference-paper writing for Robotics & AI venues. |
| `rai-coding-flow` | flow | Route Robotics & AI coding work. |
| `paper-search-protocol` | atomic | Build reproducible search logs. |
| `paper-reading-card` | atomic | Create source-grounded single-paper cards. |
| `evidence-matrix-builder` | atomic | Build comparison matrices and gap maps. |
| `research-idea-rubric` | reference | Score and refine project ideas. |
| `venue-paper-outline` | reference | Plan ICRA/RSS/CoRL/ICML/ICLR/NeurIPS-style papers. |
| `citation-integrity-auditor` | atomic | Check whether citations support claims. |
| `scientific-figure-director` | tool | Plan, prompt, and audit scientific figures. |
| `paper-red-team-review` | atomic | Perform harsh evidence-grounded paper review. |
| `robotics-ai-coding-flow` | atomic | Apply Robotics & AI code quality checks. |

All current skills are `draft` maturity. They are useful as scaffolds and review targets, but should be forward-tested before being treated as stable.

## Repository Map

```text
.
|-- catalog.json                 # Machine-readable registry
|-- catalog.schema.json          # Catalog schema
|-- docs/                        # Architecture, roadmap, and curation policy
|-- examples/                    # Realistic example prompts and artifact shapes
|-- forward-tests/               # Manual forward-test prompts and pass criteria
|-- skills/                      # Published skills
|-- templates/SKILL.md           # Starter template
|-- scripts/                     # Catalog and forward-test validators
|-- .github/workflows/validate.yml
|-- CONTRIBUTING.md
`-- LICENSE
```

## Quickstart

Clone the repository and validate the catalog:

```bash
git clone https://github.com/UCL-RAI/skills.git
cd skills
python scripts/validate_catalog.py
python scripts/validate_forward_tests.py
```

To draft a new skill:

```bash
mkdir -p skills/research/example-skill
cp templates/SKILL.md skills/research/example-skill/SKILL.md
```

Then add the skill metadata to `catalog.json` and run validation again.

See [docs/usage.md](./docs/usage.md) for local skill usage, validation, and forward-testing guidance.

## Design Principles

- **Executable over decorative.** A good skill should help an agent or human do a concrete task correctly.
- **Small surface area.** Prefer focused skills with clear trigger conditions over large, vague playbooks.
- **Inspectable reasoning.** Include assumptions, constraints, and validation steps where they matter.
- **Research-grade caution.** Do not invent facts, APIs, benchmarks, or citations. Point to primary sources when a skill depends on external knowledge.
- **Reusable by default.** Keep local paths, credentials, and project-specific assumptions out of published skills unless they are explicitly documented.

## Contributing

Contributions are welcome from UCL Robotics & AI students and the wider community.

Start with [CONTRIBUTING.md](./CONTRIBUTING.md), use [templates/SKILL.md](./templates/SKILL.md), and open a pull request with a short example of when the skill should be used.

## Contributors

- [ylhaichen](https://github.com/ylhaichen)

## Status

This is an early scaffold with 12 draft skills. The next milestone is to forward-test the highest-value skills on realistic Robotics & AI research tasks, tighten the boundaries, and promote selected skills from `draft` to `beta`.

## License

Released under the [MIT License](./LICENSE).
