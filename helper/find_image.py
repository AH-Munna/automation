from pyautogui import locateOnScreen
from time import sleep
import sys

def find_image(image, confidence=0.9, tries=8, no_exit=False)-> dict[str, int]:
    def try_to_find_image():
        try:
            image_loc = locateOnScreen(image, confidence=confidence)
            print("\033[32mimage found.\033[0m")
            return image_loc
        except:
            if k == tries:
                if no_exit:
                    print("\033[31mImage not found\033[0m")
                    return None
                else:
                    sys.exit("\033[31mImage not found. exiting...\033[0m")
    
    k = 0
    print(f'trying to find image', end=': ')
    while(k < tries):
        print(k, end=', ')
        sleep(k * 0.5)
        k = k + 1

        if image_loc:=try_to_find_image():
            break
    return image_loc
