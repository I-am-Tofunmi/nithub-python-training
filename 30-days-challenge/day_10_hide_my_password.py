# Hide my Password
def hide_password():
    password = input("Enter your password: ")
    count = len(password)
    hidden_password = count * '*'
    print(f"Your password is {count} characters long.")
    return hidden_password

print(hide_password())

# Extra Challenge: Strings With a Thousand Seperator
def convert_numbers():
    list_of_numbers =  [1000000, 2356989, 2354672, 9878098]
    list = []
    for x in list_of_numbers:
        number = (f"{x:,}")
        list.append(number)
    return list

print(convert_numbers())