# Contributing

Thanks for helping improve UCL-RAI Skills.

This repository is meant to stay practical, easy to review, and safe to reuse across research and engineering projects. Please keep contributions focused and executable.

## What Makes a Good Skill

A strong skill has:

- A clear trigger: when should an agent use it?
- A concrete workflow: what steps should it follow?
- Explicit constraints: what should it avoid?
- Validation guidance: how can a user know the work is correct?
- Minimal assumptions: no hidden credentials, local-only paths, or undocumented dependencies.

## Add a Skill

1. Create a directory under `skills/<area>/<skill-name>/`.
2. Copy `templates/SKILL.md` into that directory.
3. Fill in the frontmatter and instructions.
4. Add an entry to `catalog.json`.
5. Run:

```bash
python scripts/validate_catalog.py
```

6. Open a pull request and explain:

- What problem the skill solves.
- Who should use it.
- Any external tools, papers, APIs, or datasets it relies on.
- How you tested or sanity-checked the workflow.

## Catalog Entry Format

Each skill entry in `catalog.json` should look like this:

```json
{
  "id": "example-skill",
  "name": "Example Skill",
  "description": "A short description of the concrete task this skill handles.",
  "path": "skills/research/example-skill",
  "tags": ["research", "workflow"]
}
```

## Review Checklist

Before requesting review, check that:

- `python scripts/validate_catalog.py` passes.
- The skill has a narrow, understandable scope.
- The instructions do not require private credentials.
- Claims about tools, libraries, APIs, or research papers are accurate.
- Examples are small enough to inspect.
- The contribution does not include copyrighted text that cannot be redistributed.

## Style

- Use plain technical English in repository files.
- Prefer exact commands over vague guidance.
- Keep examples short and runnable.
- Use links to primary documentation where possible.
- Avoid adding dependencies unless they are necessary.
