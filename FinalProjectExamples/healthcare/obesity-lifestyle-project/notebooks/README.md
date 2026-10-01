# Obesity-Lifestyle Classification - Notebook

## Overview

This folder contains a comprehensive Google Colab notebook for analyzing obesity classification using lifestyle factors. The notebook investigates how much information about obesity levels exists in lifestyle characteristics independently of height and weight.

## File

### `Obesity_Lifestyle_Classification.ipynb`

A complete, self-contained Jupyter notebook covering the full machine-learning pipeline:

1. **Setup & Initialization** - Import libraries, set seed, record hypotheses, define feature sets
2. **Data Loading & Validation** - Load and validate 2,111 records, handle duplicates
3. **Exploratory Data Analysis** - 5+ visualizations analyzing distributions and patterns
4. **Data Preparation** - Categorical encoding and stratified train/test split
5. **Baseline Model** - Most-frequent-class baseline for comparison
6. **Logistic Regression** - Train on all 4 feature sets with cross-validation
7. **Decision Tree** - Hyperparameter tuning on validation set
8. **Random Forest** - Hyperparameter tuning on validation set
9. **Model Evaluation** - Comprehensive comparison across models and feature sets
10. **Feature Importance** - Permutation importance and SHAP explanations
11. **Per-Class Analysis** - Performance for each of 7 obesity categories
12. **Synthetic Data Impact** - Analysis of 77% synthetic records
13. **Hypothesis Testing** - Test 4 pre-recorded hypotheses
14. **Responsible Interpretation** - Guidelines for appropriate claims and limitations
15. **Results Output** - Save visualizations, metrics tables, and summary

## Key Research Questions

**Primary**: How much information about obesity classification exists in lifestyle characteristics independently of height and weight?

**Supporting**:
1. Which lifestyle variables are most strongly associated with obesity?
2. How accurately can lifestyle-only model classify obesity?
3. How much better with height/weight included?
4. Which obesity categories are most confused?
5. Do results differ across gender groups?
6. How might synthetic records affect findings?

## Feature Sets Compared

### Feature Set A: Body Measurements Only (2 features)
- Height, Weight
- Shows how well direct measurements reproduce labels

### Feature Set B: Lifestyle Only (12 features) - MAIN RESEARCH MODEL
- family_history_with_overweight, FAVC, FCVC, NCP, CAEC, SMOKE, CH2O, SCC, FAF, TUE, CALC, MTRANS
- Tests main research question without body measurements

### Feature Set C: Lifestyle + Demographics (14 features)
- All Set B features plus Age and Gender
- Measures if demographic information adds value

### Feature Set D: All Available Predictors (16 features)
- All 16 available features including body measurements
- Upper comparison bound using complete data

## Models Evaluated

1. **Baseline** - Most-frequent-class predictor (reference)
2. **Logistic Regression** - Multinomial classifier (3 variants - one per feature set)
3. **Decision Tree** - With hyperparameter tuning on validation set (3 variants)
4. **Random Forest** - Ensemble with hyperparameter tuning (3 variants)
- Total: 13 model configurations

## Hypotheses (Recorded Before Analysis)

- **H1**: Height/weight model will classify more accurately than lifestyle-only
- **H2**: Lifestyle variables contain useful predictive information
- **H3**: Physical activity, food consumption, transportation, family history are informative
- **H4**: Models confuse neighboring obesity categories more than distant ones

## Dataset

- **Source**: UCI Machine Learning Repository
- **Name**: Estimation of Obesity Levels Based on Eating Habits and Physical Condition
- **Records**: 2,111 (2,087 after removing duplicates)
- **Classes**: 7 obesity levels
- **Synthetic**: 77% of records (23% real)
- **Geographic**: Mexico, Peru, Colombia
- **Time**: 1 year of collection

## Data Quality

✅ No missing values  
✅ All expected columns present  
✅ 24 exact duplicate rows removed  
✅ 7 obesity categories well-distributed  
✅ Decimal values indicate synthetic generation  

## Evaluation Metrics

- **Macro F1** (primary) - Equal weight to all categories
- **Balanced Accuracy** - Adjusted for class imbalance
- **Overall Accuracy** - For context
- **Per-Class Precision/Recall** - Category-specific performance
- **Confusion Matrix** - Error patterns and category confusion

## How to Use

### Google Colab

1. Upload notebook to Colab
2. Mount Google Drive or upload data files
3. Update DATA_PATH to point to CSV location:
   ```python
   DATA_PATH = Path('data/ObesityDataSet_raw_and_data_sinthetic.csv')
   ```
4. Run all cells sequentially from top to bottom
5. Results are saved to `results/` folder

### Local Jupyter

```bash
# Install dependencies
pip install pandas numpy scikit-learn matplotlib seaborn shap

# Start Jupyter
jupyter notebook

# Open Obesity_Lifestyle_Classification.ipynb
```

## Dependencies

```
pandas >= 1.3.0
numpy >= 1.21.0
scikit-learn >= 1.0.0
matplotlib >= 3.4.0
seaborn >= 0.11.0
shap >= 0.11.0
```

## Output Files

The notebook generates results in the `results/` folder:

### Visualizations (PNG, 300 DPI)
- `01_target_distribution.png` - Obesity category counts
- `02_demographics.png` - Age, gender, height, weight distributions
- `03_lifestyle_by_obesity.png` - Lifestyle variables by obesity category
- `04_feature_correlations.png` - Numeric variable correlations
- `05_model_comparison.png` - Algorithm and feature set comparison
- `06_confusion_matrix.png` - Model confusion patterns
- `08_permutation_importance.png` - Feature importance
- `09_shap_summary.png` - SHAP feature importance

### Data Files
- `model_results.csv` - All 13 model metrics (Macro F1, Accuracy, Balanced Accuracy)
- `feature_importance.csv` - Feature importance ranking
- `per_class_metrics.csv` - Precision/Recall for each obesity category
- `analysis_summary.txt` - Research-style summary report

## Execution Time

- **Typical runtime**: 15-25 minutes on standard hardware
- **Memory requirement**: ~1 GB
- **CPU**: Benefits from multi-core systems (uses n_jobs=-1)

## Key Features

✅ **Educational**: Detailed comments explaining each step  
✅ **Reproducible**: Fixed random seed (42), documented methodology  
✅ **Rigorous**: Stratified 5-fold cross-validation, no data leakage  
✅ **Comprehensive**: 4 feature sets, 3 algorithms, 13 model configurations  
✅ **Explainable**: Permutation importance and SHAP analysis  
✅ **Responsible**: Responsible interpretation section with guidelines  
✅ **Multiclass**: 7-category classification (not binary)  
✅ **Publication-ready**: High-quality visualizations and metrics  

## Important Notes

### Correlation vs Causation

This notebook analyzes **associations** between variables and obesity labels:
- "Physical activity was associated with obesity categories" ✓
- "Physical activity prevents obesity" ✗ (different claim)

### Generalization

Results apply to:
- This specific UCI dataset ✓
- Mexico, Peru, Colombia population ✓
- Individuals similar to survey participants ✓

Results may NOT apply to:
- U.S. teenagers ✗
- Different countries ✗
- Future time periods ✗
- All people globally ✗

### Synthetic Data

- 77% of records are synthetically generated
- Patterns may be artificially clear
- Model performance may be overly optimistic
- Validation on real-world data needed

### Medical Context

- This is a dataset prediction task (not diagnosis)
- Should never replace professional medical advice
- Cannot estimate individual health risk
- Not suitable for medical decision-making

## Responsible Interpretation Examples

### ✓ APPROPRIATE (use these)
- "The lifestyle-only model predicted dataset labels with X accuracy"
- "Physical activity was associated with obesity categories"
- "Model performance may differ on real-world data"
- "Results apply to this dataset from Mexico, Peru, Colombia"

### ✗ AVOID (do not use these)
- "The model diagnoses obesity"
- "Low physical activity causes obesity"
- "Model will work on all teenagers"
- "Use for medical decisions or health assessment"

## Troubleshooting

### FileNotFoundError
- Check data path is correct
- Verify file exists at: `data/ObesityDataSet_raw_and_data_sinthetic.csv`

### Memory Issues
- Use Colab (more memory available)
- Close other applications
- Reduce dataset size if needed

### Encoding Issues
- Try: `pd.read_csv(..., encoding='latin1')`

## Research Workflow

1. **Record hypotheses** before examining data
2. **Explore data** with visualizations
3. **Prepare data** properly (no leakage)
4. **Train models** with cross-validation
5. **Evaluate** on held-out test set
6. **Analyze errors** to understand failures
7. **Test hypotheses** using results
8. **Report findings** honestly (including limitations)

## Data Citation

**UCI Obesity Dataset:**
Palechor, F. M., & de la Hoz Manotas, A. (2019). Estimation of Obesity Levels Based On Eating Habits and Physical Condition [Dataset]. UCI Machine Learning Repository. https://doi.org/10.24432/C5H31Z

Original article:
Mendoza Palechor, F., & De la Hoz Manotas, A. (2019). Dataset for estimation of obesity levels based on eating habits and physical condition in individuals from Colombia, Peru and Mexico. *Data in Brief, 25*, 104344. https://doi.org/10.1016/j.dib.2019.104344

## Next Steps

1. Run the notebook on your data
2. Review all visualizations and metrics
3. Examine per-class performance
4. Check feature importance rankings
5. Read responsible interpretation section carefully
6. Use findings to write research paper
7. Consider extensions:
   - Gender subgroup analysis
   - Binary classification (obesity vs not)
   - Additional validation on real data

## License & Usage

This notebook is provided for educational purposes. The UCI dataset is available under Creative Commons Attribution 4.0 International (CC BY 4.0) license.

---

**Notebook Status**: ✅ Production-ready  
**Last Updated**: October 1, 2026  
**Compatibility**: Google Colab ✓ | Local Jupyter ✓ | Python 3.7+ ✓
