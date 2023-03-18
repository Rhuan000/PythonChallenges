#🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()

for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇
soma = 0
for estudantes in student_heights:
    soma = soma + estudantes

soma = soma / len(student_heights)
print(round(soma))