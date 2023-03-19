from turtle import Turtle
import random

STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_CONSTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


class Snake():

    def __init__(self):
        self.snakesize = []
        self.create_snake()
        self.head = self.snakesize[0]
        self.tail = self.snakesize[len(self.snakesize) - 1]

    def snake(self, position):
        new_square = Turtle(shape='square')
        new_square.color('white')
        new_square.penup()
        new_square.speed(0)
        new_square.goto(position)
        self.snakesize.append(new_square)

    def create_snake(self):
        for position in STARTING_POSITION:
           self.snake(position)

    def increase_snake(self):
        self.snake(self.snakesize[-1].position())

    def move(self):
        for snk_num in range(len(self.snakesize) - 1, 0, -1):
            new_x = self.snakesize[snk_num - 1].xcor()
            new_y = self.snakesize[snk_num - 1].ycor()
            self.snakesize[snk_num].goto(new_x, new_y)
        self.head.forward(MOVE_CONSTANCE)

    def right(self):
        if self.head.heading() == LEFT:
            pass
        else:
            self.head.setheading(RIGHT)

    def up(self):
        if self.head.heading() == DOWN:
            pass
        else:
            self.head.setheading(UP)

    def left(self):
        if self.head.heading() == RIGHT:
            pass
        else:
            self.head.setheading(LEFT)

    def down(self):
        if self.head.heading() == UP:
            pass
        else:
            self.head.setheading(DOWN)

    def reset_snake(self):
        for seg in self.snakesize:
            seg.goto(1000,1000)

        self.snakesize.clear()
        self.create_snake()
        self.head = self.snakesize[0]

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


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.high_score = 0
        with open('data.txt') as data:
            self.high_score = int(data.read())
        self.score = 0
        self.hideturtle()
        self.penup()
        self.goto(-290, 270)
        self.color('yellow')

    def increase_score(self):
        self.score += 1



    def show_score(self):
        self.clear()
        self.write(f'Score: {self.score}, high score: {self.high_score}', move=False, align='left',font=('Arial', 15, 'normal'))

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        with open('data.txt', mode='w') as data:
            data.write(str(self.high_score))
        self.score = 0
        self.show_score()
        with open('data.txt', mode='w') as data:
            data.write(str(self.high_score))



