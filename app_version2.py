from difflib import get_close_matches

import mysql.connector

con = mysql.connector.connect(
user = "ardit700_student",
password = "ardit700_student",
host = "108.167.140.122",
database = "ardit700_pm1database"
)

def worddefinition(w):
    w = w.lower()
    wupper = w.upper()
    wcapital = w.capitalize()

    cursor = con.cursor()
    query = cursor.execute("select * from Dictionary where Expression = '{}'".format(word))
    results = cursor.fetchall()

    return results

    # if w in results:
    #     return results
    # elif wcapital in results:
    #     return results
    # elif wupper in results:
    #     return results
    # elif len(get_close_matches(w, results)) > 0:
    #     yn = input(
    #         "Did you mean {} instead? Enter Y if yes, or N if no:".format(get_close_matches(w, results)[0]))
    #     if yn == "Y":
    #         return results
    #     elif yn == "N":
    #         return "The word doesn't exist. Please double check it."
    #     else:
    #         return "We didn't understand your entry."

    # else:
    #     return "The word doesn't exist. Please double check it."


print("Enter a word: ")
word = input()

output = worddefinition(word)

for result in output:
    print(result[1])
