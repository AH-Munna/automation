from pyautogui import click, moveTo, hotkey, size, hotkey, locateOnScreen, write, position
from time import sleep
import sys
from helper.find_image import find_image
from helper.pyscreensize import screenHeight, screenWidth

def title_prepare():
    click(find_image('images/tabs/seasoninspired.png', 0.7))
    click(find_image('images/tabs/deepseek_title_prepare.png', 0.6), duration=0.5)

def pin_create():
    title_prepare()

    # click(find_image('images/tabs/deepseek_image_prompt.png', 0.6), duration=0.5)
    sleep(5)