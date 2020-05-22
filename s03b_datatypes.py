#!/usr/bin/python3

guesses = 0
current_guess = 50
min_guess = 0
max_guess = 100
feedback = ""

while feedback != "c":
    guesses += 1
    print("Computer guesses: ", current_guess)
    last_guess = current_guess
    feedback = input("Enter (h) for higher, (l) for lower, (c) for correct: ")
    if feedback == "c":
        print(f"Your number was {current_guess} and it took {guesses} guesses!")
    elif feedback == "h":
        min_guess = current_guess
    else:
        max_guess = current_guess
    current_guess = min_guess + ((max_guess - min_guess) // 2)
    if current_guess == last_guess:
        print(f"Your number was {current_guess} and it took {guesses} guesses! It can't be anything else!")
        exit()
