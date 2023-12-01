from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager():
    def __init__(self):
        self.car_holder = []
        self.move = STARTING_MOVE_DISTANCE

    def create_car(self):
        chance = random.randint(1, 6)
        if chance == 1:
            rand_ycor = random.randint(-250, 250)
            new_car = Turtle()
            new_car.penup()
            new_car.color(random.choice(COLORS))
            new_car.shape('square')
            new_car.turtlesize(stretch_wid=1, stretch_len=2)
            new_car.goto(320, rand_ycor)
            self.car_holder.append(new_car)

    def move_car(self):
        for car in self.car_holder:
            car.backward(self.move)

    def increase_speed(self):
        self.move += MOVE_INCREMENT



