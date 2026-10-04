# Data dictionary and interpretation

All observations belong to the **October 4, 2026** snapshot, with games through **October 3**. UTF-8 CSV files use a header row. Empty numeric fields mean missing/not applicable, never zero. Records and dates in the original exports retain their human-readable formats. Source IDs resolve in `sources.csv` and the report's reference list.

## `comparison.csv`

| Column | Definition |
|---|---|
| `program` | Program label as displayed in the report |
| `budget_low_USD_millions`, `budget_high_USD_millions` | Endpoints of the reported 2026 roster-budget estimate, in millions of USD; not audited actual payments |
| `record_through_Oct3_2026` | Overall win–loss record reported by the model publisher at the snapshot cutoff |
| `OpenCFB_FBS_rank` | Publisher's national FBS model rank; lower rank is better; not AP/FPI/SOR |
| `OpenCFB_rating` | Publisher's current-season schedule-adjusted results-and-margin model score; higher is better |
| `comparison_group` | Budget-cohort membership and coaching-reference status |
| `budget_source`, `performance_source` | Source URLs for the respective observations |

Budget selection is all reported P4 programs with midpoints from $20M through $24M inclusive. The 25 rows comprise 21 budget peers and four outside-budget coaching references. The repository contains the selected observations, not the complete source study's P4 budget database, so reproducing the selection's completeness requires consulting that source. The source ranges share a single underlying estimate reproduced by RealGM; they are not independent institutional confirmations.

## `coaching.csv`

| Column | Definition |
|---|---|
| `program` | Six first-full-season HC programs plus UCLA, the experienced-HC reference |
| `head_coach_prior_role` | Coach name, report's experience description, reference numbers |
| `coordinator_experience` | Report's OC/DC experience descriptions; college lower divisions, NFL and co-coordinator experience count when stated |
| `annual_head_coach_compensation_description` | Published compensation rate and qualification; text, not a uniformly comparable cash-expense field |
| `assistant_compensation_description` | Published staff-pool description or disclosure limitation; missing evidence is not zero |
| `roster_budget_description` | Displayed budget range with source reference |
| `group_position` | Within-six position by OpenCFB rating, or outside-cohort label |
| `OpenCFB_FBS_rank`, `OpenCFB_rating` | Same publisher observations as the comparison file |
| `source_ids`, `source_urls` | All cell references for the row, separated by semicolons |
| `*_source_ids`, `*_source_urls` | Per-field-group references for HC role, coordinators, compensation, roster budget and performance |

Missing assistant-compensation citations indicate a disclosure limitation rather than a sourced numeric estimate. Do not add compensation descriptions or rank staff payroll: scopes differ and are incomplete. The first-full-season cohort includes coaches who started with postseason games in 2025; it is not a strict first-game-in-2026 cohort. It also excludes experienced HCs newly hired at another school.

## `progress.csv`

| Columns | Definition |
|---|---|
| `opponent`, `date`, `result` | Cal opponent, 2026 calendar label, and full-game outcome/score |
| `yards`, `plays` | Cal full-game total offensive yards and plays |
| `opp_yards`, `opp_plays` | Opponent full-game total offensive yards and plays |
| `rush_yards`, `rushes`, `opp_rush_yards`, `opp_rushes` | Full-game rushing totals and attempts for Cal/opponent, following college box-score conventions |
| `penalties`, `penalty_yards` | Cal accepted team penalty totals and yards; not a classified pre-snap-error rate |
| `third_made`, `third_attempts` | Cal third-down conversions and opportunities |
| `fbs` | Whether the opponent is FBS; Wagner is False/FCS |
| `source` | Official Cal box-score URL for the row |
| `off_ypp`, `def_ypp` | `yards/plays`, `opp_yards/opp_plays`; higher offense/lower allowed is better |
| `rush_avg`, `opp_rush_avg` | `rush_yards/rushes`, `opp_rush_yards/opp_rushes` |

These are **unadjusted full-game totals**. They include garbage time and do not account for opponent strength or situation. Do not interpret changes as isolated coaching effects. Sacks enter college rushing statistics. Use aggregate yards divided by aggregate opportunities for pooled averages, not an unweighted mean of game ratios.

## `special-teams.csv`

| Columns | Definition |
|---|---|
| `opponent` | Game opponent |
| `punts`, `punt_yards` | Cal punt count and gross punt yards as exported from the box score |
| `punt_return_yards_allowed`, `punt_touchbacks` | Opponent punt-return yards and Cal punt touchbacks |
| `net_punt_average` | `(punt_yards - punt_return_yards_allowed - 20*punt_touchbacks)/punts`; blank when there are no punts |
| `fg_made`, `fg_attempts` | Cal field goals made and attempted; no distance adjustment |
| `pat_made`, `pat_attempts` | Cal kick PATs made and attempted; not two-point attempts |
| `kick_returns_allowed`, `kick_return_yards_allowed` | Opponent kickoff returns and total kickoff-return yards |
| `return_td_allowed` | Opponent punt/kick return touchdowns, combined |
| `source` | Official Cal box-score URL |

Small opportunity counts limit conclusions. Net punting is not adjusted for field position. Return totals omit the context provided by touchbacks and fair catches. The CSV does not fully encode special-teams events described in the report, such as a blocked punt or a fake-punt conversion; consult the cited play-by-play before treating it as a complete unit dataset.

## `adjusted-game-ratings.csv`

| Columns | Definition |
|---|---|
| `opponent` | Game opponent |
| `offense_OGR`, `defense_DGR`, `special_teams_SGR` | BCF Toys opponent-adjusted offense, defense and special-teams scoring value per non-garbage possession; higher is better for all three |
| `status` | `available`, `excluded_fcs` or `unavailable_at_snapshot` |
| `offense_source`, `defense_source`, `special_teams_source` | Publisher URLs for each rating type |
| `checked_date` | Original report's observation date |

Wagner is excluded as FCS. UNLV is unavailable at this snapshot, not assigned a zero or inferred rating. Three available adjusted observations do not establish a five-game adjusted trend. These ratings differ in construction, sample and units from OpenCFB and full-game yards per play.

## `sources.csv`

`source_id`, `title`, `url` and `notes` identify the source and its stated limitations. `snapshot_date` dates the repository's reference registry, not necessarily the source's publication date or a new independent verification. `results_cutoff` dates the games in the report. Publisher date information appears in notes where it was collected. The original source articles and models remain authoritative.

## `derived-comparison.csv`

Recomputed by `scripts/build.py`: `budget_midpoint_USD_millions` is the mean of the range endpoints. `budget_group_position` and `first_full_HC_group_position` are one plus the number of cohort ratings strictly greater than that row's rating; blanks mean outside the cohort. Ties would share a position. These are cohort ranks, not spending-normalized residuals or financial returns.

## Reproducibility boundary

The code checks extracted observations and reproduces arithmetic, cohort positions and static publication assets. Third-party adjusted models are not independently recreated. Completeness of published source inputs and causal validity are not established by passing the script. The report's narrative remains a human-reviewed snapshot.
