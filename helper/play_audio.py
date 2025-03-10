import pygame
import time
pygame.mixer.init()

def play_audio(audio_path, wait=False):
    pygame.mixer.music.load(audio_path)
    pygame.mixer.music.play()

    if wait:
        while pygame.mixer.music.get_busy():
            time.sleep(1)