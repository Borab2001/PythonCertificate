weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in m: "))

print("Your height: ", height, "m")
print("Your weight: ", weight, "kg")

imc = weight / (height ** 2)
imc_pound_inch = imc * 703

print("Your BMI in meters and kgs: ", round(imc, 2))
print("Your BMI in pounds and inches: ", round(imc_pound_inch, 2))

if (imc > 29.9):
    classification = "Obese"
elif (imc >= 24.9):
    classification = "Overweight"
elif (imc > 18.5):
    classification = "Normal Weight"
else:
    classification = "Underweight"

print("Your classification: ", classification)
