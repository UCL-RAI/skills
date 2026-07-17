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

Use the atomic skills directly when you need one artifact, such as a search log, onboarding map, evidence matrix, related-work position, abstract/introduction draft, benchmark audit, provenance ledger, citation audit, structure audit, limitations audit, writing edit, reviewer response, submission check, or figure spec.

## Grill a Plan Before Execution

Use `research-plan-grill` when the objective, scope, evidence standard,
evaluation, interface, or deliverable is still ambiguous. The skill inspects
available artifacts first, then asks one blocking question at a time and gives
a recommended answer. Use `quick` depth for one immediate blocker, `standard`
for the next artifact, and `deep` before a costly experiment, implementation,
submission, or hardware deployment.

The output is a decision brief that should be handed to the next atomic skill.
Use `research-idea-rubric` afterward when an idea is defined enough to score;
do not use the rubric as a substitute for resolving basic plan ambiguity.

## Build Surveys, Check Code, and Prepare Talks

- Use `survey-synthesis-builder` after verified reading cards and an evidence
  matrix exist. It produces a synthesis contract, taxonomy, claim-evidence
  map, section contracts, and survey draft without imposing an empirical-paper
  structure.
- Use `paper-code-consistency-auditor` when a manuscript and implementation
  may have drifted. Supply identifiable paper and code versions; use
  `experiment-provenance-auditor` separately when result lineage is the actual
  question.
- Use `slide-talk-builder` when the source package, audience, duration, and
  output format are known. A storyboard is an intermediate artifact; a deck is
  complete only after generation, rendering, and visual QA.

## Use Paper Skills Efficiently

For daily paper work, start with `rai-paper-flow` in `quick` mode. This is the default when no depth is specified. It should select one or two subskills, report the largest blocker, and avoid full checklist output.

Use these modes:

| Mode | Scope |
| --- | --- |
| `quick` | Daily edits and triage. Produces top blockers, direct edits, and one next action. |
| `standard` | Normal paper revision. Checks the selected area with focused tables and repair actions. |
| `deep` | Pre-submission, rebuttal-critical, or full audit work. Allows full references, provenance checks, and residual-risk tables. |

Use these paper passes instead of manually invoking many skills:

| Pass | Typical skills |
| --- | --- |
| Draft pass | `manuscript-structure-auditor`, `scientific-writing-editor`, optionally `abstract-introduction-builder` or `related-work-positioning` |
| Claim-evidence pass | `citation-integrity-auditor`, `benchmark-audit`, `limitations-failure-case-auditor` |
| Reviewer-risk pass | `paper-red-team-review` |
| Submission pass | `reviewer-response-builder`, `latex-submission-checker` |

Only use `deep` when the extra detail changes a decision: adding experiments, narrowing claims, preparing a rebuttal, releasing artifacts, or submitting source files.

## Remote Experiments to Local Draft

When experiments run remotely but paper writing happens locally, use a stable
Markdown handoff instead of asking the local agent to reconstruct the project
from copied logs or conversational summaries.

For individual skill installation, install `experiment-dossier-builder` and
`experiment-provenance-auditor` on the remote agent. Install
`paper-draft-builder` plus the writing/evaluation skills listed in its catalog
dependencies on the local agent. If the client can load this repository
directly, use `rai-coding-flow` remotely and `rai-paper-flow` locally instead
of copying each dependency by hand.

1. On the remote machine, run `experiment-dossier-builder` from the project
   root. The default artifact is `paper-handoff/experiment-dossier.md`.
2. Review its snapshot, headline result ledger, failures, and evidence gaps
   before transfer. A result marked `ambiguous` is not paper-ready evidence.
3. Transfer the dossier and only the selected figures/tables needed for
   writing. Use `scp`, `rsync`, Git, or another authorized mechanism outside
   the skill.
4. On the local machine, run `paper-draft-builder` with the dossier, verified
   literature artifacts, target venue, and any existing manuscript.
5. Use `rai-paper-flow quick` for daily section revision; reserve `deep` for a
   full draft consistency or pre-submission pass.

Example prompts:

```text
Use experiment-dossier-builder on this project and write
paper-handoff/experiment-dossier.md. Include all completed seed groups, failed
runs, figure sources, and anything that blocks a defensible paper claim.
```

```text
Use paper-draft-builder with experiment-dossier.md, my verified paper cards,
and the CoRL page constraints. First build the story brief, then produce a
Markdown draft. Keep unsupported claims as visible TODOs.
```

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
