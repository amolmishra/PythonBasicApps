import json
from difflib import get_close_matches

def translate(word) :
    return data[word]
result = None
data = json.load(open("data.json"))
word = input("Enter a word: ")

if word in data:
    result = data[word]
elif len(get_close_matches(word, data.keys())) > 0 :
    yn = input("Did you mean {} , Enter Y for yes, N for no: ".format(get_close_matches(word, data.keys())[0]))
    if(yn == 'Y'):
        result = data[get_close_matches(word, data.keys())[0]]
    else :
        result = "No word or close matches found. Please try again!"
else:
    result = "The meaning not found for the given word. Please check the spelling again."

if type(result) is list:
    for line in result:
        print(line)
