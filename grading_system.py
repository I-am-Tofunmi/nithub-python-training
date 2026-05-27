score = int(input("Enter student score (0 - 100): "))

if score < 0 or score > 100:
    print("Invalid score. Please enter a value between 0 and 100.")
elif score >= 70:
    print("Grade: A - Excellent")
elif score >= 60:
    print("Grade: B - Very Good")
elif score >= 50:
    print("Grade: C - Good")
elif score >= 45:
    print("Grade: D - Below Average")
elif score >= 40:
    print("Grade: E - Poor")
else:
    print("Grade: F - Fail")