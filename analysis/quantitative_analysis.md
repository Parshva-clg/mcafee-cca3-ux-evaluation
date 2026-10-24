# Quantitative comparison

Five supplied paired records, 18 parameters, scale 1–10. Means are descriptive summaries of ratings; higher is favourable for all items. The project owner supplied the ratings in chat on 25 October 2026. No Google Forms response export was imported. Rows are labelled P1–P5 in supplied order, assuming corresponding original, redesigned and demographic rows belong together. Identity alignment with transcript labels has not been independently verified.

## Results

Original overall descriptive mean: **3.77/10**. Redesigned mean: **9.39/10**. Mean paired difference: **+5.62 points**. Each person's mean across 18 items increased; all 90 supplied paired item ratings increased. These 90 item pairs come from five people, not 90 independent participants. The overall mean gives each item equal weight and is not a validated standardized UX score.

| # | Parameter | Original | Redesigned | Difference |
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

Largest mean gain: Search and Discoverability (+6.80). Usability and User Satisfaction both average 10.00 in the redesign versus 3.40 in the original (+6.60). The smallest gain is Efficiency of Interaction (+3.60). Strong agreement and near-ceiling redesign ratings limit discrimination among designs.

## Demographics

All five supplied records are male, ages 18–21 (mean 20.2). Screen time: one under 4 hours, three from 4 to 8 hours, one over 8 hours. No other profile responses were supplied. Missing values are not inferred or randomized.

## Data verification and limits

- P1 and P5 have exactly the same redesigned rating sequence; both are retained as supplied. Confirm with original response records before final submission.
- All 180 ratings are integers in the official 1–10 range; every supplied row contains 18 ratings.
- No raw response timestamps, participant identities or independent response export were supplied. The data is attributed to the project owner, not represented as an automated Google Forms export.
- No significance test is reported. Five paired participants, correlated questionnaire items and an unverified recruitment/testing process limit generalisation and causal conclusions.
- Ratings describe perceptions. They do not establish objective speed, error rates, accessibility compliance or security effectiveness.
- Earlier `SYNTHETIC_demo_*.csv` files are superseded demonstration material, excluded from every result here.

## Recalculation

Run `python3 scripts/analyze_survey.py` from the repository. The script reads `survey_data/supplied_ratings.json` and regenerates the rating, questionnaire, profile and summary files plus this analysis. It does not generate missing responses.
