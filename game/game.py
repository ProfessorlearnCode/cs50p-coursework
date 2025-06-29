

import random
import sys

computerguess = random.randint(1,100)
while True:
        try:
            level = int(input("Level: "))
        except ValueError:
            continue
        while True:
            try:
                guess = int(input("guess: "))
            except ValueError:
                continue
            if guess > computerguess:
                print("Too large!")
                continue
            elif guess < computerguess:
                print("Too small!")
            elif guess == computerguess:
                print("Just right!")
                sys.exit()
            elif guess == None:
                continue
        