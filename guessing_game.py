import random

HI = 1000

secret_number = random.randint(1, HI)
num_guesses = 0

while True:
    guess = input("What's your guess? ")
    guess = int(guess)

    num_guesses = num_guesses + 1

    # TOO HIGH
    if guess > secret_number:
        print("TOO HIGH")

    # TOO LOW
    if guess < secret_number:
        print("TOO LOW")

    # CORRECT
    if guess == secret_number:
        print("YOU GUESSED RIGHT")
        print("IT TOOK YOU", num_guesses, "GUESSES")
        break
        
