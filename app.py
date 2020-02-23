import json

data = json.load(open("data.json"))

def translate(word):
    word_lower = word.lower()
    if word_lower in data:
        return data[word_lower]
    else:
        return "The word doesn't exist. Please double check it."


input_word = input("Enter word:")
print(translate(input_word))