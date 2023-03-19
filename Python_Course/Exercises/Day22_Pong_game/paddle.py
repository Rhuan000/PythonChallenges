from turtle import  Turtle,Screen, turtlesize

class Paddle(Turtle):
    def __init__(self, x_position):
        super().__init__()
        self.color('white')
        self.shape('square')
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=1, outline=1)
        self.setx(x_position)
        self.sety(0)

    def user_moverup(self):
        newy = self.ycor() + 20
        self.sety(newy)

    def user_moverdown(self):
        newy = self.ycor() -20
        self.sety(newy)
