import random

list_rps = ["Rock", "Paper", "Scissors"]
print(type(list_rps))

def get_computer_choice():
    computer_choice = random.choice(list_rps)
    return computer_choice

def get_user_choice():
    user_choice = input("Select: ")
    return user_choice