# Same in Reverse
string = input("Enter a string: ")

def same_in_reverse(string):
    reverse_string = string[::-1]
    if string == reverse_string:
        return True
    else:
        return False
    
result = same_in_reverse(string)
print(f"The string {string} is the same in reverse: {result}")