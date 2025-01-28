from pyautogui import locateOnScreen
from time import sleep
import sys

def find_image(image, confidence=0.9)-> dict[str, int]:
    def try_to_find_image():
        try:
            image_loc = locateOnScreen(image, confidence=confidence)
            return image_loc
        except:
            if k == 10:
                sys.exit("Image not found", image)
    
    k = 0
    while(k < 10):
        sleep(k * 0.5)
        k = k + 1

        if image_loc:=try_to_find_image():
            break
    return image_loc
