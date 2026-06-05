import time
import os
import pygame
import random
import turtle
from turtle import Screen
from settings import DefaultSetup
from snake import SnakeBody
from apple import Apple
from level import Levels
from colors import Colors
from control import SnakeControl
from score import ScoreBoard
from countdown import CountDown
from border import draw_border
from window import choose_language, ready_to_play, ask_play_again
from sound import *
from difficulty import Difficulty
from lives import Lives, CrashMessage
from language import Text
from app_helpers import close_game_window, show_main_menu
from game_helpers import (
    save_snake_positions,
    restore_snake_positions,
    wait_for_safe_direction,
    get_safe_headings
)


ICON_PATH = resource_path("icon.ico")
SETUP = DefaultSetup()

original_turtle_root_init = turtle._Root.__init__

def hidden_turtle_root_init(self):
    original_turtle_root_init(self)
    self.withdraw()

turtle._Root.__init__ = hidden_turtle_root_init

my_screen = Screen()
GAME_WINDOW = my_screen.getcanvas().winfo_toplevel()
GAME_WINDOW.withdraw()

GAME_WINDOW.iconbitmap(ICON_PATH)
#GAME_WINDOW.resizable(False, False)

GAME_WINDOW.protocol("WM_DELETE_WINDOW", close_game_window)

SETUP.HEIGHT = SETUP.WIDTH
WINDOW_MARGIN = 30

my_screen.setup(
    width=SETUP.WIDTH + WINDOW_MARGIN * 2,
    height=SETUP.HEIGHT + WINDOW_MARGIN * 2
)

my_screen.bgcolor(Colors.BACKGROUND)
my_screen.title(Text.GAME_TITLE)
my_screen.update()

GAME_WINDOW.deiconify()
GAME_WINDOW.lift()
GAME_WINDOW.focus_force()

show_main_menu(my_screen)

again = True
while again:
    '''CREATE GAME'''
    difficulty = Difficulty(my_screen)
    SPEED = difficulty.choose()

    if SPEED == "back":
        show_main_menu(my_screen)
        continue

    if SPEED is None:
        close_game_window()
        
    my_screen.bgcolor(Colors.BACKGROUND)

    music1.set_volume(0.75)
    music_loop_length = music1.get_length()

    music_start_time_holder = [0]

    def start_music_with_border():
        play_tracks()
        music_start_time_holder[0] = time.perf_counter()

    draw_border(SETUP, start_music_with_border)

    music_start_time = music_start_time_holder[0]

    my_screen.listen()
    my_screen.tracer(0)

    countdown = CountDown()

    score_board = ScoreBoard()
    lives = Lives()
    level = Levels(my_screen)
    crash_message = CrashMessage()

    snake = SnakeBody()
    snake.hideturtle()

    apple = Apple()
    apple.hideturtle()

    '''START'''
    score_board.clear_scores()
    countdown.show_step(my_screen, "3")

    lives.show_lives()
    countdown.show_step(my_screen, "2")

    level.level_clear()
    countdown.show_step(my_screen, "1")

    snake.create_snake_body()
    countdown.show_step(my_screen, Text.COUNTDOWN_START)

    safe_positions = save_snake_positions(snake)
    safe_heading = snake.body[-1].heading()

    '''KEYBOARD CONTROL'''
    snake_control = SnakeControl(snake.body)

    my_screen.onkeypress(snake_control.go_up, "Up")
    my_screen.onkeypress(snake_control.go_down, "Down")
    my_screen.onkeypress(snake_control.go_left, "Left")
    my_screen.onkeypress(snake_control.go_right, "Right")

    my_screen.listen()

    apple_rand_x_cord, apple_rand_y_cord = apple.random_place()
    apple.goto(apple_rand_x_cord, apple_rand_y_cord)
    apple.showturtle()

    my_screen.update()

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
        hit_wall = (
            snake_head_xcor > SETUP.WIDTH / 2 - SETUP.MOVE_DISTANCE or
            snake_head_xcor < ((SETUP.WIDTH / 2) * -1) + SETUP.MOVE_DISTANCE or
            snake_head_ycor > SETUP.HEIGHT / 2 - SETUP.MOVE_DISTANCE or
            snake_head_ycor < ((SETUP.HEIGHT / 2) * -1) + SETUP.MOVE_DISTANCE
        )

        '''SNAKE COLLIDES WITH ITSELF'''
        hit_itself = (snake_head_xcor, snake_head_ycor) in zip(snake.body_x, snake.body_y)

        if hit_wall or hit_itself:
            snake.body_x.clear()
            snake.body_y.clear()

            lives.lose_life()

            if lives.lives == 0:
                game_is_on = False
                stop_tracks()

                random_end = random.choice(end_list)
                random_end.play(0)
                random_end.set_volume(0.7)

                for _ in range(2):
                    my_screen.bgcolor(Colors.CRASH_LIGHT)
                    time.sleep(0.4)
                    my_screen.bgcolor(Colors.CRASH_DARK)
                    time.sleep(0.4)

            else:
                restore_snake_positions(snake, safe_positions, safe_heading)

                safe_headings = get_safe_headings(snake, SETUP)

                if len(safe_headings) == 0:
                    lives.lose_all_lives()
                    game_is_on = False
                    stop_tracks()

                    random_end = random.choice(end_list)
                    random_end.play(0)
                    random_end.set_volume(0.7)

                    for _ in range(2):
                        my_screen.bgcolor(Colors.CRASH_LIGHT)
                        time.sleep(0.4)
                        my_screen.bgcolor(Colors.CRASH_DARK)
                        time.sleep(0.4)

                else:
                    crash_message.show_waiting_message(safe_headings)
                    level.flash_0()
                    crash_sound.play()
                    crash_sound.set_volume(0.15)
                    my_screen.update()

                    wait_for_safe_direction(my_screen, snake, snake_control, crash_message, safe_headings)

                    my_screen.bgcolor(Colors.BACKGROUND)
                    continue


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

            safe_positions = save_snake_positions(snake)
            safe_heading = snake.body[-1].heading()

            my_screen.update()
            snake.body[-1].forward(SETUP.MOVE_DISTANCE)
            snake.body[0].goto(snake_head_xcor, snake_head_ycor)
            last_pos = snake.body.pop(0)
            snake.body.insert(-1, last_pos)

            snake_control.reset_turn()

    my_screen.bgcolor(Colors.BACKGROUND)
    my_screen.update()

    another_game = ask_play_again(my_screen)

    if another_game == "yes":
        for segment in snake.body:
            segment.hideturtle()

        apple.hideturtle()
        score_board.hideturtle()
        level.hideturtle()
        lives.hideturtle()
        crash_message.hideturtle()

        my_screen.clearscreen()
        my_screen.bgcolor(Colors.BACKGROUND)
        my_screen.title(Text.GAME_TITLE)
        my_screen.update()

    elif another_game == "no":
        close_game_window()