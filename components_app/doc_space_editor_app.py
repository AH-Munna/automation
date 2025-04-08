from pyautogui import click, hotkey, hotkey, position
from helper.find_image import find_image

def doc_space_editor_app(num_of_line=5):
    click(find_image('images/tabs/seasoninspired_chrome.png', 0.8))

    hotkey('enter')
    hotkey('enter')
    for i in range(num_of_line-1):
        hotkey('up')
        hotkey('up')
        hotkey('end')
        hotkey('enter')
        hotkey('enter')
