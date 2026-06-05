import os
import pygame
from language import Text
from window import choose_language, ready_to_play, show_instructions
from sound import stop_tracks


def close_game_window():
    try:
        stop_tracks()
    except:
        pass

    try:
        pygame.mixer.quit()
    except:
        pass

    os._exit(0)


def show_main_menu(my_screen):
    while True:
        selected_option = ready_to_play(my_screen)

        if selected_option == "play":
            return

        elif selected_option == "instructions":
            show_instructions(my_screen)
            continue

        elif selected_option == "language":
            selected_language = choose_language(my_screen)

            if selected_language == "back":
                continue

            if selected_language is None:
                close_game_window()

            my_screen.title(Text.GAME_TITLE)

        elif selected_option == "exit":
            close_game_window()