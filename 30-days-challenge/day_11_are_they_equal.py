# Are they Equal?
string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")

def equal_strings(string1, string2):
    result1 = []
    result2 = []
    for char in string1:
        result1.append(char)
        result1.sort()
    for char2 in string2:
        result2.append(char2)
        result2.sort()
    if result1 == result2:
        return True
    else:
        return False
    
print(equal_strings(string1, string2))
