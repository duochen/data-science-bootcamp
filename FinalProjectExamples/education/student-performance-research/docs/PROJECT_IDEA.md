# Project Idea

## Project Title
Beyond Previous Grades: Investigating Academic, Behavioral, and Social Factors Associated with Secondary-School Performance

## Project Topic
Education, Data Science, and Machine Learning

## Project Problem
Students, parents, and teachers often want to understand what factors are related to academic performance. Possible influences include study time, absences, previous grades, family support, internet access, free time, social activity, and health.

This project will use the UCI Student Performance Dataset to investigate which academic, behavioral, and social factors are most strongly associated with students' final grades.

## Main Research Question
**How accurately can student academic performance be predicted without using previous grades?**

This question is important because the dataset includes first-period and second-period grades (`G1` and `G2`), which are strongly related to the final grade (`G3`). A model that uses `G1` and `G2` may predict `G3` very accurately, but that result may not tell us much about the value of other factors.

Therefore, this project will compare two types of models:

- **Model A:** Uses `G1`, `G2`, and other available features to predict `G3`
- **Model B:** Excludes `G1` and `G2` and predicts `G3` using study habits, absences, social factors, family-related factors, health, and other available variables

The main goal is to determine how much predictive power remains when previous grades are removed.

## Secondary Research Question
**Which academic, behavioral, and social factors are most strongly associated with students' final academic performance?**

## Why This Project Matters
Academic performance is influenced by many possible factors. Understanding which variables are most strongly associated with student outcomes may help students and educators think more carefully about study habits, attendance, support systems, and other behaviors.

This project is also useful for learning an important research lesson: a machine-learning model can produce high accuracy without necessarily providing a meaningful explanation. Comparing models with and without previous grades helps separate simple prediction from deeper analysis.

## Hypotheses

### Hypothesis 1
Students who report more study time will tend to have higher final grades.

### Hypothesis 2
Students with more absences will tend to have lower final grades.

### Hypothesis 3
Previous academic performance (`G1` and `G2`) will be substantially more predictive of final grade (`G3`) than lifestyle and social variables alone.

## Dataset
This project will use the **UCI Student Performance Dataset** from the UCI Machine Learning Repository.

Dataset page:

https://archive.ics.uci.edu/dataset/320/student%2Bperformance

The dataset contains information about Portuguese secondary-school students, including grades, demographic characteristics, school-related factors, family-related variables, study habits, social factors, and health-related information.

## Target Variable
The main target variable is:

- `G3` — final grade

## Example Features
Possible input features include:

- `studytime` — weekly study time
- `failures` — number of past class failures
- `absences` — number of school absences
- `famsup` — family educational support
- `internet` — internet access at home
- `freetime` — free time after school
- `goout` — frequency of going out with friends
- `health` — current health status
- `G1` — first-period grade
- `G2` — second-period grade

Additional features may also be used after reviewing the dataset documentation.

## Planned Data Analysis

The project will include:

1. Loading the dataset with Pandas
2. Checking rows, columns, data types, and missing values
3. Exploring distributions of important variables
4. Comparing groups using `groupby()`
5. Creating visualizations
6. Measuring correlations among numeric variables
7. Comparing students with different study-time and absence patterns
8. Investigating relationships between possible predictors and `G3`

## Planned Machine Learning

### Baseline
Create a simple baseline prediction, such as predicting the mean final grade for all students.

### Model A
Train a regression model using:

- `G1`
- `G2`
- academic, behavioral, social, and family-related features

### Model B
Train a regression model without `G1` and `G2`.

Possible models:

- Linear Regression
- Decision Tree Regressor
- Random Forest Regressor (optional)

## Evaluation Metrics
The models will be evaluated using:

- MAE — Mean Absolute Error
- RMSE — Root Mean Squared Error
- R² — Coefficient of Determination

The main comparison will examine how performance changes when `G1` and `G2` are removed.

## Possible Visualizations
Examples include:

- Distribution of final grades
- Study time vs. final grade
- Absences vs. final grade
- Average final grade by study-time category
- Correlation heatmap
- Actual vs. predicted final grades
- Model A vs. Model B performance comparison

## Expected Challenges
Possible challenges include:

- Some relationships may be weak
- Categorical variables will need to be encoded before modeling
- Correlation does not prove causation
- `G1` and `G2` may dominate model performance
- The dataset represents students from a specific population and may not generalize to all schools or countries

## Expected Outcome
The project is expected to show that previous grades are strong predictors of final performance. It will also investigate whether study habits, absences, family-related variables, and social factors provide meaningful predictive information when previous grades are removed.

The most important result is not simply achieving the highest prediction accuracy. The project should explain which features matter, how the models differ, and what conclusions can and cannot be supported by the dataset.

## Research Paper Goal
The final project may be developed into a research-style paper with sections such as:

1. Title
2. Abstract
3. Introduction
4. Research Question
5. Hypotheses
6. Dataset
7. Methodology
8. Exploratory Data Analysis
9. Machine-Learning Experiments
10. Results
11. Discussion
12. Limitations
13. Conclusion
14. References

## GitHub Deliverables
The repository should eventually contain files such as:

```text
README.md
PROJECT_IDEA.md
DATA_DOCUMENTATION.md
data/
notebooks/
src/
figures/
results/
```

The exact structure may be expanded as the project develops.
