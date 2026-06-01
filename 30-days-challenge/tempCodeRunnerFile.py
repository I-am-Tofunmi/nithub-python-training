list_of_strings = input("Enter the list of strings: ").split()
def convert_add(list_of_strings):
    list = []
    for x in list_of_strings:
        x = int(x)
        list.append(x)
    return sum(list)
result = convert_add(list_of_strings)
print(result)