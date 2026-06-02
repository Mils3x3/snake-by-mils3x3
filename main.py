import time
import tkinter as tk
from turtle import Screen, Turtle
from settings import DefaultSetup
from score import ScoreBoard
from control import SnakeControl
from snake import SnakeBody
from apple import Apple
from level import Levels
from countdown import CountDown
from border import draw_border
from sound import *
from window import ready_to_play, ask_play_again
import random

ICON_PATH = resource_path("icon.ico")
SETUP = DefaultSetup()

my_screen = Screen()
my_screen.getcanvas().winfo_toplevel().iconbitmap(ICON_PATH)
SETUP.HEIGHT = SETUP.WIDTH
WINDOW_MARGIN = 30

my_screen.setup(
    width=SETUP.WIDTH + WINDOW_MARGIN * 2,
    height=SETUP.HEIGHT + WINDOW_MARGIN * 2
)

my_screen.bgcolor("black")
my_screen.title("Snake by Mils3x3")
start = ready_to_play(ICON_PATH)

if not start:
    my_screen.bye()
    quit()

again = True
while again:
    '''CREATE GAME'''
    SPEED = 0.12
    my_screen.bgcolor("black")

    play_tracks()
    music1.set_volume(0.75)
    music_start_time = time.perf_counter()
    music_loop_length = music1.get_length()
    
    draw_border(SETUP)
    my_screen.listen()
    my_screen.tracer(0)
    countdown = CountDown()

    apple = Apple()
    score_board = ScoreBoard()
    level = Levels()
    snake = SnakeBody()
    snake.hideturtle()
    snake.create_snake_body()

    '''KEYBOARD CONTROL'''
    snake_control = SnakeControl(snake.body)

    my_screen.onkeypress(snake_control.go_up, "Up")
    my_screen.onkeypress(snake_control.go_down, "Down")
    my_screen.onkeypress(snake_control.go_left, "Left")
    my_screen.onkeypress(snake_control.go_right, "Right")

    '''START'''
    apple_rand_x_cord, apple_rand_y_cord = apple.random_place()
    apple.goto(apple_rand_x_cord, apple_rand_y_cord)
    countdown.countdown(my_screen)
    countdown.hideturtle()

    game_is_on = True
    while game_is_on:
        score_board.clear_scores()
        level.level_clear()
        snake_head_xcor = round(snake.body[-1].xcor())
        snake_head_ycor = round(snake.body[-1].ycor())

        for i in range(len(snake.body)):
            s_b_x = snake.body[i].xcor()
            s_b_y = snake.body[i].ycor()
            snake.body_x.append(s_b_x)
            snake.body_y.append(s_b_y)
        snake.body_x.pop(-1)
        snake.body_y.pop(-1)

        '''OUT OF BORDER'''
        if (snake_head_xcor > SETUP.WIDTH / 2 - SETUP.MOVE_DISTANCE or
                snake_head_xcor < ((SETUP.WIDTH / 2) * - 1) + SETUP.MOVE_DISTANCE or
                snake_head_ycor > SETUP.HEIGHT / 2 - SETUP.MOVE_DISTANCE or
                snake_head_ycor < ((SETUP.HEIGHT / 2) * - 1) + SETUP.MOVE_DISTANCE):
            game_is_on = False
            stop_tracks()
            random_end = random.choice(end_list)
            random_end.play(0)
            random_end.set_volume(0.7)

            for _ in range(2):
                my_screen.bgcolor("red3")
                time.sleep(0.4)
                my_screen.bgcolor("red4")
                time.sleep(0.4)

            '''SNAKE COLLIDES WITH ITSELF'''
        elif (snake_head_xcor, snake_head_ycor) in zip(snake.body_x, snake.body_y):
            game_is_on = False
            stop_tracks()
            random_end = random.choice(end_list)
            random_end.play(0)
            random_end.set_volume(0.5)

            for _ in range(2):
                my_screen.bgcolor("red3")
                time.sleep(0.4)
                my_screen.bgcolor("red4")
                time.sleep(0.4)

        else:
            snake_body_x_backup = snake.body_x.copy()
            snake_body_y_backup = snake.body_y.copy()
            snake.body_x.clear()
            snake.body_y.clear()
            my_screen.update()

            '''EATING APPLE'''
            if apple_rand_x_cord == snake_head_xcor and apple_rand_y_cord == snake_head_ycor:
                time.sleep(0.1)
                apple_rand_x_cord, apple_rand_y_cord = apple.random_place()
                apple.goto(apple_rand_x_cord, apple_rand_y_cord)

                while (
                    (apple_rand_x_cord, apple_rand_y_cord) in zip(snake_body_x_backup, snake_body_y_backup)
                    or (apple_rand_x_cord, apple_rand_y_cord) == (snake_head_xcor, snake_head_ycor)
                ):
                    apple_rand_x_cord, apple_rand_y_cord = apple.random_place()
                    apple.goto(apple_rand_x_cord, apple_rand_y_cord)

                snake.add_snake_segment()
                score_board.score += 1
                bite_sounds(music_start_time, music_loop_length, score_board)

            '''LEVELS'''
            if score_board.score < 10:
                time.sleep(SPEED)
            elif 10 <= score_board.score < 20:
                level.level = 2
                if level.flash1:
                    level.flash1 = level.flash_1()
                    SPEED *= SETUP.SPEED_UP
                    fade_in(music2, target_volume=1, duration=2)
                time.sleep(SPEED)
            elif 20 <= score_board.score < 30:
                level.level = 3
                if level.flash2:
                    level.flash2 = level.flash_2()
                    SPEED *= SETUP.SPEED_UP
                    fade_in(music3, target_volume=1, duration=2)
                time.sleep(SPEED)
            elif 30 <= score_board.score < 40:
                level.level = 4
                if level.flash1:
                    level.flash1 = level.flash_1()
                    SPEED *= SETUP.SPEED_UP
                    fade_in(music4, target_volume=1, duration=2)
                time.sleep(SPEED)
            elif 40 <= score_board.score < 50:
                level.level = 5
                if level.flash2:
                    level.flash2 = level.flash_2()
                    SPEED *= SETUP.SPEED_UP
                    fade_in(music5, target_volume=1, duration=2)
                time.sleep(SPEED)
            elif 50 <= score_board.score < 60:
                level.level = 6
                if level.flash1:
                    level.flash1 = level.flash_1()
                    SPEED *= SETUP.SPEED_UP
                    fade_in(music6, target_volume=1, duration=2)
                time.sleep(SPEED)
            elif 60 <= score_board.score < 70:
                level.level = 7
                if level.flash2:
                    level.flash2 = level.flash_2()
                    SPEED *= SETUP.SPEED_UP
                    fade_in(music7, target_volume=1, duration=2)
                time.sleep(SPEED)
            elif 70 <= score_board.score < 80:
                level.level = 8
                if level.flash1:
                    level.flash1 = level.flash_1()
                    SPEED *= SETUP.SPEED_UP
                    fade_in(music8, target_volume=1, duration=2)
                time.sleep(SPEED)
            elif 80 <= score_board.score < 90:
                level.level = 9
                if level.flash2:
                    level.flash2 = level.flash_2()
                    SPEED *= SETUP.SPEED_UP
                    fade_in(music9, target_volume=1, duration=2)
                time.sleep(SPEED)
            elif 90 <= score_board.score < 100:
                level.level = 10
                if level.flash1:
                    level.flash1 = level.flash_1()
                    SPEED *= SETUP.SPEED_UP
                    fade_in(music10, target_volume=1, duration=2)
                time.sleep(SPEED)

            snake.body[-1].forward(SETUP.MOVE_DISTANCE)
            snake.body[0].goto(snake_head_xcor, snake_head_ycor)
            last_pos = snake.body.pop(0)
            snake.body.insert(-1, last_pos)

            snake_control.reset_turn()

    another_game = ask_play_again(ICON_PATH)

    if another_game == "yes":
        for segment in snake.body:
            segment.hideturtle()

        apple.hideturtle()
        score_board.hideturtle()
        level.hideturtle()

        my_screen.clearscreen()

    elif another_game == "no":
        again = False
        my_screen.bye()