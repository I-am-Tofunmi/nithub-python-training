# User Name Generator
def user_name():
    email = input("Enter your email: ")
    character = email.split("@")
    user = character[0]
    return user

print(user_name())