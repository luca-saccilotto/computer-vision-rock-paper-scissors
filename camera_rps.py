# Import all the modules
import cv2
from keras.models import load_model
import numpy as np
import random
import time

# Create the class and methods
class CameraRPS:

    # Initialize the object's attributes
    def __init__(self):
        self.model = load_model('keras_model.h5')
        self.cap = cv2.VideoCapture(0)
        self.data = np.ndarray(shape = (1, 224, 224, 3), dtype = np.float32)
        self.computer_wins = 0
        self.user_wins = 0

    # Create a function to store the computer's choice
    def get_computer_choice(self):
        computer_choice = random.choice(list_rps)
        return computer_choice

    # Create a function that returns user's choice
    def get_prediction(self):
        start_time = time.time()
        countdown = 5

        while countdown >= 0:
            ret, frame = self.cap.read()

            """Print the countdown in the webcam display"""
            cv2.putText(frame, str(countdown), (75, 75), cv2.FONT_HERSHEY_SIMPLEX , 1, (255, 0, 0), 2, cv2.LINE_AA)
            cv2.imshow("frame", frame)
            countdown -= int(time.time() - start_time)

            """Resize the image"""
            resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
            image_np = np.array(resized_frame)

            """Normalize the image"""
            normalized_image = (image_np.astype(np.float32) / 127.0) - 1
            self.data[0] = normalized_image
            prediction = self.model.predict(self.data)
            cv2.imshow("frame", frame)
            
            # Press "q" to close the window
            if cv2.waitKey(1) & 0xFF == ord('q'):
                return None
                    
        # Return and display the user's choice
        user_choice = list_rps[prediction.argmax()]
        return user_choice
        
    # Create a function to define the logic of the game
    def get_winner(self, computer_choice, user_choice):
        if user_choice == "Nothing":
            print("Invalid. Please try again.")
            return
        if computer_choice == user_choice:
            print(f"You: {user_choice}, Computer: {computer_choice}. It is a tie!")
        elif computer_choice == "Rock":
            if user_choice == "Scissors":
                print(f"You: {user_choice}, Computer: {computer_choice}. You lost!")
                self.computer_wins += 1
            else:
                print(f"You: {user_choice}, Computer: {computer_choice}. You won!")
                self.user_wins += 1
        elif computer_choice == "Paper":
            if user_choice == "Rock":
                print(f"You: {user_choice}, Computer: {computer_choice}. You lost!")
                self.computer_wins += 1
            else:
                print(f"You: {user_choice}, Computer: {computer_choice}. You won!")
                self.user_wins += 1
        elif computer_choice == "Scissors":
            if user_choice == "Paper":
                print(f"You: {user_choice}, Computer: {computer_choice}. You lost!")
                self.computer_wins += 1
            else:
                print(f"You: {user_choice}, Computer: {computer_choice}. You won!")
                self.user_wins += 1

# Create two variables to keep track of the number of wins each player has
def play_game(list_rps):
    game_rps = CameraRPS()

    while True:
        computer_choice = game_rps.get_computer_choice()
        user_choice = game_rps.get_prediction()

        if user_choice == None:
            break
        else:
            game_rps.get_winner(computer_choice, user_choice)
        
        if game_rps.computer_wins == 3:
            print("You lost the game!")
            break
        elif game_rps.user_wins == 3:
            print("You won the game!")
            break

    # After the loop release the cap object
    game_rps.cap.release()

    # Destroy all the windows
    cv2.destroyAllWindows()

# Call the function to test the code
if __name__ == "__main__":
    list_rps = ["Rock", "Paper", "Scissors", "Nothing"]
    play_game(list_rps)