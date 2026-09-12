# Project Idea

## Project Title

**Patterns and Selection Effects in Exoplanet Discovery: A Data-Driven Analysis of NASA's Exoplanet Archive**

## Project Overview

This project investigates how exoplanet discoveries have changed over time and how the observed properties of planets differ among Transit, Radial Velocity, Imaging, and Microlensing discoveries. I will analyze planet and host-star measurements from NASA's Exoplanet Archive and test whether a machine-learning model can predict the credited discovery method from those measurements. This topic matters because telescopes and discovery techniques do not observe every kind of planet equally, so the archive may reflect scientific selection effects rather than the true population of planets in the galaxy. The project will use a dated table of confirmed exoplanets containing physical, orbital, stellar, distance, and discovery information.

## Domain

Astronomy, data science, and machine learning

## Primary Research Question

**How do observed exoplanet properties differ across discovery methods, and how accurately can a model classify discovery method from planet and host-system measurements?**

## Supporting Questions

1. How have the number and mix of exoplanet discoveries changed over time?
2. How do orbital period, planet radius, planet mass, equilibrium temperature, and system distance differ among discovery methods?
3. How much predictive information comes from planet properties compared with host-star and system properties?
4. Can missing-measurement patterns predict discovery method?
5. Which discovery methods are most frequently confused by the models, and why?

## Why This Project Matters

Scientists do not observe a random sample of all planets in the galaxy. Each discovery method is sensitive to particular types of planets, orbits, stars, and distances. A successful classifier may therefore reveal patterns created by telescope sensitivity, survey design, follow-up measurements, and data reporting. Understanding these effects helps students distinguish between the **observed dataset** and the **underlying population** scientists want to understand.

## Dataset

- **Name:** NASA Exoplanet Archive Planetary Systems Composite Parameters table (`pscomppars`)
- **Source:** https://exoplanetarchive.ipac.caltech.edu/
- **Snapshot date:** September 12, 2026 (UTC)
- **Snapshot size:** 6,366 rows and 16 selected columns
- **File:** `data/exoplanets_pscomppars_2026-09-12.csv`
- **Target variable:** `discoverymethod`
- **Recommended target classes:** Transit, Radial Velocity, Imaging, and Microlensing

## Hypotheses

- **H1:** The distribution of discovery methods changes substantially across discovery years.
- **H2:** Transit discoveries tend to have different orbital-period and radius distributions from Radial Velocity discoveries.
- **H3:** Imaging discoveries tend to occur at different system distances and planet-property ranges from Transit discoveries.
- **H4:** A model using combined planet and system features achieves a higher validation macro F1 score than models using either feature group alone.
- **H5:** Missing-measurement indicators alone predict discovery method better than a most-frequent-class baseline, indicating method-related measurement and reporting patterns.

These are testable predictions, not conclusions. They must be evaluated with the data.

## Planned Analysis

### Phase 1: Understand and Prepare the Data

- Verify the dataset shape, column names, units, and unique planet names.
- Filter the four target discovery methods.
- Identify missing values and limit-flagged measurements.
- Preserve the raw file and perform cleaning in a separate prepared dataset or notebook.
- Create base-10 logarithms for positive measurements with very wide ranges, such as orbital period, planet radius, planet mass, equilibrium temperature, and distance.

### Phase 2: Exploratory Data Analysis

Create and interpret:

- discoveries by year and discovery method;
- class counts and percentages;
- log-scale boxplots of major physical properties by discovery method;
- a radius-versus-period scatterplot colored by discovery method;
- a missingness heatmap or method-by-feature missingness table;
- the number of planets per host system.

Every figure will include a descriptive title, labeled axes, units, a readable legend, and a short interpretation.

### Phase 3: Controlled Machine-Learning Experiment

Compare the following feature sets:

| Feature set | Variables | Scientific purpose |
|---|---|---|
| A: Planet properties | Log orbital period, log radius, log mass, log equilibrium temperature | Test the predictive value of planet measurements |
| B: System context | Host-star temperature, host-star radius, log system distance | Test the predictive value of the host system |
| C: Combined | All variables from A and B | Test whether the two groups add useful information |
| D: Missingness audit | Indicators showing whether each measurement is present | Detect measurement and reporting patterns |

Compare these models:

1. Most-frequent-class baseline
2. K-Nearest Neighbors classifier
3. Decision Tree classifier
4. Random Forest classifier, optional extension

### Phase 4: Evaluation and Interpretation

- Use host-system-grouped training, validation, and test partitions so planets from the same `hostname` do not appear in different partitions.
- Select models with the validation data only.
- Use the test data once after the final configuration is fixed.
- Use **macro F1** as the primary metric.
- Also report balanced accuracy, raw accuracy, per-class precision and recall, and a confusion matrix.
- Analyze errors by discovery method and discuss how class imbalance and missing data affect the result.

## Variables That Must Not Be Used as Main Predictors

- `pl_name` and `hostname`: identifiers that may allow memorization or leakage
- `discoverymethod`: the target itself
- `disc_year`: a historical clue closely tied to when methods became common
- `disc_facility`: closely connected to particular discovery techniques
- measurement-limit flags: quality-control fields that may encode reporting practices

These fields may still be used for grouping, exploratory analysis, quality control, and the separate missingness audit.

## Success Criteria

The project will be considered successful if it:

- produces a reproducible, documented data snapshot;
- completes the required exploratory analyses and explains each result;
- prevents host-system leakage between dataset partitions;
- compares at least the baseline, KNN, and Decision Tree across feature sets A–C;
- reports macro F1, balanced accuracy, per-class results, and a confusion matrix;
- completes the missingness-only audit;
- explains selection effects without claiming that the observed archive represents all planets in the galaxy;
- produces a research paper, reproducible GitHub repository, and presentation.

A high model score is not required for project success. A careful analysis of weak or uneven performance is also a valid scientific result.

## Expected Deliverables

- `PROJECT_IDEA.md`
- `DATA_DOCUMENTATION.md`
- dated raw CSV and the exact `query.adql`
- data-preparation, EDA, modeling, and error-analysis notebooks
- saved figures and model-results tables
- project `README.md` with reproduction instructions
- final research paper
- five-to-seven-minute presentation

## Main Limitations

- The archive is dynamic, and later snapshots may contain different rows or values.
- Composite measurements can come from different published references and may not be perfectly self-consistent.
- Measurements are missing unevenly across discovery methods.
- The four classes are highly imbalanced, especially Transit versus Imaging.
- Discovery method reflects credited discovery history, not a fundamental physical category of planet.
- Observed relationships do not establish causation or describe the complete population of planets in the galaxy.

## Responsible Use Statement

This project studies patterns in a historical scientific archive. Model predictions will not be presented as new planet discoveries or as replacements for astronomical observation and expert review. All conclusions will be limited to the selected NASA archive snapshot and the methods used in this analysis.

