print("The system calculate the average calories of the user once they hit done.")
empty_list = []

def average_calories():
    while True:
        avg_calories = input("Enter your calories intake for any number of days: ")
        if avg_calories.lower() == "done":
            break
        else:
            result = float(avg_calories)
            empty_list.append(result)

    result = sum(empty_list) / len(empty_list)
    return result

print(average_calories())

