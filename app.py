import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def translate(word):
    w = word.lower()
    if w in data:
        return data[w]
    elif len(get_close_matches(w, data.keys(), cutoff=0.8)) > 0:
        return "Did you mean '%s' instead?" % get_close_matches(w, data.keys(), cutoff=0.8)[0]
    else:
        return "The word doesn't exist. Please double check it."


input_word = input("Enter word:")
print(translate(input_word))