from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('red')
        self.shapesize(0.2)
        self.penup()

    def random_food(self):
        a = int(random.randint(-14, 14) * 20)
        b = int(random.randint(-14, 14) * 20)
        self.goto(a,b)
