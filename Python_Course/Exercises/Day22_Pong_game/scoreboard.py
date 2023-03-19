from turtle import Turtle

class Score(Turtle):
    def __init__(self,x,y):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.color('white')
        self.goto(x,y)

    def increase_score(self):
        self.score += 1

    def show_score(self):
        self.clear()
        self.write(self.score, move=False, align='left', font=('Arial', 40, 'normal'))

    class Lose(Turtle):
        def __init__(self):
            super().__init__()
            self.hideturtle()
            self.penup()
            self.color('yellow')

        def you_lose(self):
            self.clear()
            self.write(f'YOU LOSE.', move=False, align='center', font=('Arial', 50, 'normal'))
