from pyautogui import click, moveTo, size, position
from helper.find_image import find_image
from helper.pyscreensize import screenHeight
from time import sleep
import sys

def download_image():
    # if find_image('images/ideogram/browswer_download_popup.png', 0.8, 2, no_exit=True):
    #     click(download_image_menu_loc.left + 100, download_image_menu_loc.top + 100)
    download_image_menu_loc = find_image('images/ideogram/menu-burger.png', 0.8)
    moveTo(download_image_menu_loc.left - 35, download_image_menu_loc.top + 25, duration=0.3)
    click()

    download_menu_loc = find_image('images/ideogram/download-option.png', 0.8, 2, no_exit=True)
    if download_menu_loc == None:
        return download_image(download_image_menu_loc)
    moveTo(download_menu_loc.left + 60, download_menu_loc.top + 25, duration=0.2)
    click()

def change_image(image_number):
    # if find_image('images/ideogram/browswer_download_popup.png', 0.8, 2, no_exit=True):
    download_image_menu_loc = find_image('images/ideogram/menu-burger.png', 0.8)
    if image_number == 1:
        moveTo(download_image_menu_loc.left + 100, download_image_menu_loc.top + 100, duration=2)
    else:
        moveTo(download_image_menu_loc.left + 100, download_image_menu_loc.top + 100)
    click()

    moveTo(download_image_menu_loc.left - 200 + (image_number * 75), download_image_menu_loc.top + 240, duration=0.2)
    click()


# code starto
def ideogram_download(direct=False):
    if not direct:
        click(find_image('images/tabs/seasoninspired_chrome.png', 0.8))
    sleep(1)
    if direct:
        ideogram_creation_loc = find_image('images/ideogram/creation_completed.png', 0.9, 30)
        moveTo(ideogram_creation_loc, duration=1)
        click()
        click(ideogram_creation_loc.left + 400, ideogram_creation_loc.top + 100, duration=1.5)
    
    for i in range(4):
        change_image(i)
        download_image()