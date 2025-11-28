from pyautogui import click, moveTo, hotkey, hotkey, position, dragTo, rightClick, scroll
from helper.get_path import get_resource_path
from helper.play_audio import play_audio
from time import sleep
import sys
from helper.find_image import find_image
from helper.pyscreensize import screenHeight
from threading import Thread

# windows required canva zoom 41%
# ubuntu required canva zoom 36%

def find_canva_controls(os):
    if os == "windows":
        canva_control_find = find_image(get_resource_path('images/canva/canva_control.png'), 0.95)
    elif os == "ubuntu":
        canva_control_find = find_image(get_resource_path('images/canva/canva_control_ubuntu.png'), 0.98)
    else:
        raise Exception("OS not supported")
    if canva_control_find is not None:
        return canva_control_find
    else:
        raise Exception("Canva controls not found, please check your canva zoom level")

def upload_to_canva (number_of_image=4, downloaded_image_pos=0, os="windows"):
    print(os, number_of_image, downloaded_image_pos, screenHeight)
    # Thread(target=play_audio, args=('audio/upload_to_canva_en.wav',), daemon=True).start()

    if os == "windows":
        click(find_image(get_resource_path('images/tabs/seasoninspired_chrome.png'), 0.8), duration=0.5)
        download_files = find_image(get_resource_path('images/tabs/downloads_folder_windows.png'), 0.8)
    elif os == "ubuntu":
        click(find_image(get_resource_path('images/tabs/firefox.png'), 0.8), duration=0.5)
        download_files = find_image(get_resource_path('images/ubuntu/downloads_folder_ubuntu.png'), 0.8)
    else:
        raise Exception("OS not supported")

    click(find_image(get_resource_path('images/tabs/canva.png'), 0.9), duration=0.5)

    # click(download_files, duration=0.5)
    # todays_downloads = find_image(get_resource_path('images/pin_upload/pic_select.png'), 0.9)
    # moveTo((todays_downloads.left + 9) + (downloaded_image_pos * 106), todays_downloads.top + 100, duration=0.3)
    # x, y = position()
    # dragTo(x+ (number_of_image * 105), y + 30, duration=1)

    canva_controls = find_canva_controls(os)
    # dragTo(canva_controls.left + 100, canva_controls.top + 100, duration=1.5)

    # # clone images
    for i in range (number_of_image-1):
        click(canva_controls.left + 358, canva_controls.top + 17, duration=0.5)

    if os == "windows":
        moveTo(canva_controls.left + 230, canva_controls.top + 450, duration=0.5)
    elif os == "ubuntu":
        moveTo(canva_controls.left + 280, canva_controls.top + 450, duration=0.5)
    else:
        raise Exception("OS not supported")

    # organize canva
    for i in range (number_of_image):
        for j in range (number_of_image):
            if i == j:
                rightClick(duration=0.3)
                def set_as_background():
                    click(find_image("images/canva/set_as_backgroung.png", 0.9, no_exit=True if i == 0 else False), duration=0.1)

                    if i == 0 and find_image("images/canva/set_as_backgroung.png", 0.9, 2, True) is not None:
                        return set_as_background()
                set_as_background()

            else:
                if os == "windows":
                    click(canva_controls.left + 230, canva_controls.top + 450, duration=0.15)
                elif os == "ubuntu":
                    click(canva_controls.left + 280, canva_controls.top + 450, duration=0.15)
                hotkey('delete')
        if i != number_of_image-1:
            if os == "windows":
                moveTo(canva_controls.left + 230, canva_controls.top + 450, duration=0.15)
            elif os == "ubuntu":
                moveTo(canva_controls.left + 280, canva_controls.top + 450, duration=0.15)
            if os == "windows":
                scroll(screenHeight - 59)
            elif os == "ubuntu":
                    sleep(1)
                    if (i%5) == 0 and i !=0:
                        scroll(8)
                    else:
                        scroll(9)
            else:
                raise Exception("OS not supported")

    # delete uploaded images
    if os == "windows":
        click(download_files, duration=0.2)
        hotkey('delete')