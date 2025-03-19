from ideogram_download import ideogram_download
from pinterest_tag import pinterest_tag
from pin_create import pin_create
from pinterest_upload import pinterest_upload
from upload_to_canva import upload_to_canva
from doc_space_editor import doc_space_editor
from repeatation_remover import remove_repetitions
from helper.play_audio import play_audio
import sys


def main_func():
    choice = get_choices()
    if 1 <= choice <= 6:
        print("\033[32mExecuting task...\033[0m")

    if choice == 1:
        handle_choice_1()
    elif choice == 2:
        handle_choice_2()
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
        print("\033[31mInvalid choice\033[0m")
        return main_func()

def handle_choice_1():
    play_audio('audio/create_image_start_en.wav')
    download_image = input("\033[33mdownload image y/n (default y): \033[0m") or 'y'
    confirm_upload_to_canva = input("\033[33mupload to canva? y/n (default y): \033[0m") or 'y'
    downloaded_image_pos = 0
    if confirm_upload_to_canva == 'y':
        downloaded_image_pos = int(input("\033[33mEnter the position of the downloaded image (default 0): \033[0m") or '0')
    pin_create()
    if download_image == 'y':
        ideogram_download(direct=True)
    if confirm_upload_to_canva == 'y':
        upload_to_canva(downloaded_image_pos)
    task_executed()

def handle_choice_2():
    confirm_upload_to_canva = input("\033[33mupload to canva? y/n (default y): \033[0m") or 'y'
    downloaded_image_pos = 0
    if confirm_upload_to_canva == 'y':
        downloaded_image_pos = int(input("\033[33mEnter the position of the downloaded image (default 0): \033[0m") or '0')
    ideogram_download()
    if confirm_upload_to_canva == 'y':
        upload_to_canva(downloaded_image_pos)
    task_executed()

def task_executed():
    play_audio('audio/task_completed.wav', wait=True)
    sys.exit("\033[32mtask executed!\033[0m")

def get_choices():
    play_audio('audio/welcome_en.wav')
    print("\033[32mWelcome to the automation controller. What would you like to do?\033[96m \n1) Create a pin from deepseek to ideogram \n2) Download ideogram generated images \n3) Upload pin images \n4) Tag pins and publish them \n5) remove keywords repetitions \n6) edit doc space \n7) Exit\033[0m\n\n")
    try:
        return int(input("\033[32mChoice (default: 6): \033[0m") or '6')
    except ValueError:
        print("\033[31mPlease enter a number\033[0m")
        return get_choices()

if __name__ == "__main__":
    main_func()