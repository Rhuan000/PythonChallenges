from turtle import  Screen
from my_snake_game import Snake,  Score, Food
import time

screen = Screen()
screen.bgcolor('darkblue')
screen.title('My Snake game')
screen.setup(width=600, height=600)
screen.tracer(0)


snake = Snake()
food = Food()
score = Score()

screen.listen()
screen.onkey(snake.up,'Up')
screen.onkey(snake.down,'Down')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')


game_is_on = True
food.random_food()

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    score.show_score()

    #increase score and snake size.
    if snake.head.distance(food) < 10:
        food.random_food()
        snake.increase_snake()
        score.increase_score()

    #detect colision with wall
    if snake.head.xcor() > 300 or snake.head.xcor() < -300 or snake.head.ycor() > 300 or snake.head.ycor() < -300:
        score.reset()
        snake.reset_snake()


    #detect colision with body
    for segment in snake.snakesize[1:]:
        if snake.head.distance(segment) < 10:
            score.reset()
            snake.reset_snake()

screen.exitonclick()