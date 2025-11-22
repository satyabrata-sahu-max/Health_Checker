🌟 Project Statement: aytas Health Checker 🌟

I. Executive Summary

The aytas Health Checker is a high-utility, command-line application developed in Python. It addresses the critical need among fitness enthusiasts, athletes, and trainers for data-driven nutritional planning. The tool translates raw biometric data (weight, height, age, gender) and activity level into actionable, precise metabolic and caloric metrics, moving users beyond generic recommendations to highly personalized goal setting.

II. Project Objectives & Deliverables

The primary objective of this project is to provide immediate, calculated metabolic insights essential for structured diet planning.

The single-file Python script delivers three core, indispensable metrics:

Body Mass Index (BMI): Assesses general health and weight classification for initial screening.

Basal Metabolic Rate (BMR): Calculates the minimum caloric requirement necessary to sustain life at rest (Mifflin-St Jeor Equation).

Total Daily Energy Expenditure (TDEE): Calculates the total calories burned daily, factoring in BMR and the user’s selected activity multiplier. This is the foundation of all subsequent caloric goals.

III. Actionable Goal Setting

A key feature of the aytas Health Checker is converting the theoretical TDEE into practical, daily caloric targets:

Goal Category

Caloric Adjustment

Rationale

Maintenance

TDEE

Maintain current weight/mass.

Fat Loss

TDEE - 500 calories

Creates a standard deficit for approximate 0.5 kg (1 lb) of weekly loss.

Muscle/Weight Gain

TDEE + 500 calories

Creates a standard surplus for approximate 0.5 kg (1 lb) of weekly gain.

IV. Technical Implementation

The project is built entirely on the Python 3.x ecosystem. It relies exclusively on standard, built-in libraries, guaranteeing zero dependency issues and maximum cross-platform compatibility. The command-line interface provides a robust, low-overhead solution for quick data acquisition and report generatio
