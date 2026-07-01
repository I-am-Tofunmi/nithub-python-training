# Strings to Integers
def convert_add(list_of_strings):
  list = []
  for x in list_of_strings:
    x = int(x)
    list.append(x)
  return sum(list)


print(convert_add(["1", "3", "5"]))