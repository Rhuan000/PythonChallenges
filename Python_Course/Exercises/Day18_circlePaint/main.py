import random
from turtle import Turtle,Screen,colormode
import turtle

#Setting the colors and the turtle settings.
RGB = [(207, 160, 82), (54, 88, 130), (145, 91, 40), (140, 26, 49), (221, 207, 105), (132, 177, 203), (158, 46, 83), (45, 55, 104), (169, 160, 39), (129, 189, 143), (83, 20, 44), (37, 43, 67), (186, 94, 107), (187, 140, 170), (85, 120, 180), (59, 39, 31), (88, 157, 92), (78, 153, 165), (194, 79, 73), (45, 74, 78), (80, 74, 44), (161, 201, 218), (57, 125, 121), (219, 175, 187), (169, 206, 172), (219, 182, 169)]
timmy = Turtle()
timmy.speed(7)
timmy.penup()
turtle.colormode(255)


def choose_random_color(rgb_list):
    '''will choose a random color in the RGB list'''
    random_color = random.choice(rgb_list)
    return random_color


#Making the turtle move and Change his color in a determinated range
grow_y = -280
for _ in range(10):
    grow_y += 50
    timmy.setx(-230)
    for a in range(10):
        timmy.sety(grow_y)
        timmy.dot(20, choose_random_color(RGB))
        timmy.forward(50)


screen = Screen()
screen.exitonclick()