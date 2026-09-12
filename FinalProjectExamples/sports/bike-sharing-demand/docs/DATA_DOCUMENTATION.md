# Data Documentation

## Dataset Name

**UCI Bike Sharing Dataset**

## Official Source

- Dataset page: [UCI Bike Sharing Dataset](https://archive.ics.uci.edu/dataset/275/bike+sharing+dataset)
- DOI: [10.24432/C5W894](https://doi.org/10.24432/C5W894)
- Original study: Fanaee-T, H. and Gama, J. (2014), *Event labeling combining ensemble detectors and background knowledge*, Progress in Artificial Intelligence.
- License: **Creative Commons Attribution 4.0 International (CC BY 4.0)**

The dataset should be cited and attributed when its data or derived results are shared.

## Dataset Description

The dataset contains bicycle-rental counts from the Capital Bikeshare system for 2011 and 2012. The rental data are combined with calendar, seasonal, and weather information. Two main CSV files are provided:

- `hour.csv` — hourly rental observations; the primary file for this project
- `day.csv` — daily summaries of the same system; optional for a separate extension

Do not combine `hour.csv` and `day.csv` as if they contain independent observations. The daily counts summarize the hourly activity.

## File Used in This Project

```text
data/raw/hour.csv
```

The raw file should remain unchanged. Any cleaned or transformed version should be saved separately, for example:

```text
data/processed/bike_sharing_hourly.csv
```

## Verified Size and Coverage

| Item | Official description | Observed in checked `hour.csv` |
|---|---|---|
| Instances | UCI metadata reports 17,389 | 17,379 rows |
| Columns | 13 predictive features in the repository metadata | 17 total source columns, including ID, date, target, and two target components |
| File size | About 1.1 MB | 1,156,736 bytes in the checked archive |
| Date range | 2011–2012 | January 1, 2011 through December 31, 2012 |
| Missing fields | UCI reports no missing values | Zero null cells |
| Time continuity | Hourly records | 165 timestamps are absent from the complete two-year hourly range |

All analysis should be based on the dimensions and contents of the exact file used. The difference between the repository metadata and the downloaded file should be reported rather than hidden or artificially corrected.

## Column Dictionary

| Column | Type | Meaning | Use in this project |
|---|---|---|---|
| `instant` | Integer | Sequential record index | Identifier only; exclude from predictors |
| `dteday` | Date | Calendar date | Used to reconstruct `datetime` and create chronological splits; raw value excluded from primary predictors |
| `season` | Category | 1 = winter, 2 = spring, 3 = summer, 4 = fall | Feature Set A; one-hot encode |
| `yr` | Category | 0 = 2011, 1 = 2012 | Feature Set A; one-hot encode |
| `mnth` | Category | Month 1–12 | Feature Set A; one-hot encode |
| `hr` | Category | Hour 0–23 | Feature Set A; one-hot encode |
| `holiday` | Binary | Whether the date is a holiday | Feature Set A; categorical/binary input |
| `weekday` | Category | Day-of-week code 0–6 | Feature Set A; one-hot encode |
| `workingday` | Binary | 1 if the day is neither a weekend nor a holiday; otherwise 0 | Feature Set A; categorical/binary input |
| `weathersit` | Category | Weather-condition code 1–4 | Feature Set B; one-hot encode |
| `temp` | Numeric | Normalized air temperature | Feature Set B; continuous input |
| `atemp` | Numeric | Normalized perceived or feels-like temperature | Feature Set B; continuous input |
| `hum` | Numeric | Normalized relative humidity | Feature Set B; continuous input |
| `windspeed` | Numeric | Normalized wind speed | Feature Set B; continuous input |
| `casual` | Integer count | Rentals by casual users during the hour | Descriptive EDA only; target component and leakage risk |
| `registered` | Integer count | Rentals by registered users during the hour | Descriptive EDA only; target component and leakage risk |
| `cnt` | Integer count | Total rentals during the hour: `casual + registered` | Regression target |

## Weather Category Codes

| Code | UCI category summary |
|---:|---|
| 1 | Clear, few clouds, or partly cloudy |
| 2 | Mist with cloudy or broken-cloud conditions |
| 3 | Light snow or light rain, including some thunderstorm conditions |
| 4 | Heavy rain, ice pellets, thunderstorm with mist, or snow with fog |

The checked hourly file contains only three category-4 records. Category counts must be reported before interpreting differences in rental demand.

## Normalized Weather Values

The weather columns do not store ordinary physical units directly. The source documentation gives the following conversions:

| Variable | Stored value | Optional interpretation |
|---|---|---|
| `temp` | Normalized using minimum −8°C and maximum 39°C | `temp_c = temp * 47 - 8` |
| `atemp` | Normalized using minimum −16°C and maximum 50°C | `feels_like_c = atemp * 66 - 16` |
| `hum` | Relative humidity divided by 100 | `humidity_percent = hum * 100` |
| `windspeed` | Wind speed divided by 67 | `windspeed_original = windspeed * 67` |

The normalized values may be used directly for modeling. Converted values may be used in selected charts to make the results easier to understand. The units used in a figure must be stated clearly.

## Derived Variables

The following variable will be reconstructed for sorting, validation, plots, and chronological splitting:

```python
df["dteday"] = pd.to_datetime(df["dteday"])
df["datetime"] = df["dteday"] + pd.to_timedelta(df["hr"], unit="h")
```

Readable labels may also be created for EDA:

- `season_name`
- `weather_name`
- `day_type` = working day or nonworking day
- `temp_c`
- `humidity_percent`

These labels should not change the meaning of the source variables.

## Feature Sets

| Set | Variables |
|---|---|
| **A — Time** | `season`, `yr`, `mnth`, `hr`, `holiday`, `weekday`, `workingday` |
| **B — Weather** | `weathersit`, `temp`, `atemp`, `hum`, `windspeed` |
| **C — Combined** | All variables from Sets A and B |

The target is `cnt`. Every model-feature-set combination must use the same eligible observations and chronological evaluation periods.

## Excluded Predictors and Leakage Risks

### Direct target leakage

The following identity should hold for every row:

```text
cnt = casual + registered
```

Therefore, `casual` and `registered` must never be used to predict `cnt`. Including either variable gives the model part of the answer.

### Identifier and time-position leakage

- `instant` is a sequential index and may act as a near-direct indicator of position in the time series.
- Raw `dteday` or `datetime` may allow a model to learn the exact progression through 2011–2012 instead of reusable calendar patterns.

These fields are useful for sorting, plots, and chronological splitting but are excluded from the primary predictor lists. A separate trend-feature experiment may be added later if it is clearly labeled and evaluated forward in time.

## Data-Quality Checks

Run the following checks before EDA or modeling:

```python
from pathlib import Path
import pandas as pd

DATA_PATH = Path("../data/raw/hour.csv")
df = pd.read_csv(DATA_PATH, parse_dates=["dteday"])

df["datetime"] = df["dteday"] + pd.to_timedelta(df["hr"], unit="h")
df = df.sort_values("datetime").reset_index(drop=True)

print("Shape before derived datetime:", (len(df), len(df.columns) - 1))
print("Date range:", df["datetime"].min(), "to", df["datetime"].max())
print("Missing cells:", int(df.isna().sum().sum()))
print("Duplicate rows:", int(df.duplicated().sum()))
print("Duplicate timestamps:", int(df["datetime"].duplicated().sum()))
print(
    "Target identity holds:",
    bool((df["cnt"] == df["casual"] + df["registered"]).all()),
)
```

Check category codes and numeric ranges:

```python
expected_values = {
    "season": {1, 2, 3, 4},
    "yr": {0, 1},
    "mnth": set(range(1, 13)),
    "hr": set(range(24)),
    "holiday": {0, 1},
    "weekday": set(range(7)),
    "workingday": {0, 1},
    "weathersit": {1, 2, 3, 4},
}

for column, allowed in expected_values.items():
    observed = set(df[column].unique())
    assert observed.issubset(allowed), (column, observed - allowed)

assert df["cnt"].ge(0).all()
assert df["temp"].between(0, 1).all()
assert df["atemp"].between(0, 1).all()
assert df["hum"].between(0, 1).all()
assert df["windspeed"].between(0, 1).all()
```

Measure gaps in the hourly sequence:

```python
complete_hours = pd.date_range(
    start=df["datetime"].min(),
    end=df["datetime"].max(),
    freq="h",
)
missing_hours = complete_hours.difference(df["datetime"])

print("Expected hours:", len(complete_hours))
print("Observed hours:", len(df))
print("Missing hourly timestamps:", len(missing_hours))
print(missing_hours[:10])
```

Do not invent rental counts for missing hours. Keep the observed rows and document the gaps. Lagged demand or rolling target features require additional time-safety rules and should not be added to the first version without mentor approval.

## Known and Potential Issues

| Issue | Why it matters | Planned response |
|---|---|---|
| Official metadata and current file row counts differ | Reproducibility depends on the exact file used | Report both values and base calculations on the downloaded file |
| Missing hourly timestamps | The sequence is not perfectly continuous | Keep observed rows, list gaps, and avoid unsupported interpolation |
| `cnt` is the sum of `casual` and `registered` | These two columns cause target leakage | Exclude both from every `cnt` predictor list |
| `instant` and exact date identify time-series position | They may capture growth or exact chronology instead of reusable patterns | Exclude from the primary models; use only for organization and splitting |
| Category 4 has only three records | Severe-weather comparisons are statistically unreliable | Report sample sizes and avoid broad conclusions |
| Hourly demand is right-skewed | Means can be influenced by high-demand periods | Report distributions and compare medians with means |
| `temp` and `atemp` are strongly related | Linear Regression coefficients may be unstable or hard to interpret | Inspect correlation and optionally run a secondary sensitivity analysis removing one |
| Observed rather than forecast weather | The model may not represent a real future forecasting system | Describe the primary task as demand estimation |
| Historical single-system sample | Patterns may change over time and across cities | Limit conclusions to the studied data and propose external validation |
| Observational design | Association does not prove causation | Use association and prediction language |

## Preprocessing Plan

1. Sort rows by reconstructed `datetime`.
2. Keep the original observations; do not randomly shuffle the primary split.
3. Use the first 70% for training, next 15% for validation, and last 15% for testing.
4. One-hot encode categorical variables.
5. Standardize continuous weather variables for Linear Regression.
6. Fit every preprocessing operation using training data only through a Scikit-learn pipeline.
7. Use the same periods, rows, models, and metrics for Feature Sets A, B, and C.
8. Choose the final configuration using validation MAE; evaluate the test period once.

## Bias, Scope, and Responsible Use

This dataset does not describe every cyclist, city, transportation system, or weather condition. The model may perform differently during rare events, after the bike-sharing system changes, or in another location. Its output should not be used by itself to make safety-critical or high-impact public decisions. Results should include uncertainty, subgroup sample sizes, error analysis, and limitations.

## Citation Example

Fanaee-T, H. (2013). *Bike Sharing Dataset* [Dataset]. UCI Machine Learning Repository. https://doi.org/10.24432/C5W894

## Reproducibility Record

Complete this section after downloading the data:

| Field | Student entry |
|---|---|
| Download date |  |
| Source URL |  |
| ZIP filename |  |
| `hour.csv` file size |  |
| `hour.csv` SHA-256 checksum |  |
| Observed rows |  |
| Observed source columns |  |
| Earliest timestamp |  |
| Latest timestamp |  |
| Null cells |  |
| Duplicate rows |  |
| Duplicate timestamps |  |
| Missing hourly timestamps |  |

