from pyautogui import click, moveTo, hotkey
from helper.get_path import get_resource_path
from helper.pyscreensize import screenHeight, screenWidth
from time import sleep
import sys
# from pandas import read_clipboard, read_csv
# from pyperclip import paste
from helper.find_image import find_image
from helper.play_audio import play_audio


def select_next_pin():
    # selected_pin_loc = find_image('images/pin_upload/pin-selected.png', 0.8)
    # moveTo(selected_pin_loc.left + 50, selected_pin_loc.top + 50)
    moveTo(150, 500)
    click()
    
def copy_tag (tag_num, notepad_loc):
    click(notepad_loc)

    moveTo(18, 85 + (tag_num * 36))
    # if tag_num is not 0:
    #     hotkey('down')

    # hotkey('end')
    # sleep(0.5)
    # hotkey('ctrl', 'shift', 'left')
    # sys.exit()

    click(clicks=3)
    hotkey('ctrl', 'c')

def paste_tag (browswer_loc):
    click(browswer_loc)

    tagbox_loc = find_image(get_resource_path('images/tagbox-warning.png'), 0.6)
    click(tagbox_loc.left + 100, tagbox_loc.top - 35)
    hotkey('ctrl', 'a')
    hotkey('ctrl', 'v')

    matched_tags_loc = find_image(get_resource_path('images/matched-tags.png'), 0.6)
    click(matched_tags_loc.left + 50, matched_tags_loc.top + 60)

def publish_post (post_num=1):
    find_image(get_resource_path('images/tag-completed.png'), 0.9)
    sleep(1)
    click(screenWidth-110, 235, duration=1)

    sleep(0.5)
    moveTo((screenWidth/2) + 50, (screenHeight/2) + 150)
    click(duration=0.5)
    print("Published post " + str(post_num))
    select_next_pin()

# code starto
def pinterest_tag():
    play_audio('audio/tag_pin_options_en.wav')
    try:
        post_amount = int(input("Number of posts to tag: "))
        play_audio('audio/tag_pin_start_en.wav')
        browswer_loc = find_image(get_resource_path('images/tabs/pinterest_chrome.png'), 0.8)
        notepad_loc = find_image(get_resource_path('images/tabs/notepad.png'), 0.9)
        for pin_num in range(post_amount):
            sleep(2)
            for i in range(9):
                sleep(0.2)
                copy_tag(i, notepad_loc)
                paste_tag(browswer_loc)
            publish_post(pin_num+1)
    except ValueError:
        sys.exit("Please enter a number")