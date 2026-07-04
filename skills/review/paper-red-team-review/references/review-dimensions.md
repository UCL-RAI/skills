# Review Dimensions

## Scientific

- Is the problem important and precisely stated?
- Is the contribution real, or only an implementation combination?
- Does the method section reveal enough to reproduce the core idea?
- Are assumptions and limitations visible?
- Are claims scoped to what was tested?
- Is novelty stated against the closest related work?

## Evidence

- Are baselines strong enough?
- Are ablations tied to claims?
- Are metrics appropriate?
- Is sim-only evidence justified?
- Are failure cases reported?
- Are dataset splits, robot setup, or simulator settings traceable?
- Are uncertainty, variance, or repeated runs reported when they matter?

## Writing

- Does each paragraph have one job?
- Are transitions logical?
- Is the tone scientific rather than promotional?
- Are terms used consistently?

## Figures and Tables

- Does each figure support a claim?
- Are arrows and labels logically correct?
- Are tables comparable across rows and columns?
- Are captions informative enough without overclaiming?

## Citations

- Are citations real?
- Do they support the exact claim?
- Are foundational and recent papers balanced?

## Blocking Patterns

- Main novelty claim is unsupported or already covered by cited prior work.
- Evaluation does not test the core claim.
- Baselines are missing, unfair, or obsolete.
- Method is too underspecified to reproduce.
- Citation audit finds fabricated, wrong, or non-supporting key citations.
- Figure/table implies a result, mechanism, or comparison not supported in text.
- Sim-only results are presented as deployment evidence without justification.

## Repair Path Types

- `rewrite`: narrow or clarify the claim without changing experiments.
- `add-source`: find and cite primary support.
- `replace-baseline`: add or justify a stronger comparison.
- `add-ablation`: isolate the mechanism behind the claim.
- `add-result`: run a missing experiment or report an existing result.
- `redesign-figure`: change visual logic, panels, or labels.
- `de-scope`: remove or weaken a contribution that cannot be defended.
