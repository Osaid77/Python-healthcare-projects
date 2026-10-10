# Emergency Department EHR Data Processing & Analytics with Pandas

## Overview

This project shows proficiency in Python and Pandas through the exploration, cleaning, transformation, integration, and analysis of real, deidentified EHR data.

Using the MIMIC-IV and MIMIC-IV-ED demonstration datasets, the project processes emergency department encounters, clinical vital signs, diagnoses, patient demographics, and hospital admission records.

The primary objective is to demonstrate comprehensive Pandas data manipulation and analytical skills, rather than train predictive models or develop a clinical decision-support system.

## Dataset

**Sources:**

- [MIMIC-IV Clinical Database Demo v2.2](https://physionet.org/content/mimic-iv-demo/2.2/)
- [MIMIC-IV-ED Demo v2.2](https://physionet.org/content/mimic-iv-ed-demo/2.2/)

**Tables used:**

| Table | Purpose |
|---|---|
| edstays | Emergency department encounters |
| triage | Initial clinical assessments |
| vitalsign | Repeated vital-sign observations |
| diagnosis | ED diagnoses |
| patients | Patient demographics |
| admissions | Hospital admissions and outcomes |
| icustays | ICU encounters |

## Technologies

- Python
- Pandas
- NumPy

## Project Implementation

### 1. Data Exploration and Validation

- Loaded and inspected seven relational EHR datasets.
- Examined dataset dimensions, data types, missing values, duplicates, and statistics.
- Identified primary and composite keys.
- Investigated duplicate records and relationships between tables.

### 2. Data Cleaning

- investigated missing and out-of-range invalid measurements.
- Applied vital sign validation rules.
- Standardized categorical values and clinical text fields.
- Preserved original data while working with cleaned copies.

### 3. Datetime Processing

- Converted clinical timestamps into datetime representations.
- Calculated ED and hospital lengths of stays.
- Examined time-based admission characteristics.

### 4. Clinical Feature Engineering

- Created exploratory Boolean indicators for abnormal vital signs.
- Applied vectorized conditional logic.
- Generated descriptive clinical features for analytical use.

### 5. Statistical and Grouped Analysis

- Calculated statistics for clinical measurements.
- Compared measurements across patient and encounter categories.
- Used single and multiple column grouping.
- Applied multiple aggregation functions to clinical variables.

### 6. Relational Data Integration

- Combined ED, patient, triage, hospital admission, and clinical measurement information.
- Examined one-to-one, one-to-many, and many-to-many relationships.
- Aggregated repeated vital sign measurements by ED stay.
- Built an analytical dataset with one record per ED encounter.
- Checked row counts, uniqueness, and duplicate identifiers after merging.

### 7. Final Data Organization

- Renamed columns for clarity.
- Removed redundant fields.
- Sorted records chronologically.
- Reset the DataFrame index.
- Exported the final analytical dataset to CSV.

## Output

The primary output is:

`ed_stay_analytic_dataset.csv`

This dataset contains cleaned and organized encounter-level information, including patient demographics, triage assessments, aggregated ED vital signs, and linked hospital information.

## Running the Project

2. Download the two mimic demonstration datasets from PhysioNet.
3. Extract the datasets and place the required `ed/`, `hosp/`, and `icu/` tables in the input data directory expected by the script.
4. Run `clinical_analytics.py`.
5. Review the resulting analytical CSV and console summaries.

## Limitations

- The demonstration cohort is small and not representative of a broader hospital population.
- Clinical flags are exploratory and should not be used for medical decisions.
- Missing measurements do not necessarily indicate normal findings.
- The project is intended to demonstrate Pandas proficiency.

## Data Attribution

The datasets were provided through PhysioNet.

- Johnson et al. (2023). *MIMIC-IV Clinical Database Demo*, version 2.2. https://doi.org/10.13026/dp1f-ex47
- *MIMIC-IV-ED Demo*, version 2.2. https://doi.org/10.13026/jzz5-vs76

Dataset use and redistribution are subject to the applicable PhysioNet license terms.
