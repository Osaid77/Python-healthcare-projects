1. Project title:
Outpatient Vital Signs Risk Flagger

2. One-sentence summary:
A Python healthcare screening prototype that validates outpatient vital signs and flags patients for urgent review using simple rule-based logic.

3. Use case:
outpatient triage & clinic intake screening

4. Features:
- stores patient demographic and vital-sign data
- validates input ranges
- derives fever / oxygen / heart-rate flags
- calculates a simple risk score
- determines whether urgent review is needed

5. Technologies / concepts used:
- Python
- variables and data types
- conditionals
- boolean logic
- input validation
- rule-based scoring

6. Example input/output:
Patient aged 30 with high temperature of 38.5, low O2 saturation of 94, normal heart rate of 90, has no diabetes,
only has 2 flags which are temperature and O2 saturation, this gives him/her risk score of 2. 

7. Real-world healthcare relevance:
A program like this helps so much in triage where patients must be categorized into high risk and emergency and low risk

8. Limitations:
Hardcoded one patient data. In real practice, healthcare professionals input many patients data. This is a prototype or a tool that can be used as a foundation or a part of a bigger system like an EHR. 

9. Real-world healthcare impact:
This project demonstrates how basic patient data can be transformed into a screening logic. In real healthcare practice, similar rule-based systems support triage and intake workflow by highlighting abnormal vital signs before a clinician review.