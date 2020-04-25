import random

DIGITS = [0, 1, 2, 3, 4, 5]

num_guesses = 0
secret_code = random.choices(DIGITS, k=4)

while True:
    print()
    guess = input("please guess a 4 digit number, digits 0 to 5: ")
    if len(guess) != 4:
        print("I said 4 digits!")
        continue
    
    try:
        guess = [int(x) for x in guess]
        if not all(0 <= x <= 5 for x in guess):
            print("I said between 0 and 5!")
            continue

    except ValueError:
        print("I said digits!")
        continue
        
    white = 0  # correct color + correct location
    red = 0    # correct color + wrong location
    num_guesses += 1
    
    for i in range(4):
        if guess[i] == secret_code[i]:
            white += 1
            guess[i] = -1  # sentinel for "already counted as white"
                        
    for i in range(4):
        if guess[i] == -1:
            continue
        try:
            idx = guess.index(secret_code[i])
            red += 1
            guess[idx] = -2 # sentinel for "already counted as red"
        except ValueError:
            continue
            
    if white == 4:
        print("That's correct, you win!")
        print("It only took", num_guesses, "guesses")
        break
        
    else:
        print("White:", white)
        print("Red:", red)

        
        
        
