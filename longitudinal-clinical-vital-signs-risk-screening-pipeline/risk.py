from configurator import (older_age_threshold, high_heart_rate_threshold, high_resp_rate_threshold,
                          low_systolic_bp_threshold, fever_threshold, low_oxygen_threshold)


def calculate_risk(age, heart_rate, respiratory_rate, systolic_BP, temperature, oxygen_sat):

    risk_score = 0
    has_elderly_age = False
    has_high_heart_rate = False
    has_high_resp_rate = False
    has_low_systolic_bp = False
    has_fever = False
    has_low_oxygen = False

    if age >= older_age_threshold:
        has_elderly_age = True
        risk_score += 1

    if heart_rate >= high_heart_rate_threshold:
        has_high_heart_rate = True
        risk_score += 1

    if respiratory_rate >= high_resp_rate_threshold:
        has_high_resp_rate = True
        risk_score += 1

    if systolic_BP <= low_systolic_bp_threshold:
        has_low_systolic_bp = True
        risk_score += 1

    if temperature >= fever_threshold:
        has_fever = True
        risk_score += 1

    if oxygen_sat <= low_oxygen_threshold:
        has_low_oxygen = True
        risk_score += 1

    return (risk_score, has_elderly_age, has_high_heart_rate, has_high_resp_rate, has_low_systolic_bp, has_fever, has_low_oxygen)


########


def classify_risk(risk_score):

    if risk_score >= 4:
        return "High risk"

    elif risk_score >= 2:
        return "Moderate risk"

    else:
        return "Low risk"
