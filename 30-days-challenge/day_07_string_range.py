# String Range
def string_range():
    end = int(input("Enter the end string: "))
    list = []
    for x in range(end):
        list.append(x)
    results = ".".join(str(x) for x in list)
    return results

solution = string_range()
print(solution)

