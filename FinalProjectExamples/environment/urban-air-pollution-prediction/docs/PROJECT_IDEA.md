# Predicting Urban Air Pollution Using Sensor Environmental and Temporal Features

## Project Summary

Urban air pollution changes across time and may be related to weather conditions and sensor behavior. This project will use the UCI Air Quality Dataset to investigate how hourly patterns, environmental variables, and metal oxide sensor responses relate to nitrogen dioxide concentration. The main machine learning task will predict hourly `NO2(GT)` using regression models. The central experiment will compare three feature sets to measure whether environmental and engineered temporal features improve prediction beyond sensor measurements alone.

## Domain

Environmental science, urban sensing, data science, and machine learning.

## Primary Research Question

**How much do environmental and engineered temporal features change the accuracy of machine learning models that predict hourly NO2 concentration from air quality sensor measurements?**

The word *change* is intentional. Temporal features may improve performance, have little effect, or make later-period predictions worse. Any of these outcomes is meaningful if the experiment is conducted correctly and reported honestly.

## Supporting Questions

1. How does NO2 concentration vary by hour of day?
2. Are weekday and weekend NO2 patterns different?
3. How does NO2 concentration change across the recorded months?
4. Which metal oxide sensor responses are most strongly associated with NO2?
5. Do temperature, relative humidity, and absolute humidity add predictive value beyond the sensor responses?
6. Do temporal features help all regression models equally?
7. During which hours or pollution ranges does the best model make its largest errors?

## Hypotheses

- **H1:** The distribution of `NO2(GT)` differs across hours of the day.
- **H2:** Adding temperature and humidity variables reduces validation MAE compared with using sensor responses alone.
- **H3:** Adding engineered temporal features changes validation MAE compared with using sensor and environmental variables.
- **H4:** A nonlinear tree-based model achieves a lower validation MAE than Linear Regression.

These hypotheses must be recorded before model results are examined. A hypothesis that is not supported by the results will not be treated as a failed project.

## Dataset

- **Name:** UCI Air Quality Dataset
- **Official source:** [UCI Machine Learning Repository](https://archive.ics.uci.edu/dataset/360/air+quality)
- **Download file:** `AirQualityUCI.csv` from the UCI ZIP archive
- **Dataset type:** Multivariate hourly time-series data
- **Collection setting:** A multisensor air-quality device deployed at road level in a polluted area of an Italian city
- **UCI-reported size:** 9,358 instances and 15 features
- **Observed CSV structure:** 9,471 rows and 17 columns when first loaded; 9,357 nonempty rows and 15 nonempty source columns after blank trailing rows and columns are removed
- **Observed time range:** March 10, 2004 at 18:00 through April 4, 2005 at 14:00
- **Usage note:** UCI states that this dataset may be used for research and excludes commercial use. The official terms must be reviewed before the raw file is redistributed.

## Target Variable

`NO2(GT)` is the hourly averaged nitrogen dioxide concentration measured by a colocated certified reference analyzer. UCI reports its unit as micrograms per cubic meter.

Rows with a missing target will be removed before modeling. In the downloaded CSV, missing numeric measurements use `-200`, which must first be converted to `NaN`.

## Planned Feature Sets

### Feature Set A Sensor Responses

- `PT08.S1(CO)`
- `PT08.S2(NMHC)`
- `PT08.S3(NOx)`
- `PT08.S4(NO2)`
- `PT08.S5(O3)`

### Feature Set B Sensor and Environmental Variables

Feature Set A plus:

- `T`
- `RH`
- `AH`

### Feature Set C Sensor Environmental and Temporal Variables

Feature Set B plus features engineered from `Date` and `Time`:

- sine and cosine encoding of hour
- sine and cosine encoding of day of week
- sine and cosine encoding of month
- weekend indicator

## Variables Excluded from the Main Predictors

The main experiment will not use the following reference-analyzer pollutant measurements as predictors:

- `CO(GT)`
- `NMHC(GT)`
- `C6H6(GT)`
- `NOx(GT)`

These variables could produce an unrealistic or leaky deployment scenario because the project is intended to evaluate prediction from metal oxide sensor responses, environmental measurements, and time. They may be examined during exploratory analysis but will not be used as inputs to the primary models.

## Planned Data Preparation

1. Load the CSV with a semicolon separator and decimal comma.
2. Remove rows and columns that are entirely empty.
3. Combine `Date` and `Time` into a `datetime` column.
4. Sort observations from earliest to latest.
5. Replace numeric `-200` codes with `NaN`.
6. Remove rows with a missing `NO2(GT)` target.
7. Keep feature imputation inside a scikit-learn pipeline so that imputation values are fitted only on training data.
8. Engineer cyclical time features without using the target.

## Experimental Design

The feature set will be the controlled experimental variable. All feature sets will use the same:

- eligible observations
- chronological training, validation, and test periods
- preprocessing rules
- model settings
- random seed where applicable
- evaluation metrics

The data will be divided chronologically into approximately 70% training, 15% validation, and 15% final testing. The final test period will remain untouched until the feature set and model have been selected using validation results. This design is more appropriate than a random split because the observations form a time series and the UCI documentation identifies sensor drift.

## Models

### Required

- Mean prediction baseline using `DummyRegressor`
- Linear Regression
- Decision Tree Regressor

### Optional

- Random Forest Regressor
- Time-series cross-validation
- Peak-pollution error analysis

## Evaluation Metrics

- **MAE:** Primary metric because it expresses average error in the target unit
- **RMSE:** Supporting metric that gives more weight to large errors
- **R squared:** Supporting metric that compares the model with a mean-prediction baseline

The project will not describe R squared as percent accuracy.

## Planned Exploratory Analysis

- distribution of valid NO2 measurements
- missingness by variable and over time
- median NO2 by hour of day
- weekday and weekend hourly profiles
- daily or weekly NO2 trend
- NO2 patterns by month
- sensor-response relationships with NO2
- temperature and humidity relationships with NO2
- identification of high-pollution periods and potential outliers

## Success Criteria

The project will be considered successfully completed when:

- the data preparation is reproducible from the original UCI file;
- all three feature sets are evaluated with the same chronological design;
- the baseline and required regression models are compared using MAE, RMSE, and R squared;
- the final selected configuration is evaluated once on the untouched test period;
- errors are analyzed by time and pollution range;
- negative or mixed results are reported accurately;
- the GitHub repository can be reproduced by following its README;
- the final research paper states the limitations of the data and experiment.

Success does not require temporal features to improve the model or a particular score to be reached.

## Expected Deliverables

- `PROJECT_IDEA.md`
- `DATA_DOCUMENTATION.md`
- `README.md`
- `requirements.txt`
- `notebooks/01_data_preparation.ipynb`
- `notebooks/02_eda.ipynb`
- `notebooks/03_feature_engineering.ipynb`
- `notebooks/04_modeling.ipynb`
- `notebooks/05_error_analysis.ipynb`
- saved figures in `figures/`
- model comparison table in `results/model_results.csv`
- research-style paper
- short technical presentation

## Risks and Limitations

- The dataset represents one historical deployment in one Italian city, so results may not generalize to other cities or current conditions.
- UCI identifies cross-sensitivity, concept drift, and sensor drift in the data.
- Missing values are substantial for some reference measurements, including the target.
- Time and weather associations do not establish that these variables cause pollution changes.
- Model performance may be worse during pollution peaks or later periods.
- Temporal features may describe patterns in the training period without improving future predictions.

## Possible Future Extension

After the UCI project is complete, the same experimental framework could be tested with data from [U.S. EPA AirData](https://www.epa.gov/outdoor-air-quality-data) for a selected U.S. pollutant monitor, geography, and time period. A more advanced science-fair version could collect local low-cost sensor readings and compare them with a nearby reference monitor, subject to mentor approval and a documented calibration plan.

## Proposed Paper Title

**Predicting Urban Air Pollution Using Sensor Environmental and Temporal Features**

