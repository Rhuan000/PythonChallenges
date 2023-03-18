from turtle import Turtle, turtlesize

class Ball(Turtle):
    def __init__(self ):
        super(Ball, self).__init__()
        self.penup()
        self.shape('circle')
        self.color('white')
        self.shapesize(stretch_wid=1)
        self.x_move = 2
        self.y_move = 2
        self.speed = 0.01
    def initial_position(self):
        self.x_move *= -1
        self.y_move *= -1
        self.speed = 0.01
        self.goto(0, 0)


    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)


    def user_contact(self):
        self.x_move *= -1
        self.speed *= 0.1

    def wall_contact(self):
        self.y_move *= -1
