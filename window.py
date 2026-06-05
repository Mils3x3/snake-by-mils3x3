import tkinter as tk
import customtkinter as ctk
from colors import Colors
from language import Text, set_language
from fonts import Fonts


ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")


def create_menu_frame(my_screen):
    canvas = my_screen.getcanvas()._canvas
    canvas.update_idletasks()

    width = 452
    height = 452

    frame = tk.Frame(
        canvas,
        width=width,
        height=height,
        bg=Colors.BACKGROUND,
        highlightthickness=0,
        bd=0
    )

    frame.pack_propagate(False)

    window_id = canvas.create_window(
        0,
        0,
        window=frame,
        anchor="center"
    )

    def keep_centered(event=None):
        if frame.winfo_exists():
            canvas.coords(window_id, 0, 0)

    canvas.bind("<Configure>", keep_centered, add="+")
    keep_centered()

    return canvas, frame, window_id


def close_menu(canvas, frame, window_id, done_variable):
    canvas.delete(window_id)
    frame.destroy()
    done_variable.set(True)


def ready_to_play(my_screen):
    selected_option = None
    done = tk.BooleanVar(value=False)

    canvas, frame, window_id = create_menu_frame(my_screen)

    def play_game():
        nonlocal selected_option
        selected_option = "play"
        close_menu(canvas, frame, window_id, done)

    def change_language():
        nonlocal selected_option
        selected_option = "language"
        close_menu(canvas, frame, window_id, done)

    def exit_game():
        nonlocal selected_option
        selected_option = "exit"
        close_menu(canvas, frame, window_id, done)

    def show_help():
        nonlocal selected_option
        selected_option = "instructions"
        close_menu(canvas, frame, window_id, done)

    menu_content = ctk.CTkFrame(frame, fg_color="transparent")
    menu_content.place(relx=0.5, rely=0.5, anchor="center")

    label = ctk.CTkLabel(
        menu_content,
        text=Text.READY_QUESTION,
        font=Fonts.MENU_LABEL,
        text_color=Colors.TEXT_PRIMARY
    )
    label.pack(pady=(0, 18))

    play_button = ctk.CTkButton(
        menu_content,
        text=Text.PLAY_BUTTON,
        width=180,
        height=35,
        font=Fonts.MENU_BUTTON,
        fg_color=Colors.BUTTON,
        hover_color=Colors.BUTTON_HOVER,
        text_color=Colors.BUTTON_TEXT,
        command=play_game
    )
    play_button.pack(pady=5)

    instructions_button = ctk.CTkButton(
        menu_content,
        text=Text.HOW_TO_PLAY_BUTTON,
        width=180,
        height=35,
        font=Fonts.MENU_BUTTON,
        fg_color=Colors.BUTTON,
        hover_color=Colors.BUTTON_HOVER,
        text_color=Colors.BUTTON_TEXT,
        command=show_help
    )
    instructions_button.pack(pady=(5))

    language_button = ctk.CTkButton(
        menu_content,
        text=Text.LANGUAGE_BUTTON,
        width=180,
        height=35,
        font=Fonts.MENU_BUTTON,
        fg_color=Colors.BUTTON,
        hover_color=Colors.BUTTON_HOVER,
        text_color=Colors.BUTTON_TEXT,
        command=change_language
    )
    language_button.pack(pady=5)

    exit_button = ctk.CTkButton(
        menu_content,
        text=Text.EXIT_BUTTON,
        width=180,
        height=35,
        font=Fonts.MENU_BUTTON,
        fg_color=Colors.EXIT_BUTTON,
        hover_color=Colors.EXIT_BUTTON_HOVER,
        text_color=Colors.BUTTON_TEXT,
        command=exit_game
    )
    exit_button.pack(pady=5)

    canvas.wait_variable(done)

    return selected_option


def choose_language(my_screen):
    selected_language = None
    done = tk.BooleanVar(value=False)

    canvas, frame, window_id = create_menu_frame(my_screen)

    def select_language(language_code):
        nonlocal selected_language
        selected_language = language_code
        set_language(language_code)
        close_menu(canvas, frame, window_id, done)

    def go_back():
        nonlocal selected_language
        selected_language = "back"
        close_menu(canvas, frame, window_id, done)

    menu_content = ctk.CTkFrame(frame, fg_color="transparent")
    menu_content.place(relx=0.5, rely=0.5, anchor="center")

    label = ctk.CTkLabel(
        menu_content,
        text=Text.CHOOSE_LANGUAGE_LABEL,
        font=Fonts.MENU_LABEL,
        text_color=Colors.TEXT_PRIMARY
    )
    label.pack(pady=(0, 15))

    english_button = ctk.CTkButton(
        menu_content,
        text=Text.ENGLISH_BUTTON,
        width=180,
        height=35,
        font=Fonts.MENU_BUTTON,
        fg_color=Colors.BUTTON,
        hover_color=Colors.BUTTON_HOVER,
        text_color=Colors.BUTTON_TEXT,
        command=lambda: select_language("en")
    )
    english_button.pack(pady=5)

    hungarian_button = ctk.CTkButton(
        menu_content,
        text=Text.HUNGARIAN_BUTTON,
        width=180,
        height=35,
        font=Fonts.MENU_BUTTON,
        fg_color=Colors.BUTTON,
        hover_color=Colors.BUTTON_HOVER,
        text_color=Colors.BUTTON_TEXT,
        command=lambda: select_language("hu")
    )
    hungarian_button.pack(pady=5)

    persian_button = ctk.CTkButton(
        menu_content,
        text=Text.PERSIAN_BUTTON,
        width=180,
        height=35,
        font=Fonts.MENU_BUTTON,
        fg_color=Colors.BUTTON,
        hover_color=Colors.BUTTON_HOVER,
        text_color=Colors.BUTTON_TEXT,
        command=lambda: select_language("fa")
    )
    persian_button.pack(pady=5)

    back_button = ctk.CTkButton(
        menu_content,
        text=Text.BACK_BUTTON,
        width=140,
        height=32,
        font=Fonts.MENU_BUTTON,
        fg_color=Colors.BACK_BUTTON,
        hover_color=Colors.BACK_BUTTON_HOVER,
        text_color=Colors.BACK_BUTTON_TEXT,
        command=go_back
    )
    back_button.pack(pady=(18, 0))

    canvas.wait_variable(done)

    return selected_language


def show_instructions(my_screen):
    canvas, frame, window_id = create_menu_frame(my_screen)
    done = tk.BooleanVar(value=False)

    menu_content = ctk.CTkFrame(frame, fg_color="transparent")
    menu_content.place(relx=0.5, rely=0.5, anchor="center")

    title_label = ctk.CTkLabel(
        menu_content,
        text=Text.INSTRUCTIONS_TITLE,
        font=Fonts.MENU_LABEL,
        text_color=Colors.TEXT_PRIMARY
    )
    title_label.pack(pady=(0, 18))

    instructions_label = ctk.CTkLabel(
        menu_content,
        text=Text.INSTRUCTIONS_TEXT,
        font=Fonts.MENU_BUTTON,
        text_color=Colors.TEXT_SECONDARY,
        justify="left",
        wraplength=360
    )
    instructions_label.pack(pady=(0, 22))

    back_button = ctk.CTkButton(
        menu_content,
        text=Text.BACK_BUTTON,
        width=160,
        height=32,
        font=Fonts.MENU_BUTTON,
        fg_color=Colors.BACK_BUTTON,
        hover_color=Colors.BACK_BUTTON_HOVER,
        text_color=Colors.BACK_BUTTON_TEXT,
        command=lambda: close_menu(canvas, frame, window_id, done)
    )
    back_button.pack()

    my_screen.getcanvas().wait_variable(done)


def ask_play_again(my_screen):
    answer = None
    done = tk.BooleanVar(value=False)

    canvas, frame, window_id = create_menu_frame(my_screen)

    def play_again():
        nonlocal answer
        answer = "yes"
        close_menu(canvas, frame, window_id, done)

    def exit_game():
        nonlocal answer
        answer = "no"
        close_menu(canvas, frame, window_id, done)

    label = ctk.CTkLabel(
        frame,
        text=Text.PLAY_AGAIN_QUESTION,
        font=Fonts.MENU_LABEL,
        text_color=Colors.TEXT_PRIMARY
    )
    label.pack(pady=(175, 15))

    button_frame = ctk.CTkFrame(frame, fg_color="transparent")
    button_frame.pack()

    play_again_button = ctk.CTkButton(
        button_frame,
        text=Text.PLAY_AGAIN_BUTTON,
        height=25,
        width=120,
        font=Fonts.MENU_BUTTON,
        fg_color=Colors.BUTTON,
        hover_color=Colors.BUTTON_HOVER,
        text_color=Colors.BUTTON_TEXT,
        command=play_again
    )
    play_again_button.pack(side="left", padx=8)

    exit_button = ctk.CTkButton(
        button_frame,
        text=Text.EXIT_BUTTON,
        height=25,
        width=120,
        font=Fonts.MENU_BUTTON,
        fg_color=Colors.EXIT_BUTTON,
        hover_color=Colors.EXIT_BUTTON_HOVER,
        text_color=Colors.BUTTON_TEXT,
        command=exit_game
    )
    exit_button.pack(side="left", padx=8)

    canvas.wait_variable(done)

    return answer