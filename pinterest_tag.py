from pyautogui import click, moveTo, hotkey, hotkey
from helper.pyscreensize import screenHeight, screenWidth
from time import sleep
import sys
# from pandas import read_clipboard, read_csv
# from pyperclip import paste
from helper.find_image import find_image


def select_next_pin():
    # selected_pin_loc = find_image('images/pin_upload/pin-selected.png', 0.8)
    # moveTo(selected_pin_loc.left + 50, selected_pin_loc.top + 50)
    moveTo(150, 500, duration=0.5)
    click()
    
def copy_tag (tag_num):
    moveTo(500, screenHeight-25)
    click()

    moveTo(18, 85 + (tag_num * 36))
    click(clicks=3)
    hotkey('ctrl', 'c')

def paste_tag ():
    moveTo(750, screenHeight-25)
    click()

    tagbox_loc = find_image('images/tagbox-warning.png', 0.6)
    moveTo(tagbox_loc.left + 100, tagbox_loc.top - 35)
    click()
    hotkey('ctrl', 'a')
    hotkey('ctrl', 'v')

    matched_tags_loc = find_image('images/matched-tags.png', 0.6)
    moveTo(matched_tags_loc.left + 50, matched_tags_loc.top + 60)
    click()

def publish_post (post_num=1):
    find_image('images/tag-completed.png', 0.9)
    sleep(1)
    moveTo(screenWidth-110, 235, duration=1)
    click()
    sleep(0.5)
    moveTo((screenWidth/2) + 50, (screenHeight/2) + 150)
    sleep(0.5)
    click()
    print("Published post " + str(post_num))
    select_next_pin()

# code starto
def pinterest_tag():
    try:
        post_amount = int(input("Number of posts to tag: "))
        for pin_num in range(post_amount):
            sleep(2)
            for i in range(9):
                sleep(0.2)
                copy_tag(i)
                paste_tag()
            publish_post(pin_num+1)
    except ValueError:
        sys.exit("Please enter a number")
