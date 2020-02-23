import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def translate(word):
    w = word.lower()
    if w in data:
        return data[w]
    elif w.title() in data: #if user entered "delhi" this will check for "Delhi" as well.
        return data[w.title()]
    elif len(get_close_matches(w, data.keys(), cutoff=0.8)) > 0:
        yn = input("Did you mean '%s' instead? \nEnter Y if yes, or N if no: " % get_close_matches(w, data.keys(), cutoff=0.8)[0])
        if yn == "Y":
            return data[get_close_matches(w, data.keys(), cutoff=0.8)[0]]
        elif yn == "N":
            return "The word doesn't exist. Please double check it."
        else:
            return "We didn't understand your entry."
    else:
        return "The word doesn't exist. Please double check it."


word = input("Enter word: ")
output = translate(word)
if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)