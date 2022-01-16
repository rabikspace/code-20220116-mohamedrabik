# code-20220116-mohamedrabik

Python BMI Calculator Offline Coding Challenge:

Problem Statement:
-------------------
1) Calculate the BMI (Body Mass Index) using FormUla 1, BMI Category and Health risk
from Table 1 of the person and add them as 3 new columns
2) Count the total number of overweight people using ranges in the column BMI Category
of Table 1, check this is consistent programmatically and add any other observations in
the documentation

Input data(JSON):
    [{"Gender": "Male", "HeightCm": 171, "WeightKg": 96 },
    { "Gender": "Male", "HeightCm": 161, "WeightKg": 85 },
    { "Gender": "Male", "HeightCm": 180, "WeightKg": 77 },
    { "Gender": "Female", "HeightCm": 166, "WeightKg": 62},
    {"Gender": "Female", "HeightCm": 150, "WeightKg": 70},
    {"Gender": "Female", "HeightCm": 167, "WeightKg": 82}]

BMI Formula:

  BMI(kg/m2) = mass(kg) / height(m)^2

The BMI (Body Mass Index) in (kg/m2) is equal to the weight in kilograms (kg) divided by your
height in meters squared (m)^2

For example,
  if you are 175cm (1.75m) in height and 75kg in weight, you can calculate your BMI as follows: 75kg / (1.75m²) = 24.49kg/m²

Table 1 - BMI Category and the Health Risk:
-------------------------------------------
BMI Category     -     BMI Range (kg/m^2)    -     Health risk <br />
-------------------------------------------------------------<br />
Underweight      -     18.4 and below       -     Malnutrition risk <br />
Normal weight    -     18.5 - 24.9          -     Low risk<br />
Overweight       -     25 - 29.9            -     Enhanced risk<br />
Moderately obese -     30 - 34.9            -     Medium risk<br />
Severely obese   -     35 - 39.9            -     High risk<br />
Very severely obese  - 40 and above         -      Very high risk<br />
