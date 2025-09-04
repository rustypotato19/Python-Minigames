import random
from os import system

def rock_paper_scissors():
    system("cls")
    
    options = [
        "rock",
        "paper",
        "scissors"
    ]
    
    combinations = {
        "rock-paper": False,
        "rock-scissors": True,
        "paper-rock": True,
        "paper-scissors": False,
        "scissors-paper": True,
        "scissors-rock": False,
    }
    
    random.seed()
    cpu_option = options[random.randrange(0,2)]
    
    print("Welcome to rock, paper, scissors!")
    
    choice = input("Enter you choice: ").lower()
    while cpu_option == choice:
        print("Draw!")
        
        random.seed()
        cpu_option = options[random.randrange(0,2)]
        
        choice = input("Enter you choice: ").lower()
    
    result = f"{cpu_option}-{choice}"
    print(f"Computer: {cpu_option}\nYou Chose: {choice}")
    if combinations[result]:
        print("You lose!")
    else:
        print("You win!")

rock_paper_scissors()