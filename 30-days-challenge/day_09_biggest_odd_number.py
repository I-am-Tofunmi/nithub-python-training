# Biggest Odd Number
def biggest_odd(string_of_numbers):
    odd_numbers = []
    # for x in string_of_numbers:
    #     x = int(x)
    #     if x % 2 == 1:
    #         odd_numbers.append(x)

    # List Comprehension
    # [expression for item in iterable if condition]
    odd_numbers = [int(x) for x in string_of_numbers if int(x) % 2 == 1]
    return max(odd_numbers) if odd_numbers else None

print(biggest_odd('23569'))