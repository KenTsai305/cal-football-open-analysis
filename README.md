# Cal football: investment, peer results and coaching progress

An independent, source-linked research snapshot through **October 3, 2026**, prepared October 4. The repository shares the underlying observations so readers can challenge assumptions, correct errors and reach their own conclusions.

**[Read the complete report](docs/index.html)** · **[Browse the CSV data](data/)** · **[Sources](data/sources.csv)** · **[Definitions](DATA_DICTIONARY.md)** · **[Contribute](CONTRIBUTING.md)**

The HTML report is preserved from the existing published analysis, including its three-question sequence, tables, citations and limitations. After GitHub Pages is enabled, use the public Pages link to read it in a browser; GitHub's repository file viewer displays HTML source.

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

This package uses GitHub Pages, not the previous ChatGPT-hosted site. In repository **Settings → Pages**, choose **Deploy from a branch**, select the default branch and **`/docs`**, then save. The site URL is normally `https://OWNER.github.io/REPOSITORY/`. Add the actual URL to this README after deployment. The root `.nojekyll` marker in `docs/` makes this a plain static site.

## Corrections and independent analyses

Open an issue for a sourcing or calculation problem. Submit a pull request with sourced CSV corrections or additional reproducible analyses. Alternative analyses should distinguish observations, assumptions and conclusions. No contributor needs to agree with the published assessment.

## Rights and affiliation

Independent analysis; no university affiliation or endorsement. Third-party source material and ratings retain their respective owners' rights. This repository does not grant rights to redistribute an original publisher's complete dataset or article. Source links identify where observations originated. A reuse license for original repository material should be selected explicitly by the repository owner before unrestricted reuse is promised.
