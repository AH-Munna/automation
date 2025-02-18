from groq_api import groq_title_divider, groq_prompt_gen
from pyautogui import click, moveTo, hotkey, size, hotkey, locateOnScreen, write, position
from time import sleep
import sys
from helper.find_image import find_image
from helper.pyscreensize import screenHeight, screenWidth
from pyperclip import copy

def doc_space_editor():
    x, y = position()