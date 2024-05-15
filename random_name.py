import random

names = []
key = random.randint(0,7)

for x in range(0,8):
    person_name = input("Enter a name: ")
    names.append(person_name)
    x += 1


print("Here is a random name:", names[key])
