'''with open('weather_data.csv') as weater:
    data = weater.readlines()'''
'''import csv

with open('weather_data.csv') as data_file:
    data = csv.reader(data_file)
    temperatures = []
    for row in data:
        if row[1] != 'temp':
            temperatures.append(int(row[1]))
'''
import pandas

'''data = pandas.read_csv('weather_data.csv')
#transform the data in a list.
temp_list = data['temp'].to_list()

avarage = data['temp'].mean() # or data.temp.mean()

#get data in a column
max = data['temp'].max()
print(avarage, max)
print(data.condition)

#get data in a row
print(data[data.temp == data.temp.max()])

#catching the row of monday and catching the singular data.
#get data in a row
monday = data[data.day == 'Monday']
temp = (monday.temp * (9/5)) + 32
print(temp)

#create a dataframe from scratch
data_dict = {
    "students": ["Any", "james", "angela"],
    'scores': [76, 56, 65]
}
data_from_sctach = pandas.DataFrame(data_dict)
print(data_from_sctach)
#data_from_sctach.to_csv('new_data_csv.csv')'''

'''squirrel_data = pandas.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')
color_list = squirrel_data['Primary Fur Color'].tolist()
black = 0
gray = 0
cinnamon = 0
for color in color_list:
    if color == 'Gray':
        gray += 1
    elif color == 'Cinnamon':
        cinnamon += 1
    elif color == 'Black':
        black += 1
new_dic = {
    'Fur Color': ['Gray', 'Cinnamon', 'Black'],
    'Count': [gray, cinnamon, black]
}
new_data = pandas.DataFrame(new_dic)
new_data.to_csv('Squirrel count.csv')'''

data = pandas.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')
color_gray = len(data[data['Primary Fur Color'] == "Gray"])
color_black = len(data[data['Primary Fur Color'] == "Black"])
color_cinnamon = len(data[data['Primary Fur Color'] == "Cinnamon"])
new_dic = {
    'Fur Color': ['Gray', 'Cinnamon', 'Black'],
    'Count': [color_gray, color_cinnamon, color_black]
}
new_data = pandas.DataFrame(new_dic)
new_data.to_csv('Squirrel count.csv')