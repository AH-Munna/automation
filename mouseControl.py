from time import sleep

from pyautogui import click, hotkey, moveTo, typewrite

moveTo(20, 750, 1)
sleep(1)
click()
moveTo(100, 195, 1)
moveTo(150, 90, 1)
click()
sleep(0.5)
typewrite("ch")
sleep(0.5)
typewrite("ro")
sleep(0.5)
typewrite("me")
sleep(1)
moveTo(500, 450, 1)
sleep(1)
click()
# moveTo(750, 420, 1)
# sleep(1)
# click()
# moveTo(250, 55, 1)
# click()
sleep(0.5)
typewrite("you")
sleep(0.5)
typewrite(" are")
sleep(0.5)
typewrite(" hacked!!!!!hacked!!!!!hacked!!!!!hacked!!!!!hacked!!!!!hacked!!!!!")
sleep(2)
hotkey("ctrlleft", "a")
hotkey("alt", "f4")