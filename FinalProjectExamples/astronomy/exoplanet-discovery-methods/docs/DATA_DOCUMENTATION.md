# Dataset Documentation

## Dataset Name

NASA Exoplanet Archive Planetary Systems Composite Parameters (`pscomppars`) project snapshot

## Source

- **Data provider:** NASA Exoplanet Archive
- **Archive home:** https://exoplanetarchive.ipac.caltech.edu/
- **Table:** Planetary Systems Composite Parameters (`pscomppars`)
- **TAP endpoint:** `https://exoplanetarchive.ipac.caltech.edu/TAP/sync`
- **Column documentation:** https://exoplanetarchive.ipac.caltech.edu/docs/API_PS_columns.html
- **PSCompPars description:** https://exoplanetarchive.ipac.caltech.edu/docs/pscp_about.html
- **Retrieval date:** September 12, 2026 (UTC)

The data were downloaded with a saved Astronomical Data Query Language file named `query.adql`. The raw snapshot should not be overwritten. A future download should use a new date in its filename.

## Files

| File | Purpose |
|---|---|
| `data/exoplanets_pscomppars_2026-09-12.csv` | Raw project snapshot downloaded from NASA |
| `query.adql` | Exact query used to select the 16 project columns |
| `SHA256SUMS.txt` | Integrity checksum for the raw CSV |
| `DATA_DOCUMENTATION.md` | Dataset definitions, validation results, and limitations |

## Dataset Size

- **Rows:** 6,366
- **Columns:** 16
- **Row meaning:** One confirmed exoplanet
- **Unique planet names:** 6,366
- **Duplicate planet names:** 0
- **Discovery-year range:** 1992–2026
- **Missing target values:** 0
- **SHA-256:** `3a43ea1f7ee36d56fa49c4b825c058eecfa457c53c1b9f5a41d74fe185a1c033`

After filtering to Transit, Radial Velocity, Imaging, and Microlensing, the planned classification dataset has **6,294 rows before any additional data preparation**.

## Discovery-Method Distribution

| Discovery method | Rows | Included in main classifier? |
|---|---:|---|
| Transit | 4,708 | Yes |
| Radial Velocity | 1,200 | Yes |
| Microlensing | 289 | Yes |
| Imaging | 97 | Yes |
| Transit Timing Variations | 29 | No |
| Eclipse Timing Variations | 17 | No |
| Orbital Brightness Modulation | 9 | No |
| Pulsar Timing | 8 | No |
| Astrometry | 6 | No |
| Pulsation Timing Variations | 2 | No |
| Disk Kinematics | 1 | No |

The target is strongly imbalanced. Transit accounts for most rows, while Imaging is rare. Raw accuracy can therefore be misleading.

## Feature Dictionary

| Column | Meaning | Unit or values | Planned role |
|---|---|---|---|
| `pl_name` | Planet name | Text identifier | Record identifier only |
| `hostname` | Host-star or host-system name | Text identifier | Grouping variable for data splits |
| `discoverymethod` | Method credited with discovering the planet | Category | Classification target |
| `disc_year` | Year the planet was discovered | Year | Exploratory analysis only |
| `disc_facility` | Facility credited with the discovery | Text | Exploratory analysis and leakage audit only |
| `pl_orbper` | Time required for one orbit | Days | Planet-property predictor after log transformation |
| `pl_orbperlim` | Limit flag for orbital period | Quality-control flag | Cleaning only; exclude from main predictors |
| `pl_rade` | Planet radius | Earth radii | Planet-property predictor after log transformation |
| `pl_radelim` | Limit flag for planet radius | Quality-control flag | Cleaning only; exclude from main predictors |
| `pl_bmasse` | Best available planet-mass estimate | Earth masses | Planet-property predictor after log transformation |
| `pl_bmasselim` | Limit flag for mass | Quality-control flag | Cleaning only; exclude from main predictors |
| `pl_eqt` | Modeled equilibrium temperature | Kelvin | Planet-property predictor after log transformation |
| `pl_eqtlim` | Limit flag for equilibrium temperature | Quality-control flag | Cleaning only; exclude from main predictors |
| `st_teff` | Host-star effective temperature | Kelvin | System-context predictor |
| `st_rad` | Host-star radius | Solar radii | System-context predictor |
| `sy_dist` | Distance to the planetary system | Parsecs | System-context predictor after log transformation |

## Missing Values

The following counts were measured directly from the September 12, 2026 snapshot:

| Column | Missing values | Missing percentage |
|---|---:|---:|
| `pl_name` | 0 | 0.00% |
| `hostname` | 0 | 0.00% |
| `discoverymethod` | 0 | 0.00% |
| `disc_year` | 0 | 0.00% |
| `disc_facility` | 0 | 0.00% |
| `pl_orbper` | 350 | 5.50% |
| `pl_orbperlim` | 350 | 5.50% |
| `pl_rade` | 50 | 0.79% |
| `pl_radelim` | 50 | 0.79% |
| `pl_bmasse` | 31 | 0.49% |
| `pl_bmasselim` | 31 | 0.49% |
| `pl_eqt` | 534 | 8.39% |
| `pl_eqtlim` | 534 | 8.39% |
| `st_teff` | 304 | 4.78% |
| `st_rad` | 328 | 5.15% |
| `sy_dist` | 28 | 0.44% |

Missingness may differ by discovery method. It is both a data-quality issue and a possible clue about which measurements each method and its follow-up programs tend to produce.

## Measurement-Limit Flags

A nonzero limit flag identifies a constrained measurement rather than an ordinary point estimate. In this snapshot:

| Measurement | Nonzero limit flags |
|---|---:|
| `pl_orbper` | 6 |
| `pl_rade` | 5 |
| `pl_bmasse` | 234 |
| `pl_eqt` | 3 |

For the first main model, replace limit-flagged measurement values with missing values in the prepared data. Preserve the original values and flags in the raw CSV. Document how many values are changed.

## Planned Data-Preparation Rules

1. Load the raw CSV without editing it.
2. Verify that all 16 required columns are present.
3. Verify that `pl_name` is nonmissing and unique.
4. Filter `discoverymethod` to Transit, Radial Velocity, Imaging, and Microlensing.
5. Convert nonzero-limit measurements to missing values in the prepared working copy.
6. Check numeric predictors for impossible or nonpositive values before logarithmic transformation.
7. Create log-transformed features only when the original value is positive.
8. Create missingness indicators before numerical imputation.
9. Split by `hostname` so a planetary system appears in only one partition.
10. Fit imputation and scaling steps using training data only.

## Recommended Feature Sets

### Feature Set A: Planet Properties

- `log10_pl_orbper`
- `log10_pl_rade`
- `log10_pl_bmasse`
- `log10_pl_eqt`

### Feature Set B: System Context

- `st_teff`
- `st_rad`
- `log10_sy_dist`

### Feature Set C: Combined

All variables from Feature Sets A and B

### Feature Set D: Missingness Audit

One binary indicator for whether each raw measurement is missing or present. This is a diagnostic experiment and should be reported separately from the physical-feature models.

## Excluded Main Predictors

| Variable | Reason for exclusion |
|---|---|
| `pl_name` | Identifier; can support memorization rather than generalization |
| `hostname` | Identifier and grouping key; planets from the same system can be related |
| `discoverymethod` | Target variable |
| `disc_year` | Direct historical clue about when discovery techniques were used |
| `disc_facility` | Closely associated with discovery techniques and likely to create target leakage |
| Limit flags | Quality-control variables that may encode reporting practices |

## Potential Data Issues

### 1. Class Imbalance

Transit has 4,708 rows, while Imaging has only 97. A model that predicts the majority class can have apparently strong accuracy while failing on rare classes. Use macro F1, balanced accuracy, per-class recall, and a confusion matrix.

### 2. Missing Values

Dropping every row with any missing value can disproportionately remove planets from particular discovery methods. Use a training-only median imputer for the main comparison and report a complete-case sensitivity analysis if time permits.

### 3. Selection Effects

The archive is not a random sample of all exoplanets. Telescope sensitivity, survey strategy, distance, orbital geometry, follow-up observation, and publication practices influence which planets appear and which measurements are available.

### 4. Composite Values

The `pscomppars` table selects useful composite values so that each planet has one row. Measurements in the same row may come from different published references and may not form a perfectly self-consistent physical model.

### 5. Dynamic Data

NASA updates the archive as discoveries and measurements change. Results must be tied to the retrieval date, saved query, row count, and checksum.

### 6. Host-System Dependence

Several planets can orbit the same host star. A random row split can place related planets in both training and test data. Use grouped partitions based on `hostname`.

### 7. Target Meaning

`discoverymethod` is the credited historical discovery method. It is not a physical class of planet, and it may not describe every technique later used to confirm or characterize that planet.

### 8. Correlation Is Not Causation

A relationship between a planet property and a discovery method does not prove that the method caused that physical property. The pattern may arise because the method is more sensitive to certain planets.

## Validation Checks

Before modeling, confirm all of the following:

- [ ] The CSV opens successfully with Pandas.
- [ ] The shape is 6,366 rows by 16 columns.
- [ ] Every required column is present.
- [ ] `pl_name` contains no missing values.
- [ ] `pl_name` is unique.
- [ ] `discoverymethod` contains no missing values.
- [ ] The four target classes contain 6,294 rows in total.
- [ ] Missing-value counts are recorded.
- [ ] Limit-flag counts are recorded.
- [ ] The SHA-256 checksum matches `SHA256SUMS.txt`.
- [ ] The retrieval date and ADQL query are committed to GitHub.

## Example Loading Code

```python
import pandas as pd

DATA_PATH = "data/exoplanets_pscomppars_2026-09-12.csv"
TARGET_METHODS = ["Transit", "Radial Velocity", "Imaging", "Microlensing"]

raw = pd.read_csv(DATA_PATH)

assert raw.shape == (6366, 16)
assert raw["pl_name"].notna().all()
assert raw["pl_name"].is_unique
assert raw["discoverymethod"].notna().all()

project_df = raw[raw["discoverymethod"].isin(TARGET_METHODS)].copy()
assert len(project_df) == 6294

print(project_df["discoverymethod"].value_counts())
print(project_df.isna().sum().sort_values(ascending=False))
```

## Citation and Attribution

The research paper should cite the NASA Exoplanet Archive, state the retrieval date, identify the `pscomppars` table, and preserve the exact ADQL query. Consult NASA's current citation guidance before submitting the paper.

