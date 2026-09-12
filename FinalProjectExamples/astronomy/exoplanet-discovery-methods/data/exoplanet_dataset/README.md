# NASA Exoplanet Archive Project Dataset

This package contains a reproducible data snapshot for the project **Patterns and Selection Effects in Exoplanet Discovery**.

## Quick facts

- Source: NASA Exoplanet Archive, Planetary Systems Composite Parameters (`pscomppars`)
- Retrieval date: September 12, 2026 (UTC)
- Rows: 6,366 confirmed planets
- Columns: 16
- CSV size: approximately 888 KB
- One row represents one confirmed planet
- Duplicate `pl_name` values found during validation: 0
- Missing `discoverymethod` values found during validation: 0
- Discovery-year range in this snapshot: 1992–2026

The archive changes over time. A later download may have a different number of planets or updated measurements.

## Files

- `data/exoplanets_pscomppars_2026-09-12.csv`: downloaded data snapshot
- `query.adql`: exact query used to retrieve the snapshot
- `SHA256SUMS.txt`: checksum used to verify that the CSV has not changed
- `README.md`: source, variables, validation results, and usage instructions

## Project target classes

The student guide recommends comparing these four discovery methods:

| Discovery method | Rows in this snapshot |
|---|---:|
| Transit | 4,708 |
| Radial Velocity | 1,200 |
| Microlensing | 289 |
| Imaging | 97 |

The CSV includes all discovery methods in the archive, not only these four. Filter the four target classes during data preparation. This preserves the original project snapshot and allows broader exploratory analysis.

## Data dictionary

| Column | Meaning | Unit or type |
|---|---|---|
| `pl_name` | Planet name | Text identifier |
| `hostname` | Host-star or host-system name | Text; use as the grouping variable when splitting data |
| `discoverymethod` | Method credited with discovering the planet | Categorical target |
| `disc_year` | Discovery year | Year |
| `disc_facility` | Facility credited with the discovery | Text; exploratory analysis only |
| `pl_orbper` | Orbital period | Days |
| `pl_orbperlim` | Upper- or lower-limit flag for orbital period | Integer quality-control flag |
| `pl_rade` | Planet radius | Earth radii |
| `pl_radelim` | Upper- or lower-limit flag for planet radius | Integer quality-control flag |
| `pl_bmasse` | Best available planet mass estimate | Earth masses |
| `pl_bmasselim` | Upper- or lower-limit flag for mass | Integer quality-control flag |
| `pl_eqt` | Modeled equilibrium temperature | Kelvin |
| `pl_eqtlim` | Upper- or lower-limit flag for equilibrium temperature | Integer quality-control flag |
| `st_teff` | Host-star effective temperature | Kelvin |
| `st_rad` | Host-star radius | Solar radii |
| `sy_dist` | Distance to the planetary system | Parsecs |

## Load the data

From the project repository root:

```python
import pandas as pd

data_path = "data/exoplanets_pscomppars_2026-09-12.csv"
df = pd.read_csv(data_path)

print(df.shape)
print(df.head())
print(df["discoverymethod"].value_counts())
```

Select the four recommended target classes:

```python
methods = ["Transit", "Radial Velocity", "Imaging", "Microlensing"]
project_df = df[df["discoverymethod"].isin(methods)].copy()
```

## Important cautions

- Many scientific measurement columns contain missing values. Do not delete every row with any missing value.
- A limit flag marks a constrained value rather than an ordinary point estimate. Keep the flags for quality control, but do not use them as physical predictors in the main model.
- Do not use `pl_name`, `hostname`, `discoverymethod`, `disc_year`, or `disc_facility` as predictors in the main classification experiment.
- Keep planets from the same `hostname` together when making training, validation, and test sets. This reduces leakage between related planets in the same system.
- Transit planets greatly outnumber Imaging planets. Use macro F1, balanced accuracy, per-class recall, and a confusion matrix. Do not rely only on raw accuracy.
- Differences between discovery methods can reflect selection effects, follow-up practices, and missing-data patterns. They do not necessarily describe the true population of planets in the galaxy.

## Verify the download

On macOS or Linux, run:

```bash
sha256sum -c SHA256SUMS.txt
```

On Windows PowerShell, run:

```powershell
Get-FileHash .\data\exoplanets_pscomppars_2026-09-12.csv -Algorithm SHA256
```

The reported hash should match the value in `SHA256SUMS.txt`.

## Re-download the snapshot

The TAP endpoint is:

`https://exoplanetarchive.ipac.caltech.edu/TAP/sync`

Submit the contents of `query.adql` as the `query` parameter and request `format=csv`. Save a new file with the new retrieval date instead of overwriting this snapshot.

## Official documentation

- NASA Exoplanet Archive: https://exoplanetarchive.ipac.caltech.edu/
- Column definitions: https://exoplanetarchive.ipac.caltech.edu/docs/API_PS_columns.html
- TAP query guide: https://exoplanetarchive.ipac.caltech.edu/docs/TAP/usingTAP.html
- PSCompPars description: https://exoplanetarchive.ipac.caltech.edu/docs/pscp_about.html

When writing the research paper, record the retrieval date and cite the NASA Exoplanet Archive according to its current citation guidance.

