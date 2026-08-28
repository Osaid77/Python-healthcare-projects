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

This is an educational healthcare screening prototype and is not intended to represent a validated clinical deterioration score or medical device.

## Dataset

The project uses a public hospital vital-sign dataset containing repeated measurements across admissions.

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
