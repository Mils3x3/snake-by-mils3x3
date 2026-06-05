from turtle import Turtle
from colors import Colors
from settings import DefaultSetup
from language import Text
from fonts import Fonts

SETUP = DefaultSetup()


class Lives(Turtle):
    def __init__(self):
        super().__init__()
        self.lives = 3
        self.hideturtle()
        self.penup()
        self.color(Colors.LIVES)
        self.goto(0, SETUP.HEIGHT / 2 - 4)

    def show_lives(self):
        self.clear()
        self.write(f"{Text.LIVES}: {self.lives}", align="center", font=Fonts.LIVES)

    def lose_life(self):
        self.lives -= 1
        self.show_lives()

    def lose_all_lives(self):
        self.lives = 0
        self.show_lives()
        

class CrashMessage(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color(Colors.TEXT_PRIMARY)

    def show_waiting_message(self, safe_headings):
        self.clear()
        self.goto(0, -SETUP.HEIGHT / 2 - 23)

        direction_names = []

        for heading in safe_headings:
            direction_names.append(Text.DIRECTION_NAMES[heading])

        directions_text = Text.DIRECTION_SEPARATOR.join(direction_names)
        direction_text = Text.PRESS_DIRECTIONS.format(directions=directions_text)

        self.write(
            f"{Text.LIFE_LOST}  {direction_text}",
            align="center",
            font=Fonts.CRASH_MESSAGE
        )

    def clear_message(self):
        self.clear()