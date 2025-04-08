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


import tkinter as tk

root = tk.Tk()
root.title("Button Design Example")

# Create a customized button
button1 = tk.Button(
    root,
    text="Click Me",
    fg="white",          # Text color
    bg="blue",           # Background color
    font=("Helvetica", 16, "bold"),  # Font style and size
    relief="raised",     # Border style
    bd=4,                # Border width
    padx=10,             # Horizontal padding
    pady=5,              # Vertical padding
    activebackground="darkblue",  # Background when button is pressed
    activeforeground="yellow"       # Text color when button is pressed
)
button1.pack(pady=20)

root.mainloop()
