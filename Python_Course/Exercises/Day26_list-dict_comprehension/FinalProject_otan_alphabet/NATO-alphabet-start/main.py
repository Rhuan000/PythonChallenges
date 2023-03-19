student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    #Access key and value
    pass

import pandas
student_data_frame = pandas.DataFrame(student_dict)

#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    #Access index and row
    #Access row.student or row.score
    pass

# Keyword Method with iterrows()

new_dataframe = pandas.read_csv('nato_phonetic_alphabet.csv')
#TODO 1. Create a dictionary in this format:

new_dic = {row.letter:row.code for index, row in new_dataframe.iterrows()}
#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
word = str(input('please insert a word: ')).upper()
word_list = [letter for letter in word]
for letter in word_list:
    print(letter, new_dic[letter])



