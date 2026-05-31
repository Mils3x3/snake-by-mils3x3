from turtle import Turtle
from settings import DefaultSetup

SETUP = DefaultSetup()


class SnakeBody(Turtle):
    def __init__(self):
        super().__init__()
        self.body_x = []
        self.body_y = []
        self.body = []

    def create_snake_body(self):
        for segment in range(5):
            snake = SnakeBody()
            snake.shape("square")
            snake.shapesize(0.90)
            snake.color("white")
            snake.penup()
            snake.speed("fastest")
            snake.goto(segment * SETUP.MOVE_DISTANCE, 0)
            self.body.append(snake)
        self.body[-1].color("red")
        self.body[-1].fillcolor("black")

    def add_snake_segment(self):
        add_snake = SnakeBody()
        add_snake.shape("square")
        add_snake.color("white")
        add_snake.shapesize(0.90)
        add_snake.penup()
        self.body.insert(0, add_snake)
