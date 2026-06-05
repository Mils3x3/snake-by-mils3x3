# Snake by Mils3x3

A modular, multilingual Python Snake game built with **Python Turtle**, **CustomTkinter**, and **Pygame**.

This project started as a classic Snake game and gradually became a more complete portfolio project with a custom menu system, difficulty selection, level progression, a three-life system, collision recovery logic, synchronised music layers, dynamic bite sound effects, and Windows executable support.

---

## Project Overview

**Snake by Mils3x3** is a custom Snake game written in Python.

The game uses:

- **Python Turtle** for the main game graphics
- **CustomTkinter / Tkinter** for embedded menu interfaces
- **Pygame Mixer** for music and sound effects

The main goal of this project is to demonstrate practical Python programming skills through a complete playable game, including modular code structure, object-oriented game components, event handling, collision logic, audio timing, resource handling, and portfolio-ready project organisation.

---

## Key Features

- Classic Snake gameplay built with Python Turtle
- Modular Python project structure split across multiple files
- Embedded CustomTkinter menus inside the Turtle game window
- Main menu with Play, Language, and Exit options
- Multilingual interface support:
  - English
  - Hungarian
  - Persian / Farsi
- Difficulty selection with seven named difficulty levels
- Centralised text management in `language.py`
- Centralised colour palette in `colors.py`
- Centralised font settings in `fonts.py`
- Score, level, and lives display
- Three-life system
- Smart collision recovery after losing a life
- Safe-direction detection after wall or self-collision
- Automatic game over if no safe direction is available
- Border collision detection
- Self-collision detection
- Random apple placement with checks to avoid the snake body and head
- Keyboard control with queued direction changes
- Animated border drawing
- Rhythmic countdown sequence before gameplay starts
- Apple appears only when the game actually begins
- Increasing speed as the player reaches higher levels
- Pygame-based sound and music system
- Multiple synchronised looping background music tracks
- Fade-in music layers as the player reaches new levels
- Dynamic apple bite sounds based on the current music loop position
- Random game-over sounds
- Replay support after game over
- Resource path handling for normal Python runs and PyInstaller builds
- Clean exit handling for the Windows executable version

---

## Controls

| Key | Action |
| --- | --- |
| Up Arrow | Move up |
| Down Arrow | Move down |
| Left Arrow | Move left |
| Right Arrow | Move right |

---

## Project Structure

```text
snake-by-mils3x3/
│
├── README.md
├── COPYRIGHT.md
├── requirements.txt
├── .gitignore
│
├── main.py
├── app_helpers.py
├── game_helpers.py
│
├── apple.py
├── border.py
├── colors.py
├── control.py
├── countdown.py
├── difficulty.py
├── fonts.py
├── language.py
├── level.py
├── lives.py
├── score.py
├── settings.py
├── snake.py
├── sound.py
├── window.py
│
├── icon.ico
│
├── sounds/
│   ├── track1.ogg
│   ├── track2.ogg
│   ├── ...
│   ├── track10.ogg
│   ├── small_bite1.ogg
│   ├── small_bite2.ogg
│   ├── small_bite3.ogg
│   ├── big_bite1.ogg
│   ├── big_bite2.ogg
│   ├── big_bite3.ogg
│   ├── end1.ogg
│   ├── end2.ogg
│   └── ...
│
└── screenshots/
    └── snake-game-demo.gif
```

---

## Main Files

| File | Purpose |
| --- | --- |
| `main.py` | Main gameplay flow, object creation, main game loop, level progression, replay flow |
| `app_helpers.py` | Main menu handling and application exit helper |
| `game_helpers.py` | Snake position saving, safe-direction checks, and collision recovery helpers |
| `snake.py` | Snake body creation and new segment handling |
| `apple.py` | Random apple placement |
| `control.py` | Keyboard direction control and queued turn logic |
| `score.py` | Score display |
| `level.py` | Level display and level flash effects |
| `lives.py` | Lives display and crash / safe-direction message handling |
| `countdown.py` | Rhythmic countdown display before gameplay starts |
| `border.py` | Animated border drawing, synchronised with music start |
| `difficulty.py` | Difficulty selection menu and speed settings |
| `language.py` | Multilingual text system |
| `colors.py` | Centralised colour palette |
| `fonts.py` | Centralised font settings |
| `sound.py` | Music loading, sound effects, fade-in logic, game-over audio, and resource paths |
| `window.py` | Embedded CustomTkinter menus inside the Turtle canvas |
| `settings.py` | Basic game settings such as board size, movement distance, and speed multiplier |

---

## Requirements

- Python 3.11+
- Pygame
- CustomTkinter

Python Turtle and Tkinter are included with the standard Python installation on most Windows Python installations.

Install the external dependencies:

```bash
pip install -r requirements.txt
```

Example `requirements.txt`:

```txt
pygame>=2.6.0
customtkinter>=5.2.0
```

---

## How to Run

Clone the repository:

```bash
git clone https://github.com/mils3x3/snake-by-mils3x3.git
cd snake-by-mils3x3
```

Install requirements:

```bash
pip install -r requirements.txt
```

Run the game:

```bash
python main.py
```

---

## Windows Executable

A Windows executable version may be provided under the **GitHub Releases** section.

The executable can be built from the Python source code using PyInstaller.

> Note: The Windows executable is not digitally signed. Windows SmartScreen or antivirus software may show a warning for unsigned Python executables, even when the file is safe.

---

## Audio System

The project uses **Pygame Mixer** for music and sound effects.

The background music system starts multiple looped music tracks at the same time and keeps them synchronised. Most tracks start with their volume set to zero and fade in when the player reaches specific score ranges and levels.

The apple bite sound system checks the current position of the music loop and selects a different bite sound depending on where the music is within the loop. This creates a more rhythmic and dynamic sound effect system instead of playing the same sound every time.

---

## Audio and Assets

The background music tracks and apple bite sound effects were created by **Milan Olah / Mils3x3** for this project.

The game-over sounds use third-party / meme-style audio clips sourced from YouTube-style internet meme sounds. They are included only as part of this personal portfolio/demo project and are not claimed as original work.

Anyone who wants to reuse or adapt this project should replace those third-party / meme-style audio files with their own licensed or original sound effects.

Audio, icons, and other media assets included in this repository are not licensed for reuse, redistribution, modification, or commercial use without permission from the relevant rights holders.

---

## Screenshots

<img src="https://raw.githubusercontent.com/mils3x3/snake-by-mils3x3/main/screenshots/snake-game-demo.gif" alt="Snake by Mils3x3 gameplay demo" width="460">

Make sure the screenshot or GIF file is stored in the repository at:

```text
screenshots/snake-game-demo.gif
```

---

## Project Status

This project is considered complete as a portfolio version.

Possible future improvements:

- replacing third-party meme-style game-over sounds with fully original sound effects
- adding high-score saving
- adding a pause option
- adding a settings menu
- adding more visual themes
- refactoring the game into a dedicated `Game` class
- creating a more advanced Windows installer

---

## Author

**Milan Olah / Mils3x3**  
GitHub: `@mils3x3`

---

## Copyright

Copyright © 2026 Milan Olah / Mils3x3. All rights reserved.

This repository is provided as a personal programming portfolio project. The source code may be viewed for educational, portfolio review, and recruitment purposes. Audio and media assets are not licensed for reuse unless explicitly stated.

See [`COPYRIGHT.md`](COPYRIGHT.md) for more details.
