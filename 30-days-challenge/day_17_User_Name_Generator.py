# User Name Generator
import random
def user_name():
    name = input("Enter your name: ")
    reversed_name = name[::-1]
    number = random.randint(0, 9)
    number = str(number)
    result = reversed_name + number
    return f"Your username is {result}"

print(user_name())