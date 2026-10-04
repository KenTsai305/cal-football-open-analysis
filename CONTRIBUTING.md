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

## Snapshot and contribution rights

The current snapshot is October 4, 2026, with games through October 3. Publication is not a live data refresh. Preserve unavailable observations and disclosure limitations. Label newer observations as a proposed dated update rather than silently mixing cutoffs.

Submit only your own work or material you have permission to contribute. Identify any third-party material, attribution, license and use restrictions. Publicly accessible source data is not automatically cleared for redistribution or commercial reuse. The project cannot grant rights it does not hold. Unless you explicitly state otherwise before submission, original code contributions are offered under MIT and original writing under CC BY 4.0; see [LICENSING.md](LICENSING.md). Sourced correction proposals remain welcome, but submission does not establish rights to underlying source material.
