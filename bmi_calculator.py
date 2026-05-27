weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in m: "))

def bmi_calculator(weight, height):
    if height <= 0 or weight <= 0:
        print("Height and weight must be greater than zero.")
        return None
    
    height_sq = height ** 2
    bmi_value = weight / height_sq
    return bmi_value

bmi_value = bmi_calculator(weight, height)
if bmi_value is not None:
    print("Your BMI is: {:.2f}".format(bmi_value))
    if bmi_value < 18.5:
        print("You are underweight.")
    elif 18.5 <= bmi_value < 25:
        print("You have a normal weight.")
    elif 25 <= bmi_value < 30:
        print("You are overweight.")
    elif bmi_value >= 30:
        print("You are obese.")
