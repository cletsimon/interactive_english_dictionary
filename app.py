import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def translate(word):
    w = word.lower()
    if w in data:
        return "\n".join(data[w])
    elif len(get_close_matches(w, data.keys(), cutoff=0.8)) > 0:
        yn = input("Did you mean '%s' instead? \nEnter Y if yes, or N if no: " % get_close_matches(w, data.keys(), cutoff=0.8)[0])
        if yn == "Y":
            return "\n".join(data[get_close_matches(w, data.keys(), cutoff=0.8)[0]])
        elif yn == "N":
            return "The word doesn't exist. Please double check it."
        else:
            return "We didn't understand your entry."
    else:
        return "The word doesn't exist. Please double check it."


input_word = input("Enter word:")
output = translate(input_word)
print(output)