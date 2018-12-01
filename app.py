import json
import difflib #this library compares text
from difflib import get_close_matches
from difflib import SequenceMatcher

data = json.load(open("data.json"))

def translate(word):
    if word.lower() in data:  # returns value in data file #changes the word to lower case
        return data[word.lower()]
    elif word.title() in data:  # if user entered "texas" this will check for "Texas" as well.
        return data[word.title()] 
    elif word.upper() in data:  # if user entered "Texas" this will check for "TEXAS" as well.
        return data[word.upper()]  
    elif len(get_close_matches(word, data.keys())) > 0:
        yn = input("Did you mean %s instead, If yes input Y, if no input N " % get_close_matches(word, data.keys()) [0])
        if yn == "Y":
            return data[get_close_matches(word, data.keys())[0]]
        elif yn == "N":
            return "The word doesn't exist, please check again "
        else:
            return "Please check that your entry is correct"
    else:
        return "The word doesn't exist, please check again "

word = input("Enter your word: ")
output = translate(word)
if type(output) == list:
    for item in output:
        print(item)
else:
    print(output) #calls the defined translate function above
