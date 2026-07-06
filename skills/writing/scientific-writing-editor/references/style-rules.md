# Scientific Style Rules

Use this reference for grammar, clarity, concision, scientific tone, and generic AI-style prose reduction.

## Preserve Meaning

Never silently change:

- numerical values, metrics, dataset names, robot names, or baseline names;
- citation placement or bibliography keys;
- equations, symbols, variables, or algorithm names;
- claim strength, unless narrowing an unsupported claim;
- limitations, uncertainty, or failure cases.

## Scientific Tone

Prefer:

- precise verbs over inflated adjectives;
- scoped claims over universal claims;
- concrete subjects over vague "this work" chains;
- active voice when it improves clarity;
- explicit uncertainty where evidence is limited.

Avoid:

- "significantly" unless statistical significance is shown;
- "novel", "robust", "seamless", "comprehensive", or "state-of-the-art" without support;
- generic openings such as "In recent years" unless time trend matters;
- promotional language such as "revolutionary" or "groundbreaking";
- overstuffed transitions such as "Furthermore, it is important to note that".

## Concision Rules

| Pattern | Prefer |
| --- | --- |
| "due to the fact that" | "because" |
| "in order to" | "to" |
| "it is worth noting that" | remove or state the point directly |
| "a large number of" | "many" or the exact count |
| "is able to" | "can" |
| "we conduct experiments to evaluate" | "we evaluate" |

## Grammar Checks

- Subject-verb agreement.
- Article use for countable nouns.
- Consistent tense within method, result, and discussion.
- Correct prepositions for technical phrases.
- Parallel structure in contribution lists.
- Clear antecedents for "this", "it", and "they".

## AI-Style Pattern Checks

Remove or rewrite:

- repeated sentence templates across paragraphs;
- balanced but empty phrases such as "not only ... but also" when no contrast matters;
- excessive hedging plus excessive confidence in the same sentence;
- generic summary sentences that do not add a claim, transition, or evidence;
- formulaic paragraph endings that restate the topic without advancing the argument.

## Academic Humanizer Checks

These checks adapt the installed `humanizer` skill's AI-writing pattern cleanup to academic paper prose. Apply them conservatively: the goal is natural scientific writing, not casual voice or AI-detector evasion.

| Pattern | Academic risk | Edit direction |
| --- | --- | --- |
| Significance inflation | Makes ordinary claims sound grander than the evidence. | Replace "crucial", "pivotal", "transformative", or "plays a key role" with the specific contribution. |
| Superficial `-ing` add-ons | Adds fake depth after a complete sentence. | Split the sentence or remove the dangling explanation unless it adds evidence. |
| Promotional adjectives | Sounds like a press release. | Replace "groundbreaking", "seamless", "comprehensive", "robust", or "powerful" with measured, testable claims. |
| Vague attribution | Hides missing citations. | Replace "recent studies show" or "researchers argue" with a specific citation, or flag evidence needed. |
| Copula avoidance | Makes prose ornate. | Prefer "is", "are", "has", or a precise verb over "serves as", "stands as", "boasts", or "showcases". |
| Rule-of-three padding | Forces false completeness. | Keep only the listed items that matter scientifically. |
| Negative parallelism | Creates rhetorical flourish without precision. | Replace "not only X but also Y" with the actual relationship. |
| False ranges | Implies a scale where none exists. | Replace "from X to Y" lists with direct categories. |
| Em dash overuse | Makes academic prose feel generated or promotional. | Use commas, parentheses, or separate sentences where clearer. |
| Synonym cycling | Damages technical consistency. | Reuse the same technical term for the same concept. |
| Generic positive endings | Adds empty closure. | End with the concrete finding, limitation, or next evidence need. |
| Chatbot artifacts | Leaves assistant voice in manuscript text. | Remove "here is", "let us", "this section explores", or "I hope this helps". |

## Voice Calibration

If the user provides a writing sample:

- match approximate sentence length and paragraph density;
- preserve their preferred spelling variant;
- keep their terminology and transition style when it is scientifically clear;
- avoid over-polishing into generic academic prose;
- do not import personal voice features that would be inappropriate for a conference paper.

If no sample is provided, default to concise, precise, reviewer-friendly academic prose.

## Edit Strength

- `light`: grammar, punctuation, and small clarity fixes only.
- `medium`: improve sentence structure, concision, and tone while preserving paragraph order.
- `heavy`: rewrite paragraph flow locally, but do not change scientific claims or evidence order.
