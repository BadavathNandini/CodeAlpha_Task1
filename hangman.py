import random

# 🎯 Word bank with hints
word_bank = {
    'easy': {'apple': 'A sweet red or green fruit', 'cat': 'A small domesticated feline', 'sun': 'It lights up the day'},
    'medium': {'robot': 'A machine that can perform tasks', 'snake': 'A legless reptile', 'piano': 'A musical instrument with keys'},
    'hard': {'triangle': 'Three-sided geometric figure', 'dinosaur': 'A prehistoric reptile', 'volcano': 'Mountain that erupts lava'}
}

def play_game():
    score = 0
    while True:
        # 🌟 Choose difficulty
        print("\nChoose difficulty: easy / medium / hard")
        difficulty = input("Enter: ").lower()

        if difficulty not in word_bank:
            print("Invalid difficulty. Try again.")
            continue

        # 🎲 Select word and hint
        word, hint = random.choice(list(word_bank[difficulty].items()))
        guessed_letters = []
        tries_left = 6
        display_word = ['_' for _ in word]

        print(f"\n💡 Hint: {hint}")

        # 🎮 Game loop
        while tries_left > 0 and '_' in display_word:
            print(f"\nWord: {' '.join(display_word)}")
            print(f"Guessed letters: {', '.join(guessed_letters)}")
            print(f"Tries left: {tries_left}")
            guess = input("Guess a letter: ").lower()

            if len(guess) != 1 or not guess.isalpha():
                print("Please enter a single alphabet letter.")
                continue
            if guess in guessed_letters:
                print("You already guessed that.")
                continue

            guessed_letters.append(guess)

            if guess in word:
                for i in range(len(word)):
                    if word[i] == guess:
                        display_word[i] = guess
                print("✅ Nice!")
            else:
                tries_left -= 1
                print("❌ Miss!")

        # 🏁 Result
        if '_' not in display_word:
            print(f"\n🎉 You guessed it! The word was: {word}")
            score += 1
        else:
            print(f"\n💀 Game Over! The word was: {word}")

        print(f"🏆 Total Wins: {score}")

        # 🔁 Replay prompt
        play_again = input("\nDo you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thanks for playing, see you next time! 👋")
            break

# 🚀 Start the game
play_game()
