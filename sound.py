import time
import pygame
import sys
from pathlib import Path
import threading


def resource_path(relative_path):
    if getattr(sys, "frozen", False):
        base_path = Path(sys._MEIPASS)

        direct_path = base_path / relative_path
        import_path = base_path / "import" / relative_path

        if direct_path.exists():
            return direct_path
        return import_path

    return Path(__file__).parent / relative_path


def sound_path(filename):
    return str(resource_path(f"sounds/{filename}"))


def play_tracks():
    pygame.mixer.stop()
    music1.play(-1)
    music2.play(-1)
    music3.play(-1)
    music4.play(-1)
    music5.play(-1)
    music6.play(-1)
    music7.play(-1)
    music8.play(-1)
    music9.play(-1)
    music10.play(-1)
    music2.set_volume(0)
    music3.set_volume(0)
    music4.set_volume(0)
    music5.set_volume(0)
    music6.set_volume(0)
    music7.set_volume(0)
    music8.set_volume(0)
    music9.set_volume(0)
    music10.set_volume(0)


def stop_tracks():
    music1.stop()
    music2.stop()
    music3.stop()
    music4.stop()
    music5.stop()
    music6.stop()
    music7.stop()
    music8.stop()
    music9.stop()
    music10.stop()


def bite_sounds(music_start_time, music_loop_length, score_board):
    loop_position = (time.perf_counter() - music_start_time) % music_loop_length
    loop_part = loop_position / music_loop_length

    if score_board.score % 10 == 0:
        if 0 <= loop_part < 0.25 or 0.50 <= loop_part < 0.75:
            big_bite1.set_volume(0.6)
            big_bite1.play(0)
        elif 0.25 <= loop_part < 0.50:
            big_bite2.set_volume(0.6)
            big_bite2.play(0)
        else:
            big_bite3.set_volume(0.6)
            big_bite3.play(0)
    else:
        if 0 <= loop_part < 0.25 or 0.50 <= loop_part < 0.75:
            small_bite1.set_volume(0.6)
            small_bite1.play(0)
        elif 0.25 <= loop_part < 0.50:
            small_bite2.set_volume(0.6)
            small_bite2.play(0)
        else:
            small_bite3.set_volume(0.6)
            small_bite3.play(0) 


def fade_in(sound, target_volume=1.0, duration=1.5, steps=30):
    def run():
        for i in range(steps + 1):
            volume = target_volume * (i / steps)
            sound.set_volume(volume)
            time.sleep(duration / steps)

    threading.Thread(target=run, daemon=True).start()


pygame.mixer.init()
pygame.mixer.set_num_channels(16)

music1 = pygame.mixer.Sound(sound_path("track1.ogg"))
music2 = pygame.mixer.Sound(sound_path("track2.ogg"))
music3 = pygame.mixer.Sound(sound_path("track3.ogg"))
music4 = pygame.mixer.Sound(sound_path("track4.ogg"))
music5 = pygame.mixer.Sound(sound_path("track5.ogg"))
music6 = pygame.mixer.Sound(sound_path("track6.ogg"))
music7 = pygame.mixer.Sound(sound_path("track7.ogg"))
music8 = pygame.mixer.Sound(sound_path("track8.ogg"))
music9 = pygame.mixer.Sound(sound_path("track9.ogg"))
music10 = pygame.mixer.Sound(sound_path("track10.ogg"))

small_bite1 = pygame.mixer.Sound(sound_path("small_bite1.ogg"))
small_bite2 = pygame.mixer.Sound(sound_path("small_bite2.ogg"))
small_bite3 = pygame.mixer.Sound(sound_path("small_bite3.ogg"))

big_bite1 = pygame.mixer.Sound(sound_path("big_bite1.ogg"))
big_bite2 = pygame.mixer.Sound(sound_path("big_bite2.ogg"))
big_bite3 = pygame.mixer.Sound(sound_path("big_bite3.ogg"))

end1 = pygame.mixer.Sound(sound_path("end1.ogg"))
end2 = pygame.mixer.Sound(sound_path("end2.ogg"))
end3 = pygame.mixer.Sound(sound_path("end3.ogg"))
end4 = pygame.mixer.Sound(sound_path("end4.ogg"))
end5 = pygame.mixer.Sound(sound_path("end5.ogg"))
end6 = pygame.mixer.Sound(sound_path("end6.ogg"))
end7 = pygame.mixer.Sound(sound_path("end7.ogg"))
end8 = pygame.mixer.Sound(sound_path("end8.ogg"))
end9 = pygame.mixer.Sound(sound_path("end9.ogg"))
end10 = pygame.mixer.Sound(sound_path("end10.ogg"))
end11 = pygame.mixer.Sound(sound_path("end11.ogg"))
end12 = pygame.mixer.Sound(sound_path("end12.ogg"))
end13 = pygame.mixer.Sound(sound_path("end13.ogg"))
end14 = pygame.mixer.Sound(sound_path("end14.ogg"))
end15 = pygame.mixer.Sound(sound_path("end15.ogg"))
end16 = pygame.mixer.Sound(sound_path("end16.ogg"))
end17 = pygame.mixer.Sound(sound_path("end17.ogg"))
end18 = pygame.mixer.Sound(sound_path("end18.ogg"))
end19 = pygame.mixer.Sound(sound_path("end19.ogg"))
end20 = pygame.mixer.Sound(sound_path("end20.ogg"))
end21 = pygame.mixer.Sound(sound_path("end21.ogg"))
end22 = pygame.mixer.Sound(sound_path("end22.ogg"))
end23 = pygame.mixer.Sound(sound_path("end23.ogg"))
end24 = pygame.mixer.Sound(sound_path("end24.ogg"))
end25 = pygame.mixer.Sound(sound_path("end25.ogg"))
end26 = pygame.mixer.Sound(sound_path("end26.ogg"))
end_list = [end1, end2, end3, end4, end5, end6, end7, end8, end9, end10, end11, end12, end13, end14, end15, end16, end17, end18, end19, end20, end21, end22, end23, end24, end25, end26]