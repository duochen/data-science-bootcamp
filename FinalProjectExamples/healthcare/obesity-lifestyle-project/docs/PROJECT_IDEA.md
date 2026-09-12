# Project Idea

## Project Title

**Evaluating the Predictive Value of Lifestyle Factors for Obesity Classification: A Machine-Learning Study**

## Topic

Health, lifestyle, data science, machine learning, and responsible AI

## Project Description

This project will investigate how eating habits, physical activity, transportation, and other lifestyle characteristics relate to the obesity-level labels in a public dataset. The main research question is: **How much information about obesity classification exists in lifestyle characteristics independently of height and weight?** To answer this question, the project will compare machine-learning models trained with body measurements against models trained with lifestyle variables. This topic is important because it demonstrates both the potential and the limitations of using behavioral data in health-related machine learning. The analysis will use the UCI *Estimation of Obesity Levels Based on Eating Habits and Physical Condition* dataset.

## Research Questions

### Main research question

> How much information about obesity classification exists in lifestyle characteristics independently of height and weight?

### Supporting questions

1. Which lifestyle variables are most strongly associated with the dataset's obesity categories?
2. How accurately can a model classify obesity level using lifestyle variables without height and weight?
3. How much better does a model perform when height and weight are included?
4. Which obesity categories are most often confused by the models?
5. Do model results differ across gender groups represented in the dataset?
6. How might the dataset's synthetic records affect model performance and generalizability?

## Hypotheses

- **H1:** A model using height and weight will classify the dataset labels more accurately than a model using lifestyle variables alone.
- **H2:** Lifestyle variables will still contain some useful predictive information after height and weight are excluded.
- **H3:** Physical activity, high-calorie food consumption, transportation method, and family history will be among the more informative lifestyle variables.
- **H4:** Models will make more mistakes between neighboring weight categories than between categories that are farther apart.

These are testable predictions, not conclusions. The evidence may support or contradict them.

## Data I Will Use

The project will use the UCI Machine Learning Repository dataset:

- **Dataset:** Estimation of Obesity Levels Based on Eating Habits and Physical Condition
- **Source:** [UCI dataset page](https://archive.ics.uci.edu/dataset/544/estimation+of+obesity+levels+based+on+eating+habits+and+physical+condition)
- **Dataset DOI:** [10.24432/C5H31Z](https://doi.org/10.24432/C5H31Z)
- **File:** `ObesityDataSet_raw_and_data_sinthetic.csv`
- **Observations:** 2,111
- **Columns:** 17 total: 16 input variables and one target variable
- **Target:** `NObeyesdad`, a seven-category obesity-level label

The records describe people from Mexico, Peru, and Colombia. The dataset creators report that approximately 23% of the records were collected through a web survey and 77% were generated synthetically.

## Planned Experiment

The project will keep the same train/test split and evaluation procedure for every feature set.

| Feature set | Variables | Purpose |
|---|---|---|
| A: Body measurements | Height and Weight | Show how well direct body measurements reproduce the target labels |
| B: Lifestyle only | Eating, activity, technology-use, transportation, family-history, and related behavior variables | Test the main research question without Height or Weight |
| C: Lifestyle plus demographics | Lifestyle variables plus Age and Gender | Measure whether limited demographic information adds predictive value |
| D: All available predictors | Body measurements, lifestyle variables, Age, and Gender | Establish an upper comparison using all available inputs |

`BMI` may be calculated for descriptive analysis, but it will **not** be used as a model input because it is calculated directly from height and weight and is closely related to the target definition.

## Planned Models

1. Most-frequent-class baseline
2. Multinomial Logistic Regression
3. Decision Tree Classifier
4. Random Forest Classifier — optional extension

Model selection will use stratified cross-validation on the training data. The untouched test set will be used only after the model choices have been finalized.

## Evaluation Metrics

- **Macro F1 score** — primary metric because each category should matter equally
- Balanced accuracy
- Per-class precision and recall
- Confusion matrix
- Overall accuracy — reported for context, but not used alone

## Possible Exploratory Analysis

- Distribution of the seven target categories
- Physical activity by obesity category
- Transportation method by obesity category
- High-calorie food consumption by obesity category
- Vegetable and water consumption by obesity category
- Age and gender distributions
- Height, weight, and BMI distributions used only for descriptive auditing
- Exact duplicate records and unusual values

## Expected Visualizations

1. Target-category count chart
2. Physical-activity distribution by target category
3. Transportation method by target category
4. High-calorie food consumption by target category
5. Lifestyle-feature correlation heatmap for numeric variables
6. Model performance comparison chart
7. Confusion matrix for the lifestyle-only model
8. Permutation-importance chart for the lifestyle-only model

## Responsible Research Rules

- This project predicts a **dataset label**; it does not diagnose a medical condition or estimate a person's health risk.
- Results will describe associations and predictive patterns, not prove that a behavior causes obesity.
- The project will not collect classmates' weight, health, or other private personal data.
- The paper will use respectful, person-first language and avoid blaming individuals.
- Results will not be generalized automatically to U.S. teenagers or other populations.
- The synthetic-data limitation will be stated prominently in the paper.

## Definition of Success

The project will be considered successful if it:

- produces a complete, reproducible data-cleaning and modeling workflow;
- compares all four predeclared feature sets fairly;
- evaluates models with appropriate multiclass metrics;
- explains the performance gap between body-measurement and lifestyle-only models;
- includes error analysis, limitations, and responsible interpretation; and
- answers the research question even if the lifestyle-only model performs poorly.

Success does **not** require achieving a particular accuracy.

## Final Deliverables

- Clean and documented dataset workflow
- Jupyter notebooks or Python scripts for EDA and modeling
- Saved figures and evaluation tables
- Research paper
- Presentation slides
- Public GitHub repository with reproducibility instructions

## Possible Paper Title

**Evaluating the Predictive Value of Lifestyle Factors for Obesity Classification: A Machine-Learning Study**

## Initial Repository Commit

After saving this file in the repository root, use:

```bash
git add PROJECT_IDEA.md
git commit -m "phase-1: add project idea"
```
