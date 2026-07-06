# Limitations Checks

Use this reference to audit limitations and failure cases.

## Source Patterns

- NeurIPS Paper Checklist asks authors to discuss limitations, assumptions, experiment details, and potential negative societal impacts where relevant: https://neurips.cc/public/guides/PaperChecklist
- ACL Rolling Review responsible NLP guidance asks authors to consider research ethics, data, intended use, and risks where applicable: https://aclrollingreview.org/responsibleNLPresearch/
- Model Cards for Model Reporting documents intended use, evaluation factors, performance characteristics, and limitations for released models: https://arxiv.org/abs/1810.03993
- Datasheets for Datasets documents motivation, composition, collection process, recommended uses, and dataset limitations: https://arxiv.org/abs/1803.09010

## Limitation Types

| Type | Question |
| --- | --- |
| Data | Which datasets, splits, demographics, domains, or collection methods constrain the claim? |
| Benchmark | Which tasks, metrics, or evaluation protocols limit interpretation? |
| Robot setup | Which hardware, sensors, objects, scenes, resets, or safety constraints matter? |
| Compute | Does performance depend on expensive training, inference, or search? |
| Robustness | What perturbations, failures, or distribution shifts were not tested? |
| Generality | Which claims apply only to this domain, embodiment, simulator, or method family? |
| Ethics/safety | Could deployment harm users, bystanders, workers, or downstream communities? |

## Failure Case Template

```markdown
Failure: [specific observed or likely failure]
Condition: [when it happens]
Evidence: [log, figure, trial, ablation, or missing test]
Interpretation: [what this says about the method]
Paper action: [limitations text, extra analysis, or claim narrowing]
```

## Good Limitation Language

- Names the boundary precisely.
- Explains the consequence for interpretation.
- Does not pretend the limitation is already solved.
- Does not undermine supported claims outside the limitation.

## Red Flags

- "Future work will explore..." with no current limitation stated.
- Safety or real-world deployment claim from simulation only.
- Failure examples shown without explaining their pattern.
- Limitation section lists generic caveats not connected to this paper.
