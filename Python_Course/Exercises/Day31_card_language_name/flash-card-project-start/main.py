import tkinter
import pandas
import random


BACKGROUND_COLOR = "#B1DDC6"
all_pairs = []
new_random_choice = None
old_random_choice = None
english_word = ''
portuguese_word = ''


#create a list with all pairs: word and translation
data = pandas.read_csv('data/English_Portuguese.csv')
for reps in range(0, len(data['English'])):
    pair = [data['English'][reps], data['Portuguese'][reps]]
    all_pairs.append(pair)


#create word pair
def create_word():
    global english_word, portuguese_word, new_random_choice
    new_random_choice = random.choice(all_pairs)
    english_word = new_random_choice[0]
    portuguese_word = new_random_choice[1]
    all_pairs.index(new_random_choice)

    #checking if the new random_choice is the same as the old_choice
    try:
        if new_random_choice == old_random_choice:
            create_word()
    except RecursionError:
        pass


#showing the word in the front
def show_front_image():
    canvas.itemconfig(canvas_image, image=card_front_img)
    canvas.itemconfig(title, text="English")
    canvas.itemconfig(word, text=english_word)


#showing the translation in the back
def show_back_card():
    canvas.itemconfig(canvas_image, image=card_back_img)
    canvas.itemconfig(title, text='Portuguese')
    canvas.itemconfig(word, text=portuguese_word)


#Create a image
def show_image():
    global old_random_choice, after
    window.after_cancel(after)
    old_random_choice = new_random_choice
    create_word()
    show_front_image()
    after = window.after(3000, show_back_card)


#Just skipping after wrong button be clicked
def wrong_answer():
    show_image()

#Remove right answers of the pack.
def right_answer():
    all_pairs.remove(all_pairs[all_pairs.index(new_random_choice)])
    show_image()

    #transforming the List into a dic to modify the csv data file, so other times we run this application the words we need to learn, will be saved
    to_learn = {'English': [],
                'Portuguese': []
                }
    for pairs in all_pairs:
        to_learn['English'].append(pairs[0])
        to_learn['Portuguese'].append(pairs[1])

    #Creating a Dataframe with the list /\ and modifying the English_Portuguese.csv
    new_data = pandas.DataFrame(to_learn)
    new_data.to_csv('../flash-card-project-start/data/English_Portuguese.csv')



#------ CREATING WINDOW ------#
window = tkinter.Tk()
window.title('Memorize words')
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
after = window.after(3000, show_back_card)

#------CREATING BUTTONS ------#
#cright button
right_img = tkinter.PhotoImage(file='../flash-card-project-start/images/right.png')
button_right = tkinter.Button(image=right_img, highlightthickness=0, command=right_answer)
button_right.grid(column=2, row=2)

#wrong button
wrong_img = tkinter.PhotoImage(file='../flash-card-project-start/images/wrong.png')
button_wrong = tkinter.Button(image=wrong_img, highlightthickness=0, command=wrong_answer)
button_wrong.grid(column=0, row=2)


#------CREATING CANVAS ------#
canvas = tkinter.Canvas(width=800, height=526)
card_front_img = tkinter.PhotoImage(file='../flash-card-project-start/images/card_front.png')
card_back_img = tkinter.PhotoImage(file='../flash-card-project-start/images/card_back.png')
canvas_image = canvas.create_image(400, 263, image=card_front_img)
title = canvas.create_text(400, 150, text="French", font=("Ariel", 40, "italic"))
word = canvas.create_text(400, 263, text="word", font=("Ariel", 60, "bold"))
canvas.grid(column=1, row=0)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)


show_image()



window.mainloop()
