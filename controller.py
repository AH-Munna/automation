from ideogram_download import ideogram_download
from pinterest_tag import pinterest_tag
from pin_create import pin_create
from pinterest_upload import pinterest_upload
import sys
from helper.find_image import find_image
from pyautogui import click

def task_executed():
    click(find_image('images/tabs/vs_code.png', 0.7))
    sys.exit("\033[32mtask executed!\033[0m")

# code starto
print("\033[32mWelcome to the controller. What would you like to do?\033[96m \n1) Download ideogram \n2) Create a pin \n3) Tag a pin \n4) Upload a pin \n5) Exit\033[0m\n\n")
try:
    choice = int(input("Choice: \033[0m"))
    if choice > 0 and choice < 5:
        print("\033[32mExecuting task...\033[0m")

    if choice == 1:
        ideogram_download()
        task_executed()
    elif choice == 2:
        pin_create()
        task_executed()
    elif choice == 3:
        pinterest_tag()
        task_executed()
    elif choice == 4:
        pinterest_upload()
        task_executed()
    elif choice == 5:
        sys.exit("\033[33mGoodbye!\033[0m")
    else:
        sys.exit("\033[31mPlease choose between 1 and 5\033[0m")
except ValueError:
    sys.exit("\033[31mPlease enter a number\033[0m")