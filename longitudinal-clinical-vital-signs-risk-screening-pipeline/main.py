import csv
import json
from risk import calculate_risk, classify_risk
import validation


try:

    with open("patients_data.csv", "r") as input_file:
        patients = csv.DictReader(input_file)

        with open("screening_results.csv", "w", newline="") as output_file:
            fieldnames = ["hadm_id", "charttime", "age", "sex", "HR", "RR",
                          "SBP", "TEMP", "SPO2", "valid_data", "fever", "low_oxygen",
                          "high_heart_rate", "high_respiratory_rate", "low_systolic_bp", "risk_score", "risk_level"]

            writer = csv.DictWriter(output_file, fieldnames=fieldnames)

            writer.writeheader()

            total_observations = 0
            valid_observations = 0
            invalid_observations = 0
            malformed_observations = 0
            low_risk = 0
            moderate_risk = 0
            high_risk = 0
            high_risk_admissions = set()

            for item in patients:
                total_observations += 1

                try:

                    hospital_adm_id = item["hadm_id"]
                    age = int(item["age"])
                    gender = item["sex"]
                    chart_time = item["charttime"]
                    heart_rate = float(item["HR"])
                    respiratory_rate = float(item["RR"])
                    systolic_BP = float(item["SBP"])
                    temperature = float(item["TEMP"])
                    oxygen_sat = float(item["SPO2"])

                except (ValueError, TypeError):
                    print("Invalid numeric data!")
                    malformed_observations += 1
                    continue

                except KeyError as error:
                    print("Key doesn't exist!", error)
                    malformed_observations += 1
                    continue

                is_valid = validation.validate_vitals(
                    heart_rate, respiratory_rate, systolic_BP, temperature, oxygen_sat)

                risk_score = ""
                risk_level = "Invalid"

                has_elderly_age = False
                has_high_heart_rate = False
                has_high_resp_rate = False
                has_low_systolic_bp = False
                has_fever = False
                has_low_oxygen = False

                if is_valid:

                    (
                        risk_score,
                        has_elderly_age,
                        has_high_heart_rate,
                        has_high_resp_rate,
                        has_low_systolic_bp,
                        has_fever,
                        has_low_oxygen

                    ) = calculate_risk(
                        age,
                        heart_rate,
                        respiratory_rate,
                        systolic_BP,
                        temperature,
                        oxygen_sat

                    )

                    risk_level = classify_risk(risk_score)

                    valid_observations += 1

                    if risk_level == "High risk":
                        high_risk += 1
                        high_risk_admissions.add(hospital_adm_id)

                    elif risk_level == "Moderate risk":
                        moderate_risk += 1

                    else:
                        low_risk += 1

                else:
                    print("Invalid data, cannot calculate risk score and level!")
                    invalid_observations += 1

                writer.writerow({
                    "hadm_id": hospital_adm_id,
                    "charttime": chart_time,
                    "age": age,
                    "sex": gender,
                    "HR": heart_rate,
                    "RR": respiratory_rate,
                    "SBP": systolic_BP,
                    "TEMP": temperature,
                    "SPO2": oxygen_sat,
                    "valid_data": is_valid,
                    "fever": has_fever,
                    "low_oxygen": has_low_oxygen,
                    "high_heart_rate": has_high_heart_rate,
                    "high_respiratory_rate": has_high_resp_rate,
                    "low_systolic_bp": has_low_systolic_bp,
                    "risk_score": risk_score,
                    "risk_level": risk_level
                })


except FileNotFoundError:
    print("Required data file not found!")
    raise

print()
print("Total ovservations:", total_observations)
print("Valid observations:", valid_observations)
print("Invalid observations:", invalid_observations)
print("Malformed observations:", malformed_observations)
print("High risk:", high_risk)
print("Moderate risk:", moderate_risk)
print("Low risk:", low_risk)

print("Admissions who had high risk:", high_risk_admissions)
print("Number of admissions with high risk:", len(high_risk_admissions))


# Dumping a screening_summary json
summary = {
    'dataset': {
        "total_observations": total_observations,
        "valid_observations": valid_observations,
        "invalid_observations": invalid_observations,
        "Malformed observations:": malformed_observations

    },
    "risk_distribution": {
        "low": low_risk,
        "moderate": moderate_risk,
        "high": high_risk
    },
    "admissions": {
        "admissions_with_high_risk_observations": len(high_risk_admissions)
    }
}


with open("screening_summary.json", "w") as file:
    json.dump(summary, file, indent=4)
