from turtle import Turtle
class Score(Turtle):
    
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.goto(-290,270)
        self.color('yellow')
        self.high_score = 0


    def increase_score(self):
        self.score += 1
        self.show_score()

    def show_score(self):
        self.clear()
        self.write(f'Score: {self.score}, high score: {self.high_score}', move=False, align='left', font=('Arial', 15, 'normal'))

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.show_score()

