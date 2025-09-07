import random
import sys
from enum import Enum

def play_rps():
    class RPS(Enum):
        ROCK = 1
        PAPER = 2
        SCISSORS = 3

    
    print(" ")  # to print something to a user
    playerchoice = input(
        "Enter ....\n1 for Rock, \n2 for Paper, or \n3 for Scissors:\n\n"
    )  # to take input from a user

    if playerchoice not in ["1","2","3"] : 
        print("Choose a number between 1, 2 and 3")
        return play_rps()


    player = int(playerchoice)  # convert a string to an integer

    

    computerchoice = random.choice("123")
    computer = int(computerchoice)

    print(" ")
    print("You chose " + str(RPS(player)).replace("RPS.", "") + ".")
    print("Computer chose " + str(RPS(computer)).replace("RPS.", "") + ".")

    if player == computer:
        sys.exit("It is a tie")

    if (player == 1 and computer == 3) or \
        (player == 2 and computer == 1) or \
        (player == 3 and computer == 2):
        print("You won")
    else:
        print("Computer won")
    print("play again ? ")

    while True : 
        playagain = input("\nPlay again?\nY for yes or N for no\n\n")
        if playagain.lower not in ["y"] : 
            continue
        else:
            break
    if playagain.lower() == "y":
        return play_rps()
    else:
        print("\nThank you")
        sys.exit("Bye")



# Start the game
play_rps()
