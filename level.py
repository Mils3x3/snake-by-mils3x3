import time
from turtle import Turtle
from colors import Colors
from settings import DefaultSetup
from language import Text
from fonts import Fonts

SETUP = DefaultSetup()


class Levels(Turtle):
    def __init__(self, my_screen):
        super().__init__()
        self.my_screen = my_screen
        self.level = 1
        self.hideturtle()
        self.color(Colors.LEVEL)
        self.penup()
        self.setposition(SETUP.WIDTH / 2 - SETUP.MOVE_DISTANCE, SETUP.HEIGHT / 2 - 4)
        self.flash1 = True
        self.flash2 = True

    def level_clear(self):
        self.clear()
        self.write(f"{Text.LEVEL}: {self.level}", align="right", font=Fonts.LEVEL)

    def flash_0(self):
        if self.flash1:
            self.my_screen.bgcolor(Colors.FLASH_GREY)
            time.sleep(0.05)
            self.my_screen.bgcolor(Colors.BACKGROUND)
            return self.flash1
        
    def flash_1(self):
        if self.flash1:
            self.flash1 = False
            self.my_screen.bgcolor(Colors.FLASH_GREY)
            time.sleep(0.05)
            self.my_screen.bgcolor(Colors.BACKGROUND)
            self.flash2 = True
            return self.flash1

    def flash_2(self):
        if self.flash2:
            self.flash2 = False
            self.my_screen.bgcolor(Colors.FLASH_GREY)
            time.sleep(0.05)
            self.my_screen.bgcolor(Colors.BACKGROUND)
            self.flash1 = True
            return self.flash2