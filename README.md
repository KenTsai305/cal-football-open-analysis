# Cal football: investment, peer results and coaching progress

An independent, source-linked research snapshot through **October 3, 2026**, prepared October 4. The repository shares the underlying observations so readers can challenge assumptions, correct errors and reach their own conclusions.

**[Read the complete report](https://kentsai305.github.io/cal-football-open-analysis/)** · **[Browse the CSV data](data/)** · **[Sources](data/sources.csv)** · **[Definitions](DATA_DICTIONARY.md)** · **[Contribute](CONTRIBUTING.md)**

Public repository: [KenTsai305/cal-football-open-analysis](https://github.com/KenTsai305/cal-football-open-analysis).

The HTML report is preserved from the existing published analysis, including its three-question sequence, tables, citations and limitations. Use the public Pages link to read it in a browser; GitHub's repository file viewer displays HTML source.

## What the snapshot reports

1. **Investment peers:** Cal places **20th of 21** P4 programs whose estimated roster-budget midpoints are within $2 million of Cal's $22 million midpoint.
2. **First-full-season college head coaches:** Cal places **5th of 6** in the defined P4 cohort. This is not the cohort of all P4 coaches new to their schools. UCLA is an experienced-coach reference outside the six.
3. **Game-to-game progress:** Isolated gains coexist with regression and recurring failures. Sustained improvement is not established; the available evidence does not demonstrate whether retaining or replacing the staff would yield better results.

These are the report's findings, not a requirement that contributors agree. Higher Open CFB ratings mean better current-season schedule-adjusted results. Spending ranges are reported estimates of roster budgets, **not audited player payments or total football expenses**. This is not a financial ROI percentage, a fitted budget-adjusted efficiency model, or proof that coaching inexperience caused results.

## Data and provenance

| File | Contents |
|---|---|
| [`comparison.csv`](data/comparison.csv) | 25 programs: 21 budget peers plus four coaching references; estimates, records, model ranks and ratings, source URLs |
| [`coaching.csv`](data/coaching.csv) | Seven staffing rows, role-experience descriptions, compensation disclosures, cohort position and cited sources |
| [`progress.csv`](data/progress.csv) | Five Cal box scores, denominators and derived offense/defense/rushing averages |
| [`special-teams.csv`](data/special-teams.csv) | Punting, kicking and coverage observations for five games |
| [`adjusted-game-ratings.csv`](data/adjusted-game-ratings.csv) | Published BCF Toys OGR, DGR and SGR observations; explicit unavailable/excluded statuses |
| [`sources.csv`](data/sources.csv) | 42 cited sources with publisher descriptions, URLs and snapshot date |
| [`derived-comparison.csv`](data/derived-comparison.csv) | Reproduced budget midpoints and within-cohort positions |

`provenance/` preserves research JSON snapshots, a report checksum and a reproduced summary. The JSON files are preserved research records, not a substitute for the source publishers. Data sources can update after this snapshot. The repository does not archive entire third-party articles or model datasets.

## Reproduce the calculations and local report

Requires Python 3.9+; no third-party dependencies.

```bash
python scripts/build.py
python -m http.server 8000 --directory docs
```

Open `http://localhost:8000`. The build validates published arithmetic and cohort positions, writes the derived comparison CSV and reproduces the frozen HTML site in `docs/`. It does **not** reconstruct Open CFB or BCF Toys models, fetch live sources, generate new narrative conclusions or apply the old report's iterative patch scripts.

The approved report snapshot lives in `report/`. If changing observations, review the implications for its tables and narrative explicitly. Data-only updates do not automatically update the frozen report; see the contribution workflow.

## Publish with GitHub Pages

This package uses GitHub Pages, not the previous ChatGPT-hosted site. In repository **Settings → Pages**, choose **Deploy from a branch**, select the default branch and **`/docs`**, then save. The published report URL is https://kentsai305.github.io/cal-football-open-analysis/. The root `.nojekyll` marker in `docs/` makes this a plain static site.

## Corrections and independent analyses

Open an issue for a sourcing or calculation problem. Submit a pull request with sourced CSV corrections or additional reproducible analyses. Alternative analyses should distinguish observations, assumptions and conclusions. No contributor needs to agree with the published assessment.

## Snapshot, completeness and reuse

This is a fixed **October 4, 2026** research snapshot covering games through **October 3, 2026**, not a live feed. GitHub publication did not refresh or independently re-check the source observations. Source pages may subsequently change. The observations are selected and incomplete: coaching-cost disclosures are not consistently comparable, some adjusted game ratings are unavailable or excluded, and the underlying publishers' complete datasets are not included. Missing values remain blank and must not be treated as zero.

Sharing the report link, opening issues, proposing sourced corrections and contributing independent analyses are welcome. Preserve source attribution, snapshot dates and limitations; identify changes clearly. Public availability alone is not a blanket license to reuse every item in the repository.

Third-party articles, ratings, datasets and other source material retain their respective owners' rights and applicable terms. This repository grants no license to those materials and makes no representation that they are cleared for commercial use. Anyone reusing source-derived observations, especially commercially, must assess the relevant source terms and obtain any permissions their intended use requires. Source links and inclusion here do not establish ownership or permission. No claim is made to exclusive rights over facts in the public domain.

Original project code is licensed under [MIT](LICENSE), and original writing under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/), allowing sharing and adaptation, including commercial reuse of those original materials, subject to their terms. **These licenses do not grant rights to third-party or source-derived data.** See [licensing scope and attribution](LICENSING.md). Contributions must be your own work or material you have permission to submit, with any third-party attribution and license requirements disclosed.

## Rights and affiliation

Independent analysis; no university affiliation or endorsement. Opinions and conclusions belong to the author. AI agents assisted with gathering and analyzing observations and with a separate verification pass; those checks do not establish source completeness, causal validity or permission to reuse third-party content.
