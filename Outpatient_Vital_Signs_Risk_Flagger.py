
# Outpatient Vital Signs Risk Flagger


# Structure: 1 raw patient data → 2 Validation -> 3 derived boolean flags → 4 risk score → 5 urgent decision


# 1 raw patient data
patient_name = "John"
patient_age = -30
temperature = 38.5
oxygen_saturation = 94
heart_rate = 90
has_diabetes = False

print("---- Outpatient Vital Signs Risk Flagger ----")
print("Name:", patient_name)
print("Age:", patient_age)
print("Temperature:", temperature)
print("Oxygen saturation:", oxygen_saturation)
print("Heart rate:", heart_rate)
print("Diabetes:", has_diabetes)

# 2 Validation
is_age_valid = True
is_temperature_valid = True
is_oxygen_saturation_valid = True
is_heart_rate_valid = True

if patient_age < 1 or patient_age > 130:
    is_age_valid = False
    print("Invalid age!")


if temperature < 33 or temperature > 42:
    is_temperature_valid = False
    print("Invalid temperature!")


if oxygen_saturation < 50 or oxygen_saturation > 100:
    is_oxygen_saturation_valid = False
    print("Invalid oxygen saturation!")


if heart_rate < 50 or heart_rate > 200:
    is_heart_rate_valid = False
    print("Invalid heart rate!")


# 3 derived boolean flags
has_fever = False
low_oxygen = False
high_heart_rate = False


# 4 risk score
risk_score = 0

# Validation
if is_age_valid and is_temperature_valid and is_oxygen_saturation_valid and is_heart_rate_valid:

    if temperature >= 38:
        has_fever = True

    if oxygen_saturation < 97:
        low_oxygen = True

    if heart_rate > 120:
        high_heart_rate = True

    if has_fever:
        risk_score += 1

    if low_oxygen:
        risk_score += 1

    if high_heart_rate:
        risk_score += 1

    if has_diabetes:
        risk_score += 1

    if patient_age > 60:
        risk_score += 1

    # 5 urgent decision
    needs_urgent_review = False

    if risk_score >= 4:
        needs_urgent_review = True

    print("Has fever:", has_fever)
    print("Low oxygen:", low_oxygen)
    print("High heart rate:", high_heart_rate)
    print("Risk score:", risk_score)
    print("Needs urgent review:", needs_urgent_review)

else:
    print("Cannot continue!")
