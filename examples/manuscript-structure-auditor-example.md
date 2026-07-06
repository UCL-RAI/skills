# Manuscript Structure Auditor Example

## User Prompt

> Audit this introduction for coherence and repetition before I do sentence-level polishing. I want to know whether reviewers can follow the argument.

## Example Input

```markdown
Long-horizon robot manipulation remains difficult because robots must reason over many steps. Recent learning-based methods have shown strong results in manipulation tasks. However, long-horizon manipulation remains challenging in real-world environments. In this paper, we propose a hierarchical policy for long-horizon manipulation. Our method decomposes tasks into subgoals and improves robustness. Existing methods often struggle when tasks require multiple stages. We evaluate our method in simulation and on a robot. The proposed method is simple and effective.
```

## Expected Skill Behavior

The agent should use `manuscript-structure-auditor`, identify the claim thread, map repetition, and recommend structural repairs before rewriting sentences.

## Example Output Shape

```markdown
## Claim Thread
problem: long-horizon robot manipulation is difficult
gap: existing methods struggle with multi-stage tasks
contribution: hierarchical policy decomposes tasks into subgoals
evidence: simulation and robot evaluation
limitation: not stated

## Structure Findings
| Severity | Location | Issue | Why it hurts the paper | Repair action |
| --- | --- | --- | --- | --- |
| major | sentences 1 and 3 | repeated problem statement without narrowing | reviewers see repetition before a precise gap | keep sentence 1, rewrite sentence 3 as the specific gap |
| major | sentence 5 | "improves robustness" lacks setup or evidence | claim appears before evaluation details | move or narrow until the experiment is described |
| minor | sentence 8 | "simple and effective" is promotional and unsupported | weakens scientific tone | replace with scoped evidence or delete |

## Repetition Map
| Repeated idea | Locations | Keep | Remove or merge |
| --- | --- | --- | --- |
| long-horizon manipulation is challenging | sentences 1, 3 | sentence 1 | merge sentence 3 into gap statement |

## Suggested Order
1. Problem and stakes.
2. Specific gap in multi-stage tasks.
3. Method thesis.
4. Evidence preview.
5. Limitations or scope if available.
```

## Quality Checks

- The audit separates structure from grammar.
- Repetition is mapped with locations.
- Repair actions preserve the original scientific claims.
