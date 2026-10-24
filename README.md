# McAfee India comparative UX evaluation

Final CCA3 assignment comparing the original McAfee India website with the redesigned prototype using supplied think-aloud comments and participant ratings.

## Group and prototype

- Project owner: Parshva Bora.
- Other group members: Ashlesha Gawkar, Hriday Sonawane.
- Original: https://www.mcafee.com/en-in/index.html
- [Figma comparison and annotated wireframe](https://www.figma.com/design/8a9YHwjJCdl8i0eRuRhmLt).
- [Supplied HTML prototype](prototype/mcafee-india-redesign.html).

The Figma file contains editable reconstructions and an annotated grayscale wireframe. It was created after the supplied HTML and is not assumed to be the artifact originally tested.

## Final conclusion summary

The five supplied paired records average **3.77/10 for the original** and **9.39/10 for the redesign**, a **+5.62-point** descriptive difference. Every participant's 18-item average increases; all 90 paired item ratings increase. The study has **five participants**, not 90 independent participants.

Supplied comments favour clearer navigation, simpler feature explanations, easier plan comparison, stronger visual hierarchy and more discoverable support information. These findings support improved perceived UX within this small evaluation. They do not establish objective task speed, accessibility compliance or security effectiveness. P3's individual/family-switch comment conflicts with the HTML's actual All-round protection/My devices selector. Redesigned rows P1 and P5 are identical and are preserved for source verification.

See the [final conclusion](reports/final_conclusion.md), [quantitative analysis](analysis/quantitative_analysis.md) and [qualitative analysis](analysis/qualitative_analysis.md).

## Results across the official 18 parameters

Question labels, order and 1–10 scale verified from the [official form](https://forms.gle/wRXTGs5DTg3Qc7qu8) on 25 October 2026. Values below are means across five supplied paired records.

| # | UX parameter | Original | Redesigned | Gain |
| --- | --- | ---: | ---: | ---: |
| 1 | Learnability | 2.80 | 8.60 | +5.80 |
| 2 | Usability | 3.40 | 10.00 | +6.60 |
| 3 | Consistency | 3.40 | 9.20 | +5.80 |
| 4 | Use of Metaphors | 3.20 | 9.40 | +6.20 |
| 5 | Navigation Structure | 3.60 | 9.60 | +6.00 |
| 6 | visual Hierarchy | 3.40 | 9.00 | +5.60 |
| 7 | Accessibility | 4.00 | 9.60 | +5.60 |
| 8 | Responsiveness | 4.20 | 9.80 | +5.60 |
| 9 | Efficiency of Interaction | 5.60 | 9.20 | +3.60 |
| 10 | Feedback and System Status | 4.80 | 9.40 | +4.60 |
| 11 | Error Prevention and Recovery | 4.40 | 9.80 | +5.40 |
| 12 | Aesthetic and Minimalist Design | 3.40 | 8.80 | +5.40 |
| 13 | Content Readability | 3.40 | 8.80 | +5.40 |
| 14 | Search and Discoverability | 2.60 | 9.40 | +6.80 |
| 15 | Performance Perception | 3.60 | 9.20 | +5.60 |
| 16 | Trust and Credibility | 4.40 | 9.40 | +5.00 |
| 17 | Personalization | 4.20 | 9.80 | +5.60 |
| 18 | User Satisfaction | 3.40 | 10.00 | +6.60 |

## Data provenance and missing fields

Ratings, ages, gender and screen time were supplied by the project owner in chat on 25 October 2026. They are recorded as supplied participant data, not as an automated Google Forms export. Corresponding rows are paired in supplied order and assigned P1–P5 labels. Their association with the similarly labelled recordings and transcripts requires verification.

All five profiles are male, ages 18–21 (mean 20.2). Screen time: one under four hours, three from four to eight hours, one over eight hours. Other responses are **Not provided**. No missing answers, identities, timestamps or measured task outcomes have been randomized or invented. Earlier `SYNTHETIC_demo_*.csv` files are superseded demonstrations and are excluded from every current result.

## Repository contents

- `audio_files/`: five supplied Opus recordings, unchanged.
- `transcripts/`: five supplied paired comment texts, unchanged.
- `survey_data/`: supplied raw ratings, verified questionnaire, demographics and descriptive summaries. See [data notes](survey_data/README.md).
- `analysis/`: qualitative themes and quantitative comparison.
- `reports/`: updated brief conclusion in Word and Markdown.
- `prototype/`: supplied HTML, unchanged.
- `scripts/analyze_survey.py`: reproducible calculations, using only Python's standard library.

## Recalculate

```bash
python3 scripts/analyze_survey.py
```

This reads `survey_data/supplied_ratings.json`. It regenerates the five CSV files, overall summary and quantitative analysis without altering the source ratings. The overall mean is an equal-weight descriptive item average, not a validated standardized UX score. No inferential significance test treats the 18 items as independent participants.
