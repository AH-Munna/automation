from pyautogui import click, moveTo, hotkey, hotkey, write, position, doubleClick, scroll
from time import sleep
from helper.find_image import find_image
from helper.play_audio import play_audio
from helper.pyscreensize import screenHeight, screenWidth
import sys

def click_and_write(image_name, text:str):
    image_loc = find_image(image_name, confidence=0.8)
    click(image_loc.left + 50, image_loc.top + 50 , duration=0.5)
    hotkey('ctrl', 'a')
    sleep(0.3)
    write(text)
    sleep(0.5)

def wordpress_paste_app(post_title:str, meta_description:str, keywords:str, post_content="", also_paste_content=False):
    """
    Function to handle WordPress paste functionality.
    """
    browswer_tab_loc = find_image('images/tabs/new_post_wp.png', confidence=0.8, tries=2, no_exit=True)
    if browswer_tab_loc is None:
        browswer_tab_loc = find_image('images/tabs/edit_post_wp.png', confidence=0.8, tries=2)

    click(browswer_tab_loc, duration=0.5)
    sleep(0.5)

    add_description_loc = find_image('images/wp/main_title.png', confidence=0.5)
    click(add_description_loc.left, add_description_loc.top + 150, duration=0.7)
    sleep(0.5)
    write(post_title)

    # rank math modal
    sleep(0.5)
    def find_edit_snippet():
        edit_snippet_loc = find_image('images/wp/edit_snippet.png', tries=2, confidence=0.8, no_exit=True)
        print(edit_snippet_loc)
        if edit_snippet_loc is None:
            click(find_image('images/wp/rank_math.png', confidence=0.8), duration=0.5)
            return find_edit_snippet()
            
        return click(edit_snippet_loc, duration=0.5)
    find_edit_snippet()

    #general tab
    click_and_write('images/wp/rank_math_title.png', post_title)

    click_and_write('images/wp/url.png', keywords.split(",")[0])

    click_and_write('images/wp/rank_math_meta_description.png', meta_description)

    # social tab
    sleep(0.5)
    click(find_image('images/wp/social_tab.png', confidence=0.8), duration=0.5)
    x, y = position()
    moveTo(x, y + 100, duration=0.5)
    click()
    scroll(-1000)
    sleep(0.3)

    click_and_write('images/wp/rank_math_title.png', post_title)

    click_and_write('images/wp/rank_math_meta_social_description.png', meta_description)

    click(find_image('images/wp/rank_math_modal_close.png', confidence=0.8), duration=0.5)

    click_and_write('images/wp/keyword_rank_math.png', keywords)

    click(find_image('images/wp/main_block.png', confidence=0.8), duration=0.5)

    moveTo(screenWidth-100, screenHeight / 2, duration=0.5)
    scroll(-1000)
    sleep(0.5)
    click_and_write('images/wp/keyword_main.png', keywords)