from pyautogui import click, moveTo, hotkey, size, hotkey, write, position, doubleClick
from time import sleep
from helper.find_image import find_image
from helper.pyscreensize import screenHeight
# import sys

def create_new():
    click(find_image('images/pin_upload/new-pin.png', 0.8))
    click(find_image('images/pin_upload/pic-upload.png', 0.8))

    slectable_image_loc = find_image('images/pin_upload/pic-select.png', 0.8)
    click(slectable_image_loc.left + 150, slectable_image_loc.top + 150)
    hotkey('delete')
    doubleClick()

def paste_texts(board_name, board_pos):
    def handle_clipboard(image_name, top=0):
        input_loc = find_image(image_name, 0.8)
        moveTo(input_loc.left + 100, input_loc.top + 50)
        click()
        hotkey('ctrl', 'a')
        hotkey('win', 'v')
        clipboard_loc = find_image('images/clipboard.png', 0.8)
        moveTo(clipboard_loc.left+150, clipboard_loc.top+top)
        click()

    handle_clipboard('images/pin_upload/pin-title.png', 330)
    handle_clipboard('images/pin_upload/pin-description.png', 250)
    handle_clipboard('images/pin_upload/pin-link.png', 180)

    # board
    pin_board_location = find_image('images/pin_upload/pin-board.png', 0.8)
    moveTo(pin_board_location.left + 200, pin_board_location.top + 40)
    click()
    pin_search_location = find_image('images/pin_upload/pin-search.png', 0.8)
    moveTo(pin_search_location.left + 200, pin_search_location.top + 40)
    click()
    hotkey('ctrl', 'a')
    write(board_name)
    current_left, current_top = position()
    moveTo(current_left + 100, current_top + (board_pos * 50), duration=0.2)
    click()

# code starto
def pinterest_upload():
    num_of_image = int(input("Number of images: "))
    board_name = input("Board name: ")
    board_pos = int(input("Board position: "))

    click(find_image('images/tabs/pinterest_chrome.png', 0.8))

    for i in range(num_of_image):
        create_new()
        sleep(0.5)
        paste_texts(board_name, board_pos)
        print("Image", i+1, "uploaded")