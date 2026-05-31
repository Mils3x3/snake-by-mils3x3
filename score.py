from turtle import Turtle
from settings import DefaultSetup

SETUP = DefaultSetup()


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.color("yellow")
        self.penup()
        self.setposition((SETUP.WIDTH / 2 - SETUP.MOVE_DISTANCE) * -1, SETUP.HEIGHT / 2 - 4)

    def clear_scores(self):
        self.clear()
        self.write(f"Score: {self.score}", align="left", font=('Arial', 16, 'normal'))
