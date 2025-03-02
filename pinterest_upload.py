from pyautogui import click, moveTo, hotkey, size, hotkey, write, position, doubleClick
from time import sleep
from helper.find_image import find_image
from helper.pyscreensize import screenHeight
import sys

def create_new():
    click(find_image('images/pin_upload/new_pin.png', 0.8), duration=0.2)
    click(find_image('images/pin_upload/pic_upload.png', 0.8), duration=0.2)

    # selectable_image_loc = find_image('images/pin_upload/pic_select.png', 0.8)
    selectable_image_loc = find_image('images/pin_upload/pic_select_2.png', 0.8)
    click(selectable_image_loc.left + 120, selectable_image_loc.top + 60, duration=0.2)
    # sleep(0.3)
    hotkey('delete')
    sleep(0.3)
    doubleClick()
    # sleep(0.3)

def paste_texts(board_name, board_pos):
    def handle_clipboard(image_name, top=0):
        input_loc = find_image(image_name, 0.8)
        click(input_loc.left + 100, input_loc.top + 50, duration=0.2)
        hotkey('ctrl', 'a')
        hotkey('win', 'v')
        clipboard_loc = find_image('images/clipboard.png', 0.8)
        click(clipboard_loc.left+150, clipboard_loc.top+top, duration=0.2)

    handle_clipboard('images/pin_upload/pin-title.png', 330)
    handle_clipboard('images/pin_upload/pin-description.png', 250)
    handle_clipboard('images/pin_upload/pin-link.png', 180)

    # board
    pin_board_location = find_image('images/pin_upload/pin-board.png', 0.8)
    click(pin_board_location.left + 200, pin_board_location.top + 40, duration=0.2)
    pin_search_location = find_image('images/pin_upload/pin-search.png', 0.8)
    click(pin_search_location.left + 200, pin_search_location.top + 40, duration=0.2)

    hotkey('ctrl', 'a')
    write(board_name)
    sleep(0.5)
    current_left, current_top = position()
    moveTo(current_left - 120, current_top + (board_pos * 50), duration=0.2)
    # sleep(0.5)
    click()

# code starto
def pinterest_upload():
    num_of_image = int(input("Number of images: "))
    board_name = input("Board name: ")
    board_pos = int(input("Board position (default 1): ") or '1')

    click(find_image('images/tabs/pinterest_chrome.png', 0.8))

    for i in range(num_of_image):
        create_new()
        sleep(0.5)
        paste_texts(board_name, board_pos)
        print("Image", i+1, "uploaded")
        sleep(1)