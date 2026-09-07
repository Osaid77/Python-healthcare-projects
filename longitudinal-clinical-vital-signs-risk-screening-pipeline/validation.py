from configurator import (min_heart_rate, max_heart_rate, min_resp_rate, max_resp_rate,
                          min_systolic_bp, max_systolic_bp, min_temp, max_temp, min_oxygen, max_oxygen)


def validate_vitals(heart_rate, respiratory_rate, systolic_BP, temperature, oxygen_sat):

    is_valid = True

    if not min_heart_rate <= heart_rate <= max_heart_rate:
        print("Invalid heart rate")
        is_valid = False

    if not min_resp_rate <= respiratory_rate <= max_resp_rate:
        print("Invalid respiratory rate")
        is_valid = False

    if not min_systolic_bp <= systolic_BP <= max_systolic_bp:
        print("Invalid systolic bp")
        is_valid = False

    if not min_temp <= temperature <= max_temp:
        print("Invalid temperature")
        is_valid = False

    if not min_oxygen <= oxygen_sat <= max_oxygen:
        print("Invalid oxygen saturation")
        is_valid = False

    return is_valid
