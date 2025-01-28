from pyautogui import click, moveTo, size, position
from helper.find_image import find_image
from helper.pyscreensize import screenHeight

def download_image(download_image_menu_loc):
    moveTo(download_image_menu_loc.left - 35, download_image_menu_loc.top + 25, duration=0.5)
    click()

    download_menu_loc = find_image('images/ideogram/download-option.png', 0.8)
    moveTo(download_menu_loc.left + 50, download_menu_loc.top + 20, duration=0.5)
    click()
    moveTo(position().x - 150, position().y - 10, duration=0.5)
    click()

def change_image(download_image_menu_loc, image_number):
    moveTo(download_image_menu_loc.left + 100, download_image_menu_loc.top + 100, duration=0.5)
    click()
    moveTo(download_image_menu_loc.left - 200 + (image_number * 75), download_image_menu_loc.top + 240, duration=0.5)
    click()

# code starto
def ideogram_download():
    click(find_image('images/tabs/seasoninspired_chrome.png', 0.8), duration=0.5)
    
    download_image_menu_loc = find_image('images/ideogram/menu-burger.png', 0.8)
    for i in range(4):
        change_image(download_image_menu_loc, i)
        download_image(download_image_menu_loc)