import tkinter as tk


def ready_to_play(icon_path):
    ready = False

    def start_game():
        nonlocal ready
        ready = True
        window.destroy()

    def close_window():
        nonlocal ready
        ready = False
        window.destroy()

    window = tk.Toplevel()
    window.iconbitmap(str(icon_path))
    window.config(padx=15, pady=15)
    window.title("")

    window.protocol("WM_DELETE_WINDOW", close_window)
    window.title("Snake by Mils3x3")

    label = tk.Label(window, text="Are you ready to play?")
    label.grid(row=0, column=0, columnspan=2)

    start_button = tk.Button(window, text="Start!", width=16, command=start_game)
    start_button.grid(row=1, column=0, padx=10, pady=10)

    exit_button = tk.Button(window, text="Exit", width=16, command=close_window)
    exit_button.grid(row=1, column=1, padx=10, pady=10)

    window.update_idletasks()

    width = window.winfo_width()
    height = window.winfo_height()

    x = (window.winfo_screenwidth() // 2) - (width // 2)
    y = (window.winfo_screenheight() // 2) - (height // 2)

    window.geometry(f"{width}x{height}+{x}+{y}")

    window.wait_window()

    return ready


def ask_play_again(icon_path):
    answer = None

    def play_again():
        nonlocal answer
        answer = "yes"
        window.destroy()

    def exit_game():
        nonlocal answer
        answer = "no"
        window.destroy()

    window = tk.Toplevel()
    window.iconbitmap(str(icon_path))
    window.config(padx=15, pady=15)
    window.title("Snake by Mils3x3")

    label = tk.Label(window, text="Do you want to play again?")
    label.grid(row=0, column=0, columnspan=2)

    play_again_button = tk.Button(window, text="Play again", width=16, command=play_again)
    play_again_button.grid(row=1, column=0, padx=10, pady=10)

    exit_button = tk.Button(window, text="Exit", width=16, command=exit_game)
    exit_button.grid(row=1, column=1, padx=10, pady=10)

    window.update_idletasks()

    width = window.winfo_width()
    height = window.winfo_height()

    x = (window.winfo_screenwidth() // 2) - (width // 2)
    y = (window.winfo_screenheight() // 2) - (height // 2)

    window.geometry(f"{width}x{height}+{x}+{y}")

    window.wait_window()

    return answer