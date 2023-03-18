from turtle import Turtle
import random
import time

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 1
MOVE_INCREMENT = 3


class CarManager():

    def __init__(self):
        super().__init__()
        self.all_cars = []
        self.speed = STARTING_MOVE_DISTANCE
        self.position = ()
    def increase_speed(self):
        self.speed += MOVE_INCREMENT

    def create_car(self):
        car = Turtle()
        random_color = random.choice(COLORS)
        car.color(random_color)
        car.shape('square')
        car.shapesize(stretch_len=2)
        car.penup()
        car.setheading(180)
        car.goto(random.randint(300,900), random.randint(-260, 260))
        self.all_cars.append(car)

    def move(self):
        for car in self.all_cars:
            car.forward(self.speed)
            if car.xcor() < -320:
                self.all_cars.remove(car)

