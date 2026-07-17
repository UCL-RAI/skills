# Forward Test: Slide Talk Builder

## Skill

`slide-talk-builder`

## Prompt

Use `slide-talk-builder` to prepare a 10-minute lab project update with 3
minutes of discussion. Editable PPTX is preferred and presentation rendering
tools are available.

```markdown
Audience: Robotics PhD students who know VLA models but not this project.
Takeaway candidate: WAM-based ranking improves selection of action chunks in
simulation, but latency and real-robot transfer remain unresolved.

Verified artifacts:
- architecture.pdf: dense paper architecture with small labels.
- table2.csv: baseline 66.0 +/- 1.5; ours 78.0 +/- 2.0 over three seeds.
- latency.csv: median 180 ms, p95 310 ms.
- failures/: unseen-layout failures in 5 of 12 layouts.
- demo.mp4: simulation demo only; no real-robot video exists.
```

## Expected Artifact Checklist

- Defines audience, purpose, duration, Q&A, and one supported takeaway.
- Allocates time by narrative beat and produces a slide-by-slide storyboard.
- Uses assertion headlines, readable visuals, speaker notes, transitions, and
  optional cut points.
- Redraws or simplifies the dense architecture instead of shrinking it.
- Includes latency and unseen-layout limitations in the main story.
- Labels the demo as simulation and does not imply real-robot validation.
- Generates and renders the requested deck, then reports visual QA findings.

## Pass Conditions

- The deck fits the 10-minute budget without hiding limitations.
- Every quantitative slide preserves values, uncertainty, units, and source.
- Render inspection catches overflow, unreadable figures, and missing assets.

## Fail Conditions

- The response only copies paper sections into bullets or stops at an outline.
- It invents real-robot results, citations, affiliations, or a live demo.
- It claims completion without rendering and inspecting the deck.
