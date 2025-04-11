from helper.groq_api import groq_title_divider, groq_prompt_gen
from pyautogui import click, moveTo, hotkey, size, hotkey, locateOnScreen, write, position
from time import sleep
import sys
from helper.find_image import find_image
from helper.pyscreensize import screenHeight, screenWidth
from pyperclip import copy

def doc_space_editor():
    num_of_times_to_space = int(input("Number of times to space (default: 5): ") or '5')
    click(find_image('images/tabs/seasoninspired_chrome.png', 0.8))
    # sleep(1)
    x, y = position()

    hotkey('enter')
    hotkey('enter')
    for i in range(num_of_times_to_space-1):
        # click(1500, y-((i+1)*19))
        hotkey('up')
        hotkey('up')
        hotkey('end')
        hotkey('enter')
        hotkey('enter')
