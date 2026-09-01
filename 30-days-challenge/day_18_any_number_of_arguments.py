# Any Number of Arguments
def any_number(*args):
    total = 0
    for number in args:
        total += number
    no_of_digit = len(args)
    average_of_number = total / no_of_digit
    return average_of_number

result = any_number(12, 90, 12, 34)
print(result)

