from pyautogui import click, hotkey, hotkey
from time import sleep
from helper.find_image import find_image
import sys

def doc_space_editor_app(num_of_line=5, browser_tab='season'):
    sleep(1)
    if browser_tab == 'season':
        click(find_image('images/tabs/seasoninspired_chrome.png', 0.8))
    elif browser_tab == 'voyager':
        click(find_image('images/tabs/voyager_chrome.png', 0.99))
    else:
        return

    hotkey('enter')
    hotkey('enter')
    for i in range(num_of_line-1):
        hotkey('up')
        hotkey('up')
        hotkey('end')
        hotkey('enter')
        hotkey('enter')
