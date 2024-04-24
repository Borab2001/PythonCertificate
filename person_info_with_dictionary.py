person = { "name": "Bora", "gender": "Male", "age": "23", "address": "102 Rue des Orteaux", "phone": "0766647521" }

key = input("What information would you like to know?: ").lower()
info = person.get(key, "This information doesn't exist")

print(info)
