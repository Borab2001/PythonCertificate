grade1 = float(input("Enter the grade of your first test: "))
grade2 = float(input("Enter the grade of your second test: "))
missed_classes = int(input("Enter the number of classes you missed: "))
number_of_classes = int(input("Enter the total number of classes: "))

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
