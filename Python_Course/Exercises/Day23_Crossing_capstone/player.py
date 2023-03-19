from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 2
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super(Player, self).__init__()
        self.shape('turtle')
        self.penup()
        self.setheading(90)
        self.goto(STARTING_POSITION)

    def move(self):
        if self.ycor() >= FINISH_LINE_Y:
            return 0
        self.forward(MOVE_DISTANCE)

    def return_position(self):
        self.goto(STARTING_POSITION)