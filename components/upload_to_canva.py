from pyautogui import click, moveTo, hotkey, hotkey, position, dragTo, rightClick, scroll
from helper.play_audio import play_audio
from time import sleep
import sys
from helper.find_image import find_image
from helper.pyscreensize import screenHeight
from threading import Thread

def upload_to_canva (number_of_image=4, downloaded_image_pos=0):
    # Thread(target=play_audio, args=('audio/upload_to_canva_en.wav',), daemon=True).start()

    # setup tabs
    # if number_of_image != 4:
    click(find_image('images/tabs/seasoninspired_chrome.png', 0.8), duration=0.5)

    click(find_image('images/tabs/canva.png', 0.9), duration=0.5)
    download_files = find_image('images/tabs/downloads_folder.png', 0.8)
    click(download_files, duration=0.5)

    # move to files
    todays_downloads = find_image('images/pin_upload/pic_select.png', 0.9)
    moveTo((todays_downloads.left + 9) + (downloaded_image_pos * 106), todays_downloads.top + 100, duration=0.3)
    # select files and paste to canva

    x, y = position()
    dragTo(x+ (number_of_image * 105), y + 30, duration=2)

    canva_controls = find_image('images/canva/canva_control.png', 0.9)
    dragTo(canva_controls.left + 100, canva_controls.top + 100, duration=1.5)
    sleep(number_of_image/1.5)

    # # clone images
    for i in range (number_of_image-1):
        click(canva_controls.left + 358, canva_controls.top + 15, duration=number_of_image/8)

    moveTo(canva_controls.left + 200, canva_controls.top + 400, duration=0.2)

    # organize canva
    for i in range (number_of_image):
        for j in range (number_of_image):
            if i == j:
                rightClick(duration=0.3)
                def set_as_background():
                    click(find_image("images/canva/set_as_backgroung.png", 0.9), duration=0.15)

                    if i == 0 and find_image("images/canva/set_as_backgroung.png", 0.9, 2, True) is not None:
                        return set_as_background()
                set_as_background()

            else:
                click(canva_controls.left + 200, canva_controls.top + 450, duration=0.15)
                hotkey('delete')
        if i != number_of_image-1:
            moveTo(canva_controls.left + 200, canva_controls.top + 450, duration=0.15)
            scroll(screenHeight-55)

    # delete uploaded images
    click(download_files, duration=0.2)
    hotkey('delete')