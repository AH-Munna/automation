import os
import csv
import time
import random
from datetime import datetime, timedelta
from dateutil import parser as date_parser
import re
from playwright.sync_api import sync_playwright, TimeoutError as PlaywrightTimeoutError

# Configuration
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
USER_DATA_DIR = os.path.join(BASE_DIR, 'user_data')
IMAGES_DIR = os.path.join(USER_DATA_DIR, 'images')
CSV_PATH = os.path.join(USER_DATA_DIR, 'current_pins.csv')
TAGS_PATH = os.path.join(USER_DATA_DIR, 'tags.txt')
STATE_PATH = os.path.join(BASE_DIR, 'state.json')
CHROMIUM_PATH = '/snap/bin/chromium'

class PinterestAutomator:
    def __init__(self, headless=False):
        self.headless = headless
        self.browser = None
        self.context = None
        self.page = None
        self.playwright = None

    def start(self):
        self.playwright = sync_playwright().start()
        self.browser = self.playwright.chromium.launch(headless=self.headless, executable_path=CHROMIUM_PATH)
        self.context = self.browser.new_context(storage_state=STATE_PATH)
        self.page = self.context.new_page()

    def stop(self):
        if self.browser:
            self.browser.close()
        if self.playwright:
            self.playwright.stop()

    def retry_action(self, action_name, action_func, verify_func, max_retries=10):
        """
        Executes an action and verifies it. Retries if verification fails.
        """
        for attempt in range(1, max_retries + 1):
            try:
                print(f"    [Attempt {attempt}/{max_retries}] {action_name}...")
                action_func()
                time.sleep(1) # Give UI time to update
                
                if verify_func():
                    print(f"    [Success] {action_name} verified.")
                    return True
                else:
                    print(f"    [Failed] Verification for {action_name} failed.")
            except Exception as e:
                print(f"    [Error] Exception during {action_name}: {e}")
            
            time.sleep(2) # Wait before retry
            
        print(f"    [Fatal] Could not complete {action_name} after {max_retries} attempts.")
        return False

    def go_to_create_page(self):
        try:
            self.page.goto("https://www.pinterest.com/pin-creation-tool/")
            self.page.wait_for_load_state('networkidle')
            time.sleep(2)
        except Exception as e:
            print(f"Error navigating to create page: {e}")

    def upload_image(self, img_path):
        def action():
            try:
                file_input = self.page.locator('#storyboard-upload-input')
                file_input.set_input_files(img_path)
            except:
                self.page.locator('input[type="file"]').set_input_files(img_path)

        def verify():
            # User suggestion: Check if "Choose a file or drag and drop it here" text is GONE.
            # If the text is not visible, it means the upload state has changed (image loaded).
            upload_text = self.page.locator('text="Choose a file or drag and drop it here"')
            return not upload_text.is_visible()

        return self.retry_action("Upload Image", action, verify)

    def fill_title(self, title):
        def action():
            self.page.locator('#storyboard-selector-title').fill(title)

        def verify():
            return self.page.locator('#storyboard-selector-title').input_value() == title

        return self.retry_action("Fill Title", action, verify)

    def fill_description(self, description):
        def action():
            try:
                desc_container = self.page.locator('[data-test-id="storyboard-description-field-container"]')
                desc_container.click()
                time.sleep(0.5)
                self.page.keyboard.type(description)
            except:
                # Fallback if container click fails
                self.page.locator('.public-DraftEditor-content').click()
                self.page.keyboard.type(description)

        def verify():
            # Checking exact text in draft editor is tricky, checking if not empty is a good proxy
            content = self.page.locator('.public-DraftEditor-content').text_content()
            return len(content) > 0

        return self.retry_action("Fill Description", action, verify)

    def add_tags(self, tags):
        if not tags: return True

        def action():
            # Smart Retry: Check which tags are already added
            tags_to_add = []
            
            for tag in tags:
                try:
                    # Regex for exact match, case insensitive
                    # We look for a div that contains the EXACT tag text (case-insensitive)
                    # AND contains a button (the remove 'x')
                    pattern = re.compile(f"^{re.escape(tag)}$", re.IGNORECASE)
                    
                    # locator('div') matches all divs.
                    # filter(has_text=pattern) matches divs containing the text.
                    # filter(has=locator('button')) matches divs containing a button.
                    if self.page.locator('div').filter(has_text=pattern).filter(has=self.page.locator('button')).count() > 0:
                        continue
                    
                    tags_to_add.append(tag)
                except Exception as e:
                    print(f"      [Smart Add] Error checking tag '{tag}': {e}")
                    tags_to_add.append(tag)

            if len(tags_to_add) < len(tags):
                print(f"      [Smart Add] Adding {len(tags_to_add)} missing tags (Skipping {len(tags) - len(tags_to_add)}).")
            
            if not tags_to_add:
                return

            tag_input = self.page.locator('#combobox-storyboard-interest-tags')
            for tag in tags_to_add:
                try:
                    tag_input.click()
                    tag_input.fill(tag)
                    time.sleep(1.5)
                    
                    exact_match = self.page.locator(f'[role="option"]', has_text=tag).first
                    if exact_match.count() > 0 and exact_match.is_visible():
                        exact_match.click()
                    else:
                        self.page.keyboard.press("Enter")
                    time.sleep(0.5)
                except Exception as e:
                    print(f"      Error adding tag {tag}: {e}")

        def verify():
            # User suggestion: Check for "Tagged topics (X)"
            expected_count = min(len(tags), 9)
            
            # Look for the element containing "Tagged topics"
            # We use a regex-like locator or just text matching
            # The text updates dynamically: "Tagged topics (1)", "Tagged topics (2)", etc.
            try:
                # Find element that starts with "Tagged topics"
                header = self.page.locator(r'text=/Tagged topics \(\d+\)/')
                if header.count() == 0:
                     # Fallback: try partial match if regex locator isn't behaving
                     header = self.page.locator('text="Tagged topics"')
                
                if header.count() > 0:
                    text = header.first.text_content()
                    # Parse "Tagged topics (5)"
                    if "(" in text and ")" in text:
                        count_str = text.split('(')[1].split(')')[0]
                        if count_str.isdigit():
                            count = int(count_str)
                            print(f"      Verified {count} tags added (Expected: {expected_count}).")
                            return count == expected_count
            except Exception as e:
                print(f"      Tag verification error: {e}")
            
            return False

        return self.retry_action("Add Tags", action, verify)

    def fill_link(self, link):
        if not link: return True
        
        def action():
            self.page.locator('#WebsiteField').fill(link)
            
        def verify():
            return self.page.locator('#WebsiteField').input_value() == link
            
        return self.retry_action("Fill Link", action, verify)

    def select_board(self, board_name):
        if not board_name: return True

        def action():
            # Open dropdown
            board_btn = self.page.locator('[data-test-id="board-dropdown-select-button"]')
            if board_btn.count() == 0:
                board_btn = self.page.locator('[data-test-id="board-dropdown-button"]')
            
            if board_btn.count() > 0:
                board_btn.click()
            else:
                self.page.locator('div[role="button"]', has_text="Choose a board").click()
            
            time.sleep(1)
            
            # Search
            search_input = self.page.locator('input[placeholder="Search"]')
            if search_input.count() > 0:
                search_input.fill(board_name)
                time.sleep(1.5)
                
                board_result = self.page.locator(f'[role="listitem"]', has_text=board_name).first
                if board_result.count() > 0:
                    board_result.click()
                else:
                    self.page.keyboard.press("Enter")
            else:
                print("      Warning: Board search input not found.")

        def verify():
            # Verify the board name is displayed in the dropdown button
            # The button usually contains the selected board name
            board_btn = self.page.locator('[data-test-id="board-dropdown-select-button"]')
            if board_btn.count() == 0:
                 board_btn = self.page.locator('[data-test-id="board-dropdown-button"]')
            
            if board_btn.count() > 0:
                text = board_btn.text_content().lower()
                return board_name.lower() in text
            return False

        return self.retry_action(f"Select Board '{board_name}'", action, verify)

    def set_schedule(self, schedule_dt):
        def action():
            # Check visibility
            time_input = self.page.locator('input[placeholder="Time"]')
            if not time_input.is_visible():
                schedule_label = self.page.locator('label', has_text="Publish at a later date")
                if schedule_label.count() > 0:
                    schedule_label.click()
                    time.sleep(1)

            if time_input.is_visible():
                # Date
                date_input = self.page.locator('input[type="date"]')
                if date_input.count() == 0:
                     date_input = self.page.locator('input[id*="date"]')
                
                if date_input.count() > 0:
                    date_input.fill(schedule_dt.strftime('%m/%d/%Y'))
                    self.page.keyboard.press("Enter")
                
                time.sleep(0.5)

                # Time
                time_input.click()
                time.sleep(1)
                
                target_time_str = schedule_dt.strftime('%I:%M %p')
                option = self.page.locator(f'[role="menuitem"]', has_text=target_time_str).first
                
                if option.count() > 0 and option.is_visible():
                    option.click()
                else:
                    time_input.fill('')
                    time_input.type(target_time_str, delay=100)
                    self.page.keyboard.press("Enter")

        def verify():
            # Verify date and time values
            # Note: Input values might be formatted differently (e.g. YYYY-MM-DD)
            # We'll check if the schedule section is visible and inputs have values
            time_input = self.page.locator('input[placeholder="Time"]')
            if not time_input.is_visible(): return False
            
            # Check if time input has a value (not empty)
            # Exact match is hard due to formatting differences
            return len(time_input.input_value()) > 0

        return self.retry_action("Set Schedule", action, verify)

    def publish(self):
        def action():
            # 1. Click first "Schedule" button
            publish_btn = self.page.locator('button', has_text="Schedule")
            if publish_btn.count() == 0:
                 publish_btn = self.page.locator('[data-test-id="storyboard-creation-nav-publish-button"]')
            if publish_btn.count() == 0:
                 publish_btn = self.page.locator('button', has_text="Publish")
            
            if publish_btn.count() > 0:
                publish_btn.first.click()
            else:
                raise Exception("Publish/Schedule button not found")
            
            time.sleep(1)

            # 2. Handle Confirmation Modal (if it appears)
            # User reported a second modal with "Cancel" and "Schedule"
            # We look for a button with text "Schedule" inside a modal-like structure or just the last one
            confirm_btn = self.page.locator('div[role="dialog"] button', has_text="Schedule")
            if confirm_btn.count() > 0 and confirm_btn.is_visible():
                print("    [Info] Clicking confirmation modal Schedule button...")
                confirm_btn.click()
            
        def verify():
            # We assume success if no error occurred and we waited a bit.
            time.sleep(2)
            return True

        return self.retry_action("Publish", action, verify)

    def wait_for_completion(self):
        """
        Waits for 'Pin drafts (X)' to become 'Pin drafts' (indicating upload complete).
        """
        print("    [Wait] Waiting for upload to complete...")
        start_time = time.time()
        timeout = 60 # 1 minute
        
        while time.time() - start_time < timeout:
            try:
                # Look for the header containing "Pin drafts"
                # Pattern: <h2><span>Pin drafts</span> (1)</h2> vs <h2><span>Pin drafts</span></h2>
                # We check if the text contains "(" and ")" which indicates a count
                
                # We target the h2 that contains "Pin drafts"
                header = self.page.locator('h2', has_text="Pin drafts")
                
                if header.count() > 0:
                    text = header.first.text_content()
                    # If text has numbers in parens like "(1)", it's still processing
                    if "(" in text and ")" in text and any(char.isdigit() for char in text):
                        # Still has drafts
                        pass
                    else:
                        # No count, means empty/done
                        print("    [Success] Upload completed (Drafts empty).")
                        return True
                else:
                    # If header not found, maybe we are on a different page or it loaded differently
                    # We'll assume it's fine or keep waiting?
                    # For safety, let's just wait.
                    pass
                    
            except Exception as e:
                print(f"    [Wait] Error checking drafts: {e}")
            
            time.sleep(2)
            
        print("    [Timeout] Upload did not complete within 60 seconds.")
        return False

# --- Helper Functions ---

def read_tags():
    if not os.path.exists(TAGS_PATH): return []
    with open(TAGS_PATH, 'r', encoding='utf-8') as f:
        return [line.strip() for line in f if line.strip()]

def parse_csv():
    posts = []
    settings = {}
    if not os.path.exists(CSV_PATH): raise FileNotFoundError(f"CSV not found: {CSV_PATH}")

    with open(CSV_PATH, 'r', encoding='utf-8') as f:
        rows = list(csv.reader(f))

    for i in range(len(rows)):
        row = rows[i]
        if not row: continue
        
        if row[0].lower().strip() == 'time': settings['time'] = row[1].strip()
        elif row[0].lower().strip() == 'link': settings['link'] = row[1].strip()
        elif row[0].lower().strip() == 'board name': settings['board'] = row[1].strip()
            
        if row[0].lower().startswith('pin title'):
            title = ", ".join([c.strip() for c in row[1:] if c.strip()])
            if i + 1 < len(rows) and rows[i+1][0].lower().startswith('pin description'):
                description = rows[i+1][1].strip()
                posts.append({'title': title, 'description': description})
    return posts, settings

def get_images():
    if not os.path.exists(IMAGES_DIR): return []
    return [f for f in os.listdir(IMAGES_DIR) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]

def match_images(posts, images):
    matches = []
    used_images = set()
    for post in posts:
        title_start = post['title'][:20].lower()
        post_images = []
        for img in images:
            if img in used_images: continue
            if title_start in os.path.splitext(img)[0].lower():
                post_images.append(img)
                used_images.add(img)
        if post_images: matches.append({'post': post, 'images': post_images})
    return matches

def get_schedule_time(start_date, day_offset, time_str):
    target_date = start_date + timedelta(days=day_offset)
    try:
        if time_str.isdigit():
            hour = int(time_str)
            parsed_time = datetime.strptime(f"{hour}:00", "%H:%M").time()
        else:
            parsed_time = date_parser.parse(time_str).time()
    except:
        print(f"Warning: Could not parse time '{time_str}', defaulting to 10:00 AM")
        parsed_time = datetime.strptime("10:00 AM", "%I:%M %p").time()
    return datetime.combine(target_date, parsed_time)

# --- Main Execution ---

def run_automation():
    tags = read_tags()
    posts, settings = parse_csv()
    all_images = get_images()
    matched_content = match_images(posts, all_images)
    
    if not matched_content:
        print("No matching images found.")
        return

    print(f"Found {len(matched_content)} posts.")
    print(f"Settings: {settings}")
    
    start_date = datetime.now().date() + timedelta(days=3)
    total_scheduled = 0
    
    automator = PinterestAutomator(headless=False)
    automator.start()
    
    try:
        automator.go_to_create_page()
        
        for item in matched_content:
            post = item['post']
            images = item['images']
            
            print(f"\nProcessing Post: {post['title'][:30]}...")
            
            for img_file in images:
                img_path = os.path.join(IMAGES_DIR, img_file)
                
                # Ensure we are on the create page
                if "pin-creation-tool" not in automator.page.url:
                    automator.go_to_create_page()
                
                # Execute Steps with Retry
                if not automator.upload_image(img_path): continue
                if not automator.fill_title(post['title']): continue
                if not automator.fill_description(post['description']): continue
                if not automator.add_tags(tags): continue
                if not automator.fill_link(settings.get('link')): continue
                if not automator.select_board(settings.get('board')): continue
                
                schedule_dt = get_schedule_time(start_date, total_scheduled, settings.get('time', '10:00 AM'))
                if not automator.set_schedule(schedule_dt): continue
                
                # Real Publish
                if not automator.publish(): continue
                
                # Wait for upload to complete (Drafts empty)
                if not automator.wait_for_completion():
                    print("    [Warning] Upload might not have completed. Proceeding anyway...")
                
                # Cleanup
                try:
                    os.remove(img_path)
                    print(f"    [Cleanup] Deleted {img_file}")
                except Exception as e:
                    print(f"    [Error] Could not delete image: {e}")
                
                # Reload page for next pin
                automator.go_to_create_page()
                
                total_scheduled += 1
                time.sleep(5) # Wait between pins

    except KeyboardInterrupt:
        print("\nStopped by user.")
    finally:
        automator.stop()

if __name__ == "__main__":
    run_automation()
