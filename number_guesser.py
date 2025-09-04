from os import system
import random

def higher_lower():
    system("cls")
    
    random.seed()
    target = random.randrange(1,100)
    
    guesses = 0
    print("I'm thinking of a number between 1 and 100.. I'll give you 5 guesses")
    guess = int(input(f"Guess [{guesses+1}/5]: "))
    guesses += 1
    while guess != target and guesses < 5:
        if guess < target:
            guess = int(input(f"\rIncorrect, too low!. Guess [{guesses+1}/5]: "))
        else:
            guess = int(input(f"\rIncorrect, too high!. Guess [{guesses+1}/5]: "))
        guesses += 1
    if guesses == 5:
        print(f"\rUnlucky! The number was {target}")
    else:
        print(f"\rYou got it! The number was {target}")