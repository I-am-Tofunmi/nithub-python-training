# All The Same
# def all_the_same(a_list):
#     all_same = all(s == a_list[0] for s in a_list)
#     return all_same

# output = all_the_same(["Mary"])
# print(output)

def all_the_same(a_list):
    all_same = len(set(a_list)) <= 1
    return (all_same)

result = all_the_same(["Mary"])
print(result)