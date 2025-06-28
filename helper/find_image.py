from pyautogui import locateOnScreen, PyAutoGUIException
from pyscreeze import Box
from time import sleep
import sys
from typing import NamedTuple

class ImageNotFoundError(Exception):
    """Custom exception for when an image cannot be found on screen."""
    pass

def find_image(
    image: str,
    confidence: float = 0.9,
    tries: int = 8,
    no_exit: bool = False,
    long: bool = False,
) -> Box | None:
    """
    Looks for an image on the screen, retrying a specified number of times with a delay.

    This function attempts to find the given image on the screen. It retries
    multiple times with a delay between each attempt.

    Args:
        image (str): Path to the image file to find.
        confidence (float, optional): The confidence level for the image search.
            Defaults to 0.9.
        tries (int, optional): The total number of attempts to find the image.
            Defaults to 8.
        no_exit (bool, optional): If True, returns None on failure instead of
            raising an exception. If False (default), raises ImageNotFoundError
            on failure.
        long (bool, optional): If True, uses a decreasing sleep interval between
            tries. Defaults to False, which uses a linear backoff (increasing
            sleep time).

    Returns:
        pyautogui.Box | None: A Box object (left, top, width, height) if the
            image is found. Returns None if the image is not found and no_exit
            is True.

    Raises:
        ImageNotFoundError: If the image is not found after all tries and
            no_exit is False. Also raised if the image file cannot be processed.
    """
    print(f"Trying to find '{image}'. Pausing before attempts for:", end=' ', flush=True)

    for attempt in range(tries):
        if long:
            sleep_time = max(0, int((tries - attempt) / 3))
        else:
            sleep_time = attempt * 0.5

        print(f"{sleep_time:.1f}s", end=', ', flush=True)
        sleep(sleep_time)

        try:
            image_loc = locateOnScreen(image, confidence=confidence)
            if image_loc:
                print("\n\033[32mImage found.\033[0m")
                return image_loc
        except PyAutoGUIException as e:
            error_message = f"Error processing image file '{image}': {e}"
            print(f"\n\033[31m{error_message}\033[0m", file=sys.stderr)

    # After all tries, if image is not found
    final_message = f"Image '{image}' not found after {tries} attempts."
    print(f"\n\033[31m{final_message}\033[0m")

    if no_exit:
        return None

    raise ImageNotFoundError(final_message)