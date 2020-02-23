import json

data = json.load(open("data.json"))

def translate(word):
    if word in data:
        return data[word]
    else:
        return "The word doesn't exist. Please double check it."


input_word = input("Enter word:")
print(translate(input_word))