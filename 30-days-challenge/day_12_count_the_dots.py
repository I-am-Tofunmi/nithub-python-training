# Count the Dots
string_seperated_dots = input("Enter a string with dots separated by spaces: ")
def count_dots(string_seperated_dots):
    return string_seperated_dots.count(".")

print(count_dots(string_seperated_dots))

# Extra Challenge: Your age in Minutes
year_of_birth = input("Enter your year of birth: ")
while not year_of_birth.isdigit() or int(year_of_birth) < 1900 or int(year_of_birth) > 2026:
    year_of_birth = input("Please enter a valid year of birth (between 1900 and 2600): ")

def age_in_minutes(year_of_birth):
    current_age = 2026 - int(year_of_birth)
    return (f"You are {current_age * 365 * 24 * 60} minutes old.")

print(age_in_minutes(year_of_birth))