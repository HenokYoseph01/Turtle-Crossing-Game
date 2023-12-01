from turtle import Turtle
FONT = ("Courier", 12, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.level = 1
        self.goto(-240,260)
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Level: {self.level}",align="center",font=FONT)

    def increase_score(self):
        self.level += 1
        self.update_score()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center",font=("Courier", 20, "bold"))

