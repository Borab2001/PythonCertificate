import random

number = random.randint(0,10)

guess = int(input("I'm thinking about a number between 0 and 10. Can you guess it?: "))

while True:
    if guess == number:
        break
    else:
        guess = int(input("Nope... Try again: "))

print("You guess it. I was thinking about", number)
