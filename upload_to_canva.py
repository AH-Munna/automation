from pyautogui import click, moveTo, hotkey, size, hotkey, locateOnScreen, write, position, dragTo, rightClick, scroll
from time import sleep
import sys
from helper.find_image import find_image
from helper.pyscreensize import screenHeight, screenWidth

def upload_to_canva ():
    # setup tabs
    click(find_image('images/tabs/canva.png', 0.9), duration=1)
    download_files = find_image('images/tabs/downloads_folder.png', 0.8)
    click(download_files, duration=1)

    # move to files
    # todays_downloads = find_image('images/files/image_captions.png', 0.3, 3)
    todays_downloads = find_image('images/pin_upload/pic_select_2.png', 0.7)
    moveTo(todays_downloads.left + 45, todays_downloads.top + 50, duration=1)

    # select files and paste to canva
    x, y = position()
    dragTo(x+400, y + 10, duration=1)
    canva_controls = find_image('images/canva/canva_control.png', 0.9)

    dragTo(canva_controls.left + 100, canva_controls.top + 100, duration=1.5)
    sleep(1)

    # # clone images
    for i in range (3):
        click(canva_controls.left + 358, canva_controls.top + 15, duration=1)

    moveTo(canva_controls.left + 200, canva_controls.top + 400, duration=1)

    # organize canva
    for i in range (4):
        for j in range (4):
            if i == j:
                rightClick(duration=1)
                def set_as_background():
                    click(find_image("images/canva/set_as_backgroung.png", 0.9), duration=1)

                    if find_image("images/canva/set_as_backgroung.png", 0.9, 2, True) is not None:
                        return set_as_background()
                set_as_background()

            else:
                click(canva_controls.left + 200, canva_controls.top + 450, duration=1)
                hotkey('delete')
        if i != 3:
            moveTo(canva_controls.left + 200, canva_controls.top + 450, duration=1)
            scroll(screenHeight-80)

    # delete uploaded images
    click(download_files, duration=1)
    hotkey('delete')