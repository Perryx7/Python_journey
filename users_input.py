import random
import sys
from enum import Enum

class RPS (Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3

print(" ")#to print something to a user
playerchoice = input(
    "Enter ....\n1 for Rock, \n2 for paper, or \n3 for scissors:\n\n")#to take input from a user

player = int(playerchoice)#convert a string to an integer 

if player < 1 or player > 3 :
    sys.exit("Choose a number between 1 , 2 and 3")

computerchoice = random.choice("123")

computer = int(computerchoice)

print(" ")
print("you chose" + str(RPS(player)).replace('RPS.' , "") + ".")
print("computer" + str(RPS(computer)).replace('RPS.' , "") + ".")

if player == computer : 
    sys.exit("it isa tie")

if (player == 1 and computer == 3) or (player == 2 and computer ==1) or (player == 3 and computer == 2):

    print("you won")
else: print('computer won') 
