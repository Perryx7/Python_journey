import random
import sys
from enum import Enum

def rps() :
  game_count = 0
  player_wins = 0
  python_wins = 0

  def play_rps():
        
        nonlocal player_wins
        nonlocal python_wins
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

        def decide_winner(player, computer) :
            nonlocal player_wins
            nonlocal python_wins
            if player == computer:
              return "it is a tie"

            if (player == 1 and computer == 3) or \
                (player == 2 and computer == 1) or \
                (player == 3 and computer == 2):
                player_wins += 1
                return "You won"
            else:
                python_wins += 1
                return "Computer won"
            
        game_result = decide_winner(player,computer)

        print(game_result)

        nonlocal game_count
        game_count += 1

        print("\n Game count: " + str(game_count))
        print("\n player wins: " + str(player_wins))
        print("\n python wins: " + str(python_wins))
        print("play again ? ")

        while True:
            playagain = input("\nPlay again? Y/N: ")
            if playagain.lower() == "y":
                return play_rps()
            elif playagain.lower() == "n":
                print("Thank you")
                sys.exit("Bye")
            else:
                print("Invalid input, enter Y or N")

  return play_rps



    # Start the game

play = rps()
play ()
