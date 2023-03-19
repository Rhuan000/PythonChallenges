from scoreboard import Score
from turtle import Screen
from paddle import Paddle
from ball import Ball
import time

screen = Screen()
screen.tracer(0)
screen.title('Pong')
screen.bgcolor('black')
screen.setup(width=800, height=600)

is_on = True
user1 = Paddle(350)
user2 = Paddle(-350)
ball = Ball()
score_user1 = Score(100, 240)
score_user2 = Score(-100, 240)

screen.listen()
screen.onkey(user1.user_moverup, 'Up')
screen.onkey(user1.user_moverdown, 'Down')
screen.onkey(user2.user_moverup, 'w')
screen.onkey(user2.user_moverdown, 's')



while is_on:
    screen.update()
    ball.move()
    time.sleep(ball.speed)
    score_user1.show_score()
    score_user2.show_score()

    # User 2 Point
    if ball.xcor() >= 360:
        score_user2.increase_score()
        ball.initial_position()
        screen.update()
        time.sleep(0.5)

    # User 1 Point
    if ball.xcor() <= -360:
        score_user1.increase_score()
        ball.initial_position()
        screen.update()
        time.sleep(0.5)

    # Contact with wall.
    if ball.ycor() >= 280 or ball.ycor() <= -280:
        ball.wall_contact()

    #Contact with user.
    elif user1.distance(ball.pos()) <= 50 and ball.xcor() >= 340 or user2.distance(ball.pos()) <= 50 and ball.xcor() <= -340:
        ball.user_contact()









screen.exitonclick()
