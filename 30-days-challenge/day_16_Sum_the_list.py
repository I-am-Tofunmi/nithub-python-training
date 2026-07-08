# Sum the list
def sum_list(nested_list):
    total = []
    for char in nested_list:
        for x in char:
            total.append(x)
    result = sum(total)
    return result

print(sum_list([[2, 4, 5, 6], [2, 3, 5, 6]]))