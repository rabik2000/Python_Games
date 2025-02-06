import random
import sys

def game(user_choice, comp_choice):
     print("Computer Choice:", comp_choice)
     if user_choice == comp_choice:
        print("It's a draw")
     elif (user_choice == "rock" and comp_choice == "scissor") or \
         (user_choice == "scissor" and comp_choice == "paper") or \
         (user_choice == "paper" and comp_choice == "rock"):
        print("You win")
     else:
        print("You Lose!")





print("Welcome to the game of rock, paper, scissor\n")
user_choice = str(input("Enter your option exactly as shown above: \n"))
options = ["rock", "paper", "scissor"]
comp_choice = random.choice(options)


if user_choice not in options:
     print("Please follow the instructions properly!")
     sys.exit()
else:
     game(user_choice, comp_choice)


