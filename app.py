import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def getWord(word):
    if word in data:
        return data[word]
    elif len(get_close_matches(word, data.keys())) > 0:
        yn = input("Did you mean {} instead? Enter Y if yes, or N if no: ".format(get_close_matches(word, data.keys())[0])).lower()
        if yn == 'y':
            return data[get_close_matches(word, data.keys())[0]]
        elif yn == 'n':
            return "The word you passed me: {} is not in this dictionary".format(word)
        else:
            return "Error, you didn't pass in Y or N, i don't understand: {}".format(yn)
    else:
        return "The word you passed me: {} is not in this dictionary".format(word)
    





print("Hello, welcome to my dictionary program!")

while True:
    print("Instructions: Enter a word or type exit to close the program:")
    userInput = input("Input: ").lower()
    if userInput == 'exit':
        break
    output = getWord(userInput)
    if type(output) == list:
        for item in output:
            print(item)
        print("\n")
    else:
        print(output)
        print("\n")