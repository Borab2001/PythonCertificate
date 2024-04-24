data_valid = False

while data_valid == False:
    grade1 = float(input("Enter the grade of your first test: "))
    if grade1 < 0 or grade1 > 10:
        print("Grade should be between 0 and 10")
        continue
    else :
        data_valid = True

data_valid = False

while data_valid == False:
    grade2 = float(input("Enter the grade of your second test: "))
    if grade2 < 0 or grade2 > 10:
        print("Grade should be between 0 and 10")
        continue
    else :
        data_valid = True

data_valid = False

while data_valid == False:
    number_of_classes = int(input("Enter the total number of classes: "))
    if number_of_classes <= 0:
        print("The number of classes can't be less or equal to zero")
        continue
    else :
        data_valid = True

data_valid = False

while data_valid == False:
    missed_classes = int(input("Enter the number of classes you missed: "))
    if missed_classes < 0 or missed_classes > number_of_classes:
        print("The number of missed classes can't be less than zero or greater than the number of classes")
        continue
    else :
        data_valid = True
        

average_grade = (grade1 + grade2) / 2
attendance = (number_of_classes - missed_classes) / number_of_classes

print("Average grade: ", round(average_grade, 2))
print("Attendance: ", str(round((attendance * 100), 2))+"%")

if (average_grade >= 6 and attendance >= 0.8):
    print("The student has been approved")
elif (average_grade < 6 and attendance < 0.8):
    print("The student has failed due to an attendence rate lower than 80% and an average grade lower than 6.0")
elif (attendance >= 0.8):
    print("The student failed due to an average grade lower than 6.0") 
else:
    print("The student has failed due to an attendence rate lower than 80%")
