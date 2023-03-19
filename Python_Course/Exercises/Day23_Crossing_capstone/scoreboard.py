from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 0
        self.hideturtle()
        self.penup()
        self.goto(-280,250)



    def increase_score(self):
        self.level += 1

    def show_score(self):
        self.clear()
        self.write(f'Level: {self.level}', move=False, align='left', font=FONT)

    def you_lose(self):
        self.goto(0,0)
        self.clear()
        self.write(f'YOU LOSE.', move=False, align='center', font=('Arial', 50, 'normal'))

