---
name: experiment-dossier-builder
description: Builds a portable, source-grounded Markdown dossier from a remote research project, including method state, experiment design, result ledgers, figures, failures, provenance, and paper-ready claim candidates. Use on the machine that contains the code and experiment outputs when preparing a handoff for local paper writing, collaborator review, or project archiving.
---

# Experiment Dossier Builder

Use this on the machine that can read the project repository and experiment
outputs. Produce one compact evidence handoff for a paper-writing agent; do not
write the paper or copy the whole project into the dossier.

Read `references/dossier-contract.md` before producing the final artifact.

## Inputs

- Project repository, including local instructions and documentation.
- Experiment configs, commands, logs, tracker exports, tables, plots, and
  checkpoints that are in scope.
- Optional target venue, current paper claims, and result priorities.
- Optional output path; default to `paper-handoff/experiment-dossier.md`.

If the available outputs are too large to inspect fully, state the sampling
rule before selecting runs. Never silently summarize only the best runs.

## Workflow

1. Read project instructions, entry points, configs, evaluation code, and
   result-generation paths before interpreting outputs.
2. Record the repository snapshot: project name, commit, branch, dirty state,
   run date range, environment evidence, and scope inspected. Mark unavailable
   fields explicitly.
3. Build a project map that explains the research question, method components,
   training or control pipeline, datasets/environments, evaluation path, and
   important implementation assumptions. Cite repository-relative paths.
4. Inventory experiment families before selecting headline results. Group runs
   by research question, baseline, ablation, seed, dataset/task, and hardware or
   simulator condition where relevant.
5. Build a result ledger. For every number or trend that may enter the paper,
   record its exact source artifact, config/run identity, metric definition,
   aggregation, uncertainty, and provenance status.
6. Trace transformations from raw outputs through analysis scripts to tables
   or figures. Use `experiment-provenance-auditor` when the chain is incomplete
   or publication-grade reproducibility is requested.
7. Extract only evidence-supported candidate claims. Link each claim to result
   rows and record counterevidence, scope limits, and confidence.
8. Capture negative results, failed runs, known bugs, confounders, surprising
   observations, and missing comparisons. These are paper-planning evidence,
   not cleanup noise.
9. Inventory useful figures and tables with repository-relative source paths,
   generation commands when known, and the scientific message each supports.
10. Write the dossier using the contract. End with prioritized evidence gaps
    and concrete next experiments, not generic future work.

## Evidence Status

Use only these labels:

- `verified`: directly supported by inspected artifacts with a traceable chain;
- `derived`: recomputed from verified inputs with the transformation recorded;
- `ambiguous`: plausible source exists but identity or transformation is not
  uniquely established;
- `missing`: required evidence was not found;
- `not-applicable`: the field genuinely does not apply.

Do not use `verified` merely because a filename, README statement, or tracker
run name resembles the claimed experiment.

## Portability Rules

- Use repository-relative paths and stable run or artifact ids in the dossier.
- Sanitize credentials, private hostnames, participant data, and local absolute
  paths. Preserve a useful non-sensitive locator instead.
- Do not embed large logs, checkpoints, datasets, or generated binaries.
- If figures must travel with the dossier, list the smallest selected bundle
  under `paper-handoff/assets/`; do not copy files unless the user requests it.
- Record the transfer mechanism as out of scope. Never assume SSH credentials
  or upload project artifacts without explicit authorization.

## Output

Produce `paper-handoff/experiment-dossier.md` by default. Keep the narrative
concise and make ledgers complete enough that the local agent does not need the
remote filesystem to understand the evidence.

The dossier must contain:

- snapshot and inspection scope;
- research question and method map;
- experiment matrix and result ledger;
- claim-evidence candidates;
- figure/table inventory;
- failures, caveats, and negative results;
- provenance and environment summary;
- prioritized evidence gaps;
- source index and handoff manifest.

## Validation

- Every headline claim points to one or more result-ledger rows.
- Every result row has a source locator and evidence status.
- Metric definitions, aggregation, seeds/sample counts, and uncertainty are
  recorded or explicitly missing.
- Results are not cherry-picked without a declared selection rule.
- Method descriptions point to inspected code/config evidence.
- The Markdown contains no credentials or machine-specific absolute paths.
- A local reader can distinguish fact, interpretation, and proposed narrative.

## Completion

Done means one portable dossier exists, the inspected project snapshot is
identifiable, paper-relevant results are traceable or risk-labeled, and the
remaining evidence gaps are explicit.
