# Input and validation of patient data

patient_name = input("Enter name: ")

age = int(input("Enter age: "))
is_age_valid = 1 <= age <= 130
while not is_age_valid:
    print("Invalid input. Try again!")

    age = int(input("Enter age: "))
    is_age_valid = 1 <= age <= 130


temp = float(input("Enter temperature: "))
is_temp_valid = 33 <= temp <= 42
while not is_temp_valid:
    print("Invalid input. Try again!")

    temp = float(input("Enter temperature: "))
    is_temp_valid = 33 <= temp <= 42


oxygen_sat = int(input("Enter oxygen saturation: "))
is_oxygen_sat_valid = 50 <= oxygen_sat <= 100
while not is_oxygen_sat_valid:
    print("Invalid input. Try again!")

    oxygen_sat = int(input("Enter oxygen saturation: "))
    is_oxygen_sat_valid = 50 <= oxygen_sat <= 100


heart_rate = int(input("Enter heart rate: "))
is_heart_rate_valid = 50 <= heart_rate <= 200
while not is_heart_rate_valid:
    print("Invalid input. Try again!")

    heart_rate = int(input("Enter heart rate: "))
    is_heart_rate_valid = 50 <= heart_rate <= 200


has_dm = input("Does the patient have diabetes? (yes/no): ")

while has_dm != "yes" and has_dm != "no":
    print("Invalid input. Try again!")
    has_dm = input("Does the patient have diabetes? (yes/no): ")

if has_dm == "yes":
    has_dm = True

elif has_dm == "no":
    has_dm = False


# Risk score calculation
risk_score = 0

if age >= 60:
    risk_score += 1

if temp >= 38:
    risk_score += 1

if oxygen_sat < 94:
    risk_score += 1

if heart_rate >= 90:
    risk_score += 1

if has_dm:
    risk_score += 1


# risk level calculation
risk_level = 0
if risk_score >= 4:
    risk_level = "High risk"

elif risk_score >= 2:
    risk_level = "Moderate risk"

else:
    risk_level = "Low risk"

needs_urgent_review = False

if risk_level == "High risk":
    needs_urgent_review = True


# Output all information
print("-----Patient Assessment-----")
print("Name:", patient_name)
print("Age:", age)
print("Temperature:", temp)
print("Oxygen saturation:", oxygen_sat)
print("Heart rate:", heart_rate)
print("Diabetes:", has_dm)

if temp >= 38:
    print(f"Patient has fever with temperature of {temp}")

if oxygen_sat < 94:
    print(f"Patient has hypoxemia with an oxygen level of {oxygen_sat}")

if heart_rate >= 90:
    print(f"Patient is tachycardic with heart rate of {heart_rate}")

print("Risk score:", risk_score)
print("Risk level:", risk_level)
print("Needs urgent review:", needs_urgent_review)

if needs_urgent_review:
    print("Patient needs urgent review!")
