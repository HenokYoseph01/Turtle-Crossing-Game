from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self, color):
        super().__init__()
        self.penup()
        self.shape("turtle")
        self.color(color)
        self.goto(STARTING_POSITION)
        self.setheading(90)

    def move_up(self):
        self.fd(MOVE_DISTANCE)

    def reach_finish(self):
        self.goto(STARTING_POSITION)



