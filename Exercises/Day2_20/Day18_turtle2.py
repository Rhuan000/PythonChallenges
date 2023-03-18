import turtle
from turtle import Turtle, Screen, colormode
import random


timmy = Turtle()
timmy.shape('turtle')
timmy.color('orange')
timmy.speed(0)
timmy.speed(7)
timmy.pensize(30)
turtle.colormode(255)
def colours():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r,g,b)
directions = [0,90,180,270]
for _ in range(0,100):
    timmy.color(colours())
    timmy.forward(30)
    timmy.setheading(random.choice(directions))

















