import json
from difflib import get_close_matches

data = json.load(open('files/data.json'))

def translate(word):
        word = word.lower()
        
        if word in data:
            return data[word]
        elif len(get_close_matches(word, data.keys())) > 0:
            YN = input('is %s what you meant to enter? Enter Y if yes, or N if no:' % get_close_matches(word, data.keys())[0])
            if YN == 'Y':
                return data[get_close_matches(word, data.keys())[0]]
            elif YN == 'N':
                return 'please try another word'
            else: 
                return 'Incorrect Input'
        else:
            return 'Word does not exist'

words = input('Enter a Word: ')

output = (translate(words))

if type(output) == list:
    for item in output:
        print(item)
else:
    print (output)