# AiCore Scenario - Computer Vision RPS

This is an implementation of the "Rock-Paper-Scissors" game, that allows the user to play against the computer using their camera. The game uses computer vision algorithms to detect the user's hand gesture and match it with the three possible moves in the game (rock, paper, or scissors).

## Milestone 1
In Milestone 1, the focus was on setting up the development environment. This involved installing the necessary tools and libraries required to run the program. A virtual environment was created to keep the dependencies for the project isolated from the other projects on the machine. This step helped to avoid potential conflicts with other projects.

## Milestone 2 & 3
The game uses a deep learning model created with "Teachable Machine" to recognize different hand gestures. In particular, the model was trained to recognize four classes: rock, paper, scissors, and no gestures. Then, the output was exported along with the files `keras_model.h5` and `labels.txt` containing its structure and parameters.

## Milestone 4
In Milestone 4, the following functions were defined: `get_computer_choice()`, `get_user_choice()`, `get_winner()`, and `play()`. Specifically, `get_computer_choice()` generates a random choice for the computer, `get_user_choice()` prompts the user for input, and `get_winner()` compares the two choices to determine the winner. Finally, `play()` simulates a game by calling the other functions.