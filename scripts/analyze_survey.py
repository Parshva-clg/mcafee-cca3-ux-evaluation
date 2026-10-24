"""Recalculate descriptive survey results from supplied_ratings.json using Python 3."""
from pathlib import Path
import csv,json,statistics
ROOT=Path(__file__).resolve().parents[1]
def write_csv(path,header,rows):
 with path.open('w',newline='',encoding='utf-8') as f:
  w=csv.writer(f);w.writerow(header);w.writerows(rows)
def main():
 src=json.loads((ROOT/'survey_data/supplied_ratings.json').read_text())
 old,new=src['original'],src['redesigned'];questions=src['questions']
 assert len(old)==len(new)==5 and len(questions)==18
 assert all(len(r)==18 for r in old+new)
 assert all(type(x) is int and 1<=x<=10 for r in old+new for x in r)
 raw=[];summary=[];people=[]
 for i in range(5):
  for j,q in enumerate(questions):raw.append([f'P{i+1}',j+1,q['parameter'],old[i][j],new[i][j],new[i][j]-old[i][j]])
  people.append([f'P{i+1}',statistics.mean(old[i]),statistics.mean(new[i]),statistics.mean([b-a for a,b in zip(old[i],new[i])])])
 for j,q in enumerate(questions):
  a=[r[j] for r in old];b=[r[j] for r in new];d=[v-u for u,v in zip(a,b)]
  summary.append([j+1,q['parameter'],5,statistics.mean(a),statistics.mean(b),statistics.mean(d),statistics.median(a),statistics.median(b),sum(v>0 for v in d)])
 write_csv(ROOT/'survey_data/participant_ratings.csv',['participant_id','question_number','parameter','original_rating','redesigned_rating','paired_difference'],raw)
 write_csv(ROOT/'survey_data/parameter_summary.csv',['question_number','parameter','n_paired','original_mean','redesigned_mean','mean_difference','original_median','redesigned_median','participants_with_higher_redesign_rating'],summary)
 write_csv(ROOT/'survey_data/participant_summary.csv',['participant_id','original_mean','redesigned_mean','mean_difference'],people)
 write_csv(ROOT/'survey_data/questionnaire.csv',['question_number','parameter','exact_question','scale_min','scale_max'],[[i+1,q['parameter'],q['question'],1,10] for i,q in enumerate(questions)])
 write_csv(ROOT/'survey_data/participant_profiles.csv',['participant_id','age_years','gender','daily_screen_time','prior_original_use','domain_use_frequency','corrective_lenses_or_colour_vision_deficiency','handedness','regular_fast_paced_games','computer_science_interest'],[[f'P{i+1}',src['ages'][i],'Male',src['screen_time'][i]]+['Not provided']*6 for i in range(5)])
 overall={'participants':5,'parameters':18,'paired_ratings':90,'individual_ratings':180,'scale_min':1,'scale_max':10,'original_sum':sum(map(sum,old)),'redesigned_sum':sum(map(sum,new)),'original_mean':statistics.mean(x for r in old for x in r),'redesigned_mean':statistics.mean(x for r in new for x in r),'mean_difference':statistics.mean(b-a for a,b in zip([x for r in old for x in r],[x for r in new for x in r])),'all_90_pairs_increase':all(r[-1]>0 for r in raw),'duplicate_redesigned_rows':[['P1','P5']] if new[0]==new[4] else []}
 (ROOT/'survey_data/overall_summary.json').write_text(json.dumps(overall,indent=2)+'\n')
 table='| # | Parameter | Original | Redesigned | Difference |\n| --- | --- | ---: | ---: | ---: |\n'+'\n'.join(f'| {row[0]} | {row[1]} | {row[3]:.2f} | {row[4]:.2f} | +{row[5]:.2f} |' for row in summary)
 (ROOT/'analysis/quantitative_analysis.md').write_text(f'''# Quantitative comparison

Five supplied paired records, 18 parameters, scale 1–10. Means are descriptive summaries of ratings; higher is favourable for all items. The project owner supplied the ratings in chat on 25 October 2026. No Google Forms response export was imported. Rows are labelled P1–P5 in supplied order, assuming corresponding original, redesigned and demographic rows belong together. Identity alignment with transcript labels has not been independently verified.

## Results

Original overall descriptive mean: **{overall['original_mean']:.2f}/10**. Redesigned mean: **{overall['redesigned_mean']:.2f}/10**. Mean paired difference: **+{overall['mean_difference']:.2f} points**. Each person's mean across 18 items increased; all 90 supplied paired item ratings increased. These 90 item pairs come from five people, not 90 independent participants. The overall mean gives each item equal weight and is not a validated standardized UX score.

{table}

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
''')
 print(json.dumps(overall,indent=2))
if __name__=='__main__':main()
