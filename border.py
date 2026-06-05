from turtle import Turtle
from colors import Colors
import time


def draw_border(SETUP, start_callback=None):
    border = Turtle()
    border.hideturtle()
    border.speed(100000000)
    border.penup()
    border.color(Colors.BORDER)
    border.pensize(3)

    half_w = SETUP.WIDTH / 2 - SETUP.MOVE_DISTANCE / 2 + 1
    half_h = SETUP.HEIGHT / 2 - SETUP.MOVE_DISTANCE / 2 + 1

    border.goto(-half_w, half_h)
    border.pendown()
    border.speed(3)

    if start_callback is not None:
        start_callback()

    border.goto(half_w, half_h)
    time.sleep(0.2)
    border.goto(half_w, -half_h)
    time.sleep(0.2)
    border.goto(-half_w, -half_h)
    time.sleep(0.2)
    border.goto(-half_w, half_h)
    time.sleep(0.25)