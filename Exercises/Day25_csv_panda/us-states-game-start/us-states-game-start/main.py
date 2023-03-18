import turtle
from turtle import Turtle
import pandas

screen = turtle.Screen()
screen.title('U.S state game')
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
count = 0
is_on = True
data_state = pandas.read_csv('50_states.csv')
state_list = data_state['state'].to_list()
while is_on:

    answer_state = screen.textinput(title=f'{count}/50 States correct', prompt="What's another state's name?").title()
    for check in state_list:
        if answer_state == check:
            count += 1
            state = data_state[data_state['state'] == answer_state]
            x = int(state.x)
            y = int(state.y)
            turtle = Turtle()
            turtle.penup()
            turtle.hideturtle()
            turtle.goto(x, y)
            turtle.write(arg=answer_state)
            state_list.remove(answer_state)
    if count == 50:
        is_on = False
    elif answer_state == 'Exit':
        is_on = False
state_to_learn ={
    'State to Learn': state_list
}
new_data = pandas.DataFrame(state_to_learn)
new_data.to_csv('State_to_lean.csv')




screen.exitonclick()