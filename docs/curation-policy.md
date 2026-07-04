# Curation Policy

This repository accepts skills that help Robotics & AI researchers do concrete work more reliably.

## Accept

- Reusable workflows for literature search, paper reading, evidence synthesis, ideation, writing, reviewing, figures, experiments, code, and reproducibility.
- Skills with narrow triggers and clear completion criteria.
- Skills that explicitly handle citation, provenance, or evidence when scientific claims are involved.
- Tool workflows that include validation, not just usage instructions.

## Reject

- Prompt dumps without workflow or completion criteria.
- Skills that encourage fabricated citations, unsupported claims, or unverifiable benchmark statements.
- Private paths, credentials, lab-only assumptions, or undocumented external services.
- Large third-party content copied without license/provenance review.
- Mega-skills that should be split into a router plus atomic skills.

## Maturity

- `draft`: usable scaffold, not yet forward-tested.
- `beta`: used on at least one realistic task and revised.
- `stable`: used repeatedly across projects with no major scope changes.

## Examples and Forward Tests

Core skills should include either a realistic example in `examples/` or a forward-test fixture in `forward-tests/` before promotion beyond `draft`.

Examples show artifact shape. Forward tests check whether a fresh agent can use the skill without leaked context. Neither should include fabricated citations, unverifiable metrics, private paths, or credentials.

## Provenance

When a skill is inspired by another repo or method, record it in `catalog.json` under `source_inspiration`. This is not a license grant; it is a provenance note. Do not copy source text unless the license permits it and attribution is included.
