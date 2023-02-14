# Import "random" module
import random

# Create a function to store the computer's choice
def get_computer_choice():
    list_rps = ["Rock", "Paper", "Scissors"]
    computer_choice = random.choice(list_rps)
    return computer_choice

# Create a functione to store the user's choice
def get_user_choice():
    user_choice = input("Select: ")
    return user_choice

# Create a function to define the logic of the game
def get_winner(computer_choice, user_choice):
    if computer_choice == user_choice:
        print("It is a tie!")
    if computer_choice == "Rock":
        if user_choice == "Scissors":
            print("You lost")
        else:
            print("You won!")
    elif computer_choice == "Paper":
        if user_choice == "Rock":
            print("You lost")
        else:
            print("You won!")
    elif computer_choice == "Scissors":
        if user_choice == "Paper":
            print("You lost")
        else:
            print("You won!")

# Create a function to simulate the game
def play():
    get_computer_choice()
    get_user_choice()
    get_winner()