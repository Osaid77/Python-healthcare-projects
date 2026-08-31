# Longitudinal Clinical Vital-Signs Risk Screening Pipeline

A Python healthcare data-processing project that screens repeated hospital vital-sign observations, validates physiologic measurements, calculates configurable rule-based risk scores, and exports structured CSV and JSON results.

## Project Overview

This project processes a public longitudinal hospital vital-sign dataset containing repeated observations across multiple hospital admissions.

The pipeline:

- reads structured patient observations from CSV
- validates physiologic measurements against configurable ranges
- applies rule-based clinical risk flags
- calculates a risk score for each valid observation
- classifies observations as Low, Moderate, or High risk
- tracks admissions that contain at least one high-risk observation
- exports row-level screening results to CSV
- generates an aggregate JSON summary
- Handles all types of errors such as FileNotFound, KeyError, ValueError, and jsonDecodeError

This is an educational healthcare screening prototype and is not intended to represent a validated clinical deterioration score or medical device.

## Dataset

This project uses the **Patient Vital Signs and Event Tracking** dataset available on Kaggle:

[Patient Vital Signs and Event Tracking — Kaggle](https://www.kaggle.com/datasets/parmajha/patient-vital-signs-and-event-tracking)
Key variables used:

- `hadm_id` — hospital admission identifier
- `HR` — heart rate
- `RR` — respiratory rate
- `SBP` — systolic blood pressure
- `TEMP` — temperature
- `SPO2` — oxygen saturation
- `age` — patient age
- `sex` — patient sex
- `charttime` — observation timestamp

The dataset contains repeated observations for the same hospital admission, allowing the pipeline to evaluate vital-sign changes over time.

The full dataset is not redistributed in this repository.  
To reproduce the project:

1. Download the dataset from Kaggle.
2. Place the CSV file in the project directory.
3. Rename it to:

```text
patients_data.csv
```

## Features

- CSV ingestion using `csv.DictReader`
- CSV result export using `csv.DictWriter`
- JSON configuration loading
- JSON summary generation
- physiologic range validation
- configurable clinical thresholds
- repeated-observation screening
- rule-based risk scoring
- Low / Moderate / High risk classification
- invalid-data detection
- unique high-risk admission tracking using Python sets
- aggregate observation statistics
- modular function-based design

## Clinical Rules

The prototype uses configurable thresholds stored in `risk_config.json`.

Example screening flags include:

- fever
- low oxygen saturation
- high heart rate
- high respiratory rate
- low systolic blood pressure
- older age

Each positive flag contributes one point to the rule-based risk score.

Risk classification:

- `0–1` → Low risk
- `2–3` → Moderate risk
- `4+` → High risk

These thresholds are used for educational demonstration only and are not presented as a validated clinical scoring system.

## Data Validation

Before risk scoring, the program checks whether vital signs fall within predefined plausible physiologic ranges.

Observations with invalid measurements are:

- marked as invalid
- excluded from clinical risk classification
- still preserved in the output dataset for transparency and data-quality review

This prevents physiologically impossible measurements from being interpreted as true clinical risk.

## Project Structure

```text
Longitudinal_Clinical_Vital-Signs_Risk_Screening_Pipeline/
│
├── Longitudinal_Clinical_Vital-Signs_Risk_Screening_Pipeline.py
├── patients_data.csv
├── risk_config.json
├── screening_results.csv
├── screening_summary.json
└── README.md
```


## Project Workflow

risk_config.json
        ↓
Load validation ranges and clinical thresholds
        ↓
patients_data.csv
        ↓
Read observation
        ↓
Convert data types
        ↓
Handle errors if they exist
        ↓
Validate vital signs
        ↓
If valid:
    calculate clinical flags
    calculate risk score
    classify risk level
        ↓
Write observation to screening_results.csv
        ↓
Track dataset statistics
        ↓
Generate screening_summary.json


## Python Concepts Demonstrated

This project applies:

- functions
- loops
- conditionals
- dictionaries
- sets
- CSV processing
- JSON processing
- type conversion
- counters
- Boolean logic
- file handling
- data validation


## Skills Demonstrated

The project demonstrates practical foundations relevant to healthcare AI and software engineering:

- structured healthcare data processing
- reusable Python functions
- separation of configuration from logic
- rule-based clinical screening
- longitudinal data handling
- data-quality validation
- structured result generation
- reproducible processing pipelines
- Error handling

## Limitations
- the risk score is rule-based rather than statistically learned
- the thresholds are not a validated clinical deterioration score
- the project does not yet use Pandas, NumPy, or machine learning
- repeated observations are screened independently rather than modeled as a full time series

## Planned Improvements

Future versions may include:
- modular Python files
- Pandas-based preprocessing
- missing-data handling
- exploratory data analysis
- visualization
- feature engineering
- machine-learning risk prediction
- comparison between rule-based and ML-based screening

## Purpose

This project was built as part of a progression from Python fundamentals toward healthcare AI, machine learning, NLP, and clinical software engineering.
It demonstrates the transition from single-patient interactive scripts to structured processing of real-world longitudinal healthcare data.
