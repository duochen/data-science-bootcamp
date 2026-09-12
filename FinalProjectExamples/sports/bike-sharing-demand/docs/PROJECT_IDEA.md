# Project Idea

## Project Title

**Understanding and Predicting Urban Bike-Sharing Demand Using Weather and Temporal Factors**

## Project Summary

Bike-sharing systems must place enough bicycles at the right stations and times, but demand changes with commuting schedules, seasons, holidays, and weather. This project will investigate how calendar, time, and weather variables relate to the number of bicycles rented each hour. It will then compare regression models that predict hourly rental demand using different groups of features. The project is important because better demand estimates may help bike-sharing systems plan bicycle availability, staffing, and maintenance, while also showing how machine learning can support urban transportation decisions.

## Primary Research Question

> **How much predictive value do weather variables add beyond calendar and time variables when estimating hourly bike-sharing demand?**

## Supporting Questions

1. At which hours is bike-sharing demand highest?
2. How do hourly patterns differ between working and nonworking days?
3. How does demand vary across weekdays, months, seasons, and weather categories?
4. Is the relationship between temperature and demand approximately linear?
5. Which model performs best on later, unseen observations?
6. When does the selected model make its largest errors, and does it underestimate peak demand?

## Hypotheses

- **H1:** Hourly demand patterns differ between working and nonworking days.
- **H2:** Calendar and time variables predict demand better than weather variables alone.
- **H3:** Adding weather variables to calendar and time variables reduces validation mean absolute error.
- **H4:** A Decision Tree Regressor performs better than Linear Regression on the chronological validation period.

These hypotheses must be written down before comparing model results. A hypothesis does not need to be correct; the student should report the evidence honestly.

## Dataset

The project will use `hour.csv` from the [UCI Bike Sharing Dataset](https://archive.ics.uci.edu/dataset/275/bike+sharing+dataset). The data describe hourly bicycle rentals from the Capital Bikeshare system during 2011 and 2012, together with calendar, seasonal, and weather information.

The checked `hour.csv` file contains:

- **17,379 rows**
- **17 source columns**
- Dates from **January 1, 2011 through December 31, 2012**
- No null cells in the source file

UCI's repository metadata reports 17,389 instances. The project will document both the official metadata and the row count observed in the downloaded file, but all calculations will use the actual file being analyzed.

## Target Variable

The regression target is:

```text
cnt = total number of bicycles rented during an hour
```

## Experimental Design

The main experiment will compare three controlled feature sets. The same rows, chronological periods, preprocessing rules, models, and evaluation metrics will be used in every comparison.

| Feature set | Variables | Purpose |
|---|---|---|
| **A — Time** | `season`, `yr`, `mnth`, `hr`, `holiday`, `weekday`, `workingday` | Measure how well calendar and time information estimates demand. |
| **B — Weather** | `weathersit`, `temp`, `atemp`, `hum`, `windspeed` | Measure how well weather information estimates demand without time context. |
| **C — Combined** | All variables from Sets A and B | Measure the value of adding weather information beyond calendar and time. |

### Required models

1. Mean-prediction baseline using `DummyRegressor`
2. Linear Regression
3. Decision Tree Regressor

### Optional models

- Random Forest Regressor
- Gradient Boosting Regressor

The optional models should be added only after the required experiment works correctly.

## Evaluation Plan

The rows will be sorted by their reconstructed hourly timestamp and divided chronologically:

- First 70%: training data
- Next 15%: validation data
- Final 15%: test data

The data must not be randomly shuffled for the primary experiment. Models and settings will be selected using only training and validation data. The final test period will be evaluated once after the final configuration has been selected.

The project will report:

- **MAE:** average absolute prediction error in rentals per hour
- **RMSE:** gives additional weight to large errors
- **R²:** compares explained variation with a mean-prediction reference

MAE will be the primary model-selection metric. The student will also examine predicted-versus-actual plots, residuals over time, errors during peak-demand hours, and errors across relevant subgroups.

## Data-Leakage Rules

The following variables will not be used as predictors in the primary models:

- `casual`
- `registered`
- `cnt`
- `instant`
- raw `dteday`
- reconstructed `datetime`

The dataset defines `cnt` as `casual + registered`. Therefore, using `casual` or `registered` to predict `cnt` would give the model part of the answer. `instant` and the raw date may also act as near-direct proxies for a record's position in the two-year series and are excluded from the controlled feature comparison.

## Planned Analyses and Visualizations

The project will include at least six useful figures:

1. Distribution of hourly rental count
2. Median demand by hour
3. Hourly demand on working days versus nonworking days
4. Demand by weekday or month
5. Temperature versus demand
6. Demand by season and weather category
7. Demand over calendar time
8. Predicted versus actual test demand
9. Residuals over time or by demand range

Every figure will have a descriptive title, labeled axes, units when appropriate, a readable legend, and a short written interpretation.

## Expected Tools

- Python
- Jupyter Notebook, VS Code notebooks, or Google Colab
- Pandas and NumPy
- Matplotlib and Seaborn
- Scikit-learn
- Git and GitHub

## Expected Deliverables

- `PROJECT_IDEA.md`
- `DATA_DOCUMENTATION.md`
- Data download instructions and the unchanged `hour.csv` file
- Data-preparation, EDA, feature-engineering, modeling, and error-analysis notebooks
- Saved figures
- `model_results.csv`
- Reproducible `README.md`
- Research-style paper
- Five-to-seven-minute presentation

## Important Limitations

- The data represent one historical bike-sharing system in 2011–2012, so the results may not generalize to another city or a modern system.
- The data are observational. Relationships should be described as associations, not proof that weather or time causes a change in demand.
- The hourly sequence contains missing timestamps even though the source fields have no null values.
- Severe-weather category 4 contains only three records in the checked file, so broad conclusions about severe weather would be unreliable.
- The primary task estimates demand using observed weather values. It should not be called true future forecasting unless the model is supplied with weather forecasts or other information actually available before the predicted hour.

## Possible Future Extensions

- Test the method on recent Capital Bikeshare data.
- Build a true next-hour forecasting experiment using only information available beforehand.
- Compare casual-user and registered-user demand in separate experiments.
- Classify whether an hour will have unusually high demand.
- Evaluate model performance across rolling time periods to study concept drift.

