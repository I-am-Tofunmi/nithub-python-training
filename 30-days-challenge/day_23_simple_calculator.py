# Simple Calculator
def add(a, b):
    return a + b

def subtract(a, b):
    result = a - b
    return result

def divide(a, b):
    result = a / b
    return result

def multiply(a, b):
    result = a * b
    return result

print("==== PANDA SIMPLE CALCULATOR ====")
print("1 - Addition")
print("2 - Subtraction")
print("3 - Division")
print("4 - Multiply")
print("Enter the value and number for specific operation")
try:
    a = float(input("Enter your value of a: "))
    b = float(input("Enter the value of b: "))
    number_of_selection = int(input("Enter the number for specific operation: "))

    if number_of_selection == 1:
        result = add(a, b)

    elif number_of_selection == 2:
        result = subtract(a, b)

    elif number_of_selection == 3:
        result = divide(a, b)

    elif number_of_selection == 4:
        result = multiply(a, b)

    print(result)

except ValueError:
    print("This is an invalid value.")
except ZeroDivisionError:
    print("This is a zero division error.")
except NameError:
    print("This is an invalid name.")