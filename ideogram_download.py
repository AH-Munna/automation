from pyautogui import click, moveTo, size, position
from helper.find_image import find_image
from helper.pyscreensize import screenHeight
from time import sleep
import sys

def download_image(download_image_menu_loc):
    click(download_image_menu_loc.left - 35, download_image_menu_loc.top + 25, duration=0.3)

    download_menu_loc = find_image('images/ideogram/download-option.png', 0.8)
    click(download_menu_loc.left + 60, download_menu_loc.top + 25, duration=0.3)

def change_image(download_image_menu_loc, image_number):
    click(download_image_menu_loc.left + 100, download_image_menu_loc.top + 100, duration=0.3)
    sleep(0.5)
    click(download_image_menu_loc.left + 100, download_image_menu_loc.top + 105, duration=0.3)

    click(download_image_menu_loc.left - 200 + (image_number * 75), download_image_menu_loc.top + 240, duration=0.3)


# code starto
def ideogram_download():
    click(find_image('images/tabs/seasoninspired_chrome.png', 0.8))
    sleep(1)
    # ideogram_creation_loc = find_image('images/ideogram/creation_completed.png', 0.9, 30)
    # click(ideogram_creation_loc, duration=1)
    # click(ideogram_creation_loc.left + 400, ideogram_creation_loc.top + 100, duration=1.5)
    
    download_image_menu_loc = find_image('images/ideogram/menu-burger.png', 0.8)
    for i in range(4):
        change_image(download_image_menu_loc, i)
        download_image(download_image_menu_loc)