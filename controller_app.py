import os
import tkinter as tk
from app_settings import AutomationControllerApp
from helper.local_api import find_text_on_screen

if __name__ == "__main__":
    print(find_text_on_screen("python"))
    root = tk.Tk()
    
    # Trying to set icon if available
    try:
        if os.path.exists("assets/icon.ico"):
            root.iconbitmap("assets/icon.ico")
    except:
        pass
    
    # Initializing the app
    app = AutomationControllerApp(root)
    
    # Running the application
    root.mainloop()