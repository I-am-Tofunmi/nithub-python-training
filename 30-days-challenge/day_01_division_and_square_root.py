# Division and Square Root
number = int(input("Enter a number: "))

def divide_or_square(number):
    if number % 5 == 0:
        sq_root = number ** 0.5
        return sq_root
    else:
        remainder = number % 5
        return remainder

result = divide_or_square(number)
print("{:.2f}".format(result))