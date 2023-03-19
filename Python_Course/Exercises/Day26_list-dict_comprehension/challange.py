numbers = [1,1,2,3,5,8,13,21,34,55]

squared_numbers = [(number*number) for number in numbers]
even_numbers = [number for number in numbers if (number%2) == 0]

print(squared_numbers, even_numbers)

numbers = [1,2,3]
new_numbers = [n+1 for n in numbers]
name = 'RhuaN'
new_list = [letter for letter in name]
new_list = [n*2 for n in range(1,5)]
print(new_list)
names = ['aline','marcio','pedro','jorge','luis','marcelo','joao']
list_names = [name for name in names if len(name) <= 4]
print(list_names)
upper_names = [name.upper() for name in names if len(name) > 5]
print(upper_names)
import random
names = ['Alex','Beth','Caroline','Dave','Eleanor','Freddie']
student_score = {student:random.randint(1,100) for student in names}
passed_student = {student:score for student,score in student_score.items() if score >= 60}
print(student_score)
print(passed_student)

weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}

new_dictionary = {key: (value * 9/5) + 32 for key,value in weather_c.items()}
print(new_dictionary)

import pandas
student_dict = {
    'student': ['carlos','maria','jose','pedro'],
    'score': [50,60,70,80]
}
student_data_frame = pandas.DataFrame(student_dict)
for index, row in student_data_frame.iterrows():
    if row.student:
        print(row.student)
