import time
from turtle import Turtle
from language import Text
from colors import Colors
from fonts import Fonts


class CountDown(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color(Colors.TEXT_PRIMARY)

    def show_countdown_text(self, text):
        self.clear()
        self.goto(0, 25)
        self.write(
            text,
            align="center",
            font=Fonts.COUNTDOWN
        )

    def wait_step(self, my_screen, duration=0.581):
        end_time = time.perf_counter() + duration

        while time.perf_counter() < end_time:
            my_screen.update()
            time.sleep(0.01)

    def show_step(self, my_screen, text, duration=0.581):
        self.show_countdown_text(text)
        self.wait_step(my_screen, duration)
        self.clear()
        my_screen.update()