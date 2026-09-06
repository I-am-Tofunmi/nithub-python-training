# Words and Elements

# count_words
def count_words(string_of_words):
    return len(string_of_words.split())

result = count_words("I love learning")
print(result)

# count_elements

def count_elements(words):
    result_words = words.replace(" ", "")
    return len(result_words)

output = count_elements("I love learning")
print(output)