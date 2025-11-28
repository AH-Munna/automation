from pyautogui import click, moveTo, hotkey
from helper.get_path import get_resource_path
from helper.pyscreensize import screenHeight, screenWidth
from time import sleep
import sys
import threading
import re
from tkinter import messagebox
# from pandas import read_clipboard, read_csv
from pyperclip import paste, copy
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
    click(clicks=3)
    hotkey('ctrl', 'c')

def paste_tag (tag_position=1):
    print("here...3")
    tagbox_loc = find_image(get_resource_path('images/pin_tag/tagbox-warning.png'), 0.6)
    print("here...")
    if tagbox_loc is None:
        tagbox_loc = find_image(get_resource_path('images/pin_tag/tagbox.png'), 0.6)
    print("here...2")
    click_x = tagbox_loc.left + 100
    click_y = tagbox_loc.top - 35
    click(click_x, click_y)
    hotkey('ctrl', 'a')
    hotkey('ctrl', 'v')
    sleep(0.5) # Wait for tag suggestions to load

    found_not_found_tag = False
    for _ in range(10):
        if find_image(get_resource_path('images/pin_tag/not_found_tag.png'), 0.9, tries=2, no_exit=True):
            sleep(0.5)
            found_not_found_tag = True
        else:
            found_not_found_tag = False
            break
    
    if not found_not_found_tag:
        # if not_found_tag is not found, it means suggestions are loaded.
        sleep(0.5)
        if find_image(get_resource_path('images/pin_tag/tagbox-warning.png'), 0.6, tries=1, no_exit=True):
            # suggestions are above
            click(click_x + 100, click_y - 330)
        else:
            # click lower to select the suggestion.
            click(click_x, click_y + (50 * tag_position))
    else:
        raise Exception("Tag suggestions did not load in time.")

def publish_post (post_num=1, new_update=False, os: str = 'windows'):
    if new_update:
        if os == 'windows':
            find_image(get_resource_path('images/pin_upload/tag-completed-new.png'), 0.98)
        elif os == 'ubuntu':
            find_image(get_resource_path('images/ubuntu/4/tag_completed.png'), 0.95)
        else:
            raise ValueError("Unsupported OS. Please use 'windows' or 'ubuntu'.")
    else:
        find_image(get_resource_path('images/pin_upload/tag-completed.png'), 0.95)
    sleep(1)
    if os == 'windows':
        click(screenWidth-110, 220, duration=1)
    elif os == 'ubuntu':
        publish_button_loc = find_image(get_resource_path('images/ubuntu/4/schedule_button.png'), 0.8, 2, True)
        if publish_button_loc is None:
            publish_button_loc = find_image(get_resource_path('images/ubuntu/4/publish_button.png'), 0.8)
        click(publish_button_loc, duration=0.5)

    sleep(0.5)
    if os == 'windows':
        moveTo((screenWidth/2) + 50, (screenHeight/2) + 150)
        click(duration=0.5)
    elif os == 'ubuntu':
        try:
            click(find_image(get_resource_path('images/ubuntu/4/shedule_confirm.png'), 0.8, 2, True), duration=0.5)
        except:
            pass
    else:
            raise ValueError("Unsupported OS. Please use 'windows' or 'ubuntu'.")
    print("Published post " + str(post_num))
    select_next_pin()

# code starto
def pinterest_tag_app(post_amount, new_update:bool=False, custom_tags:list[str]=[], os: str = 'windows'):
    def run_tagging():
        # play_audio('audio/tag_pin_start_jp_01.wav')
        # play_audio('audio/tag_pin_start_jp_02.wav')
        custom_tags_len = len(custom_tags)
        if os == 'windows':
            browser_loc = find_image(get_resource_path('images/tabs/pinterest_chrome.png'), 0.8)
        elif os == 'ubuntu':
            browser_loc = find_image(get_resource_path('images/tabs/firefox.png'), 0.8)
        if custom_tags_len == 9:
            for pin_num in range(post_amount):
                if pin_num == 0:
                    click(browser_loc)
                sleep(2)
                for i in range(9):
                    sleep(0.2)

                    # --- custom_tags filtering and preparing ---
                    tag_string = custom_tags[i]
                    tag_position = 1
                    
                    # Use regex to find a number in parentheses at the end of the string
                    match = re.search(r'\s*\((\d+)\)$', tag_string)
                    if match:
                        tag_position = int(match.group(1))
                        tag_name = tag_string[:match.start()].strip()
                    else:
                        tag_name = tag_string.strip()

                    copy(tag_name)
                    paste_tag(tag_position)
                publish_post(pin_num + 1, new_update, os=os)

        else:
            notepad_loc = find_image(get_resource_path('images/tabs/notepad.png'), 0.9)
            for pin_num in range(post_amount):
                sleep(2)
                for i in range(9):
                    sleep(0.2)
                    copy_tag(i, notepad_loc)
                    click(browser_loc)
                    paste_tag()
                publish_post(pin_num + 1, new_update, os=os)

    run_tagging()
    # threading.Thread(target=run_tagging, daemon=True).start()