import time
import random
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.title("Turtle Crossing")
color = screen.textinput("Pick your color","What color do you want your turtle to be?").lower()

if color == 'white':
    screen.bgcolor('black')

#Create Player
player = Player(color)

#Create Scoreboard
score = Scoreboard()

# Create car manager
car_manager = CarManager()

#Add Listeners
screen.listen()
screen.onkey(player.move_up,"Up")


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_car()

    #Detect collision with cars
    if len(car_manager.car_holder) > 0:
        for car in car_manager.car_holder:
            if player.distance(car) <18:
                game_is_on = False
                score.game_over()

    #Detect collision with finish line
    if player.ycor() > 280:
        player.reach_finish()
        score.increase_score()
        car_manager.increase_speed()




screen.exitonclick()