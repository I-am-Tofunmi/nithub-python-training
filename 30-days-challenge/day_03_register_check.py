# Register Check
register = {'Micheal':'yes', 'John':'no', 'Peter':'yes', 'Mary':'yes'}
def register_check(register):
    number = 0
    for key, value in register.items():
        if value == "yes":
            number += 1
        else:
            continue
    return number

print(register_check(register))