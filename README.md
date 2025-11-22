🩺 aytas Health Checker: Personal Fitness & Calorie Tracker

🚀 Overview

The aytas Health Checker is a simple yet powerful command-line utility built in Python . Designed specifically for gym-goers, athletes, and anyone serious about tracking their fitness, this tool provides personalized metabolic rates and precise daily calorie targets. It's your essential first step toward effective nutritional planning, whether your goal is fat loss, muscle gain, or maintenance.

✨ Key Features

The calculator determines your caloric needs based on standard fitness science:

Body Mass Index (BMI): Assesses general health classification (Underweight, Healthy, etc.).

Basal Metabolic Rate (BMR): Calculates the energy (calories) your body burns purely at rest.

Total Daily Energy Expenditure (TDEE): The most crucial metric. It adjusts your BMR based on your activity level to determine the total calories you burn per day.

Goal Calorie Targets: Automatically provides daily targets for Maintenance, Fat Loss (500-calorie deficit), and Muscle/Weight Gain (500-calorie surplus).

⚙️ Setup and Execution

1. Requirements

This project uses only core Python libraries. You only need a working installation of Python 3.x.

2. Run the Script

Save the project code (from health_checker.py) into a file named health_checker.py.

Open your terminal or command prompt.

Navigate to the directory containing the file and run:

python health_checker.py


The program will prompt you for your weight (kg), height (cm), age, gender, and activity level.

🧪 Metrics and Formulas

The calculator utilizes the following established industry standards for accuracy:

BMI (Body Mass Index):


$$BMI = \frac{\text{Weight (kg)}}{\text{Height (m)}^2}$$

BMR (Basal Metabolic Rate): Calculated using the highly reliable Mifflin-St Jeor Equation:

Men: $BMR = (10 \times W) + (6.25 \times H) - (5 \times A) + 5$

Women: $BMR = (10 \times W) + (6.25 \times H) - (5 \times A) - 161$
(Where $W$ = weight in kg, $H$ = height in cm, $A$ = age in years)

TDEE (Total Daily Energy Expenditure):


$$TDEE = BMR \times \text{Activity Factor}$$
