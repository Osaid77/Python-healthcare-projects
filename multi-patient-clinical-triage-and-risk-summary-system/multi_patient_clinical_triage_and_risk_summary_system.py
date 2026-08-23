# Get patients' data

patients = [
    {
        "name": "Karim",
        "age": 30,
        "temperature": 37,
        "oxygen_saturation": 99,
        "heart_rate": 70,
        "has_diabetes": False
    },

    {
        "name": "Sid",
        "age": 40,
        "temperature": 38.5,
        "oxygen_saturation": 97,
        "heart_rate": 80,
        "has_diabetes": False
    },

    {
        "name": "Osaid",
        "age": 22,
        "temperature": 37,
        "oxygen_saturation": 89,
        "heart_rate": 77,
        "has_diabetes": False
    },

    {
        "name": "",
        "age": -50,
        "temperature": 20,
        "oxygen_saturation": 110,
        "heart_rate": 10,
        "has_diabetes": False
    },

    {
        "name": "Ahmad",
        "age": 67,
        "temperature": 38,
        "oxygen_saturation": 65,
        "heart_rate": 120,
        "has_diabetes": True
    }
]



# Validation

MIN_AGE, MAX_AGE = (1, 130)
MIN_TEMPERATURE, MAX_TEMPERATURE = (32, 42)
MIN_O2_SATURATION, MAX_O2_SATURATION = (50, 100)
MIN_HEART_RATE, MAX_HEART_RATE = (50, 200)


def validate_patient(patient):

    errors = []

    if patient["age"] < MIN_AGE or patient["age"] > MAX_AGE:
        errors.append("Invalid age")

    if patient["temperature"] < MIN_TEMPERATURE or patient["temperature"] > MAX_TEMPERATURE:
        errors.append("Invalid temperature")

    if patient["oxygen_saturation"] < MIN_O2_SATURATION or patient["oxygen_saturation"] > MAX_O2_SATURATION:
        errors.append("Invalid oxygen saturation")

    if patient["heart_rate"] < MIN_HEART_RATE or patient["heart_rate"] > MAX_HEART_RATE:
        errors.append("Invalid heart rate")

    if errors:
        return errors     # the program stops here if there are errors and doesn't output Valid

    return "Valid"


for patient in patients:
    print(validate_patient(patient))


print()




# Risk score calculation


def calculate_risk_score(patient):

    risk_score = 0

    if patient["age"] >= 60:
        risk_score += 1

    if patient["temperature"] >= 38:
        risk_score += 1

    if patient["oxygen_saturation"] < 94:
        risk_score += 1

    if patient["heart_rate"] >= 90:
        risk_score += 1

    if patient["has_diabetes"]:
        risk_score += 1

    return risk_score


for patient in patients:
    print(calculate_risk_score(patient))

print()




# Risk Classification

def classify_risk(patient):

    risk_score = calculate_risk_score(patient)

    if risk_score >= 4:
        risk_level = "High risk"

    elif risk_score >= 2:
        risk_level = "Moderate risk"

    else:
        risk_level = "Low risk"

    return risk_level


for patient in patients:
    print(classify_risk(patient))

print()





# Risk factor/s of each patient

def get_risk_factors(patient):
    risk_factors = []

    if patient["age"] >= 60:
        risk_factors.append("Age risk factor")

    if patient["temperature"] >= 38:
        risk_factors.append("Temperature risk factor")

    if patient["oxygen_saturation"] < 94:
        risk_factors.append("Oxygen saturation risk factor")

    if patient["heart_rate"] >= 90:
        risk_factors.append("heart rate risk factor")

    if patient["has_diabetes"]:
        risk_factors.append("Diabetes risk factor")

    if risk_factors:
        return risk_factors

    return risk_factors


for patient in patients:
    if validate_patient(patient) == "Valid":
        print(get_risk_factors(patient))

    else:
        print(validate_patient(patient))


print()




# Structured report for every patient

for patient in patients:
    if validate_patient(patient) == "Valid":
        print("-----Patient Report-----")
        print("Patient name:", patient["name"])
        print("Patient age:", patient["age"])
        print("Temperature:", patient["temperature"])
        print("Oxygen saturation:", patient["oxygen_saturation"])
        print("Heart rate:", patient["heart_rate"])
        print("Has diabetes:", patient["has_diabetes"])
        print("Risk score:", calculate_risk_score(patient))
        print("Risk classification:", classify_risk(patient))
        print("Risk factors:", get_risk_factors(patient))
        print()

    else:
        print("-----Invalid Patient-----")
        print(validate_patient(patient))
        print()



# Clinic-level Summary

def clinic_summary(patients):
    summary = {}

    total_patients = 0
    valid_patients = 0
    invalid_patients = 0
    low_risk = 0
    moderate_risk = 0
    high_risk = 0

    for patient in patients:
        total_patients += 1

        if validate_patient(patient) == "Valid":
            valid_patients += 1

        else:
            invalid_patients += 1
            continue

        if classify_risk(patient) == "High risk":
            high_risk += 1

        elif classify_risk(patient) == "Moderate risk":
            moderate_risk += 1

        else:
            low_risk += 1

    summary["total_patients"] = total_patients
    summary["valid_patients"] = valid_patients
    summary["invalid_patients"] = invalid_patients
    summary["high_risk"] = high_risk
    summary["moderate_risk"] = moderate_risk
    summary["low_risk"] = low_risk

    return summary


print(clinic_summary(patients))


print()



# A set of risk factors present in those patients

def risk_factors(patients):
    risk_factors = set()

    for patient in patients:

        if validate_patient(patient) != "Valid":
            continue

        if patient["age"] >= 60:
            risk_factors.add("Elderly age")

        if patient["temperature"] >= 38:
            risk_factors.add("High temperature")

        if patient["oxygen_saturation"] < 94:
            risk_factors.add("Low oxygen saturation")

        if patient["heart_rate"] >= 90:
            risk_factors.add("High heart rate")

        if patient["has_diabetes"]:
            risk_factors.add("Diagnosed with diabetes")

    return risk_factors


print("Risk factors detected:", risk_factors(patients))
