# This program checks if a person is eligible to vote based on their age, citizenship, and registration status.
age = int(input("Enter your age: "))
citizenship = input("Are you a citizen? (yes/no): ").strip().lower()
registered = input("Are you registered to vote? (yes/no): ").strip().lower()

eligible = True

if 0 <= age < 18:
    print("You are not eligible to vote because you are under 18.")
    eligible = False
elif age >= 120 or age < 0:
    print("Invalid age entered.")
    eligible = False

if citizenship != "yes":
    print("You are not eligible to vote because you are not a citizen.")
    eligible = False

if registered != "yes":
    print("You are not eligible to vote because you are not registered.")
    eligible = False

if eligible:
    print("You are eligible to vote.")