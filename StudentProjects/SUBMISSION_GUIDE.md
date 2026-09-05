# Data Science Project Submission Guide

## Overview

This guide explains how to complete and submit your data science project. Follow each step carefully and submit your work to GitHub as specified.

---

## Project Phases (In Order)

### Phase 1: Define Your Project Idea
**What to do:**
- Choose a **real-world problem or question** you are curious about
- Write a short description (3–5 sentences) explaining:
  - The problem/question you want to solve
  - Why this topic is interesting or important
  - What type of data you think you will need

**Deliverable:** `PROJECT_IDEA.md` — A text file with your problem description

**How instructor checks:** 
- Reads your problem statement
- Verifies it is specific and feasible (not too broad)
- Confirms data availability is realistic

---

### Phase 2: Collect Your Data
**What to do:**
- Find or build a dataset using one of these methods:
  1. Search online (Kaggle, UCI, government portals, etc.)
  2. Download public data (CSV, JSON, Excel)
  3. Collect your own data (surveys, scraping, observations)

**Requirements:**
- Minimum **200 rows** (records) and **5 features** (columns)
- Data must be **relevant** to your project idea
- Avoid overused datasets (Titanic) unless you add your own twist
- If self-collected, document your methodology

**Deliverable:** `data.csv` (or `.xlsx`, `.json`) — Your raw dataset file

**How instructor checks:**
- Opens the file and counts rows/columns
- Verifies data relevance to your stated problem
- Checks data quality and completeness

---

### Phase 3: Document Your Dataset
**What to do:**
Write a **data documentation report** (1–2 pages) that explains:

1. **Source** – Where you obtained the data
2. **Size** – Number of rows and columns
3. **Features** – List each column with a short description
4. **Potential Issues** – Any missing values, errors, biases, or data quality concerns

**Example format:**
```
# Dataset Documentation

**Name:** Student Study Habits Dataset

**Source:** Self-collected via Google Form (link: ...)

**Size:** 245 rows × 8 columns

**Features:**
- student_id (numeric): Unique student identifier
- study_hours (numeric): Weekly study hours (0-50)
- gpa (numeric): Grade point average (0-4.0)
- major (categorical): Field of study
- ...

**Potential Issues:**
- 3 missing values in `gpa` column (0.1%)
- Potential self-reporting bias in `study_hours`
```

**Deliverable:** `DATA_DOCUMENTATION.md` — Your dataset explanation

**How instructor checks:**
- Reads source information (verifiable and legitimate)
- Confirms feature descriptions match actual data
- Assesses data quality and identifies potential issues

---

## GitHub Submission Instructions

### Repository Structure
Your GitHub repository should contain **exactly these files** in the root directory:

```
your-project-repo/
├── PROJECT_IDEA.md           (Phase 1)
├── DATA_DOCUMENTATION.md     (Phase 3)
└── data.csv                  (Phase 2)
```

### Step-by-Step Submission

1. **Create a GitHub repository** (if you don't have one):
   - Go to github.com/new
   - Name it something descriptive (e.g., `student-project-housing-prices`)
   - Initialize with a README

2. **Upload Phase 1 – Project Idea:**
   - Create a new file called `PROJECT_IDEA.md`
   - Paste your 3–5 sentence problem description
   - Commit with message: `phase-1: add project idea`

3. **Upload Phase 2 – Dataset:**
   - Upload your `data.csv` (or `.json` or `.xlsx`)
   - Commit with message: `phase-2: add dataset`
   - **IMPORTANT:** If your file is > 100 MB, use GitHub Large File Storage (LFS) or split the data

4. **Upload Phase 3 – Documentation:**
   - Create a file called `DATA_DOCUMENTATION.md`
   - Paste your dataset documentation
   - Commit with message: `phase-3: add data documentation`

5. **Verify your submission:**
   - Navigate to your GitHub repository
   - Confirm all 3 files are visible in the root directory
   - Check that file contents are readable (not corrupted)

### Example GitHub Commit Messages
```
phase-1: add project idea
phase-2: add dataset (245 rows, 8 features)
phase-3: add data documentation
```

---

## Verification Checklist for Students

Before submitting, verify:

- [ ] **PROJECT_IDEA.md** exists in root directory
  - [ ] Contains 3–5 sentences
  - [ ] Problem/question is clear and specific
  - [ ] Explains why the topic matters
  - [ ] Describes expected data type
  
- [ ] **data.csv** exists in root directory
  - [ ] Has at least 200 rows
  - [ ] Has at least 5 columns/features
  - [ ] File opens without errors
  - [ ] Data is relevant to your project idea
  
- [ ] **DATA_DOCUMENTATION.md** exists in root directory
  - [ ] Includes "Source" section
  - [ ] Includes "Size" section (row and column count)
  - [ ] Includes "Features" section (all columns listed with descriptions)
  - [ ] Includes "Potential Issues" section

- [ ] GitHub repository is **public** (so instructor can access it)
- [ ] All files are readable (not corrupted)

---

## Instructor Verification Checklist

Instructors will verify submissions by checking:

| Phase | File | Criteria | Pass/Fail |
|-------|------|----------|-----------|
| 1 | PROJECT_IDEA.md | File exists, problem is specific/feasible | ✓/✗ |
| 2 | data.csv | File exists, ≥200 rows, ≥5 columns | ✓/✗ |
| 2 | data.csv | Data is relevant and clean | ✓/✗ |
| 3 | DATA_DOCUMENTATION.md | File exists, includes Source/Size/Features/Issues | ✓/✗ |
| 3 | DATA_DOCUMENTATION.md | Documentation is accurate and complete | ✓/✗ |
| All | GitHub | Repository is public and all files are accessible | ✓/✗ |

---

## Common Submission Errors to Avoid

❌ **Files in wrong location** → Put them in the root directory, not in a subfolder  
❌ **Missing documentation** → All 3 files must be present  
❌ **Incomplete dataset** → Fewer than 200 rows or 5 columns  
❌ **Private repository** → Make your repo public so instructor can view it  
❌ **Corrupted files** → Test that CSV/JSON opens before submitting  
❌ **Dataset is overused** → Titanic, Iris, etc. require a unique twist  
❌ **Vague project idea** → "Analyze data" is not specific enough  
