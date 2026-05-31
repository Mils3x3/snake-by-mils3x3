import random
from turtle import Turtle
from settings import DefaultSetup

SETUP = DefaultSetup()


class Apple(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.color("green")
        self.shape("circle")
        self.shapesize(0.80)
        self.w_max_num_20 = int((SETUP.WIDTH / SETUP.MOVE_DISTANCE) - 1)
        self.w_r_number = 0
        self.w_r_cord = 0
        self.h_max_num_20 = int((SETUP.WIDTH / SETUP.MOVE_DISTANCE) - 1)
        self.h_r_number = 0
        self.h_r_cord = 0

    def random_place(self):
        self.w_r_number = random.randint(1, self.w_max_num_20)
        self.w_r_cord = round((self.w_r_number * SETUP.MOVE_DISTANCE) - (SETUP.WIDTH / 2))
        self.h_r_number = random.randint(1, self.h_max_num_20)
        self.h_r_cord = round((self.h_r_number * SETUP.MOVE_DISTANCE) - (SETUP.WIDTH / 2))
        return self.w_r_cord, self.h_r_cord
