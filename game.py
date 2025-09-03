import random
import time

def number_guessing_game():
    high_scores = {"Easy": None, "Medium": None, "Hard": None}

    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    print("Try to guess it within the allowed number of chances!\n")

    while True:
        print("Please select the difficulty level:")
        print("1. Easy (10 chances)")
        print("2. Medium (5 chances)")
        print("3. Hard (3 chances)")
        
        choice = input("Enter your choice (1/2/3): ")

        if choice == "1":
            difficulty = "Easy"
            chances = 10
            break
        elif choice == "2":
            difficulty = "Medium"
            chances = 5
            break
        elif choice == "3":
            difficulty = "Hard"
            chances = 3
            break
        else:
            print("Invalid choice! Try again.\n")
            continue

    number = random.randint(1, 100)
    attempts = 0
    start_time = time.time()
    print(f"\nGreat! You have selected {difficulty} mode. Let's start!\n")

    while attempts < chances:
        try:
            guess = int(input(f"Enter your guess ({chances - attempts} chances left): "))
        except ValueError:
            print("Invalid input! Please enter a number.\n")
            continue

        attempts += 1
        if guess == number:
                end_time = time.time()
                duration = round(end_time - start_time, 2)
                print(f"\nCongratulations! You guessed the number {number} correctly "
                      f"in {attempts} attempts and {duration} seconds.")