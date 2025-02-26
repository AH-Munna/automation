from ideogram_download import ideogram_download
from pinterest_tag import pinterest_tag
from pin_create import pin_create
from pinterest_upload import pinterest_upload
from upload_to_canva import upload_to_canva
from doc_space_editor import doc_space_editor
from groq_api import groq_title_divider, groq_prompt_gen
import sys
from helper.find_image import find_image
from helper.repeatation_remover import remove_repetitions
from pyautogui import click
from time import sleep

def task_executed():
    # sleep(1)
    # click(find_image('images/tabs/vs_code.png', 0.8))
    sys.exit("\033[32mtask executed!\033[0m")

# code starto
def main_func():
    print("\033[32mWelcome to the automation controller. What would you like to do?\033[96m \n1) Create a pin from deepseek to ideogram \n2) Download ideogram generated images \n3) Upload pin images \n4) Tag pins and publish them \n5) remove keywords repetitions \n6) edit doc space \n7) Exit \n8) experimental feature\033[0m\n\n")
    try:
        choice = int(input("\033[32mChoice (default: 6): \033[0m") or '6')
        if choice > 0 and choice < 6:
            print("\033[32mExecuting task...\033[0m")

        if choice == 1:
            download_image = input("download image y/n (default n): ") or 'n'
            pin_create()
            if download_image == 'y':
                ideogram_download(direct=True)
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
            remove_repetitions()
        elif choice == 6:
            doc_space_editor()
        elif choice == 7:
            sys.exit("\033[33mGoodbye!\033[0m")
        else:
            print("\033[31mPlease choose between 1 and 6\033[0m")
            return main_func()
    except ValueError:
        print("\033[31mPlease enter a number\033[0m")
        return main_func()

if __name__ == "__main__":
    main_func()