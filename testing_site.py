# import tkinter as tk

# # Create the main window
# root = tk.Tk()
# root.title("Tkinter Grid Example")

# # Create and place widgets using grid
# btn1 = tk.Button(root, text="Button 1")
# btn1.grid(row=0, column=0, padx=10, pady=10)

# btn2 = tk.Button(root, text="Button 2")
# btn2.grid(row=0, column=1, padx=10, pady=10)

# btn3 = tk.Button(root, text="Button 3")
# btn3.grid(row=1, column=0, padx=10, pady=10)

# btn4 = tk.Button(root, text="Button 4")
# btn4.grid(row=1, column=1, padx=10, pady=10)

# # Using sticky to align widgets within their grid cell:
# btn5 = tk.Button(root, text="Spanning Button")
# btn5.grid(row=2, column=0, columnspan=2, padx=10, pady=10, sticky="ew")

# # Allow the grid cells to expand with window resizing
# root.grid_rowconfigure(2, weight=1)
# root.grid_columnconfigure(0, weight=1)
# root.grid_columnconfigure(1, weight=1)

# root.mainloop()

# import GOOGLE_AI_STUDIO_KEY from env
import os
import dotenv

dotenv.load_dotenv()
gemini_api_key = os.getenv("GOOGLE_AI_STUDIO_KEY")


from google import genai

client = genai.Client(api_key=gemini_api_key)

response = client.models.generate_content(
    model="gemini-2.0-flash", contents="Explain how AI works in a few words"
)
print(response)
