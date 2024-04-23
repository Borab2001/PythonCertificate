date = input("Please enter your date of birth in JJ-MM-AAAA format: ")
months = ("January", "February", "March", "April", "May", "June", "July", "September", "Octobre", "November", "December")

entered_month = int(date[3:5])
month_number = entered_month - 1


print("You were born in", months[month_number])
