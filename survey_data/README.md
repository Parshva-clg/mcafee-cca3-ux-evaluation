# Survey data

## Current participant ratings

The current analysis uses the five paired rating rows and demographics supplied by the project owner on 25 October 2026. These supplied values are not labelled synthetic. They have not been independently reconciled with a Google Forms response export.

The official form was inspected read-only on that date. All 18 question names, their order and the 1–10 scale were verified. No response was submitted or edited in Google Forms. Higher is favourable on every rating item. The original form's case is retained in `visual Hierarchy`.

- `supplied_ratings.json`: source values exactly as supplied, with the verified questionnaire and row-order assumption.
- `participant_ratings.csv`: 90 paired item records, preserving all 180 ratings.
- `participant_profiles.csv`: ages, gender and screen-time categories. Other profile fields are `Not provided`.
- `questionnaire.csv`: exact parameter and prompt wording in form order.
- `parameter_summary.csv`: means, medians and differences for all 18 parameters.
- `participant_summary.csv`: five paired within-person descriptive averages.
- `overall_summary.json`: totals, overall means and validation checks.

P1–P5 identify supplied row order. Association with the P-labelled recordings and transcripts requires source verification. Redesigned P1 and P5 have identical sequences; neither was changed or silently removed. All records are retained, and duplicate sequences are flagged in the analysis.

No missing answers have been randomized. Prior original-site use, domain use frequency, vision/lenses response, handedness, regular fast-paced gaming and CS interest were not supplied. Names, phone numbers, emails, project group number and interviewer PRN are not reconstructed. No response timestamps are invented.

## Superseded demonstration files

`SYNTHETIC_demo_ratings.csv` and `SYNTHETIC_demo_summary.csv` belong to the earlier demonstration. They are not collected data, do not use the verified official questions/scale, and are excluded from the current analysis. Their explicit labels remain intact to prevent confusion. Git history preserves the earlier report versions.

## Recalculate

Run `python3 scripts/analyze_survey.py`. The analysis treats the five supplied rows as paired in the order given. Overall averages are descriptive equal-weight item summaries, not a standardized UX instrument score. No inferential test treats the 90 item pairs as 90 participants.
