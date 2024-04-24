import random

colors = ["Red", "Blue", "Green", "Purple", "Black", "White"]
guess = input("I'm thinking about a color between Red, Blue, Green, Purple, Black and White. Can you guess it?: ")


while True:
    index = random.randint(0,5)
    chosen_number = colors[index]

    if guess == chosen_number:
        print("You guess it. I was thinking about", chosen_number)
        guess = input("Wanna play again?: ")

        if guess == "No":
            break
    else:
        guess = input("Nope... Try again: ")


print("Game ended")
