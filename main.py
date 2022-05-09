import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

turtle_player = Player()

screen.listen()
screen.onkey(fun=turtle_player.move_up, key="Up")
screen.onkey(fun=turtle_player.move_down, key="Down")

car = CarManager()
scoreboard = Scoreboard()


game_is_on = True

while game_is_on: # what is in the while loop will refresh every 0.1 second 
    time.sleep(0.1)
    screen.update()
    car.create_car()
    car.move()

    # detect collision with car
    for vehicle in car.car_list:
        if turtle_player.distance(vehicle) < 20:
            scoreboard.game_over()
            game_is_on = False

    
    # detect collision with upper screen edge
    if turtle_player.ycor() > 290:
        scoreboard.increase_level()
        scoreboard.display_level()
        turtle_player.go_to_start()
        car.level_up()
        
        
        
        




screen.exitonclick()