# Input and validation of patient data

patient_name = input("Enter name: ")


def validate_age():
    age = int(input("Enter age: "))
    is_age_valid = 1 <= age <= 130

    while not is_age_valid:
        print("Invalid input, Try again!")
        age = int(input("Enter age: "))
        is_age_valid = 1 <= age <= 130

    return age


age = validate_age()

####


def validate_temperature():
    temp = float(input("Enter temperature: "))
    is_temp_valid = 32 <= temp <= 42

    while not is_temp_valid:
        print("Invalid input, Try again!")
        temp = float(input("Enter temperature: "))
        is_temp_valid = 32 <= temp <= 42

    return temp


temperature = validate_temperature()

####


def validate_o2_sat():
    oxygen_sat = int(input("Enter oxygen saturation: "))
    is_o2_sat_valid = 50 <= oxygen_sat <= 100

    while not is_o2_sat_valid:
        print("Invalid input, Try again!")
        oxygen_sat = int(input("Enter oxygen saturation: "))
        is_o2_sat_valid = 50 <= oxygen_sat <= 100

    return oxygen_sat


oxygen_saturation = validate_o2_sat()

####


def validate_heart_rate():
    heart_rate = int(input("Enter heart rate: "))
    is_heart_rate_valid = 50 <= heart_rate <= 200

    while not is_heart_rate_valid:
        print("Invalid input, Try again!")
        heart_rate = int(input("Enter heart rate: "))
        is_heart_rate_valid = 50 <= heart_rate <= 200

    return heart_rate


heart_rate = validate_heart_rate()

####


def get_diabetes_status():
    has_diabetes = input("Does the patient have diabetes (yes/no): ")

    while has_diabetes != "yes" and has_diabetes != "no":
        print("Invalid input, Try again!")
        has_diabetes = input("Does the patient have diabetes (yes/no): ")

    if has_diabetes == "yes":
        has_diabetes = True

    elif has_diabetes == "no":
        has_diabetes = False

    return has_diabetes


has_diabetes = get_diabetes_status()


# risk score calculation


def risk_score_calc(age, temperature, oxygen_saturation, heart_rate, has_diabetes):

    risk_score = 0

    if age >= 60:
        risk_score += 1

    if temperature >= 38:
        risk_score += 1

    if oxygen_saturation < 94:
        risk_score += 1

    if heart_rate >= 90:
        risk_score += 1

    if has_diabetes == True:
        risk_score += 1

    return risk_score


risk_score = risk_score_calc(
    age, temperature, oxygen_saturation, heart_rate, has_diabetes)

# Risk level calculation


def risk_level_calc(risk_score):

    risk_level = 0

    if risk_score >= 4:
        risk_level = "High risk"

    elif risk_score >= 2:
        risk_level = "Moderate risk"

    else:
        risk_level = "Low risk"

    return risk_level


risk_level = risk_level_calc(risk_score)

needs_urgent_review = False

if risk_level == "High risk":
    needs_urgent_review = True


# Output patient details

def display_patient_details(patient_name, age, temperature, oxygen_saturation, heart_rate,
                            has_diabetes, risk_score, risk_level, needs_urgent_review):

    print("----Patient Details----")
    print("Patient name: ", patient_name)
    print("Patient age: ", age)
    print("Temperature: ", temperature)
    print("Oxygen saturation: ", oxygen_saturation)
    print("Heart rate: ", heart_rate)
    print("Diabetes status: ", has_diabetes)

    if temperature >= 38:
        print(f"Patient has fever with temperature of {temperature}")

    if oxygen_saturation < 94:
        print(
            f"Patient has hypoxemia with an oxygen level of {oxygen_saturation}")

    if heart_rate >= 90:
        print(f"Patient is tachycardic with heart rate of {heart_rate}")

    print("Risk score: ", risk_score)
    print("Risk level: ", risk_level)
    print("Needs urgent review: ", needs_urgent_review)


display_patient_details(patient_name, age, temperature, oxygen_saturation,
                        heart_rate, has_diabetes, risk_score, risk_level, needs_urgent_review)
