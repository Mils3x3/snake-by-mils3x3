from turtle import Turtle
import time


class CountDown(Turtle):
    def __init__(self):
        super().__init__()

    def countdown(self, my_screen):
        for number in range(3, 0, -1):
            for font_size in range(5, 60):
                time.sleep(0.0058)
                self.color("White")
                self.shapesize(10)
                self.hideturtle()
                self.penup()
                self.goto(x=0, y=-font_size + 80)
                self.write(arg=number, align="center", font=('Arial', font_size, 'normal'), move=False)
                my_screen.update()
                self.reset()
        for font_size in range(5, 60):
            time.sleep(0.0058)
            self.color("White")
            self.shapesize(10)
            self.hideturtle()
            self.penup()
            self.goto(x=0, y=-font_size + 80)
            self.write(arg="Start", align="center", font=('Arial', font_size, 'normal'), move=False)
            my_screen.update()
            self.reset()
