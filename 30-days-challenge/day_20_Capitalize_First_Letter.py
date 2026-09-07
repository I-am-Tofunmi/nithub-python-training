# Capitalize First Letter

def capitalize(words):
    sent = []
    list = words.split()
    for text in list:
        result = text.capitalize()
        sent.append(result)
    return " ".join(sent)


result = capitalize("i like learning")
print(result)