import tkinter as tk
import customtkinter as ctk
from colors import Colors
from window import create_menu_frame, close_menu
from language import Text
from fonts import Fonts


class Difficulty:
    def __init__(self, my_screen):
        self.my_screen = my_screen
        self.speed = None

        self.speeds = [0.26, 0.21, 0.17, 0.14, 0.12, 0.10, 0.08]
        self.difficulty_levels = list(zip(Text.DIFFICULTY_NAMES, self.speeds))

    def choose(self):
        done = tk.BooleanVar(value=False)

        canvas, frame, window_id = create_menu_frame(self.my_screen)

        menu_content = ctk.CTkFrame(frame, fg_color="transparent")
        menu_content.place(relx=0.5, rely=0.5, anchor="center")

        label = ctk.CTkLabel(
            menu_content,
            text=Text.CHOOSE_DIFFICULTY_LABEL,
            font=Fonts.MENU_LABEL,
            text_color=Colors.TEXT_PRIMARY
        )
        label.pack(pady=(0, 8))

        for name, speed in self.difficulty_levels:
            button = ctk.CTkButton(
                menu_content,
                text=name,
                width=230,
                height=35,
                font=Fonts.MENU_BUTTON,
                fg_color=Colors.BUTTON,
                hover_color=Colors.BUTTON_HOVER,
                text_color=Colors.BUTTON_TEXT,
                command=lambda selected_speed=speed: self.select_difficulty(
                    canvas,
                    frame,
                    window_id,
                    done,
                    selected_speed
                )
            )
            button.pack(pady=4)

        back_button = ctk.CTkButton(
            menu_content,
            text=Text.BACK_BUTTON,
            width=160,
            height=32,
            font=Fonts.MENU_BUTTON,
            fg_color=Colors.BACK_BUTTON,
            hover_color=Colors.BACK_BUTTON_HOVER,
            text_color=Colors.BACK_BUTTON_TEXT,
            command=lambda: self.go_back(canvas, frame, window_id, done)
        )
        back_button.pack(pady=(18, 0))

        canvas.wait_variable(done)

        return self.speed

    def select_difficulty(self, canvas, frame, window_id, done, selected_speed):
        self.speed = selected_speed
        close_menu(canvas, frame, window_id, done)

    def go_back(self, canvas, frame, window_id, done):
        self.speed = "back"
        close_menu(canvas, frame, window_id, done)