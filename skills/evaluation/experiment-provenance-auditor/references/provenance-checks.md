# Provenance Checks

Use this reference when auditing experiment traceability.

## Source Patterns

- ACM Artifact Review and Badging distinguishes artifacts that are available, functional, reusable, and able to reproduce or replicate results: https://www.acm.org/publications/policies/artifact-review-and-badging-current
- NeurIPS Code and Data Submission Policy points authors toward code, data, scripts, environments, and instructions that support reproducibility: https://neurips.cc/public/guides/CodeSubmissionPolicy
- Papers with Code's ML Code Completeness Checklist includes dependencies, training code, evaluation code, pretrained models, data processing, and documentation: https://github.com/paperswithcode/releasing-research-code
- FAIR principles emphasize findability, accessibility, interoperability, and reusability of data and metadata: https://www.go-fair.org/fair-principles/

## Result Ledger Fields

| Field | What to capture |
| --- | --- |
| Paper location | Section, table, figure, caption, appendix, or paragraph. |
| Numeric value | Exact score, unit, confidence interval, or qualitative label. |
| Run id | Experiment tracker id, folder, log filename, or job id. |
| Code version | Commit hash, branch, patch state, or release tag. |
| Config | Full config file, command line, launch file, or sweep parameters. |
| Data | Dataset name, version, split, preprocessing, simulator assets, or robot task list. |
| Seeds | Seed list, missing seed policy, and stochastic components controlled. |
| Environment | Python/C++/CUDA/ROS/simulator versions, OS, container, hardware. |
| Post-processing | Scripts or notebooks that turn raw logs into table or figure values. |

## Status Labels

- `verified`: artifact exists and links directly to the manuscript result.
- `ambiguous`: a plausible artifact exists but identity or transformation is unclear.
- `missing`: no artifact was found.
- `not applicable`: the field is genuinely irrelevant for this result.

## Common Gaps

- Plot generated from a notebook cell without saved parameters.
- Table value copied from a chat, spreadsheet, or screenshot without raw log.
- Best seed reported without disclosure.
- Baseline run produced with different code or data preprocessing.
- Robot trial failures excluded without an exclusion rule.
- Simulation assets or pretrained weights unavailable.
- Local absolute paths or private credentials embedded in scripts.

## Repair Priority

1. Restore traceability for main result tables and headline figures.
2. Capture code/config/data versions for all baselines.
3. Save raw logs and plotting scripts before polishing captions.
4. Add an appendix note for irreducible hardware or data constraints.
