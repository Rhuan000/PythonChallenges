import turtle
from turtle import Turtle, Screen, colormode
import random


timmy = Turtle()
timmy.shape('turtle')
timmy.color('orange')
timmy.speed(0)
timmy.speed(6)

colours = ["white", "black", "red", "green", "blue", "cyan", "yellow","magenta", "CornflowerBlue", "DarkOrchid",
           "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

def make_shapes(num_sides):
    sides =  360/num_sides
    for _ in range(num_sides):
        timmy.forward(50)
        timmy.right(sides)

for num_sides in range(3,11):
    timmy.color(random.choice(colours))
    make_shapes(num_sides)


















