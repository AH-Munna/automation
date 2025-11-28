from pyautogui import click, moveTo, hotkey, hotkey, write, position, doubleClick
from time import sleep
from helper.find_image import find_image
from helper.get_path import get_resource_path
from helper.play_audio import play_audio
import sys

def create_new(new_update=False, os='windows'):
    if os == 'ubuntu':
        click(find_image(get_resource_path('images/ubuntu/downloads_folder_ubuntu.png'), 0.8), duration=0.5)
        editable_files_quick_list_loc = find_image(get_resource_path('images/ubuntu/3/file_quick_list.png'))
        click(editable_files_quick_list_loc.left + 290, editable_files_quick_list_loc.top + 10, duration=0.5)
        sleep(0.2)
        hotkey('delete')
        sleep(0.2)
    
        click(find_image(get_resource_path('images/tabs/firefox.png'), 0.8), duration=0.5)
        sleep(0.2)
        click(find_image(get_resource_path('images/ubuntu/pinterest_browser_tab.png'), 0.8), duration=0.5)

    if new_update:
        click(find_image(get_resource_path('images/pin_upload/new_pin_new.png'), 0.8), duration=0.5)
    else:
        click(find_image(get_resource_path('images/pin_upload/new_pin.png'), 0.8), duration=0.2)

    if new_update:
        if os == 'windows':
            click(find_image(get_resource_path('images/pin_upload/pic_upload_new.png'), 0.8), duration=0.5)
        elif os == 'ubuntu':
            click(find_image(get_resource_path('images/ubuntu/3/upload_a_pin.png'), 0.8), duration=0.5)
        else:
            raise ValueError("Unsupported OS. Please use 'windows' or 'ubuntu'.")
    else:
        click(find_image(get_resource_path('images/pin_upload/pic_upload.png'), 0.8), duration=0.5)

    if os == 'windows':
        selectable_image_loc = find_image(get_resource_path('images/pin_upload/pic_select_2.png'), 0.8)
        click(selectable_image_loc.left + 120, selectable_image_loc.top + 60, duration=0.5)
        sleep(0.2)
        hotkey('delete')
        sleep(0.2)
        doubleClick()
    elif os == 'ubuntu':
        if find_image(get_resource_path('images/ubuntu/3/file_quick_list.png'), 0.8, 4, True) is not None:
            hotkey('enter')
        else:
            raise ValueError("File select menu not found.")
    else:
        raise ValueError("Unsupported OS. Please use 'windows' or 'ubuntu'.")

def paste_texts(board_name, board_pos, new_update=False, os='windows'):
    def handle_clipboard(image_name, top=0):
        input_loc = find_image(get_resource_path(image_name), 0.8)
        click(input_loc.left + 100, input_loc.top + 50, duration=0.5)
        hotkey('ctrl', 'a')
        hotkey('win', 'v')
        clipboard_loc = find_image(get_resource_path('images/clipboard.png'), 0.8)
        click(clipboard_loc.left+150, clipboard_loc.top+top, duration=0.5)
    def handle_ubuntu_clipboard(image_name, top=0):
        input_loc = find_image(get_resource_path(image_name), 0.8)
        click(input_loc.left + 100, input_loc.top + 60, duration=0.5)
        hotkey('ctrl', 'a')
        # hotkey ctrl alt h in ubuntu
        hotkey('ctrl', 'alt', 'g')
        sleep(0.2)
        clipboard_loc = find_image(get_resource_path('images/ubuntu/3/clipboard.png'), 0.8)
        click(clipboard_loc.left + 300, clipboard_loc.top - 15 + top, duration=0.5)
        sleep(0.2)
        hotkey('ctrl', 'v')

    if os == 'windows':
        handle_clipboard('images/pin_upload/pin-title.png', 330)
        handle_clipboard('images/pin_upload/pin-description.png', 250)
        handle_clipboard('images/pin_upload/pin-link.png', 180)
    elif os == 'ubuntu':
        handle_ubuntu_clipboard('images/ubuntu/3/pin-title.png', 100)
        handle_ubuntu_clipboard('images/pin_upload/pin-description.png', 100)
        handle_ubuntu_clipboard('images/pin_upload/pin-link.png', 100)
    else:
        raise ValueError("Unsupported OS. Please use 'windows' or 'ubuntu'.")

    # board
    pin_board_location = find_image(get_resource_path('images/pin_upload/pin-board.png'), 0.8)
    click(pin_board_location.left + 200, pin_board_location.top + 40, duration=0.5)
    if new_update:
        pin_search_location = find_image(get_resource_path('images/pin_upload/pin-search-new.png'), 0.8)
    else:
        pin_search_location = find_image(get_resource_path('images/pin_upload/pin-search.png'), 0.8)
    click(pin_search_location.left + 200, pin_search_location.top + 40, duration=0.5)

    sleep(0.2)
    hotkey('ctrl', 'a')
    write(board_name, 0.1)
    sleep(0.5)
    current_left, current_top = position()
    moveTo(current_left - 120, current_top + (board_pos * 50), duration=0.5)
    click()

# code starto
def pinterest_upload_app(num_of_image, board_name, board_pos=1, new_update=False, os='windows'):
    """
    Uploads a specified number of images to a Pinterest board.

    Parameters:
    - num_of_image (int): Number of images to upload.
    - board_name (str): Name of the Pinterest board.
    - board_pos (int, optional): Position of the board (default is 1).
    - new_update (bool, optional): Whether to use new update settings.
    """
    # play_audio('audio/pinterest_upload_en.wav')
    if os == 'windows':
        click(find_image(get_resource_path('images/tabs/pinterest_chrome.png'), 0.8))
    elif os == 'ubuntu':
        pass
    else:
        raise ValueError("Unsupported OS. Please use 'windows' or 'ubuntu'.")

    for i in range(num_of_image):
        create_new(new_update, os=os)
        sleep(0.5)
        paste_texts(board_name, board_pos, new_update, os=os)
        print(f"Image {i+1} uploaded")
        sleep(2)