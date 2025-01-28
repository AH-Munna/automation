from ideogram_download import ideogram_download
from pinterest_tag import pinterest_tag
from pin_create import pin_create
from pinterest_upload import pinterest_upload
import sys
from helper.find_image import find_image
from pyautogui import click
from time import sleep

def task_executed():
    sleep(1)
    click(find_image('images/tabs/vs_code.png', 0.8))
    sys.exit("\033[32mtask executed!\033[0m")

# code starto
print("\033[32mWelcome to the controller. What would you like to do?\033[96m \n1) Create a pin \n2) Download ideogram \n3) Upload a pin \n4) Tag a pin \n5) Exit\033[0m\n\n")
try:
    choice = int(input("\033[32mChoice: \033[0m"))
    if choice > 0 and choice < 5:
        print("\033[32mExecuting task...\033[0m")

    if choice == 1:
        pin_create()
        task_executed()
    elif choice == 2:
        ideogram_download()
        task_executed()
    elif choice == 3:
        pinterest_upload()
        task_executed()
    elif choice == 4:
        pinterest_tag()
        task_executed()
    elif choice == 5:
        sys.exit("\033[33mGoodbye!\033[0m")
    else:
        sys.exit("\033[31mPlease choose between 1 and 5\033[0m")
except ValueError:
    sys.exit("\033[31mPlease enter a number\033[0m")