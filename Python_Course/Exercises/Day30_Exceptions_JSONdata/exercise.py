import  pandas
'''fruits = ["Apple", "Pear", "Orange"]

def make_pie(index):
    try:
        fruit = fruits[index]
    except IndexError:
        print('fruit pie')
    else:
        print(fruit + ' pie')

make_pie(1)

facebook_posts = [
    {'likes': 21, 'comments': 2},
    {'likes': 13, 'comments': 2, 'shares':1},
    {'likes': 33, 'comments': 8, 'shares':3},
    {'shares': 2, 'comments': 4},
    {'shares': 1, 'comments': 1},
    {'likes': 19, 'comments': 3}
]

total_likes = 0
for post in facebook_posts:
    try:
        post['likes']
    except KeyError:
        pass
    else:
        total_likes = total_likes + post['likes']
print(total_likes)'''

def main():
    new_dataframe = pandas.read_csv('nato_phonetic_alphabet.csv')
    #TODO 1. Create a dictionary in this format:

    new_dic = {row.letter:row.code for index, row in new_dataframe.iterrows()}
    #TODO 2. Create a list of the phonetic code words from a word that the user inputs.
    word = str(input('please insert a word: ')).upper()

    try:
        word_list = [new_dic[letter] for letter in word]

    except KeyError:
        print('Sorry, only letters in the alphabet please')
        main()
    else:
        print(word_list)

main()
