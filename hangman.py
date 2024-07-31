import random

def get_random_word():
    words = ['python', 'hangman', 'challenging', 'programming', 'computer', 'science', 'education', 'development']
    return random.choice(words)

def display_word(word, guessed_letters):
    displayed_word = ''.join([letter if letter in guessed_letters else '_' for letter in word])
    return displayed_word

def hangman():
    word = get_random_word()
    guessed_letters = set()
    incorrect_guesses = 0
    max_incorrect_guesses = 6

    print("Welcome to Hangman!")
    print(f"The word has {len(word)} letters.")

    while incorrect_guesses < max_incorrect_guesses:
        print(display_word(word, guessed_letters))
        guess = input("Guess a letter: ").lower()

        if guess in guessed_letters:
            print("You've already guessed that letter.")
        elif guess in word:
            guessed_letters.add(guess)
            print("Correct!")
        else:
            guessed_letters.add(guess)
            incorrect_guesses += 1
            print(f"Incorrect! You have {max_incorrect_guesses - incorrect_guesses} incorrect guesses left.")

        if set(word).issubset(guessed_letters):
            print(f"Congratulations! You guessed the word: {word}")
            break
    else:
        print(f"Game over! The word was: {word}")

if __name__ == "__main__":
    hangman()
import random

def get_random_word():
    words = ['python', 'hangman', 'challenging', 'programming', 'computer', 'science', 'education', 'development']
    return random.choice(words)

def display_word(word, guessed_letters):
    displayed_word = ''.join([letter if letter in guessed_letters else '_' for letter in word])
    return displayed_word

def hangman():
    word = get_random_word()
    guessed_letters = set()
    incorrect_guesses = 0
    max_incorrect_guesses = 6

    print("Welcome to Hangman!")
    print(f"The word has {len(word)} letters.")

    while incorrect_guesses < max_incorrect_guesses:
        print(display_word(word, guessed_letters))
        guess = input("Guess a letter: ").lower()

        if guess in guessed_letters:
            print("You've already guessed that letter.")
        elif guess in word:
            guessed_letters.add(guess)
            print("Correct!")
        else:
            guessed_letters.add(guess)
            incorrect_guesses += 1
            print(f"Incorrect! You have {max_incorrect_guesses - incorrect_guesses} incorrect guesses left.")

        if set(word).issubset(guessed_letters):
            print(f"Congratulations! You guessed the word: {word}")
            break
    else:
        print(f"Game over! The word was: {word}")

if __name__ == "__main__":
    hangman()
