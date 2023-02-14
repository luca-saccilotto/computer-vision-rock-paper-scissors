import random

def get_computer_choice():
    list_rps = ["Rock", "Paper", "Scissors"]
    computer_choice = random.choice(list_rps)
    return computer_choice

def get_user_choice():
    user_choice = input("Select: ")
    return user_choice

def get_winner(computer_choice, user_choice):
    if computer_choice == user_choice:
        return("It's a tie!")
    if computer_choice == "Rock":
        if user_choice == "Scissors":
            return("You lost")
        else:
            return("You won!")
    elif computer_choice == "Paper":
        if user_choice == "Rock":
            return("You lost")
        else:
            return("You won!")
    elif computer_choice == "Scissors":
        if user_choice == "Paper":
            return("You lost")
        else:
            return("You won!")