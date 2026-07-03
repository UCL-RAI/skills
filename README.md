<div align="center">

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

The repository is intentionally small at the start. The first public skills will be added after review; until then, this repo provides the structure, contribution path, validation workflow, and skill template.

The homepage style is inspired by clear, developer-facing open-source repositories such as [f/prompts.chat](https://github.com/f/prompts.chat), [DayuanJiang/next-ai-draw-io](https://github.com/DayuanJiang/next-ai-draw-io), and [mattpocock/skills](https://github.com/mattpocock/skills).

## At a Glance

| Area | What to expect |
| --- | --- |
| Research workflows | Literature review, experiment tracking, paper writing, reproducibility, and evaluation helpers. |
| Robotics workflows | Simulation, control, hardware bring-up, debugging, and deployment helpers. |
| AI engineering | Dataset preparation, model evaluation, agent workflows, prompt systems, and tooling. |
| Teaching and coursework | Practical templates that are easy to inspect, adapt, and cite. |

## Repository Map

```text
.
|-- catalog.json                 # Machine-readable registry of published skills
|-- skills/                      # Published skills live here
|-- templates/SKILL.md           # Starter template for new skills
|-- scripts/validate_catalog.py  # Lightweight catalog validation
|-- .github/workflows/validate.yml
|-- CONTRIBUTING.md
`-- LICENSE
```

## Current Catalog

No public skills have been added yet.

The catalog is ready for reviewable entries once the first skills are selected. Each published skill should have:

| Field | Purpose |
| --- | --- |
| `id` | Stable kebab-case identifier. |
| `name` | Human-readable title. |
| `description` | One-sentence summary of what the skill does. |
| `path` | Directory containing the skill's `SKILL.md`. |
| `tags` | Searchable topics such as `robotics`, `research`, `python`, or `evaluation`. |

## Quickstart

Clone the repository and validate the empty catalog:

```bash
git clone https://github.com/UCL-RAI/skills.git
cd skills
python scripts/validate_catalog.py
```

To draft a new skill:

```bash
mkdir -p skills/research/example-skill
cp templates/SKILL.md skills/research/example-skill/SKILL.md
```

Then add the skill metadata to `catalog.json` and run validation again.

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

This is an early scaffold. The first skills will be added after the maintainers agree on scope, naming, and review standards.

## License

Released under the [MIT License](./LICENSE).
