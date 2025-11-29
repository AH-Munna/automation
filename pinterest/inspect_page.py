from playwright.sync_api import sync_playwright
import os

STATE_PATH = os.path.join(os.path.dirname(__file__), 'state.json')
CHROMIUM_PATH = '/snap/bin/chromium'

def inspect():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, executable_path=CHROMIUM_PATH)
        context = browser.new_context(storage_state=STATE_PATH)
        page = context.new_page()
        
        print("Navigating to pin-creation-tool...")
        page.goto("https://www.pinterest.com/pin-creation-tool/")
        page.wait_for_load_state('networkidle')
        
        print("Taking screenshot...")
        page.screenshot(path='pinterest_debug.png')
        
        print("Dumping HTML...")
        with open('pinterest_debug.html', 'w', encoding='utf-8') as f:
            f.write(page.content())
            
        print("Finding inputs...")
        inputs = page.locator('input').all()
        for i, inp in enumerate(inputs):
            try:
                print(f"Input {i}: id={inp.get_attribute('id')}, name={inp.get_attribute('name')}, placeholder={inp.get_attribute('placeholder')}, data-test-id={inp.get_attribute('data-test-id')}")
            except:
                pass
                
        browser.close()

if __name__ == "__main__":
    inspect()
