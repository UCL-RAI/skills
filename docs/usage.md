# Usage

This repository can be used in three modes:

- as a source repository for reading and improving Robotics & AI skills;
- as a local skill library for agents that support `SKILL.md`-style skills;
- as a forward-test suite for checking whether skills produce useful artifacts.

## Validate the Repository

Run both validators before opening a pull request:

```bash
python scripts/validate_catalog.py
python scripts/validate_forward_tests.py
git diff --check
```

`validate_catalog.py` checks catalog metadata, skill frontmatter, dependency integrity, path safety, required skill sections, reference links, line counts, and package-level `license` / `compatibility`.

`validate_forward_tests.py` checks that each forward test names a known skill and includes prompt, expected artifact checklist, pass conditions, and fail conditions.

## Use with Codex-Style Local Skills

For local Codex setups that load skills from a skills directory, copy or symlink individual skill folders from `skills/<area>/<skill-name>/` into the local skills directory used by that client.

Preserve this shape:

```text
skill-name/
|-- SKILL.md
`-- references/
    `-- optional-reference.md
```

Install only the skills you need. Start with the router skills if you want the full workflow:

- `skills/flows/rai-research-flow`
- `skills/flows/rai-paper-flow`
- `skills/flows/rai-coding-flow`

Use the atomic skills directly when you need one artifact, such as a search log, evidence matrix, citation audit, or figure spec.

## Use with Claude Code or Other Manual Skill Clients

This repo uses self-contained `SKILL.md` folders and one-level `references/` files so it can be adapted to clients that support Agent Skills-style packages.

Client-specific installation paths and strict metadata support can differ. If a strict parser rejects custom frontmatter such as `disable-model-invocation`, keep the skill body and move that flag into client-specific configuration or remove it before installing the flow skill.

Do not assume a client will load repo-level files such as `catalog.json`, `examples/`, or `forward-tests/`. Those files are for discovery, validation, and maintainers.

## Forward-Test a Skill

Use `forward-tests/` to test skills in a fresh agent context:

1. Pick a forward test.
2. Start a fresh context.
3. Ask the agent to use the named skill on the prompt.
4. Compare the result against the checklist and pass/fail conditions.

Forward tests are designed to check artifact quality and failure-mode handling, not to grade research truth.
