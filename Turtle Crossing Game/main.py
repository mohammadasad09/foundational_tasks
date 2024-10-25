import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

scoreboard = Scoreboard()

screen.listen()

turtle_crosser = Player()

screen.onkey(turtle_crosser.move_up, "Up")
screen.onkey(turtle_crosser.move_down, "Down")

managing_car = CarManager()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    
    managing_car.create_car()
    managing_car.move_cars()

    for car in managing_car.all_cars:
        if car.distance(turtle_crosser) < 20:
            game_is_on = False
            scoreboard.game_over()
        
    if turtle_crosser.is_at_finish_line():
        turtle_crosser.go_to_start()
        managing_car.level_up()
        scoreboard.increase_level()

screen.exitonclick()