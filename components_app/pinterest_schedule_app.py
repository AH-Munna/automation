from pyautogui import click, moveTo, hotkey, scroll
from helper.get_path import get_resource_path
from helper.pyscreensize import screenHeight, screenWidth
from time import sleep
from datetime import datetime, timedelta
from pyperclip import paste, copy
from typing import Literal
import sys
from helper.find_image import find_image
from helper.play_audio import play_audio

def _find_time_and_click(schedule_hour, am_pm, max_scrolls=12, os: str = 'windows'):
    """
    Iteratively scrolls to find the target time image and clicks it.
    Returns True if found and clicked, False otherwise.
    """
    for _ in range(max_scrolls):
        if os == 'windows':
            time_loc = find_image(get_resource_path(f'images/pin_schedule/times/{schedule_hour}{am_pm.lower()}.png'), 0.9, tries=1, no_exit=True)
        elif os == 'ubuntu':
            time_loc = find_image(get_resource_path(f'images/ubuntu/2/{schedule_hour}{am_pm.lower()}.png'), 0.9, tries=1, no_exit=True)
        else:
            raise ValueError("Unsupported OS. Please use 'windows' or 'ubuntu'.")
        if time_loc:
            click(time_loc, duration=0.5)
            return True
        if os == 'windows':
            scroll(-200)
        elif os == 'ubuntu':
            scroll(-2)
        sleep(0.2)
    return False

def _find_current_pin_loc(trying_times=0, os: str = 'windows'):
    if trying_times > 5:
        return None
    current_pin_loc = find_image(get_resource_path('images/pin_upload/next_pin.png'), 0.8, tries=2, no_exit=True)
    if current_pin_loc is None or current_pin_loc.top > (screenHeight - (320 if os == 'windows' else 240)):
        moveTo(130, 500, duration=0.5)
        if os == 'windows':
            scroll(-500)
        elif os == 'ubuntu':
            scroll(-5)
        sleep(0.2)
        return _find_current_pin_loc(trying_times + 1, os=os)
    return current_pin_loc

def pinterest_schedule_app(num_of_pins: int = 1, schedule_time:int = 13, twice_per_day:bool=False, os: str = 'windows'):
    # --- Time and Date Setup ---
    # Convert 24hr input to 12hr for image searching
    schedule_time_12hr = schedule_time
    if schedule_time > 12:
        schedule_time_12hr = schedule_time - 12
    elif schedule_time == 0:
        schedule_time_12hr = 12

    # Determine initial AM/PM for the 'once a day' case
    initial_am_pm = 'AM'
    if schedule_time > 11:
        initial_am_pm = 'PM'

    start_date = datetime.today() + timedelta(days=1)

    # --- GUI Automation ---
    if os == 'windows':
        click(find_image(get_resource_path('images/tabs/pinterest_chrome.png'), 0.8), duration=1)
    elif os == 'ubuntu':
        click(find_image(get_resource_path('images/tabs/firefox.png'), 0.8), duration=1)
        click(find_image(get_resource_path('images/ubuntu/pinterest_browser_tab.png'), 0.8), duration=1)
    else:
        raise ValueError("Unsupported OS. Please use 'windows' or 'ubuntu'.")

    # --- Main Loop for Scheduling Pins ---
    for i in range(num_of_pins):
        schedule_button = find_image(get_resource_path('images/pin_schedule/schedule_off.png'), 0.8, tries=1, no_exit=True)
        if schedule_button is None:
            moveTo((screenWidth/2) - 50, (screenHeight/2) - 50, duration=0.2)
            if os == 'windows':
                scroll(-500)
            elif os == 'ubuntu':
                scroll(-5)
            sleep(0.2)
            schedule_button = find_image(get_resource_path('images/pin_schedule/schedule_off.png'), 0.8, tries=2, no_exit=True)

        if schedule_button:
            click(schedule_button, duration=0.5)

        # Calculate date and time for the current pin
        if twice_per_day:
            day_offset = i // 2
            current_schedule_date = start_date + timedelta(days=day_offset)
            current_am_pm = 'AM' if i % 2 == 0 else 'PM'
        else:
            day_offset = i
            current_schedule_date = start_date + timedelta(days=day_offset)
            current_am_pm = initial_am_pm

        # --- Set Date ---
        calender_loc = find_image(get_resource_path('images/pin_schedule/calender.png'), 0.8, tries=2, no_exit=True)
        if calender_loc is None:
            moveTo((screenWidth/2) - 50, (screenHeight/2) - 50, duration=0.2)
            if os == 'windows':
                scroll(-500)
            elif os == 'ubuntu':
                scroll(-5)
            sleep(0.2)
            calender_loc = find_image(get_resource_path('images/pin_schedule/calender.png'), 0.8, tries=2, no_exit=True)
            if calender_loc is None:
                raise Exception(f"Calender not found for pin {i+1}")
            
        click(calender_loc, duration=0.5)
        copy(f"{current_schedule_date.strftime('%m/%d/%Y')}")
        hotkey('ctrl', 'a')
        hotkey('ctrl', 'v')
        sleep(0.2) # Small pause after pasting

        # --- Set Time ---
        clock_loc = find_image(get_resource_path('images/pin_schedule/clock.png'), 0.8)
        if clock_loc is None:
             raise Exception(f"Time field not found for pin {i+1}")
        
        click(clock_loc.left - 100, clock_loc.top + 15, duration=0.5)
        moveTo(clock_loc.left - 50, clock_loc.top - 150, duration=0.5)
        sleep(0.2)

        if not _find_time_and_click(schedule_time_12hr, current_am_pm, os=os):
            raise Exception(f"Could not find time {schedule_time_12hr}{current_am_pm.lower()} for pin {i+1}")
        
        sleep(1)

        # --- Select Next Pin ---
        if i < num_of_pins - 1:
            current_pin_loc = _find_current_pin_loc(os=os)
            click(current_pin_loc.left + 150, current_pin_loc.top + 180, duration=0.5) # type: ignore
            sleep(0.5)