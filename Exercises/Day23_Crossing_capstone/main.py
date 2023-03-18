import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)



player = Player()
screen.listen()
screen.onkey(player.move, 'Up')


level = Scoreboard()
car = CarManager()

game_is_on = True
while game_is_on:
    level.show_score()
    time.sleep(0.0001)
    screen.update()
    if len(car.all_cars) < 20:
        car.create_car()
    car.move()
    if player.ycor() >= 280:
        player.return_position()
        car.increase_speed()
        level.increase_score()

    for contact in car.all_cars[0:]:
        if contact.distance(player) < 20:
            game_is_on = False
            level.you_lose()
