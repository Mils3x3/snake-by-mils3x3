from turtle import Turtle
from colors import Colors
from settings import DefaultSetup

SETUP = DefaultSetup()


class SnakeBody(Turtle):
    def __init__(self):
        super().__init__()
        self.body_x = []
        self.body_y = []
        self.body = []

    def create_snake_body(self):
        snake_length = 5

        for segment in range(snake_length):
            snake = SnakeBody()
            snake.shape("square")
            snake.shapesize(0.90)
            snake.color(Colors.SNAKE_BODY)
            snake.penup()
            snake.speed("fastest")

            x_position = (segment - snake_length + 1) * SETUP.MOVE_DISTANCE
            snake.goto(x_position, 0)

            self.body.append(snake)

        self.body[-1].color(Colors.SNAKE_HEAD_OUTLINE)
        self.body[-1].fillcolor(Colors.SNAKE_HEAD)
        
    def add_snake_segment(self):
        add_snake = SnakeBody()
        add_snake.shape("square")
        add_snake.color(Colors.SNAKE_BODY)
        add_snake.shapesize(0.90)
        add_snake.penup()
        add_snake.goto(self.body[0].xcor(), self.body[0].ycor())
        self.body.insert(0, add_snake)
