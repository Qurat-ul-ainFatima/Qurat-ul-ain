Welcome to the Hangman Game! This is a classic word-guessing game implemented in Python. The game selects a random word, and your goal is to guess it one letter at a time. But be careful—you only have a limited number of incorrect guesses before the game is over.

How to Play
Start the Game: When you run the game, it will select a random word from a predefined list. The length of the word will be shown as underscores (_), with each underscore representing a letter in the word.

Make a Guess: You'll be prompted to guess a letter. Enter any letter you think might be in the word.

Correct Guess: If the letter you guessed is in the word, all instances of that letter will be revealed in their correct positions.

Incorrect Guess: If the letter is not in the word, you'll lose one of your allowed incorrect guesses. You have up to 6 incorrect guesses before the game ends.

Win or Lose:

Win: If you guess all the letters in the word before running out of incorrect guesses, you win!
Lose: If you use up all your incorrect guesses without uncovering the entire word, the game ends, and you'll be shown the word you were trying to guess.

Example Gameplay:
Welcome to Hangman!
The word has 8 letters.
_ _ _ _ _ _ _ _
Guess a letter: e
Correct!
_ _ _ _ _ _ _ e
Guess a letter: a
Incorrect! You have 5 incorrect guesses left.
_ _ _ _ _ _ _ e
Guess a letter: c
Correct!
_ c _ _ _ _ _ e

How to Run
Make sure you have Python installed on your system.
Copy the code into a Python file (e.g., hangman.py).
Open your terminal or command prompt.
Navigate to the directory where you saved hangman.py.
Run the script by typing python hangman.py.
Enjoy playing the Hangman Game!
