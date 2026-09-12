# Dataset Documentation

## Dataset Name
UCI Student Performance Dataset

## Source
The dataset comes from the **UCI Machine Learning Repository**.

Dataset page:

https://archive.ics.uci.edu/dataset/320/student%2Bperformance

The dataset contains student achievement information from Portuguese secondary schools.

## Purpose of the Dataset in This Project
The dataset will be used to study relationships between student academic performance and factors such as:

- study time
- absences
- previous grades
- family support
- social activity
- free time
- internet access
- health
- school-related variables

The primary target variable will be the student's final grade, `G3`.

## Files
The UCI dataset contains student performance data for two subjects:

- Mathematics
- Portuguese language

Students should use one subject dataset first so that the project remains easy to manage and interpret.

Recommended starting file:

```text
student-mat.csv
```

An advanced version of the project may later compare the mathematics and Portuguese datasets.

## Dataset Size
The dataset contains hundreds of student records and about 30 variables.

The exact number of rows depends on which subject file is used.

Before beginning analysis, the student should confirm the exact size with Pandas:

```python
import pandas as pd

df = pd.read_csv("student-mat.csv", sep=";")

print(df.shape)
```

Record the result here after loading the dataset:

- Number of rows: __________
- Number of columns: __________

## Target Variable

### `G3`
Final grade.

This will be the main target variable for regression.

Possible alternative use:

- Convert `G3` into categories such as Pass / Fail for a classification extension

## Important Predictor Variables

### Academic Variables

#### `G1`
First-period grade.

This variable is expected to be strongly related to `G3`.

#### `G2`
Second-period grade.

This variable is also expected to be strongly related to `G3`.

#### `studytime`
Weekly study time.

This variable can be used to investigate whether students who study more tend to receive higher final grades.

#### `failures`
Number of previous class failures.

This may be associated with future academic performance.

#### `absences`
Number of school absences.

This can be used to investigate whether missing more school is associated with lower academic performance.

## Family and Support Variables

### `famsup`
Whether the student receives family educational support.

### `schoolsup`
Whether the student receives extra educational support from the school.

### `paid`
Whether the student receives extra paid classes related to the subject.

### `higher`
Whether the student wants to pursue higher education.

These variables may help investigate whether support and educational goals are related to academic performance.

## Lifestyle and Social Variables

### `freetime`
Amount of free time after school.

### `goout`
Frequency of going out with friends.

### `health`
Current health status.

### `internet`
Whether the student has internet access at home.

These variables may help investigate whether lifestyle and access factors are related to final grades.

## Other Variables
The dataset also contains demographic, family, school, and personal variables.

Students should review the full UCI dataset description before deciding which features to include in the final model.

## Data Types
The dataset includes both:

- Numerical variables
- Categorical variables

Examples of numerical variables:

```text
age
studytime
failures
absences
G1
G2
G3
```

Examples of categorical variables may include:

```text
school
sex
address
famsize
Pstatus
schoolsup
famsup
paid
internet
higher
```

Categorical variables must be converted into numerical form before many machine-learning models can use them.

A common approach is one-hot encoding.

## File Format
The UCI student dataset is stored as a text-based CSV-style file.

Important:

The separator may be a semicolon (`;`) instead of a comma.

Example:

```python
df = pd.read_csv("student-mat.csv", sep=";")
```

If the file does not load correctly with the default comma separator, check the separator.

## Initial Data Quality Checks
The student should run the following checks before doing any analysis.

```python
import pandas as pd

df = pd.read_csv("student-mat.csv", sep=";")

print(df.head())
print(df.shape)
print(df.columns)
print(df.info())
print(df.isnull().sum())
print(df.duplicated().sum())
```

The student should record:

- Are any values missing?
- Are any rows duplicated?
- Are the data types correct?
- Are there unusual or impossible values?
- Are the grade ranges reasonable?
- Are all categorical values understandable?

## Potential Data Issues

### 1. Previous Grades May Dominate Prediction
`G1` and `G2` are strongly related to the final grade `G3`.

If these variables are included, a machine-learning model may appear very accurate.

However, this does not necessarily mean that the model has discovered meaningful lifestyle or behavioral patterns.

For this reason, the main project will compare:

```text
Model A:
G1 + G2 + other features → G3
```

with:

```text
Model B:
other features without G1 and G2 → G3
```

This comparison is one of the most important parts of the project.

## 2. Correlation Does Not Prove Causation
If students with more absences tend to have lower grades, the project may report an association.

It should NOT automatically claim:

```text
Absences cause lower grades.
```

Other variables may influence both attendance and academic performance.

The paper should use language such as:

- "is associated with"
- "is correlated with"
- "shows a relationship with"

unless the study design supports a causal conclusion.

## 3. Limited Population
The data comes from Portuguese secondary-school students.

Therefore, the results may not automatically apply to:

- all high school students
- U.S. students
- students from other countries
- students from different school systems

This limitation should be discussed in the final paper.

## 4. Self-Reported Variables
Some behavioral or lifestyle variables may come from student-reported information.

Self-reported data can contain:

- memory errors
- misunderstanding
- social desirability bias
- inaccurate responses

This should be considered when interpreting results.

## 5. Categorical Variables
Many features are categorical.

Machine-learning models such as Linear Regression require these variables to be converted into numerical representations.

The project may use:

```text
One-Hot Encoding
```

within a preprocessing pipeline.

## 6. Possible Feature Leakage
Students must think carefully about whether a feature contains information that would not realistically be available at the time of prediction.

For this project, `G1` and `G2` are intentionally examined because they may make prediction much easier.

The student should clearly document whether they are included or excluded in each experiment.

## Planned Feature Groups

### Model A: Previous Grades Included
Possible features:

```text
G1
G2
studytime
failures
absences
famsup
schoolsup
higher
internet
freetime
goout
health
other selected features
```

Target:

```text
G3
```

## Model B: Previous Grades Excluded
Possible features:

```text
studytime
failures
absences
famsup
schoolsup
higher
internet
freetime
goout
health
other selected non-grade features
```

Excluded:

```text
G1
G2
```

Target:

```text
G3
```

## Planned Exploratory Analysis
The dataset will be explored using:

- summary statistics
- missing-value checks
- histograms
- boxplots
- scatter plots
- bar charts
- group comparisons
- correlation analysis

Important questions include:

1. What does the distribution of final grades look like?
2. How are `G1` and `G2` related to `G3`?
3. How is study time related to `G3`?
4. How are absences related to `G3`?
5. Do students with family support show different average outcomes?
6. Do students who want higher education show different average grades?
7. Which numerical features have the strongest correlations with `G3`?

## Planned Machine-Learning Use
The dataset will be used primarily for regression.

Possible models:

```text
Baseline Mean Predictor
Linear Regression
Decision Tree Regressor
Random Forest Regressor (optional)
```

Evaluation metrics:

```text
MAE
RMSE
R²
```

The project may later include cross-validation to make model comparisons more reliable.

## Optional Classification Extension
The final grade may be converted into categories such as:

```text
Pass
Fail
```

If this extension is used, students may train classification models such as:

```text
Logistic Regression
Decision Tree Classifier
K-Nearest Neighbors
```

Possible evaluation metrics include:

```text
Accuracy
Precision
Recall
F1 Score
Confusion Matrix
```

The threshold used to define Pass / Fail must be documented clearly.

## Data Ethics and Responsible Interpretation
This dataset contains information about students.

The project should not use the results to label individual students as "good" or "bad."

Machine-learning predictions should not be treated as certain outcomes.

The project should emphasize that:

- academic success is complex
- models can be wrong
- datasets can contain bias
- associations do not prove causes
- predictions should not replace human judgment

## Dataset Citation
Students should cite the UCI Student Performance Dataset in their final report and README.

At minimum, include:

- Dataset name
- UCI Machine Learning Repository
- Dataset URL
- Date accessed

## Student Verification Checklist
Before beginning the main analysis, confirm:

- [ ] I downloaded the dataset from the UCI source
- [ ] I can load the file using Pandas
- [ ] I know the number of rows and columns
- [ ] I checked for missing values
- [ ] I checked for duplicate rows
- [ ] I reviewed the meaning of important columns
- [ ] I identified `G3` as the main target
- [ ] I understand why `G1` and `G2` require special attention
- [ ] I understand that correlation does not prove causation
- [ ] I documented the dataset source
