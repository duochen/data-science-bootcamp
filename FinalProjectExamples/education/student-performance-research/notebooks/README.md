# Student Academic Performance Analysis - Notebook

## Overview

This folder contains a comprehensive Jupyter notebook for analyzing student academic performance using the UCI Student Performance Dataset.

## Files

### `Student_Academic_Performance_Analysis.ipynb`

A complete, self-contained notebook that covers all phases of student performance analysis:

1. **Setup & Initialization** - Import libraries and configure environment
2. **Data Loading & Exploration** - Load and validate both datasets (Math and Portuguese)
3. **Exploratory Data Analysis (EDA)**
   - Distribution of final grades
   - Relationships between grades (G1, G2 vs G3)
   - Study time impact on grades
   - Absences impact on grades
   - Correlation heatmap analysis
   - Categorical variable analysis (family support, internet access, etc.)
   - Exploratory statistics with group comparisons

4. **Data Preparation**
   - One-hot encoding of categorical variables
   - Feature selection (Model A with G1/G2, Model B without)
   - Feature scaling (StandardScaler)
   - Train/Validation/Test split (60/20/20)

5. **Machine Learning Experiments**
   - Baseline model (mean predictor)
   - Linear Regression (Model A & B)
   - Decision Tree Regressor (hyperparameter tuning)
   - Random Forest Regressor (hyperparameter tuning)
   - Cross-validation analysis (5-fold)

6. **Evaluation & Comparison**
   - Comprehensive metrics table (MAE, RMSE, R²)
   - Model A vs Model B performance comparison
   - Actual vs Predicted visualizations
   - Feature importance analysis for both models
   - Side-by-side performance metrics

7. **Scientific Interpretation**
   - Answer primary research question
   - Answer secondary research question
   - Hypothesis testing results
   - Key findings summary
   - Limitations and caveats
   - Recommendations for students and educators

8. **Results Output**
   - Save all visualizations
   - Generate results table (CSV)
   - Create summary report

## Key Research Questions

**Primary**: How accurately can student academic performance be predicted without using previous grades?

**Secondary**: Which academic, behavioral, and social factors are most strongly associated with students' final academic performance?

## Datasets

The notebook analyzes **both** datasets:
- **Mathematics** (`student-mat.csv`) - ~395 students, 32 variables
- **Portuguese** (`student-por.csv`) - ~649 students, 32 variables

Students are analyzed separately to compare patterns between subjects.

## Models Compared

### Model A: With Previous Grades (G1, G2)
Uses first and second period grades along with other features to predict final grade (G3).

**Expected outcome**: Very high accuracy (these are strong predictors)

### Model B: Without Previous Grades
Uses only behavioral, social, and family factors to predict final grade (G3).

**Expected outcome**: Lower accuracy, but reveals what other factors matter

### Algorithms
- **Baseline**: Mean predictor (reference point)
- **Linear Regression**: Interpretable, shows feature relationships
- **Decision Tree**: Nonlinear patterns, feature importance visible
- **Random Forest**: Ensemble approach, better generalization

## Evaluation Metrics

- **MAE** (Mean Absolute Error): Error in grade units (0-20 scale)
- **RMSE** (Root Mean Squared Error): Penalizes larger errors
- **R²** (Coefficient of Determination): Variance explained (0-1 scale)
- **Cross-Validation**: 5-fold CV for robustness

## How to Use

### Google Colab

1. Upload the notebook to Google Colab
2. Upload or mount the data folder containing:
   - `data/student-mat.csv`
   - `data/student-por.csv`
3. Update the `DATA_PATH_MATH` and `DATA_PATH_PORTUGUESE` variables
4. Run all cells sequentially from top to bottom

### Local Jupyter

```bash
# Install dependencies
pip install pandas numpy scikit-learn matplotlib seaborn scipy

# Start Jupyter
jupyter notebook

# Open Student_Academic_Performance_Analysis.ipynb
```

## Key Features

✅ **Comprehensive Analysis**: 4 major phases (EDA, prep, modeling, evaluation)

✅ **Educational**: Detailed comments explaining the WHY behind each step

✅ **Two Datasets**: Both Math and Portuguese analyzed separately

✅ **Model Comparison**: Model A vs Model B reveals impact of removing previous grades

✅ **Multiple Algorithms**: Linear Regression, Decision Tree, Random Forest

✅ **Cross-Validation**: More robust performance estimates

✅ **Feature Importance**: See which non-grade factors matter most

✅ **Publication-Ready**: High-quality visualizations and results tables

✅ **Reproducible**: Fixed random seed and documented methodology

## Dependencies

```
pandas >= 1.3.0
numpy >= 1.21.0
scikit-learn >= 1.0.0
matplotlib >= 3.4.0
seaborn >= 0.11.0
scipy >= 1.7.0
```

## Output Files

The notebook generates results in the `results/` folder:

- `01_grade_distributions.png` - Final grade distributions
- `02_grades_relationships.png` - G1/G2 vs G3 relationships
- `03_study_time_vs_grades.png` - Study time impact
- `04_absences_vs_grades.png` - Absences impact
- `05_correlation_heatmaps.png` - Correlation matrices
- `06_categorical_analysis.png` - Categorical variable effects
- `07_model_a_vs_b_comparison_math.png` - Performance comparison
- `08_actual_vs_predicted.png` - Model predictions visualization
- `09_feature_importance.png` - Top predictive features
- `model_comparison_results.csv` - All metrics table
- `analysis_summary.txt` - Executive summary

## Execution Time

- **Expected duration**: 5-15 minutes on standard hardware
- **Memory requirement**: ~500 MB
- **CPU**: Parallelized for multi-core systems

## Important Notes

### Correlations vs Causation
The notebook finds **associations** between variables and academic performance. We can say "students with more absences tend to have lower grades" but NOT "absences cause low grades" — other factors might influence both.

### Generalization
These students are from Portuguese secondary schools. Results may not apply to:
- Other countries or school systems
- Different age groups
- Different socioeconomic contexts

### Data Quality
Some variables are self-reported (study time, free time, etc.). Be aware of:
- Memory errors
- Social desirability bias
- Misunderstanding of questions

## Hypothesis Testing

The notebook tests three hypotheses:

1. **H1**: Students with more study time have higher final grades
   - **Status**: SUPPORTED (positive correlation in both datasets)

2. **H2**: Students with more absences have lower final grades
   - **Status**: SUPPORTED (negative correlation in both datasets)

3. **H3**: Previous grades are more predictive than behavioral/social factors
   - **Status**: STRONGLY SUPPORTED (Model A vastly outperforms Model B)

## Key Findings

- **Previous grades dominate**: Model A R² ~ 0.8-0.9, Model B R² ~ 0.3-0.5
- **Top non-grade factors**: Past failures, study time, family support, school support
- **Study habits matter**: Positive correlation with grades
- **Attendance matters**: Negative correlation with absences
- **Support systems help**: Family and school support associated with higher grades

## Data Citation

**UCI Student Performance Dataset**
- Source: https://archive.ics.uci.edu/dataset/320/student%2Bperformance
- Subjects: Mathematics and Portuguese Language
- Accessed: [Your access date]

Reference these files in academic work using the UCI citation format.

## Next Steps

1. Review the visualizations to understand the data
2. Run the notebook on Colab or locally
3. Examine the results table and summary
4. Use findings to inform a research paper
5. Consider extensions:
   - Classification (Pass/Fail instead of regression)
   - Comparison across datasets
   - Causal analysis with observational data
   - Demographic subgroup analysis

## Troubleshooting

### FileNotFoundError
- Check that data files are in the correct location
- Verify separator is semicolon (`;`) not comma
- Example: `pd.read_csv("student-mat.csv", sep=";")`

### Memory Issues
- Reduce dataset size or use only one subject
- Close other applications
- Use cloud platform (Colab) instead of local machine

### Encoding Issues
- Ensure UTF-8 encoding when loading files
- On Windows, you might need: `encoding='latin1'` or `encoding='utf-8'`

## License & Usage

This notebook is provided for educational purposes as part of a data science bootcamp. Use it to learn data analysis, machine learning, and research methodology.

For publication or commercial use, cite the UCI Student Performance Dataset appropriately.
