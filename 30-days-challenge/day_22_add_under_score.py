# Add Under_Score
def add_hash(string):
    result = string.replace(" ", "#")
    return result

output = add_hash("Hello Tofunmi World")    
print(output)

def add_underscore(output):
    result_2 = output.replace("#","_")
    return result_2

output_2 = add_underscore(output)
print(output_2)

def remove_underscore(output_2):
    result_3 = output_2.replace("_", "")
    return result_3

output_3 = remove_underscore(output_2)
print(output_3)
print(remove_underscore(add_underscore(add_hash("Python"))))