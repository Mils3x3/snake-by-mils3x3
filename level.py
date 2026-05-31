from turtle import Turtle, Screen
import time
from settings import DefaultSetup

SETUP = DefaultSetup()
my_screen = Screen()


class Levels(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.color("orange")
        self.penup()
        self.setposition(SETUP.WIDTH / 2 - SETUP.MOVE_DISTANCE, SETUP.HEIGHT / 2 - 4)
        self.flash1 = True
        self.flash2 = True

    def level_clear(self):
        self.clear()
        self.write(f"Level: {self.level}", align="right", font=('Arial', 16, 'normal'))

    def flash_1(self):
        if self.flash1:
            self.flash1 = False
            my_screen.bgcolor("#555555")
            time.sleep(0.05)
            my_screen.bgcolor("black")
            self.flash2 = True
            return self.flash1

    def flash_2(self):
        if self.flash2:
            self.flash2 = False
            my_screen.bgcolor("#555555")
            time.sleep(0.05)
            my_screen.bgcolor("black")
            self.flash1 = True
            return self.flash2
