import random


def hangman():
    # Predefined list of words
    words = ["python", "computer", "hangman", "science", "engineer"]

    # Randomly select a word
    word = random.choice(words)
    guessed_letters = []  # list to store guessed letters
    attempts = 6  # number of allowed wrong guesses
    word_display = ["_"] * len(word)  # display word as underscores

    print("🎯 Welcome to Hangman Game!")
    print("Guess the word, one letter at a time.")
    print("You have 6 chances to make mistakes.\n")

    # Main game loop
    while attempts > 0:
        print("Word:", " ".join(word_display))
        print(f"Remaining attempts: {attempts}")

        guess = input("Enter a letter: ").lower()

        # Check valid input
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single alphabet letter.\n")
            continue

        # Check if letter already guessed
        if guess in guessed_letters:
            print("You already guessed that letter!\n")
            continue

        guessed_letters.append(guess)

        # Correct guess
        if guess in word:
            print("✅ Good job! Letter found.\n")
            for i in range(len(word)):
                if word[i] == guess:
                    word_display[i] = guess
        else:
            attempts -= 1
            print("❌ Wrong guess!\n")

        # Check if player won
        if "_" not in word_display:
            print("🎉 Congratulations! You guessed the word:", word)
            break
    else:
        print("😢 Out of attempts! The word was:", word)


# Run the game
hangman()
