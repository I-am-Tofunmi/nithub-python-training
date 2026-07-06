# Flatten the List 
def flat_list(nested_list):
    flat = []
    for item in nested_list:
        for x in item:
            flat.append(x)
    return flat

print(flat_list([[2, 4], [5, 6]]))

# Extra Challenge: Teacher's Salary

def your_salary(teacher_name, number_of_periods, rate_per_period):
    if number_of_periods > 100:
        regular_period = 100
        current_period = number_of_periods - 100
        gross_salary = (regular_period * 20) + (current_period * rate_per_period)
    else:
        gross_salary = number_of_periods * rate_per_period
    return f"Teacher: {teacher_name},\nPeriods: {number_of_periods}\nGross Salary: ${gross_salary:,}"

print(your_salary("John Kelly", 105, 25))