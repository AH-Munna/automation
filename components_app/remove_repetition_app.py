import re
from pyperclip import copy, paste
import sys
from time import sleep

def sort_forbidden(first_str: list[str], second_str: list[str]) -> list[str]:
    """
    Sorts a list of strings (first_str) by moving items to the last position
    if they contain any string present in another list of strings (second_str).

    Args:
        first_str: A list of strings to be sorted.
        second_str: A list of strings to check for within items of first_str.

    Returns:
        A new list with strings from first_str sorted according to the condition.
    """
    moved_to_end = []
    not_moved = []

    second_str = [item.lower() for item in second_str]

    for item_first in first_str:
        should_move = False
        for item_second in second_str:
            # if item_second in item_first or re.search(r'\b(1[0-9]{3}|2[0-9]{3})\b', item_first):
            if item_second in item_first:
                print("\nsorting", item_first, "\n")
                should_move = True
                break
        if should_move:
            moved_to_end.append(item_first)
        else:
            not_moved.append(item_first)

    return not_moved + [""] + moved_to_end

def remove_repetitions_app(keywords_text:str=None, filter_str:str=""):
    if not keywords_text:
        keywords_text = paste()
    
    keywords = re.split(r'[,\n]', keywords_text)
    filter_str = filter_str.lower()
    processed_items = [keyword.strip().lower() for keyword in keywords if keyword.strip()]
    
    filtered_items = [keyword for keyword in processed_items if filter_str in keyword]
    seen = set()
    unique_items:list[str] = []
    for item in filtered_items:
        if item not in seen:
            seen.add(item)
            unique_items.append(item)
    
    processed_unique_items = sort_forbidden(unique_items, ["pinterest", "facebook", "image", "download", "gif", "reddit", "netflix", 'printable', 'free', 'pdf', 'tumblr', 'english', 'Bangladesh'])

    final_list = []
    for item in processed_unique_items:
            final_list.append(item + ",\n" if item.strip() else "\n")
            
    copy("".join(final_list))

    print("\033[32mItem Copied:\033[0m")

    return final_list