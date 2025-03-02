from pyautogui import click, moveTo
from helper.find_image import find_image
from time import sleep
import sys


def change_image(image_number, download_button_const):
    download_button = find_image('images/ideogram/download_button.png', 0.95, 2, True)
    if download_button == None:
        click(download_button_const.left + 120, download_button_const.top, duration= 0.3)
        return change_image(image_number, download_button_const)

    moveTo(download_button.left - 160 + (image_number * 75), download_button.top + 220, duration=0.2)
    download_button = find_image('images/ideogram/download_button.png', 0.95, 2, True)
    if download_button == None:
        click(download_button_const.left + 120, download_button_const.top, duration= 0.3)
        return change_image(image_number, download_button_const)
    click(duration=0.3)

def download_image(image_number, download_button_const):
    download_button_loc = find_image(image='images/ideogram/download_button.png', confidence=0.95, tries=2, no_exit=True)
    if download_button_loc == None:
        change_image(image_number, download_button_const)
        return download_image(image_number, download_button_const)
    
    moveTo(download_button_loc, duration=0.3)

    if find_image('images/ideogram/download_button.png', 0.95, 2, True) == None:
        change_image(image_number, download_button_const)
        return download_image(image_number, download_button_const)
    
    if find_image(f'images/ideogram/{image_number}.png', 0.9, 2, True) == None:
        change_image(image_number, download_button_const)
        return download_image(image_number, download_button_const)
    click()

    # old ideogram
    # download_button = find_image('images/ideogram/download_button.png', 0.8)
    # moveTo(download_button.left - 35, download_button.top + 25, duration=0.3)
    # download_menu_loc = find_image('images/ideogram/download-option.png', 0.8, 2, no_exit=True)
    # if download_menu_loc == None:
    #     return download_image()
    # moveTo(download_menu_loc.left + 60, download_menu_loc.top + 25, duration=0.2)
    # click()

# code starto
def ideogram_download(direct=False):
    if not direct:
        click(find_image('images/tabs/seasoninspired_chrome.png', 0.8))
    sleep(1)
    if direct:
        ideogram_creation_loc = find_image('images/ideogram/creation_completed.png', 0.9, 50)
        moveTo(ideogram_creation_loc, duration=1)
        click()
        click(ideogram_creation_loc.left + 400, ideogram_creation_loc.top + 100, duration=1.5)
    
    download_button_const = find_image('images/ideogram/download_button.png', 0.8)

    for i in range(4):
        sleep(2)
        change_image(i, download_button_const)
        download_image(i, download_button_const)