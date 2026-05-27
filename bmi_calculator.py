weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in m: "))

def bmi_calculator(weight, height):
    height_sq = height ** 2
    bmi_value = weight / height_sq
    return bmi_value

bmi_value = bmi_calculator(weight, height)
print("Your BMI is: {:.2f}".format(bmi_value))