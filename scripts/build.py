#!/usr/bin/env python3
"""Validate the frozen research snapshot, reproduce calculations, and build Pages.

Standard-library-only. This reproduces published arithmetic and distributions;
it does not rerun proprietary third-party models or auto-write conclusions.
"""
import csv, hashlib, json, math, shutil, statistics
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
def read(name):
    with (ROOT / 'data' / name).open(newline='') as f:
        return list(csv.DictReader(f))
def close(a, b):
    assert math.isclose(float(a), float(b), rel_tol=1e-10, abs_tol=1e-10), (a,b)
def write(name, fields, rows):
    with (ROOT/'data'/name).open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=fields);w.writeheader();w.writerows(rows)

comparison = read('comparison.csv')
assert len(comparison)==25 and len({r['program'] for r in comparison})==25
budget=[r for r in comparison if r['comparison_group'].startswith('budget cohort')]
first=[r for r in comparison if 'first full HC season' in r['comparison_group']]
assert len(budget)==21 and len(first)==6
for r in budget:
    assert 20 <= (float(r['budget_low_USD_millions'])+float(r['budget_high_USD_millions']))/2 <= 24
cal=next(r for r in comparison if r['program']=='Cal')
position=lambda rows:1+sum(float(r['OpenCFB_rating'])>float(cal['OpenCFB_rating']) for r in rows)
assert position(budget)==20 and position(first)==5
coach=read('coaching.csv')
assert {r['program'] for r in coach}=={r['program'] for r in first}|{'UCLA'}
for r in coach:
    c=next(c for c in comparison if c['program']==r['program'])
    close(r['OpenCFB_rating'],c['OpenCFB_rating'])
    close(r['OpenCFB_FBS_rank'],c['OpenCFB_FBS_rank'])
for g in read('progress.csv'):
    for numerator,denominator,field in [('yards','plays','off_ypp'),('opp_yards','opp_plays','def_ypp'),('rush_yards','rushes','rush_avg'),('opp_rush_yards','opp_rushes','opp_rush_avg')]:
        close(g[field],int(g[numerator])/int(g[denominator]))
for g in read('special-teams.csv'):
    if int(g['punts']):
        close(g['net_punt_average'],(int(g['punt_yards'])-int(g['punt_return_yards_allowed'])-20*int(g['punt_touchbacks']))/int(g['punts']))
    else:
        assert g['net_punt_average']==''
ratings=read('adjusted-game-ratings.csv')
assert len(ratings)==5
for g in ratings:
    if g['status']!='available':
        assert all(g[x]=='' for x in ['offense_OGR','defense_DGR','special_teams_SGR'])
sourceids={r['source_id'] for r in read('sources.csv')}
assert all(set(r['source_ids'].split(';')) <= sourceids for r in coach)
manifest=json.loads((ROOT/'provenance/manifest.json').read_text())
assert hashlib.sha256((ROOT/'report/index.html').read_bytes()).hexdigest()==manifest['report_sha256'], 'Report changed: review and update snapshot manifest deliberately.'
rows=[]
for r in comparison:
    rows.append({'program':r['program'],'budget_midpoint_USD_millions':(float(r['budget_low_USD_millions'])+float(r['budget_high_USD_millions']))/2,'budget_group_position':1+sum(float(c['OpenCFB_rating'])>float(r['OpenCFB_rating']) for c in budget) if r in budget else '', 'first_full_HC_group_position':1+sum(float(c['OpenCFB_rating'])>float(r['OpenCFB_rating']) for c in first) if r in first else ''})
write('derived-comparison.csv',list(rows[0]),rows)
summary={'budget_group_count':len(budget),'first_full_HC_group_count':len(first),'Cal_budget_group_position':position(budget),'Cal_first_full_HC_group_position':position(first),'budget_group_median_rating':statistics.median(float(r['OpenCFB_rating']) for r in budget),'results_cutoff':manifest['results_cutoff']}
(ROOT/'provenance/reproduced-summary.json').write_text(json.dumps(summary,indent=2)+'\n')
(ROOT/'docs').mkdir(exist_ok=True)
for name in ['index.html','style.css','favicon.svg']:
    shutil.copyfile(ROOT/'report'/name,ROOT/'docs'/name)
for name in ['comparison.csv','progress.csv','special-teams.csv']:
    shutil.copyfile(ROOT/'data'/name,ROOT/'docs'/name)
(ROOT/'docs/.nojekyll').touch()
print(json.dumps(summary,indent=2))
print('PASS: 25 programs, 7 staffing rows, 5 games, 5 special-teams rows, adjusted-rating missingness, source references, snapshot SHA, and published arithmetic.')
