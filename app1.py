import json
from difflib import get_close_matches

data = json.load(open("../Application2/data.json"))


def returnMeaning(w):
    w = w.lower()
    wupper = w.upper()
    wcapital = w.capitalize()
    if w in data:
        return data[w]
    elif wcapital in data:
        return data[wcapital]
    elif wupper in data:
        return data[wupper]
    elif len(get_close_matches(w, data.keys())) > 0:
        yn = input(
            "Did you mean {} instead? Enter Y if yes, or N if no:".format(get_close_matches(w, data.keys())[0]))
        if yn == "Y":
            return data[get_close_matches(w, data.keys())[0]]
        elif yn == "N":
            return "The word doesn't exist. Please double check it."
        else:
            return "We didn't understand your entry."

    else:
        return "The word doesn't exist. Please double check it."


print("Enter the word: ")
word = input()

output = returnMeaning(word)

if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)
