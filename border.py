from turtle import Screen, Turtle
from settings import DefaultSetup
import time

def draw_border(SETUP):
    border = Turtle()
    border.hideturtle()
    border.speed(100000000)
    border.penup()
    border.color("gray40")
    border.pensize(3)

    half_w = SETUP.WIDTH / 2 - SETUP.MOVE_DISTANCE / 2 + 1
    half_h = SETUP.HEIGHT / 2 - SETUP.MOVE_DISTANCE / 2 + 1

    border.goto(-half_w, half_h)
    border.pendown()
    border.speed(3)
    border.goto(half_w, half_h)
    time.sleep(0.2)
    border.goto(half_w, -half_h)
    time.sleep(0.2)
    border.goto(-half_w, -half_h)
    time.sleep(0.2)
    border.goto(-half_w, half_h)
    time.sleep(0.2)
