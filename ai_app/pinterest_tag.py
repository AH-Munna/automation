import sys
import os

from pyperclip import copy, paste

# Get the absolute path of the script
script_dir = os.path.dirname(os.path.abspath(__file__))
# Get the parent directory of the script's directory (the project root)
project_root = os.path.dirname(script_dir)
# Add the project root to the Python path
sys.path.append(project_root)

from pyautogui import click, moveTo, sleep, write
from helper.local_api import find_text_on_screen

tags = [
    "House Smell",
"Air Freshener",
"Instant Pot Recipes",
"One Pot Recipes",
"Pressure Cooker Recipes",
"Dinner Recipes",
"Thanksgiving Recipes",
"Healthy Recipes",
"Stovetop Kettles",
]

input_box = find_text_on_screen("tagged topics")

for tag in tags:
    moveTo(input_box['screen_elements'][0]['center_coordinates']['x'], input_box['screen_elements'][0]['center_coordinates']['y'] - 330, 1)
    break
    copy(tag)
    paste()
    sleep(0.5)
    screen_elements = find_text_on_screen(tag)
    print(screen_elements)

    for i in range(2):
        click(screen_elements['screen_elements'][i]['center_coordinates']['x'], screen_elements['screen_elements'][i]['center_coordinates']['y'], 1)
    sleep(1)