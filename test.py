from pyautogui import moveTo, click
from helper.pyscreensize import screenHeight
from helper.find_image import find_image

click(find_image('images/tabs/pinterest_chrome.png', 0.8), duration=1)
moveTo(100, screenHeight - 200, duration=1)