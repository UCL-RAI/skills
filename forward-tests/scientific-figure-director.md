# Forward Test: Scientific Figure Director

## Skill

`scientific-figure-director`

## Prompt

Use `scientific-figure-director` to specify a figure for a robot learning paper. The method uses offline demonstrations, trains in simulation, and evaluates the final policy on a real robot. The figure must not imply that real-robot data is used for training.

## Expected Artifact Checklist

- Figure job and one-sentence scientific claim are stated.
- Figure type is chosen.
- Panels are specified with content, claim, and required labels.
- Arrow semantics distinguish data flow, training loop, and evaluation.
- Sim/real boundary is explicit.
- Forbidden ambiguities include real-robot training, invented metrics, and unsupported hardware details.
- Audit checklist or verdict criteria are included.

## Pass Conditions

- The figure spec can be handed to an image/diagram tool or human designer.
- The output blocks unsupported visual implications.
- The prompt or spec avoids exact numeric results unless real data is supplied.

## Fail Conditions

- The figure prompt asks an image model to invent results or robot hardware.
- Arrows mix training, inference, and evaluation without labels.
- The sim-to-real boundary is unclear.
