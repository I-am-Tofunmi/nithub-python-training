# List of Tuples


def make_tuples(list_a, list_b):
    Total_list = []
    for x, y in zip(list_a, list_b):
        list_of_tuples = x, y
        Total_list.append(list_of_tuples)
    return Total_list
    

output = make_tuples([1, 2, 3, 4], [5, 6, 7, 8])
print(output)
    