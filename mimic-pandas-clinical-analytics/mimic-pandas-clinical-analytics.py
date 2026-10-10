import numpy as np
import pandas as pd 


# Emergency Dept EHR Data Processing & Analytics with Pandas

edstays = pd.read_csv("ed/edstays.csv")
triage = pd.read_csv("ed/triage.csv")
vitals = pd.read_csv("ed/vitalsign.csv")
diagnosis = pd.read_csv("ed/diagnosis.csv")

patients = pd.read_csv("hosp/patients.csv")
admissions = pd.read_csv("hosp/admissions.csv")

icustays = pd.read_csv("icu/icustays.csv")




# investigating datasets

print(edstays.ndim)
print(edstays.shape)
print(edstays.dtypes)
edstays.info()
print(edstays.describe())
print(edstays.columns)
print(edstays.nunique())

print(edstays["arrival_transport"].value_counts(dropna=False))    
print(edstays["gender"].value_counts(dropna=False))       
print(edstays["race"].value_counts(dropna=False))       
print(edstays["disposition"].value_counts(dropna=False))       

print(edstays.isna().sum())
print(edstays.notna().sum())

print("Rows count:", edstays.shape[0])
print("Columns count:", edstays.shape[1])

print("Primary key: stay_id")
print("Unique:", edstays["stay_id"].is_unique)
print("Missing IDs:", edstays["stay_id"].isna().sum())


# 

print(triage.ndim)
print(triage.columns)
print(triage.shape)
print(triage.dtypes)
triage.info()
print(triage.describe())
print(triage.nunique())

print(triage["chiefcomplaint"].value_counts(dropna=False))
print(triage["acuity"].value_counts(dropna=False))

print(triage.isna().sum())
print(triage.notna().sum())

print("Rows count", triage.shape[0])
print("Columns count", triage.shape[1])

print("Key: stay_id")
print("Unique:", triage["stay_id"].is_unique)
print("Missing IDs:", triage["stay_id"].isna().sum())

#

print(vitals.shape)
print(vitals.columns)
print(vitals.dtypes)
print(vitals.ndim)
vitals.info()
print(vitals.describe())
print(vitals.nunique())

print(vitals["rhythm"].value_counts(dropna=False))
print(vitals["pain"].value_counts(dropna=False))

print(vitals.isna().sum())
print(vitals.notna().sum())


print("Rows count:", vitals.shape[0])
print("Columns count:", vitals.shape[1])


#

print(diagnosis.shape)
print(diagnosis.ndim)
print(diagnosis.columns)
print(diagnosis.dtypes)
diagnosis.info()
print(diagnosis.describe())
print(diagnosis.nunique())

print(diagnosis["icd_code"].value_counts(dropna=False))
print(diagnosis["icd_version"].value_counts(dropna=False))
print(diagnosis["icd_title"].value_counts(dropna=False))

print(diagnosis.isna().sum())
print(diagnosis.notna().sum())

print("Rows count:", diagnosis.shape[0])
print("Columns count:", diagnosis.shape[1])

print(diagnosis["subject_id"].is_unique)           # no unique columns in the dataset but I'll do stay_id + seq_num
print(diagnosis["stay_id"].is_unique)
print(diagnosis["icd_code"].is_unique)
print(diagnosis["icd_version"].is_unique)
print(diagnosis["icd_title"].is_unique)
print(diagnosis["seq_num"].is_unique)

print("Key: stay_id + seq_num")
print("Unique:", diagnosis[["stay_id", "seq_num"]].duplicated().sum())
print("Missing IDs:", diagnosis[["stay_id", "seq_num"]].isna().sum())

#

print(patients.ndim)
print(patients.shape)
print(patients.columns)
print(patients.dtypes)
patients.info()
print(patients.describe())
print(patients.nunique())

print(patients["gender"].value_counts(dropna=False))
print(patients["anchor_year_group"].value_counts(dropna=False))

print(patients.isna().sum())
print(patients.notna().sum())

print("Rows count:", patients.shape[0])
print("Columns count:", patients.shape[1])

print("Key: subject_id")
print("Unique:", patients["subject_id"].is_unique)
print("Missing IDs:", patients["subject_id"].isna().sum())

#

print(admissions.shape)
print(admissions.ndim)
print(admissions.columns)
print(admissions.dtypes)
admissions.info()
print(admissions.describe())
print(admissions.nunique())

print(admissions["insurance"].value_counts(dropna=False))
print(admissions["language"].value_counts(dropna=False))
print(admissions["marital_status"].value_counts(dropna=False))
print(admissions["race"].value_counts(dropna=False))
print(admissions["hospital_expire_flag"].value_counts(dropna=False))

print(admissions.isna().sum())
print(admissions.notna().sum())

print("Rows count:", admissions.shape[0])
print("Columns count:", admissions.shape[1])

print("Key: hadm_id")
print("Unique:", admissions["hadm_id"].is_unique)
print("Missing IDs:", admissions["hadm_id"].isna().sum())


#

print(icustays.shape)
print(icustays.ndim)
print(icustays.columns)
print(icustays.dtypes)
icustays.info()
print(icustays.describe())
print(icustays.nunique())

print(icustays["first_careunit"].value_counts(dropna=False))
print(icustays["last_careunit"].value_counts(dropna=False))

print(icustays.isna().sum())
print(icustays.notna().sum())

print("Rows count:", icustays.shape[0])
print("Columns count:", icustays.shape[1])

print("Key: stay_id")
print("Unique:", icustays["stay_id"].is_unique)
print("Missing IDs:", icustays["stay_id"].isna().sum())





# Determining unique ids/keys for each dataset

print(edstays.shape[0])
print(edstays["subject_id"].nunique())

print(patients.shape[0])
print(patients["subject_id"].nunique())

print((edstays["subject_id"].isin(patients["subject_id"])).all())      # All ED patient IDs are in the patients table

print((triage["stay_id"].isin(edstays["stay_id"])).all())       # all triage stay_id are present in edstays



no_vitals = ~edstays["stay_id"].isin(vitals["stay_id"])
print(no_vitals.sum())
print(edstays[no_vitals])



print((vitals["stay_id"].isin(edstays["stay_id"])).all())       # all stay_id are present in both datasets

print((diagnosis["stay_id"].isin(edstays["stay_id"])).all())     # all stay_id are present in both datasets





print(edstays["hadm_id"].is_unique)
print(edstays["stay_id"].is_unique)    # unique

print(triage["subject_id"].is_unique)
print(triage["stay_id"].is_unique)     # unique

print(vitals["subject_id"].is_unique)     
print(vitals["stay_id"].is_unique)
print(vitals["charttime"].is_unique)     # unique

print(diagnosis["subject_id"].is_unique)      # no unique columns in dataset
print(diagnosis["stay_id"].is_unique)
print(diagnosis["icd_code"].is_unique)

print(patients["subject_id"].is_unique)     # unique

print(admissions["subject_id"].is_unique)
print(admissions["hadm_id"].is_unique)        # unique

print(icustays["subject_id"].is_unique)
print(icustays["hadm_id"].is_unique)
print(icustays["stay_id"].is_unique)       # unique








# Duplicated rows in datasets

print(edstays[edstays.duplicated()])      # no duplicated records in edstays
print(edstays.duplicated().sum())

print(triage[triage.duplicated()])        # no duplicated records in triage
print(triage.duplicated().sum())

print(vitals[vitals.duplicated()])        # no duplicated records in vitals
print(vitals.duplicated().sum())

print(diagnosis[diagnosis.duplicated()])     # no duplicated records in diagnosis
print(diagnosis.duplicated().sum())

print(patients[patients.duplicated()])      # no duplicated records in patients
print(patients.duplicated().sum())

print(admissions[admissions.duplicated()])      # no duplicated records in admissions
print(admissions.duplicated().sum())

print(icustays[icustays.duplicated()])       # no duplicated records in icustays
print(icustays.duplicated().sum())





# Detecting invalid vital signs across datasets

print(triage.loc[(triage["temperature"].notna()) & (~triage["temperature"].between(90, 110)), "temperature"])   # 1 invalid value of 36.5 at record 151 could have been because °C was counted instead of °F

print(triage.loc[(triage["heartrate"].notna()) & (~triage["heartrate"].between(10, 250)), "heartrate"])  # no clinically invalid heart rates were recorded

print(triage.loc[(triage["resprate"].notna()) & (~triage["resprate"].between(5, 80)), "resprate"]) # no clinically invalid respiratory rates were recorded

print(triage.loc[(triage["o2sat"].notna()) & (~triage["o2sat"].between(60, 100)), "o2sat"]) # no clinically invalid oxygen saturations were recorded

print(triage.loc[(triage["sbp"].notna()) & (~triage["sbp"].between(40, 250)), "sbp"])   # no clinically invalid systolic blood pressures were recorded

print(triage.loc[(triage["dbp"].notna()) & (~triage["dbp"].between(20, 150)), "dbp"])   # 1 invalid diastolic blood pressure value of 879 was recorded on record 94




print(vitals.loc[vitals["temperature"].notna() & (~vitals["temperature"].between(90, 110) & ~vitals["temperature"].between(33, 43)), "temperature"])   # Here some values were recorded in °C and invalid values were spotted between records 609-619

print(vitals.loc[(vitals["heartrate"].notna()) & (~vitals["heartrate"].between(10, 250)), "heartrate"])     # no clinically invalid

print(vitals.loc[(vitals["resprate"].notna()) & (~vitals["resprate"].between(5, 80)), "resprate"])     # no clinically invalid

print(vitals.loc[(vitals["o2sat"].notna()) & (~vitals["o2sat"].between(60, 100)), "o2sat"])     # 1 invalid value of 10 was recorded on record 786

print(vitals.loc[(vitals["sbp"].notna()) & (~vitals["sbp"].between(40, 250)), "sbp"])     # 1 invalid value of 11 was recorded on recorded on record 291

print(vitals.loc[(vitals["dbp"].notna()) & (~vitals["dbp"].between(20, 150)), "dbp"])     # 1 invalid value of 184 was recorded on record 291 the same record of sbp



# counting invalid vital signs BEFORE cleaning:

print("Missing vital signs BEFORE cleaning in triage:")

print(triage["temperature"].isna().sum())
print(triage["heartrate"].isna().sum())
print(triage["resprate"].isna().sum())
print(triage["o2sat"].isna().sum())
print(triage["sbp"].isna().sum())
print(triage["dbp"].isna().sum())

print("Total invalid vital signs BEFORE cleaning in vitals:")

print(vitals["temperature"].isna().sum())
print(vitals["heartrate"].isna().sum())
print(vitals["resprate"].isna().sum())
print(vitals["o2sat"].isna().sum())
print(vitals["sbp"].isna().sum())
print(vitals["dbp"].isna().sum())





# cleaning vital signs

triage_clean = triage.copy()

triage_clean.loc[(triage_clean["temperature"].notna()) & (~triage_clean["temperature"].between(90, 110)), "temperature"] = np.nan

triage_clean.loc[(triage_clean["heartrate"].notna()) & (~triage_clean["heartrate"].between(10, 250)), "heartrate"] = np.nan

triage_clean.loc[(triage_clean["resprate"].notna()) & (~triage_clean["resprate"].between(5, 80)), "resprate"] = np.nan

triage_clean.loc[(triage_clean["o2sat"].notna()) & (~triage_clean["o2sat"].between(60, 100)), "o2sat"] = np.nan

triage_clean.loc[(triage_clean["sbp"].notna()) & (~triage_clean["sbp"].between(40, 250)), "sbp"] = np.nan

triage_clean.loc[(triage_clean["dbp"].notna()) & (~triage_clean["dbp"].between(20, 150)), "dbp"] = np.nan


vitals_clean = vitals.copy()

vitals_clean.loc[vitals_clean["temperature"].notna() & (~vitals_clean["temperature"].between(90, 110) & ~vitals_clean["temperature"].between(33, 43)), "temperature"] = np.nan

vitals_clean.loc[(vitals_clean["heartrate"].notna()) & (~vitals_clean["heartrate"].between(10, 250)), "heartrate"] = np.nan

vitals_clean.loc[(vitals_clean["resprate"].notna()) & (~vitals_clean["resprate"].between(5, 80)), "resprate"] = np.nan

vitals_clean.loc[(vitals_clean["o2sat"].notna()) & (~vitals_clean["o2sat"].between(60, 100)), "o2sat"] = np.nan

vitals_clean.loc[(vitals_clean["sbp"].notna()) & (~vitals_clean["sbp"].between(40, 250)), "sbp"] = np.nan

vitals_clean.loc[(vitals_clean["dbp"].notna()) & (~vitals_clean["dbp"].between(20, 150)), "dbp"] = np.nan



# counting invalid vital signs AFTER cleaning:

print("Total invalid vital signs AFTER cleaning in triage:")

print(triage["temperature"].isna().sum())
print(triage["heartrate"].isna().sum())
print(triage["resprate"].isna().sum())
print(triage["o2sat"].isna().sum())
print(triage["sbp"].isna().sum())
print(triage["dbp"].isna().sum())

print("Difference:")
print(triage_clean["temperature"].isna().sum() - triage["temperature"].isna().sum())
print(triage_clean["heartrate"].isna().sum() - triage["heartrate"].isna().sum())
print(triage_clean["resprate"].isna().sum() - triage["resprate"].isna().sum())
print(triage_clean["o2sat"].isna().sum() - triage["o2sat"].isna().sum())
print(triage_clean["sbp"].isna().sum() - triage["sbp"].isna().sum())
print(triage_clean["dbp"].isna().sum() - triage["dbp"].isna().sum())


print("Total invalid vital signs AFTER cleaning in vitals:")

print(vitals["temperature"].isna().sum())
print(vitals["heartrate"].isna().sum())
print(vitals["resprate"].isna().sum())
print(vitals["o2sat"].isna().sum())
print(vitals["sbp"].isna().sum())
print(vitals["dbp"].isna().sum())

print("Difference:")
print(vitals_clean["temperature"].isna().sum() - vitals["temperature"].isna().sum())
print(vitals_clean["heartrate"].isna().sum() - vitals["heartrate"].isna().sum())
print(vitals_clean["resprate"].isna().sum() - vitals["resprate"].isna().sum())
print(vitals_clean["o2sat"].isna().sum() - vitals["o2sat"].isna().sum())
print(vitals_clean["sbp"].isna().sum() - vitals["sbp"].isna().sum())
print(vitals_clean["dbp"].isna().sum() - vitals["dbp"].isna().sum())







# Categorical data cleaning and text handling:

edstays["gender"] = edstays["gender"].str.strip().str.lower()

edstays["race"] = edstays["race"].str.strip().str.lower()

edstays["arrival_transport"] = edstays["arrival_transport"].str.strip().str.lower()

edstays["disposition"] = edstays["disposition"].str.strip().str.lower()




triage["chiefcomplaint"] = triage["chiefcomplaint"].str.strip().str.lower()

triage["chiefcomplaint"] = triage["chiefcomplaint"].replace({ 
    "wound eval, transfer": "wound eval",
    "dvt, transfer": "dvt",
    "l leg dvt": "dvt",
    "lower back pain, s/p fall": "back pain",
    "lower back pain": "back pain"
})


triage["chiefcomplaint"] = triage["chiefcomplaint"].str.replace("eval", "evaluation")
triage["chiefcomplaint"] = triage["chiefcomplaint"].str.replace("abd", "abdominal")
triage["chiefcomplaint"] = triage["chiefcomplaint"].str.replace("sob", "dyspnea")
triage["chiefcomplaint"] = triage["chiefcomplaint"].str.replace("resp", "respiratory")
triage["chiefcomplaint"] = triage["chiefcomplaint"].str.replace("?", "possible")
# triage["chiefcomplaint"] = triage["chiefcomplaint"].str.replace("l", "left")         Sometimes l means lower so it's bad decision to implement this
# triage["chiefcomplaint"] = triage["chiefcomplaint"].str.replace("r", "right")    





vitals["rhythm"] = vitals["rhythm"].str.strip().str.lower()
vitals["rhythm"] = vitals["rhythm"].replace({
    "normal sinus rhythm": "sinus rhythm",
    "afib": "atrial fibrillation",
    "sr": "sinus rhythm"
})





diagnosis["icd_title"] = diagnosis["icd_title"].str.strip().str.lower()
# print(diagnosis["icd_title"].value_counts())    # I'm guessing we shouldn't do anything to it because these are icd titles and shouldn't be changed





admissions["admission_location"] = admissions["admission_location"].str.strip().str.lower()

admissions["admission_location"] = admissions["admission_location"].replace({
    "clinic referral": "physician referral"
})

admissions["discharge_location"] = admissions["discharge_location"].str.strip().str.lower()

admissions["insurance"] = admissions["insurance"].str.strip().str.lower()

admissions["language"] = admissions["language"].str.strip().str.lower()

admissions["language"] = admissions["language"].replace({
    "?": "Unknown"
})

admissions["marital_status"] = admissions["marital_status"].str.strip().str.lower()

admissions["race"] = admissions["race"].str.strip().str.lower()

admissions["race"] = admissions["race"].replace({
    "unable to obtain": "unknown", 
    "patient declined to answer": "unknown"
})






icustays["first_careunit"] = icustays["first_careunit"].str.strip().str.lower()

icustays["first_careunit"] = icustays["first_careunit"].replace({
    "neuro surgical intensive care unit (neuro sicu)": "neuro sicu",
    "neuro stepdown": "neuro sicu",
    "neuro intermediate": "neuro sicu",
    "cardiac vascular intensive care unit (cvicu)": "cvsicu",
    "coronary care unit (ccu)": "cvsicu"
})


icustays["last_careunit"] = icustays["last_careunit"].str.strip().str.lower()

icustays["last_careunit"] = icustays["last_careunit"].replace({
    "neuro surgical intensive care unit (neuro sicu)": "neuro sicu",
    "neuro stepdown": "neuro sicu",
    "neuro intermediate": "neuro sicu",
    "cardiac vascular intensive care unit (cvicu)": "cvsicu",
    "coronary care unit (ccu)": "cvsicu"
})





# Date/time handling and length of stay generation


edstays["intime"] = pd.to_datetime(edstays["intime"], errors="coerce")

edstays["outtime"] = pd.to_datetime(edstays["outtime"], errors="coerce")

edstays["ed_length_of_stay"] = edstays["outtime"] - edstays["intime"]

edstays["ed_length_of_stay_hrs"] = (edstays["ed_length_of_stay"] / pd.Timedelta(hours=1)).round(2)


vitals["charttime"] = pd.to_datetime(vitals["charttime"], errors="coerce")


admissions["admittime"] = pd.to_datetime(admissions["admittime"], errors="coerce")
admissions["dischtime"] = pd.to_datetime(admissions["dischtime"], errors="coerce")

admissions["length_of_stay"] = admissions["dischtime"] - admissions["admittime"]

admissions["length_of_stay_days"] = (admissions["length_of_stay"] / pd.Timedelta(days=1)).round(2)

overnight_admissions = admissions[admissions["admittime"].dt.hour.between(0, 5)]

admissions["deathtime"] = pd.to_datetime(admissions["deathtime"], errors="coerce")

admissions["edregtime"] = pd.to_datetime(admissions["edregtime"], errors="coerce")

admissions["edouttime"] = pd.to_datetime(admissions["edouttime"], errors="coerce")



icustays["intime"] = pd.to_datetime(icustays["intime"], errors="coerce")

icustays["outtime"] = pd.to_datetime(icustays["outtime"], errors="coerce")

icustays["los"] = pd.to_timedelta(icustays["los"], errors="coerce")






# Feature engineering of clinical flags:


triage_clean["fever"] = triage_clean["temperature"] >= 99.5
triage_clean["tachycardia"] = triage_clean["heartrate"] >= 120
triage_clean["tachypnea"] = triage_clean["resprate"] > 20
triage_clean["hypoxemia"] = triage_clean["o2sat"] < 94
triage_clean["hypertension"] = (triage_clean["sbp"] > 120) & (triage_clean["dbp"] > 80)
triage_clean["hypotension"] = (triage_clean["sbp"] < 90) & (triage_clean["dbp"] < 60)


triage_clean["needs_review"] = ((triage_clean["heartrate"] >= 120) & 
    ((triage_clean["o2sat"] < 94) | ((triage_clean["sbp"] > 120) & (triage_clean["dbp"] > 80))))


triage_clean["needs_admission"] = triage_clean["fever"] & triage_clean["hypoxemia"] & triage_clean["tachypnea"]

triage_clean["normal_but_edge_case"] = triage_clean["heartrate"].between(110, 120) & ((triage_clean["o2sat"].between(94, 96)) | (triage_clean["sbp"].between(110, 120)))






vitals_clean["fever"] = vitals_clean["temperature"] >= 99.5
vitals_clean["tachycardia"] = vitals_clean["heartrate"] >= 120
vitals_clean["tachypnea"] = vitals_clean["resprate"] > 20
vitals_clean["hypoxemia"] = vitals_clean["o2sat"] < 94
vitals_clean["hypertension"] = (vitals_clean["sbp"] > 120) & (vitals_clean["dbp"] > 80)
vitals_clean["hypotension"] = (vitals_clean["sbp"] < 90) & (vitals_clean["dbp"] < 60)


vitals_clean["needs_review"] = ((vitals_clean["heartrate"] >= 120) & 
    ((vitals_clean["o2sat"] < 94) | ((vitals_clean["sbp"] > 120) & (vitals_clean["dbp"] > 80))))

vitals_clean["needs_admission"] = vitals_clean["fever"] & vitals_clean["hypoxemia"] & vitals_clean["tachypnea"]

vitals_clean["normal_but_edge_case"] = vitals_clean["heartrate"].between(110, 120) & ((vitals_clean["o2sat"].between(94, 96)) | (vitals_clean["sbp"].between(110, 120)))







# Statistics

percentage_of_each = triage_clean[["fever", "tachycardia", "tachypnea", "hypertension", "hypotension", "hypoxemia", "needs_review", 
                    "needs_admission", "normal_but_edge_case"]].mean() * 100

median = triage_clean[["fever", "tachycardia", "tachypnea", "hypertension", "hypotension", "hypoxemia", "needs_review", 
                    "needs_admission", "normal_but_edge_case"]].median()

standard_dev = triage_clean[["fever", "tachycardia", "tachypnea", "hypertension", "hypotension", "hypoxemia", "needs_review", 
                    "needs_admission", "normal_but_edge_case"]].std()

count_of_each = triage_clean[["fever", "tachycardia", "tachypnea", "hypertension", "hypotension", "hypoxemia", "needs_review", 
                    "needs_admission", "normal_but_edge_case"]].count()



vitals_features = vitals_clean[["fever", "tachycardia", "tachypnea", "hypoxemia", "hypertension", "hypotension", 
            "needs_review", "needs_admission", "normal_but_edge_case"]]

vitals_statistics = vitals_features.agg(["mean", "median", "std", "count"])

print(vitals_statistics.round(2))






# Grouping meaningful data


print(triage_clean.groupby("hypertension")[["sbp", "dbp"]].mean())        # average sbp and dbp per hypertension groups

print(triage_clean.groupby("fever")["temperature"].mean())        # average temp per fever groups

print(triage_clean.groupby("hypoxemia")["o2sat"].mean())        # average spo2 per hypoxemia groups

print(triage_clean.groupby("hypoxemia")["o2sat"].min())        # min spo2 per hypoxemia groups


triage_need_review_stats = triage_clean.groupby("needs_review")[["o2sat", "heartrate", "sbp", "dbp"]].agg(["mean", "median", "std", "max", "min"])

triage_need_adm_stats = triage_clean.groupby("needs_admission")[["o2sat", "temperature", "resprate"]].agg(["mean", "median", "std", "max", "min"])

triage_edge_case_stats = triage_clean.groupby("normal_but_edge_case")[["o2sat", "heartrate", "sbp"]].agg(["mean", "median", "std", "max", "min"])

#

print(vitals_clean.groupby("hypertension")[["sbp", "dbp"]].mean())        # average sbp and dbp per hypertension groups

print(vitals_clean.groupby("fever")["temperature"].mean())        # average temp per fever groups

print(vitals_clean.groupby("hypoxemia")["o2sat"].mean())        # average spo2 per hypoxemia groups

print(vitals_clean.groupby("hypoxemia")["o2sat"].min())        # min spo2 per hypoxemia groups


vitals_need_review_stats = vitals_clean.groupby("needs_review")[["o2sat", "heartrate", "sbp", "dbp"]].agg(["mean", "median", "std", "max", "min"])

vitals_need_adm_stats = vitals_clean.groupby("needs_admission")[["o2sat", "temperature", "resprate"]].agg(["mean", "median", "std", "max", "min"])

vitals_edge_case_stats = vitals_clean.groupby("normal_but_edge_case")[["o2sat", "heartrate", "sbp"]].agg(["mean", "median", "std", "max", "min"])







print(edstays.groupby(["gender", "race"])["ed_length_of_stay_hrs"].mean().sort_values(ascending=False))    # average los per gender and race

print(edstays.groupby(["gender", "race"])["ed_length_of_stay_hrs"].agg(["mean", "median", "min", "max"]).sort_values("mean", ascending=False))    # stats of gender & race




print(admissions.groupby("insurance")["length_of_stay_days"].agg(["mean", "max", "min"]))

print(admissions.groupby("admission_type")["length_of_stay_days"].mean().sort_values(ascending=False))    # Comparing avrg los for each admission type

print(admissions.groupby("admission_location")["length_of_stay_days"].agg(["mean", "max", "min"]).sort_values("mean", ascending=False))   # each location's los stats 





# Primary and secondary diagnoses feature engineering and analysis


print((edstays["stay_id"].isin(diagnosis["stay_id"])).all())      # False. Meaning not every edstay has a diagnosis in the diagnosis dataset.

print((diagnosis["stay_id"].isin(edstays["stay_id"])).all())      # the reverse is True i.e. every diagnosis is present in edstays


diagnosis_assoc_edstay = pd.merge(edstays, diagnosis, how="inner", on="stay_id")    # link each edstay with its diagnoses, multiple records per an edstay because there could be multiple diagnoses for an edstay


primary_diagnosis = diagnosis_assoc_edstay.loc[diagnosis_assoc_edstay["seq_num"] == 1, ["stay_id", "icd_title"]].rename(columns={
    "icd_title": "primary_diagnosis"})


secondary_diagnoses = diagnosis_assoc_edstay.loc[diagnosis_assoc_edstay["seq_num"] != 1, ["stay_id", "icd_title"]].rename(columns={
    "icd_title": "secondary_diagnoses"
})    


all_diagnoses = pd.merge(primary_diagnosis, secondary_diagnoses, how="inner", on="stay_id")







# Master encounter table major merge

# Prep help for crafting the merged dataframes especially the master encounters  
print("patients")
print(patients.columns)      # subject_id
print(patients.shape)        # (100, 6)

print("edstays")
print(edstays.columns)        # stay_id       subject_id       hadm_id
print(edstays.shape)         # (222, 11)

print("triage")
print(triage.columns)         # stay_id      subject_id
print(triage.shape)          # (222, 11)

print("admissions")
print(admissions.columns)    # hadm_id       subject_id
print(admissions.shape)      # (275, 18)

print("icustays")
print(icustays.columns)      # stay_id
print(icustays.shape)        # (140, 8)

print("vitals")
print(vitals.columns)         # stay_id       subject_id
print(vitals.shape)           # (1038, 11)

print("diagnosis")
print(diagnosis.columns)    # stay_id + seq_num
print(diagnosis.shape)      # (545, 6)




# Connect each patient to edstays and triage and admissions and icustays and vitals and diagnosis

patient_edstay = pd.merge(patients, edstays, how="inner", on="subject_id")
print(patient_edstay)       # (222, 16)

patient_triage = pd.merge(patients, triage, how="inner", on="subject_id")
print(patient_triage)       # (222, 16)

patient_admission = pd.merge(patients, admissions, how="inner", on="subject_id")
print(patient_admission)    # (275, 23)

patient_icustay = pd.merge(patients, icustays, how="inner", on="subject_id")
print(patient_icustay)      # (140, 13)

patient_vitals = pd.merge(patients, vitals, how="inner", on="subject_id")
print(patient_vitals)       # (1038, 16)

patient_diagnoses = pd.merge(patients, diagnosis, how="inner", on="subject_id")
print(patient_diagnoses)    # (545, 11)






# edstays that became admissions are 172:

edstays_admission = pd.merge(edstays, admissions, how="inner", on="hadm_id")
print(edstays_admission)      # (172, 28)


# triage that became admissions are 174:

triage_edstays = pd.merge(triage, edstays, how="inner", on="stay_id")
triage_admissions = pd.merge(triage_edstays, edstays_admission, how="inner", on="hadm_id")

print(triage_admissions)        # (174, 48)


# vitals for admitted patients:

edstays_vitals = pd.merge(edstays, vitals, how="inner", on="stay_id")    # (1038, 21)
admission_vitals = pd.merge(edstays_vitals, admissions, how="inner", on="hadm_id")
print(admission_vitals)      # (905, 28)   many-to-many     Repeated vitals linked to hosp adm



# Other hospital outcomes

# edstays that end up admitted:

edstays_admitted_subj = pd.merge(edstays, admissions, how="inner", on="subject_id")    # here we're linking each ed visit with an admission using patient data. 
# Combine visits and admissions belonging to the same patients. Patient-level relationship. 

edstays_admitted_hadm = pd.merge(edstays, admissions, how="inner", on="hadm_id")       # here we're linking each ed visit with an admission using admission data. 
# represent matched ED–hospital admission records. Encounter-to-adm relationship. 

print(edstays_admitted_subj.shape)      # (1684, 28)    1 patient can have multiple ED visits and multiple admissions. many-to-many merge. But we don't want that, we want the following:
print(edstays_admitted_hadm.shape)      # (172, 28)     Match ed visit to linked admissions. Not every ed visit became an admission


# hospital mortality:
patient_admission = pd.merge(patients, admissions, how="inner", on="subject_id")     

print(patient_admission[["subject_id", "hospital_expire_flag"]])     # it's showing patient and if they died in that admission

print(patient_admission[patient_admission["hospital_expire_flag"] == 1])     # exact records of died patients in the hospital


# discharge location:
print(patient_admission[["subject_id", "discharge_location"]])     # it's showing patient and discharge location 


# admissions with ICU care:

admissions_ICU = pd.merge(admissions, icustays, how="inner", on="hadm_id")

print(admissions_ICU["hadm_id"].nunique())     # how many unique admissions involved an ICU stay







# Master dataframe

master_encounters = pd.merge(edstays, patients, how="left", on="subject_id")

master_encounters = pd.merge(master_encounters, triage_clean, how="left", on="stay_id")

master_encounters = pd.merge(master_encounters, admissions, how="left", on="hadm_id")

vitals_summary = (vitals_clean.groupby("stay_id").agg({
    "heartrate": "mean",
    "o2sat": "min",
    "sbp": "mean",
    "resprate": "mean",
    "temperature": "max"
}).reset_index())

master_encounters = pd.merge(master_encounters, vitals_summary, how="left", on="stay_id")





# checking merges worked correctly:

print("Original ed stays records", edstays.shape[0])     
print("Master encounters records", master_encounters.shape[0])
print("Rows preserved:", (edstays.shape[0] == master_encounters.shape[0]))

print("Unique ed stays keys:", edstays["stay_id"].is_unique)
print("Unique master counters keys:", master_encounters["stay_id"].is_unique)
print("Duplicated ed stays keys:", edstays["stay_id"].duplicated().sum())
print("Duplicated master counters keys:", master_encounters["stay_id"].duplicated().sum())

print("ed stays without admission:", master_encounters["hadm_id"].isna().sum())




# Final dataset organization

master_encounters_final = master_encounters.copy()

print(master_encounters_final.columns)
print(master_encounters_final.shape)

# pd.set_option("display.max_rows", None)



master_encounters_final = master_encounters_final.drop(columns={"subject_id", "subject_id_y", "race_y", "gender_y"})

master_encounters_final = master_encounters_final.rename(columns={
    "subject_id_x": "subject_id",
    "gender_x": "gender",
    "race_x": "race",
    "temperature_x": "temperature_triage",
    "temperature_y": "ed_max_temperature",
    "heartrate_x": "heartrate_triage",
    "heartrate_y": "ed_mean_heartrate",
    "resprate_x": "resprate_triage",
    "resprate_y": "ed_mean_resprate",
    "o2sat_x": "o2sat_triage",
    "o2sat_y": "ed_min_spo2",
    "sbp_x": "sbp_triage",
    "sbp_y": "ed_mean_sbp",
    "length_of_stay": "admit_length_of_stay",
    "length_of_stay_days": "admit_length_of_stay_days"
})

print(master_encounters_final["stay_id"].is_unique)
print(master_encounters_final.columns)  


ed_stay_analytic_dataset = master_encounters_final.sort_values("intime", ascending=True).reset_index(drop=True)

ed_stay_analytic_dataset.to_csv("ed_stay_analytic_dataset.csv", index=False)
