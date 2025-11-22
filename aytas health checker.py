import sys

# --- Calculation Functions ---

def calculate_bmi(weight_kg, height_cm):
    """Calculates Body Mass Index (BMI)."""
    if height_cm <= 0:
        return 0
    # Convert height from cm to meters
    height_m = height_cm / 100
    # Formula: weight (kg) / height (m)^2
    bmi = weight_kg / (height_m ** 2)
    return round(bmi, 2)

def interpret_bmi(bmi):
    """Provides a health category for the calculated BMI."""
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Healthy Weight"
    elif 25.0 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obese"

def calculate_bmr(weight_kg, height_cm, age_yrs, gender):
    """Calculates Basal Metabolic Rate (BMR) using the Mifflin-St Jeor formula."""
    
    # Formula components: (10 * W) + (6.25 * H) - (5 * A) 
    base = (10 * weight_kg) + (6.25 * height_cm) - (5 * age_yrs)
    
    # Adjust based on gender
    if gender.lower() == 'male':
        bmr = base + 5
    elif gender.lower() == 'female':
        bmr = base - 161
    else:
        # Default if gender is invalid (though input validation should prevent this)
        bmr = base 
        
    return round(bmr)

def calculate_tdee(bmr, activity_level):
    """
    Calculates Total Daily Energy Expenditure (TDEE) based on BMR and 
    an activity multiplier.
    """
    # Activity multipliers: Moderately Active (1.55) is typical gym-goer, 
    # Very Active (1.725) is typical athlete.
    activity_factors = {
        'sedentary': 1.2, 
        'lightly active': 1.375, 
        'moderately active': 1.55, 
        'very active': 1.725,      
        'extra active': 1.9
    }
    
    factor = activity_factors.get(activity_level.lower(), 1.2)
    
    # TDEE = BMR * Activity Factor
    tdee = bmr * factor
    return round(tdee)

# --- Input Function ---

def get_user_data():
    """Prompts the user for all necessary health and activity data."""
    print("--- Fitness Metric Calculator ---")
    
    # Get Weight
    while True:
        try:
            weight = float(input("Enter your weight in kilograms (kg): "))
            if weight <= 0: raise ValueError
            break
        except ValueError:
            print("Invalid input. Please enter a positive number for weight.")

    # Get Height
    while True:
        try:
            height = float(input("Enter your height in centimeters (cm): "))
            if height <= 0: raise ValueError
            break
        except ValueError:
            print("Invalid input. Please enter a positive number for height.")
            
    # Get Age
    while True:
        try:
            age = int(input("Enter your age in years: "))
            if age <= 0: raise ValueError
            break
        except ValueError:
            print("Invalid input. Please enter a positive integer for age.")
            
    # Get Gender
    while True:
        gender = input("Enter your gender (Male/Female): ").strip().lower()
        if gender in ['male', 'female']:
            break
        else:
            print("Invalid input. Please enter 'Male' or 'Female'.")
            
    # Get Activity Level
    print("\nSelect your Activity Level:")
    print("  [1] Sedentary (little or no exercise)")
    print("  [2] Lightly Active (light exercise 1-3 days/week)")
    print("  [3] Moderately Active (3-5 days/week - Gym-goer)")
    print("  [4] Very Active (6-7 days/week - Athlete)")
    print("  [5] Extra Active (hard exercise + physical job)")
    
    activity_levels = {
        '1': 'sedentary', '2': 'lightly active', '3': 'moderately active',
        '4': 'very active', '5': 'extra active'
    }
    
    while True:
        choice = input("Enter the number corresponding to your activity level: ").strip()
        if choice in activity_levels:
            activity = activity_levels[choice]
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 5.")
            
    return {
        'weight_kg': weight,
        'height_cm': height,
        'age_yrs': age,
        'gender': gender,
        'activity_level': activity
    }

# --- Main Execution and Display ---

def display_results(data):
    """
    Calculates all metrics using the provided user data and prints a formatted report.
    """
    
    # 1. Calculate Core Health Metrics
    bmi = calculate_bmi(data['weight_kg'], data['height_cm'])
    bmi_status = interpret_bmi(bmi)
    
    bmr = calculate_bmr(
        data['weight_kg'], 
        data['height_cm'], 
        data['age_yrs'], 
        data['gender']
    )
    
    # 2. Calculate Calorie Needs
    tdee = calculate_tdee(bmr, data['activity_level'])
    
    # 3. Calculate Goals
    # Simple recommendation for weight management
    loss_cal = tdee - 500
    gain_cal = tdee + 500
    
    # --- Output Report ---
    print("\n" + "="*50)
    print("🏋️  HEALTH & CALORIE REPORT FOR ATHLETES/GYM-GOERS 📈")
    print("="*50)
    
    print(f"Gender: {data['gender'].capitalize()} | Age: {data['age_yrs']} years")
    print(f"Weight: {data['weight_kg']} kg | Height: {data['height_cm']} cm")
    print(f"Activity Level: {data['activity_level'].title()}")
    print("-" * 50)
    
    # BMI Section
    print(f"** Body Mass Index (BMI): {bmi} **")
    print(f"   Status: {bmi_status}")
    
    # BMR Section
    print(f"\n** Basal Metabolic Rate (BMR): {bmr} Calories/day **")
    print("   (Energy your body needs at rest)")
    
    # TDEE Section (Maintenance Calories)
    print(f"\n** Total Daily Energy Expenditure (TDEE): {tdee} Calories/day **")
    print("   (Maintenance calories to stay at current weight)")
    
    # Goal Section (Critical for Gym-goers/Athletes)
    print("\n--- Recommended Daily Calorie Goals ---")
    print(f"🔥 For **Fat Loss** (Approx 0.5 kg/week deficit): {loss_cal} Calories/day")
    print(f"💪 For **Muscle Gain/Weight Gain** (Approx 0.5 kg/week surplus): {gain_cal} Calories/day")
    
    print("="*50)


if __name__ == "__main__":
    try:
        # 1. Get user inputs
        user_data = get_user_data()
        
        # 2. Display the final results and recommendations
        display_results(user_data)
        
    except KeyboardInterrupt:
        print("\nProgram interrupted. Exiting.")
        sys.exit(0)
    except Exception as e:
        print(f"\nAn unexpected error occurred: {e}")