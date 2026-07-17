# Talk Contract

Use this contract before building a full deck.

The audience-first timing and narrative guidance is consistent with Mike
Dahlin's primary guide,
[Giving a Conference Talk](https://www.cs.utexas.edu/~dahlin/professional/goodTalk.pdf).

## Planning Schema

```markdown
# Talk Contract

## Context
- Talk type:
- Audience:
- Purpose:
- Duration and Q&A:
- Venue/mode:
- Output/template:

## Audience Takeaway

## Narrative Beats
| Beat | Question answered | Evidence/visual | Time | Slides |
| --- | --- | --- | --- | --- |

## Storyboard
| Slide | Assertion headline | Job | Primary visual/evidence | Source | Time | Transition |
| --- | --- | --- | --- | --- | --- | --- |

## Backup and Demo Plan

## Risks
```

## Slide Budget Heuristics

Use duration as a constraint, not a quota. A dense result walkthrough may take
two minutes; a transition may take seconds. As a starting range:

| Talk | Typical duration | Starting range |
| --- | --- | --- |
| Lightning/poster pitch | 3-5 min | 4-7 slides |
| Spotlight | 5-8 min | 6-10 slides |
| Lab/project update | 10-20 min | 8-18 slides |
| Conference oral | 15-25 min | 12-22 slides |
| Invited/thesis | 30-50 min | 20-40 slides |

Adjust for demos, audience familiarity, equations, and discussion. Put
secondary results and derivations in backup slides.

## Speaker Note Contract

For each substantive slide, record:

- target time;
- spoken key point;
- how to read the visual or evidence;
- transition to the next slide;
- optional cut point if running late.

## Render QA

- Inspect title, body, captions, equations, citations, legends, and notes.
- Check all slides at actual 16:9 or requested aspect ratio.
- Check minimum readable type and plots at presentation resolution.
- Check contrast without relying on hue alone and verify color-blind-safe plots
  when categories depend on color.
- Check that images are not stretched, cropped misleadingly, or pixelated.
- Check that animations or media have a static fallback.
- Check timing totals and identify slides likely to overrun.
