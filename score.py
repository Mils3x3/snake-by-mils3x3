from turtle import Turtle
from colors import Colors
from settings import DefaultSetup
from language import Text
from fonts import Fonts

SETUP = DefaultSetup()


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.color(Colors.SCORE)
        self.penup()
        self.setposition((SETUP.WIDTH / 2 - SETUP.MOVE_DISTANCE) * -1, SETUP.HEIGHT / 2 - 4)

    def clear_scores(self):
        self.clear()
        self.write(f"{Text.SCORE}: {self.score}", align="left", font=Fonts.SCORE)