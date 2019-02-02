import urllib.request
import json
from pprint import pprint

# Print intro, initialise points variable, etc here
print("Type 'exit' to end game at any time.")

while True:
    # Get question each time the game is played
    # Would be better to get multiple at a time but whatever
    json_raw = urllib.request.urlopen("https://opentdb.com/api.php?amount=1")
    data = json.load(json_raw)
    pprint(data) # Just to see what JSON looks like, delete this later
    try:
        if data['response_code'] != 0:
            input("Bad response from api. Press enter to try again...")
            continue # Go back to top of while loop
        result = data['results'][0] # Get first (and only) question

        # Question should really be a class. But lets keep it simple for now.
        category = result['category']
        correct_answer = result['correct_answer']
        difficulty = result['difficulty']
        incorrect_answers = result['incorrect_answers'] # Careful: this is a list
        question = result['question']
        type = result['type'] # either 'boolean' or 'multiple'
    except:
        input("Bad response from api. Press enter to try again...")
        continue # Go back to top of while loop

    # For testing only delete these later
    print('Category:',category)
    print(question)
    print(correct_answer)
    print(incorrect_answers)
    print('Difficulty:', difficulty)
    print('Type:', type)
    # Testing ^

    # print out question, include Category and Difficulty here

    # print out options here, remember to shuffle options if multiple choice

    # get user input, check if 'exit' typed
    user_input = input('What is the correct answer? ')
    if user_input.lower() == 'exit':
        break # leave while loop

    # check if answer right or wrong here, add points appropriately
    # for bonus point, hard = 3, medium = 2, easy = 1 points

# this will run after the game, print final score and anything else here
