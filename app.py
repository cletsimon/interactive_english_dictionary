import json

data = json.load(open("data.json"))

def translate(word):
    return data[word]


print(translate("rain"))