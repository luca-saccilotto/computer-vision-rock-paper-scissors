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

def play():
    get_computer_choice()
    get_user_choice()
    get_winner()