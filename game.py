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