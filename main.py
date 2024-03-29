import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen() 
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()

screen.onkey(player.move, "Up")
screen.onkey(player.go_back, "Down")
screen.onkey(player.go_left, "Left")
screen.onkey(player.go_right, "Right")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.make_car()
    car_manager.move()

    for cars in car_manager.car_list:
        if cars.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

    if player.at_finish():
        player.go_start()
        scoreboard.increase_level()
        car_manager.level_up()
screen.exitonclick()
