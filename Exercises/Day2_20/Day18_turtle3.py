import turtle
from turtle import Turtle, Screen, colormode
import random


def colours():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r,g,b)
timmy = Turtle()

timmy.color('orange')
timmy.speed(11)

turtle.colormode(255)
for _ in range(0,360, 5):
    timmy.setheading(_)
    timmy.color(colours())
    timmy.circle(100)

screen = Screen()
screen.exitonclick()















