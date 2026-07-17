# Forward Test: Survey Synthesis Builder

## Skill

`survey-synthesis-builder`

## Prompt

Use `survey-synthesis-builder` in standard depth for this robot-skills survey.

```markdown
Scope: reusable robot skills from explicit skill libraries through modular VLA
experts and WAM-based arbitration. Generic VLA scaling is out of scope.

Verified evidence:
- CARD-01: classical option/skill methods define initiation, policy, and
  termination, but evaluation is task-specific.
- CARD-02: a modular VLA uses several action experts with learned routing; it
  does not use predicted future consequences.
- CARD-03: a WAM scores candidate action chunks using predicted futures; it
  does not expose multiple named skill heads.

Working matrix:
- All three cards are traceable.
- Cross-embodiment skill arbitration has no included source.

Abandoned draft claim:
- "WAM skill arbitration is the inevitable next stage of robot learning."
  No source is attached.
```

## Expected Artifact Checklist

- Produces a bounded synthesis contract rather than an empirical-paper plan.
- Considers at least two organizing structures before selecting a taxonomy.
- Keeps explicit skills, routed VLA experts, and WAM action-chunk scoring
  distinct.
- Builds traceable synthesis claims and section contracts from CARD ids.
- Treats cross-embodiment arbitration as uncovered within this source set, not
  automatically as a field-wide research gap.
- Rejects or relabels the abandoned draft's deterministic claim.

## Pass Conditions

- The proposed thesis remains true under the limitations of all three cards.
- Taxonomy categories have definitions, membership rules, and edge cases.
- Author proposals remain separate from surveyed findings.

## Fail Conditions

- The response forces Method, Experiments, and Results sections.
- It equates WAM action-chunk scoring with skill-head arbitration.
- It fabricates supporting papers or converts missing coverage into proof of a
  research gap.
