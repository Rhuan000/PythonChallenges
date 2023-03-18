from turtle import Turtle,Screen
import turtle
import random

is_race_on = False
screen = Screen()
screen.setup(width=500,height=400)
user_bet = screen.textinput(title='Make your bet', prompt='Which turtle will the race? Enter a color: ')
print(user_bet)
colours = ['red', 'green', 'orange', 'purple', 'yellow', 'blue']
all_turtles = []


y = -170

for turtle_index in range(0,6):

    new_turtle = Turtle()
    new_turtle.shape('turtle')
    new_turtle.color(colours[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y)
    y += 60
    all_turtles.append(new_turtle)
if user_bet:
    is_race_on = True

while is_race_on:
    for turtle1 in all_turtles:
        rand_distance = random.randint(0,10)
        turtle1.forward(rand_distance)

        if turtle1.xcor() >= 250:
            is_race_on = False
            if user_bet == turtle1.color()[1]:
                print('You won')
            else:
                print(f'You lose! {turtle1.color()[1]}, is the winner')
screen.exitonclick()