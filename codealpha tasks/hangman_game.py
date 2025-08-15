import random

def hangman():
    # Predefined list of 5 words
    words = ["python", "hangman", "program", "code", "alpha"]
    word = random.choice(words)
    guessed_letters = []
    attempts = 6  # Limit incorrect guesses to 6

    print("🎯 Welcome to Hangman Game!")
    print("_ " * len(word))

    while attempts > 0:
        guess = input("\nGuess a letter: ").lower()

        if not guess.isalpha() or len(guess) != 1:
            print("⚠ Please enter a single valid letter.")
            continue

        if guess in guessed_letters:
            print("🔁 You already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess in word:
            print("✅ Good guess!")
        else:
            attempts -= 1
            print(f"❌ Wrong guess! Remaining attempts: {attempts}")

        # Display current progress
        display_word = ""
        for letter in word:
            if letter in guessed_letters:
                display_word += letter + " "
            else:
                display_word += "_ "
        print(display_word)

        # Check if the player has guessed the word
        if "_" not in display_word:
            print("\n🎉 Congratulations! You guessed the word correctly.")
            break
    else:
        print(f"\n💀 Game Over! The word was '{word}'.")

# Run the game
if __name__ == "__main__":
    hangman()
