import time
from turtle import Screen

from car_manager import CarManager
from player import Player
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
score = Scoreboard()
car = CarManager()

screen.listen()
screen.onkey(key="Up", fun=player.move_player)

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.create_car()
    car.move_car()
    for single_car in car.all_cars:
        if single_car.distance(player) < 25:
            score.game_over()
            game_is_on = False

    if player.ycor() > 270:
        score.update_level()
        player.reset_player_position()

screen.exitonclick()
