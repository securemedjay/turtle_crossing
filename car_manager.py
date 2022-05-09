from turtle import Turtle
import random


COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5
STARTING_X = 310
MINIMUM_Y = -250
MAXIMUM_Y = 250

class CarManager:
    
    def __init__(self):
        self.car_list = []
        self.car_speed = STARTING_MOVE_DISTANCE


    def create_car(self):
        if random.randint(1,6) == 3:
            car = Turtle("square")
            # car.shape("square")
            car.shapesize(stretch_wid=1, stretch_len=2)
            car.color(random.choice(COLORS))
            car.penup()
            car.setposition(STARTING_X, random.randint(MINIMUM_Y, MAXIMUM_Y))
            self.car_list.append(car)


    def move(self):
        for car in self.car_list:
            car.backward(self.car_speed)


    def level_up(self):
        self.car_speed += MOVE_INCREMENT
