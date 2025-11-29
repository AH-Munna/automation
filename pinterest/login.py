import os
from playwright.sync_api import sync_playwright

def login():
    """
    Launches a browser for the user to log in manually.
    Saves the storage state (cookies, etc.) to 'state.json' upon closing.
    """
    with sync_playwright() as p:
        # Launch browser in headed mode so user can see and interact
        # Using system chromium to avoid downloading playwright's version
        browser = p.chromium.launch(headless=False, executable_path='/snap/bin/chromium')
        context = browser.new_context()
        page = context.new_page()

        print("Navigating to Pinterest login page...")
        page.goto("https://www.pinterest.com/login/")

        print("Please log in manually in the browser window.")
        print("When you are successfully logged in and can see your home feed, press Enter here in the terminal to save the session and exit.")
        input("Press Enter to save session...")

        # Save storage state
        state_path = os.path.join(os.path.dirname(__file__), 'state.json')
        context.storage_state(path=state_path)
        print(f"Session saved to {state_path}")

        browser.close()

if __name__ == "__main__":
    login()
