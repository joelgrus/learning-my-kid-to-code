PROTOTYPE = """
 ┏━━┑
 ┃  O>
 ┃>╦╧╦<
 ┃ ╠═╣
 ┃ ╨ ╨
 ┻━━━━
"""

STEPS = [
"""
 ┏━━┑
 ┃
 ┃
 ┃
 ┃
 ┻━━━━
""",
"""
 ┏━━┑
 ┃  O
 ┃
 ┃
 ┃
 ┻━━━━
""",
"""
 ┏━━┑
 ┃  O>
 ┃
 ┃
 ┃
 ┻━━━━
""",
"""
 ┏━━┑
 ┃  O>
 ┃ ╔╧╗
 ┃ ╚═╝
 ┃
 ┻━━━━
""",
"""
 ┏━━┑
 ┃  O>
 ┃>╦╧╗
 ┃ ╚═╝
 ┃
 ┻━━━━
""",
"""
 ┏━━┑
 ┃  O>
 ┃>╦╧╦<
 ┃ ╚═╝
 ┃
 ┻━━━━
""",
"""
 ┏━━┑
 ┃  O>
 ┃>╦╧╦<
 ┃ ╠═╝
 ┃ ╨
 ┻━━━━
""",
"""
 ┏━━┑
 ┃  O>
 ┃>╦╧╦<
 ┃ ╠═╣
 ┃ ╨ ╨
 ┻━━━━
"""
]

MIN_LENGTH = 3
MAX_LENGTH = 8

with open('words1000.txt') as f:
    words = [line.strip() for line in f]

words = [w for w in words if MIN_LENGTH <= len(w) <= MAX_LENGTH]
words = [w for w in words if all('a' <= c <= 'z' for c in w)]

import random
word = random.choice(words)

step = 0
guessed = set()

def show():
    print(STEPS[step])
    chars = [c if c in guessed else "_" for c in word]
    print(" ", " ".join(chars))
    print()
    print("guessed:", " ".join(guessed))


while True:
    show()
    c = input("pick a letter: ")
    if len(c) != 1 or c < 'a' or c > 'z':
        print("a lowercase letter!")
        continue
    if c in guessed:
        print("you already guessed that one!")
        continue
    guessed.add(c)
    if c not in word:
        step += 1
    if step == len(STEPS) - 1:
        show()
        print("YOU LOSE, the word was", word)
        break
    if all(c in guessed for c in word):
        show()
        print("YOU WIN!!")
        break

