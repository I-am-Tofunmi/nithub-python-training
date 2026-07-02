# Odd and Even
list_of_numbers = input("Enter a list of numbers: ")
def odd_and_even(list_of_numbers):
    list_of_numbers = list_of_numbers.strip("[, ]")
    x = list_of_numbers.split(",")
    odd = []
    even = []
    for num in x:
        num = int(num)
        if num % 2 == 0:
            even.append(num)
        else:
            odd.append(num)
    return int(max(even) - min(odd)) if even and odd else "No valid odd or even numbers found."

print(odd_and_even(list_of_numbers))