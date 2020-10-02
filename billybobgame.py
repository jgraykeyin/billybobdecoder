# Decodertron will grab a random sentence from the collection and prompt
# the user to decode it. Getting one correct will end the game but eventually
# I'd like to loop over to the next sentence and increment a score for each correct answer.
# TODO: Input validation
# TODO: Put the decodertron into a function
# TODO: Add a score system
# TODO: Loop to next prompt after a correct answer

import os
import random

collection = ["Billy Bob rules the world!",
            "The secret codes are hidden inside Area 51",
            "Mcdonalds coffee is better than Tim Hortons coffee",
            "Billy Bob has kidnapped Nicholas Cage and demands one million dollars",
            "Billy Bob is going to have The Office removed from all streaming services by Monday afternoon"
            ]

# Generate a random number that's within the limits of 0 and length of collection
# This will let us grab a random sentence from the list
x = random.randint(0,len(collection)-1)
codeWords = collection[x]

# Setup a list of letters to blank out
# Maybe this list can grow to make the questions more difficult
alpha = ["a","e","i","o","u","y"]

# Replace chosen characters with *
for i in alpha:
    codeWords = codeWords.replace(i,"*")

# Setup any pre-loop variables that should be initialized
sorryMessage = ""
tries = 3

# Start the game loop! End it if the tries go below 1 or "0" is typed
while tries > 0:
    os.system('clear')
    print("Billy Bob Decodertron 1.0")
    print("(Enter 0 to quit)\n")

    if sorryMessage:
        print(sorryMessage)

    print("You have {} tries left!\n".format(tries))
    print("{} \n".format(codeWords))
    guess = input("Decode this sentence: ")

    if guess == "0":
        break

    if guess.upper() == collection[x].upper():
        print("You got it!")
        break
    else:
        sorryMessage = "Sorry, that's wrong."
        tries = tries - 1

if guess == "0":
    print("You've given up, Billy Bob laughs at you!")
elif tries < 1:
    print("\nYou were unable to decode Billy Bob's message, oh no!")
    print("Game Over!")
elif tries > 0:
    print("\nYou decoded Billy Bob's secret message, way to go!")
    print("A winner is you!")