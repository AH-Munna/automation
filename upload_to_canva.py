from pyautogui import click, moveTo, hotkey, size, hotkey, locateOnScreen, write, position
from time import sleep
import sys
from helper.find_image import find_image
from helper.pyscreensize import screenHeight, screenWidth

def upload_to_canva ():
    click(find_image('images/tabs/downloads_folder.png', 0.8), duration=1)