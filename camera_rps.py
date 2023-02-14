# Import all the modules
import cv2
from keras.models import load_model
import numpy as np
import time

# Import functions defined previously
from manual_rps import get_computer_choice, get_winner

# Create a function that will return the output of the model
def get_prediction():
    model = load_model('keras_model.h5')
    cap = cv2.VideoCapture(0)
    data = np.ndarray(shape = (1, 224, 224, 3), dtype = np.float32)

    while True:
        ret, frame = cap.read()
        resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
        image_np = np.array(resized_frame)
        normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
        data[0] = normalized_image
        prediction = model.predict(data)
        cv2.imshow('frame', frame)

        # Press q to close the window
        print(prediction)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
                
    # After the loop release the cap object
    cap.release()

    # Destroy all the windows
    cv2.destroyAllWindows()

    # Return the user choice
    list_rps = ["Rock", "Paper", "Scissors", "Nothing"]
    user_choice = list_rps[prediction.argmax()]
    return user_choice

# Compute how much time has passed since the script started
start_time = time.time()

while True:
    elapsed_time = time.time() - start_time
    countdown = 5 - int(elapsed_time)

    if countdown <= 0:
        break

# Create two variables to keep track of the number of wins each player has
computer_wins = 0
user_wins = 0

while computer_wins < 3 and user_wins < 3:
    computer_choice = get_computer_choice()
    user_choice = get_prediction()
    result = get_winner(computer_choice, user_choice)
    print(result)

    if result == "You lost":
        computer_wins += 1
    elif result == "You won!":
        user_wins += 1

# The program outputs the result of the game when one of the players has won three rounds
if computer_wins == 3:
    print("You lost the game!")
elif user_wins == 3:
    print("You won the game!")