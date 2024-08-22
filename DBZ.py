import tkinter as tk
import random

class GuessingGame:
    def __init__(self, master):
        # Initialize the main window of the application
        self.master = master
        master.title("Number Guessing Game")

        # Difficulty settings, determining the range of the random number
        self.difficulty_levels = {
            "Easy": 50,       # Maximum number is 50
            "Medium": 100,    # Maximum number is 100
            "Hard": 1000      # Maximum number is 1000
        }
        self.difficulty = tk.StringVar(master, "Medium")  # Set default difficulty to 'Medium'

        # Create and pack widgets for selecting the difficulty level
        tk.Label(master, text="Select Difficulty:").pack()
        for level in self.difficulty_levels:
            tk.Radiobutton(master, text=level, variable=self.difficulty, value=level, command=self.initialize_game).pack()

        # Label to display the current range of guessing
        self.label = tk.Label(master, text="Guess a number between 1 and 100")
        self.label.pack()

        # Entry widget for user to enter their guess
        self.entry = tk.Entry(master)
        self.entry.pack()

        # Button to submit the guess, triggering the guessing process
        self.guess_button = tk.Button(master, text="Guess", command=self.process_guess)
        self.guess_button.pack()

        # Label to display hints or the result of the guess
        self.result_label = tk.Label(master, text="")
        self.result_label.pack()

        # Button to restart the game, reinitializes the game state
        self.restart_button = tk.Button(master, text="Restart Game", command=self.initialize_game)
        self.restart_button.pack()

        # Initialize the game state for the first time
        self.initialize_game()

    def initialize_game(self):
        # Set the maximum number based on the selected difficulty and generate a secret number
        max_number = self.difficulty_levels[self.difficulty.get()]
        self.secret_number = random.randint(1, max_number)
        self.attempts = 0
        # Update the label to reflect the current range
        self.label.config(text=f"Guess a number between 1 and {max_number}")
        # Reset other components
        self.result_label.config(text="", bg='SystemButtonFace')
        self.guess_button.config(state='normal')
        self.entry.delete(0, tk.END)

    def process_guess(self):
        # Validate and process the user's guess
        guess = self.entry.get().strip()
        if not guess.isdigit():  # Check if the input is a digit
            self.result_label.config(text="Invalid input! Please enter a valid number.", bg='pink')
            self.entry.delete(0, tk.END)
            return

        guess = int(guess)
        self.attempts += 1
        # Check the guess against the secret number and provide feedback
        if guess == self.secret_number:
            self.result_label.config(text=f"Congratulations! You've guessed the number in {self.attempts} attempts!", bg='green')
            self.guess_button.config(state='disabled')  # Disable the guess button after a correct guess
        elif guess < self.secret_number:
            self.result_label.config(text="Too low. Try again!", bg='yellow')
        else:
            self.result_label.config(text="Too high. Try again!", bg='red')

def main():
    root = tk.Tk()
    game = GuessingGame(root)
    root.mainloop()

if __name__ == "__main__":
    main()





