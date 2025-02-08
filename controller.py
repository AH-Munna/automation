from ideogram_download import ideogram_download
from pinterest_tag import pinterest_tag
from pin_create import pin_create
from pinterest_upload import pinterest_upload
from upload_to_canva import upload_to_canva
import sys
from helper.find_image import find_image
from helper.repeatation_remover import remove_repetitions
from pyautogui import click
from time import sleep

def task_executed():
    sleep(1)
    click(find_image('images/tabs/vs_code.png', 0.8))
    sys.exit("\033[32mtask executed!\033[0m")

# code starto
print("\033[32mWelcome to the automation controller. What would you like to do?\033[96m \n1) Create a pin from deepseek to ideogram \n2) Download ideogram generated images \n3) Upload pin images \n4) Tag pins and publish them \n5) remove keywords repetitions \n6) Exit\033[0m\n\n")
try:
    choice = int(input("\033[32mChoice: \033[0m"))
    if choice > 0 and choice < 6:
        print("\033[32mExecuting task...\033[0m")

    if choice == 1:
        download_image = input("\033[33mWould you also like to download the image from ideogram? (y/n): \033[0m")
        pin_create()
        if download_image == 'y':
            ideogram_download()
        task_executed()
    elif choice == 2:
        experimental_feature = input("\033[33mWould you also like to run the experimental feature to upload to canva? (y/n): \033[0m")
        ideogram_download()
        if experimental_feature == 'y':
            upload_to_canva()
        task_executed()
    elif choice == 3:
        pinterest_upload()
        task_executed()
    elif choice == 4:
        pinterest_tag()
        task_executed()
    elif choice == 5:
        keywords = ""
        print("\033[33mEnter the keywords: \033[0m")
        while True:
            input_str = input()
            if input_str == '':
                break
            keywords += input_str + ','
        remove_repetitions(keywords)
        sys.exit("\033[32mtask executed!\033[0m")
    elif choice == 6:
        sys.exit("\033[33mGoodbye!\033[0m")
    else:
        sys.exit("\033[31mPlease choose between 1 and 6\033[0m")
except ValueError:
    sys.exit("\033[31mPlease enter a number\033[0m")