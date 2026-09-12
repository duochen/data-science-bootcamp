# Data Documentation

## Dataset Overview

| Item | Description |
|---|---|
| Dataset name | Estimation of Obesity Levels Based on Eating Habits and Physical Condition |
| Provider | UCI Machine Learning Repository |
| Dataset page | [UCI Obesity Levels Dataset](https://archive.ics.uci.edu/dataset/544/estimation+of+obesity+levels+based+on+eating+habits+and+physical+condition) |
| DOI | [10.24432/C5H31Z](https://doi.org/10.24432/C5H31Z) |
| Main data file | `ObesityDataSet_raw_and_data_sinthetic.csv` |
| Geographic context | Mexico, Peru, and Colombia |
| Number of rows | 2,111 |
| Number of columns | 17: 16 predictors and one target |
| Machine-learning task | Seven-class classification |
| Missing values reported by UCI | None |
| License | Creative Commons Attribution 4.0 International (CC BY 4.0) |

## Recommended Repository Location

Save the downloaded CSV as:

```text
data/ObesityDataSet_raw_and_data_sinthetic.csv
```

Do not rename columns until the original file has been preserved. If a cleaned version is created, save it separately, for example:

```text
data/obesity_clean.csv
```

## Source and Citation

The dataset is hosted by the UCI Machine Learning Repository. The accompanying article is:

> Mendoza Palechor, F., & De la Hoz Manotas, A. (2019). Dataset for estimation of obesity levels based on eating habits and physical condition in individuals from Colombia, Peru and Mexico. *Data in Brief, 25*, 104344. https://doi.org/10.1016/j.dib.2019.104344

Suggested dataset citation:

> Palechor, F. M., & de la Hoz Manotas, A. (2019). Estimation of Obesity Levels Based On Eating Habits and Physical Condition [Dataset]. UCI Machine Learning Repository. https://doi.org/10.24432/C5H31Z

Students should record the date on which they downloaded the data because online datasets can be updated.

## How the Data Was Created

The data describes eating habits and physical-condition variables for individuals from Mexico, Peru, and Colombia. According to the dataset creators:

- approximately **23%** of the records were collected directly from users through a web platform; and
- approximately **77%** of the records were generated synthetically using the Weka tool and the SMOTE procedure.

The CSV does not provide a row-level column identifying which records are original and which are synthetic. Therefore, this project cannot reliably compare the two groups or determine the origin of an individual row.

## Column Dictionary

### Demographic and body-measurement variables

| Column | Meaning | Type or coding | Planned use |
|---|---|---|---|
| `Gender` | Gender recorded in the dataset | Categorical: `Female`, `Male` | Demographic extension and subgroup audit |
| `Age` | Age in years | Numeric; some values are decimal because of synthetic generation | Demographic extension and EDA |
| `Height` | Height in meters | Numeric | Body-measurement comparison only |
| `Weight` | Weight in kilograms | Numeric | Body-measurement comparison only |
| `family_history_with_overweight` | Whether a family member has had overweight | Categorical: `yes`, `no` | Lifestyle/context feature |

### Eating-habit variables

| Column | Meaning | Type or coding | Planned use |
|---|---|---|---|
| `FAVC` | Frequent consumption of high-calorie food | Categorical: `yes`, `no` | Lifestyle feature |
| `FCVC` | Frequency of vegetable consumption | Numeric scale, approximately 1–3 | Lifestyle feature |
| `NCP` | Number of main meals | Numeric scale, approximately 1–4 | Lifestyle feature |
| `CAEC` | Consumption of food between meals | Categorical: `no`, `Sometimes`, `Frequently`, `Always` | Lifestyle feature |
| `SMOKE` | Whether the person smokes | Categorical: `yes`, `no` | Lifestyle feature |
| `CH2O` | Daily water consumption | Numeric scale, approximately 1–3 | Lifestyle feature |
| `SCC` | Whether calorie consumption is monitored | Categorical: `yes`, `no` | Lifestyle feature |
| `CALC` | Frequency of alcohol consumption | Categorical: `no`, `Sometimes`, `Frequently`, `Always` | Lifestyle feature |

### Physical-condition and activity variables

| Column | Meaning | Type or coding | Planned use |
|---|---|---|---|
| `FAF` | Frequency of physical activity | Numeric scale, approximately 0–3 | Lifestyle feature |
| `TUE` | Time using technology devices | Numeric scale, approximately 0–2 | Lifestyle feature |
| `MTRANS` | Usual transportation method | Categorical: `Automobile`, `Bike`, `Motorbike`, `Public_Transportation`, `Walking` | Lifestyle feature |

### Target variable

| Column | Meaning | Type | Planned use |
|---|---|---|---|
| `NObeyesdad` | Obesity-level category assigned in the dataset | Seven-class categorical target | Prediction target only |

The seven target labels are:

1. `Insufficient_Weight`
2. `Normal_Weight`
3. `Overweight_Level_I`
4. `Overweight_Level_II`
5. `Obesity_Type_I`
6. `Obesity_Type_II`
7. `Obesity_Type_III`

## Feature Groups for the Experiment

### Set A — Body measurements

```text
Height
Weight
```

### Set B — Lifestyle only

```text
family_history_with_overweight
FAVC
FCVC
NCP
CAEC
SMOKE
CH2O
SCC
FAF
TUE
CALC
MTRANS
```

### Set C — Lifestyle plus demographics

```text
All Set B variables
Age
Gender
```

### Set D — All available predictors

```text
All Set C variables
Height
Weight
```

The target `NObeyesdad` must never be included among the input features.

## Important Potential Issues

### 1. Most records are synthetic

Approximately 77% of the records were generated rather than directly observed. Synthetic examples may make class patterns clearer and model scores higher than they would be on fully independent real-world data.

### 2. Original and synthetic rows are not identified

There is no provenance flag for individual rows. A student must not claim to have measured performance separately on original and synthetic records.

### 3. Target leakage and circular prediction

The target categories are closely related to body measurements. A model using `Height`, `Weight`, or calculated BMI may reproduce the labeling rule rather than discover meaningful lifestyle patterns. For this reason:

- the lifestyle-only model is the main scientific model;
- the height-and-weight model is a comparison;
- calculated BMI is used only for descriptive auditing; and
- target labels are never used as predictors.

### 4. Exact duplicate records

The downloaded UCI file should be checked for duplicate rows. An inspection of the referenced file found 24 rows that exactly duplicated an earlier row. Students should calculate this value themselves, report it, and remove exact duplicates **before** creating the train/test split so that identical records cannot appear in both sets.

### 5. Decimal values in survey-like fields

Fields such as `Age`, `FCVC`, `NCP`, `CH2O`, `FAF`, and `TUE` can contain decimal values. These may result from synthetic generation. Do not round or convert them to integers without documenting and justifying the decision.

### 6. Limited geographic generalizability

The data concerns people from three Latin American countries. Results should not automatically be generalized to U.S. high-school students, all teenagers, or the global population.

### 7. Self-reported variables

At least some source data was collected through a web survey. Eating, activity, and related behaviors may contain recall error or social-desirability bias.

### 8. Association is not causation

This is an observational/synthetic dataset, not a controlled experiment. A predictive association does not prove that changing a particular behavior will change a person's weight or health.

### 9. Sensitive health context

Gender, height, weight, and eating behavior can be sensitive. The project should use respectful language, avoid individual judgments, and never present its output as medical advice or diagnosis.

## Initial Data Validation

Run the following after downloading the file:

```python
from pathlib import Path

import pandas as pd


DATA_PATH = Path("data/ObesityDataSet_raw_and_data_sinthetic.csv")

df = pd.read_csv(DATA_PATH)

print(df.head())
print("Shape:", df.shape)
print("Columns:", df.columns.tolist())
print("Missing values:\n", df.isna().sum())
print("Exact duplicate rows:", df.duplicated().sum())
print("Target counts:\n", df["NObeyesdad"].value_counts())
print(df.info())
```

Expected high-level checks for the referenced UCI file:

```text
Rows: 2111
Columns: 17
Target classes: 7
Missing values: 0
```

If the results differ, stop and verify that the correct file was downloaded. Record any legitimate dataset update rather than silently forcing the data to match these numbers.

## Cleaning Plan

1. Preserve the original CSV unchanged.
2. Confirm the expected filename, shape, columns, and target labels.
3. Check missing values and data types.
4. Count exact duplicates and save the count in the project notes.
5. Remove exact duplicates before splitting the data.
6. Check numeric ranges for impossible values, but do not delete unusual values without evidence.
7. Keep decimal values unless a documented experiment requires another treatment.
8. Encode categorical features inside a machine-learning pipeline.
9. Fit all preprocessing steps using training data only.
10. Save the cleaned dataset or reproducible cleaning script.

Example:

```python
clean_df = df.drop_duplicates().copy()

clean_df.to_csv("data/obesity_clean.csv", index=False)

print("Original rows:", len(df))
print("Rows after deduplication:", len(clean_df))
```

## Train/Test and Preprocessing Rules

- Use one stratified 80/20 train/test split for all feature sets.
- Use a fixed random seed, such as `random_state=42`.
- Keep the test set untouched during model selection.
- Use stratified cross-validation on the training set.
- Standardize numeric variables for Logistic Regression.
- One-hot encode categorical variables using training data only.
- Put preprocessing and the model in a scikit-learn `Pipeline` to prevent leakage.
- Compare feature sets using the same rows, split, cross-validation folds, and metrics.

## Planned Evaluation

The primary metric will be **macro F1**, which gives equal importance to all seven categories. The project will also report:

- balanced accuracy;
- overall accuracy;
- per-class precision and recall; and
- a normalized confusion matrix.

A most-frequent-class baseline must be included. A model is useful only if it is interpreted relative to the baseline and the study limitations.

## Reproducibility Record

Complete this table when the dataset is downloaded:

| Item | Student record |
|---|---|
| Download date | |
| Dataset page URL | |
| Original filename | |
| Original row and column count | |
| Exact duplicate count | |
| Cleaned row and column count | |
| File SHA-256 checksum | |
| Python version | |
| Pandas version | |
| scikit-learn version | |
| Train/test random seed | |

To calculate the SHA-256 checksum:

```python
from hashlib import sha256
from pathlib import Path


path = Path("data/ObesityDataSet_raw_and_data_sinthetic.csv")
checksum = sha256(path.read_bytes()).hexdigest()
print(checksum)
```

## Appropriate and Inappropriate Claims

| Appropriate statement | Statement to avoid |
|---|---|
| “The lifestyle-only model predicted the dataset labels with a macro F1 of …” | “The model diagnoses obesity.” |
| “Physical activity was associated with the target labels in this dataset.” | “Low physical activity causes obesity.” |
| “Performance may be influenced by the synthetic records.” | “The model will work equally well on real patients.” |
| “Results may not generalize beyond the studied data.” | “The findings apply to all teenagers.” |

## Data License and Use

The UCI page lists the dataset under the **Creative Commons Attribution 4.0 International** license. Students may reuse it with proper attribution. Include the dataset citation in the repository README, research paper, and presentation.

## Git Commit

After adding the dataset documentation, use:

```bash
git add DATA_DOCUMENTATION.md
git commit -m "phase-3: add data documentation"
```
