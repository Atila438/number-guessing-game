import random
import time

def number_guessing_game():
    high_scores = {"Easy": None, "Medium": None, "Hard": None}

    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    print("Try to guess it within the allowed number of chances!\n")

    while True:
        # Difficulty selection
        print("Please select the difficulty level:")
        print("1. Easy (10 chances)")
        print("2. Medium (5 chances)")
        print("3. Hard (3 chances)")

        choice = input("Enter your choice (1/2/3): ")

        if choice == "1":
            difficulty = "Easy"
            chances = 10
        elif choice == "2":
            difficulty = "Medium"
            chances = 5
        elif choice == "3":
            difficulty = "Hard"
            chances = 3
        else:
            print("Invalid choice! Try again.\n")
            continue

        number = random.randint(1, 100)
        attempts = 0
        start_time = time.time()
        print(f"\nGreat! You have selected {difficulty} mode. Let's start!")
        print("Type 'exit' to quit the current round, or 'hint' to get a clue.\n")

        while attempts < chances:
            guess = input(f"Enter your guess ({chances - attempts} chances left): ")

            # Early exit
            if guess.lower() == "exit":
                print("\nExiting current round...")
                break

            # Hint system
            if guess.lower() == "hint":
                if number % 2 == 0:
                    print("Hint: The number is even.\n")
                else:
                    print("Hint: The number is odd.\n")

                if number > 50:
                    print("Hint: The number is greater than 50.\n")
                else:
                    print("Hint: The number is 50 or less.\n")
                continue  # Don’t count this as an attempt

            # Input validation
            try:
                guess = int(guess)
            except ValueError:
                print("Invalid input! Please enter a number, 'hint', or 'exit'.\n")
                continue

            attempts += 1

            # Correct guess
            if guess == number:
                end_time = time.time()
                duration = round(end_time - start_time, 2)
                print(f"\n🎉 Congratulations! You guessed the number {number} correctly "
                      f"in {attempts} attempts and {duration} seconds.")

                # Update high score
                if high_scores[difficulty] is None or attempts < high_scores[difficulty]:
                    high_scores[difficulty] = attempts
                    print(f"🏆 New high score for {difficulty} mode: {attempts} attempts!")
                break

            # Wrong guess
            elif guess < number:
                print("Incorrect! The number is greater than your guess.\n")
            else:
                print("Incorrect! The number is less than your guess.\n")

        else:
            # Only runs if loop ends naturally (out of chances)
            print(f"\n💀 Game Over! You ran out of chances. The correct number was {number}.")

        # Show high scores
        print("\nCurrent High Scores:")
        for mode, score in high_scores.items():
            if score is None:
                print(f"{mode}: None yet")
            else:
                print(f"{mode}: {score} attempts")

        play_again = input("\nDo you want to play again? (yes/no): ").lower()
        print()
        if play_again != "yes":
            print("Thanks for playing! Goodbye")
            break


if __name__ == "__main__":
    number_guessing_game()
