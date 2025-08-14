import sys
import os

def get_resource_path(relative_path):
    """
    Get the absolute path to a resource, handling both development and PyInstaller environments.
    """
    if hasattr(sys, '_MEIPASS'):
        # PyInstaller creates a temporary folder and stores path in _MEIPASS
        # This is the path to the extracted bundle
        base_path = sys._MEIPASS # type: ignore
    else:
        # Normal Python execution (e.g., via `python controller_app.py`)
        # The base path is the directory where the script is located
        base_path = os.path.abspath(".") # Assumes script is run from project root

    return os.path.join(base_path, relative_path)