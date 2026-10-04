# Contributing

Corrections, new observations, methodological challenges and alternative conclusions are welcome.

1. Identify the row/column or report statement and explain the issue.
2. Supply a public source URL, publication/observation date, precise definition and denominator. Prefer primary sources; distinguish estimates from actual expenses.
3. Preserve old snapshot dates. Do not silently mix later games or newer model ratings into the October 4 snapshot. Propose a dated new release for a new cutoff.
4. Keep missing values blank with an explicit explanation; never substitute zero for unavailable evidence. Wagner is FCS and excluded from the adjusted FBS game ratings.
5. Run `python scripts/build.py` and include the output. Check how changes affect both cohort comparisons and narrative conclusions.
6. If updating the approved report, edit `report/index.html`, review it in a browser and deliberately update `provenance/manifest.json`'s checksum and dates. Rebuild `docs/`. The report is a fixed editorial snapshot, so CSV changes alone must not be described as a report refresh.

For alternative analyses, add a self-contained file under `analyses/` with a method, source dates, execution instructions, limitations and results. Do not overwrite the original conclusion just to impose a different preference. Avoid causal claims that observational comparisons cannot support.

Use issues for discussion and pull requests for reviewed updates. Do not publish credentials, private contracts, personal information, complete copyrighted articles or redistributed commercial datasets without appropriate rights.
