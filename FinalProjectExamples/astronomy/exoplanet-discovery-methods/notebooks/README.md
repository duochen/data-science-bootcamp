# Exoplanet Discovery Methods Analysis - Notebooks

## Overview

This folder contains a comprehensive Jupyter notebook for analyzing exoplanet discovery methods using NASA's Exoplanet Archive data.

## Files

### `Exoplanet_Discovery_Methods_Analysis.ipynb`

A complete, self-contained notebook that covers all phases of the exoplanet discovery analysis:

1. **Setup & Initialization** - Import libraries and configure environment
2. **Utility Functions** - Helper functions for data processing and modeling
3. **Phase 1: Data Understanding & Preparation**
   - Load and validate raw data (6,366 planets)
   - Filter to 4 target discovery methods
   - Handle missing values and measurement flags
   - Create log-transformed features
   - Create missingness indicators
   - Perform group-aware train/val/test split

4. **Phase 2: Exploratory Data Analysis (EDA)**
   - Discovery trends over time
   - Class distribution analysis
   - Physical properties by discovery method
   - Radius vs. orbital period visualization
   - Missingness patterns

5. **Phase 3: Machine Learning**
   - Define 4 feature sets (A, B, C, D)
   - Train 4 models:
     - Most-Frequent-Class Baseline
     - K-Nearest Neighbors (KNN)
     - Decision Tree
     - Random Forest
   - Evaluate on test set with proper protocol

6. **Phase 4: Evaluation & Interpretation**
   - Model comparison across feature sets
   - Confusion matrices
   - Per-class performance metrics
   - Feature importance analysis
   - Scientific interpretation of results

## How to Use

### Option 1: Google Colab (Recommended)

1. Upload the notebook to Google Colab
2. Upload the data files or mount Google Drive
3. Update the `DATA_PATH` variable to match your file location
4. Run cells sequentially from top to bottom

### Option 2: Local Jupyter

1. Install dependencies: `pip install pandas numpy scikit-learn matplotlib seaborn scipy`
2. Start Jupyter: `jupyter notebook`
3. Open `Exoplanet_Discovery_Methods_Analysis.ipynb`
4. Update `DATA_PATH` to point to your data folder
5. Run all cells

## Data Requirements

The notebook expects the following file structure:

```
data/
  exoplanet_dataset/
    data/
      exoplanets_pscomppars_2026-09-12.csv
```

The CSV file should contain 16 columns with exoplanet measurements from NASA's archive.

## Output

The notebook generates results in the `results/` folder:

- **PNG visualizations**: EDA plots and model performance charts
- **CSV tables**: Model comparison metrics
- **Text summaries**: Analysis documentation

## Key Features

✅ **Educational**: Detailed comments explaining each step  
✅ **Reproducible**: Fixed random seeds and proper data splitting  
✅ **Comprehensive**: All phases from data prep to interpretation  
✅ **Publication-ready**: High-quality visualizations  
✅ **Responsible**: Includes caveats about selection effects and limitations  

## Requirements

- Python 3.7+
- pandas >= 1.3.0
- numpy >= 1.21.0
- scikit-learn >= 1.0.0
- matplotlib >= 3.4.0
- seaborn >= 0.11.0
- scipy >= 1.7.0

Optional:
- shap >= 0.40.0 (for SHAP feature importance analysis)

## Running Time

Expect approximately 5-10 minutes to run the full notebook, depending on your hardware.

## Notes

- The notebook uses hostname-based splitting to prevent leakage from multi-planet systems
- Models are evaluated using **Macro F1** as the primary metric to handle class imbalance
- All preprocessing (imputation, scaling) is fit on training data only
- Results are specific to the September 12, 2026 NASA Exoplanet Archive snapshot

## Responsible Use

This analysis studies patterns in a historical scientific archive. Model predictions are NOT new discoveries. All conclusions are limited to the selected NASA snapshot and the analysis methods used. Results reflect selection effects and observational biases, not the true population of exoplanets in the galaxy.

## Citation

NASA Exoplanet Archive. (2026). Planetary Systems Composite Parameters. Retrieved from https://exoplanetarchive.ipac.caltech.edu/

Snapshot date: September 12, 2026
