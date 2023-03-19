# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
bmi = weight / (height ** 2)

if bmi > 18.5:
    print(f"your BMI is, {round(bmi)} you have a normal weight")
elif bmi > 25:
    print(f"your BMI is, {round(bmi)} you have a overweight")
elif bmi > 30:
    print(f"your BMI is, {round(bmi)} you have a obese")
elif bmi > 35:
    print(f"your BMI is, {round(bmi)} you have a clinically obese")
else:
    print(f"your BMI is, {round(bmi)} you have a underweight")

