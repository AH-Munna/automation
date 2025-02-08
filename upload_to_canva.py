from pyautogui import click, moveTo, hotkey, size, hotkey, locateOnScreen, write, position
from time import sleep
import sys
from helper.find_image import find_image
from helper.pyscreensize import screenHeight, screenWidth

def upload_to_canva ():
    print("wip...")
    sys.exit()
    click(find_image('images/tabs/downloads_folder.png', 0.8), duration=1)


    selectable_image_loc = find_image('images/pin_upload/pic_select_2.png', 0.8)
    click(selectable_image_loc.left + 80, selectable_image_loc.top + 40, duration=0.5)
