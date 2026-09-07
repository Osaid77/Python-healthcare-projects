import json


# Configure validation and thresholds

def load_config():
    try:
        with open("risk_config.json", "r") as file:
            return json.load(file)

    except json.JSONDecodeError:
        print("Invalid json file configuration!")
        raise

    except FileNotFoundError:
        print("File not found!")
        raise


config = load_config()
try:

# Thresholds
    fever_threshold = config["thresholds"]["fever"]
    low_oxygen_threshold = config["thresholds"]["low_oxygen"]
    high_heart_rate_threshold = config["thresholds"]["high_heart_rate"]
    high_resp_rate_threshold = config["thresholds"]["high_respiratory_rate"]
    low_systolic_bp_threshold = config["thresholds"]["low_systolic_bp"]
    older_age_threshold = config["thresholds"]["older_age"]

# Valid ranges
    min_temp = config["valid_ranges"]["temperature_min"]
    max_temp = config["valid_ranges"]["temperature_max"]
    min_oxygen = config["valid_ranges"]["oxygen_min"]
    max_oxygen = config["valid_ranges"]["oxygen_max"]
    min_heart_rate = config["valid_ranges"]["heart_rate_min"]
    max_heart_rate = config["valid_ranges"]["heart_rate_max"]
    min_resp_rate = config["valid_ranges"]["respiratory_rate_min"]
    max_resp_rate = config["valid_ranges"]["respiratory_rate_max"]
    min_systolic_bp = config["valid_ranges"]["systolic_bp_min"]
    max_systolic_bp = config["valid_ranges"]["systolic_bp_max"]

except KeyError as error:
    print("Key doesn't exist!", error)
    raise
