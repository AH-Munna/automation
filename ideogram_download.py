from pyautogui import click, moveTo
from helper.find_image import find_image
from helper.play_audio import play_audio
from time import sleep
import sys
from threading import Thread


def change_image(image_number, download_button_const):
    download_button = find_image('images/ideogram/download_button.png', 0.95, 2, True)
    if download_button == None:
        click(download_button_const.left + 120, download_button_const.top, duration= 0.3)
        return change_image(image_number, download_button_const)

    moveTo(download_button.left - 160 + (image_number * 75), download_button.top + 270, duration=0.2)
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

    if find_image('images/ideogram/download_button.png', 0.8, 2, True) == None:
        change_image(image_number, download_button_const)
        return download_image(image_number, download_button_const)
    
    if find_image(f'images/ideogram/{image_number}.png', 0.8, 2, True) == None:
        change_image(image_number, download_button_const)
        return download_image(image_number, download_button_const)
    click()

# code starto
def ideogram_download(direct=False):
    if not direct:
        Thread(target=play_audio, args=('audio/ideogram_download_en.wav',), daemon=True).start()
        click(find_image('images/tabs/seasoninspired_chrome.png', 0.8))
    if direct:
        ideogram_creation_loc = find_image(image='images/ideogram/creation_completed.png', confidence=0.9, tries=40, long=True)
        moveTo(ideogram_creation_loc, duration=1)
        click()
        click(ideogram_creation_loc.left + 400, ideogram_creation_loc.top + 100, duration=1.5)
    
    download_button_const = find_image('images/ideogram/download_button.png', 0.8)

    for i in range(4):
        sleep(2)
        change_image(i, download_button_const)
        download_image(i, download_button_const)