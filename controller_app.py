import tkinter as tk
from tkinter import messagebox, simpledialog
from ideogram_download import ideogram_download
from components_app.pin_create_app import pin_create_app
from components_app.pinterest_upload_app import pinterest_upload_app
from components_app.pinterest_tag_app import pinterest_tag_app
from components_app.doc_space_editor_app import doc_space_editor_app
from upload_to_canva import upload_to_canva
from components_app.remove_repetition_app import remove_repetitions_app
from helper.play_audio import play_audio
import sys

input_vars = {}

def update_input_frame(*args):
    """Update the input frame based on the selected choice."""
    choice = choice_var.get()
    for widget in input_frame.winfo_children():
        widget.destroy()

    if choice == 1:
        type_of_execution_var = tk.IntVar(value=1)
        thinking_model_var = tk.StringVar(value='y')
        browser_tab_var = tk.StringVar(value='season')
        title_var = tk.StringVar()
        
        # Define variables for existing inputs (if any)
        download_var = tk.StringVar(value='y')
        upload_var = tk.StringVar(value='y')
        position_var = tk.StringVar(value='0')
        
        # Store variables in input_vars for later retrieval
        input_vars[1] = {
            'type_of_execution': type_of_execution_var,
            'thinking_model': thinking_model_var,
            'browser_tab': browser_tab_var,
            'title': title_var,
            'download': download_var,
            'upload': upload_var,
            'position': position_var
        }
        
        # Add widgets for pin_create inputs
        tk.Label(input_frame, text="Select service:").pack(anchor='w')
        tk.Radiobutton(input_frame, text="1] API", variable=type_of_execution_var, value=1).pack(anchor='w')
        tk.Radiobutton(input_frame, text="2] Web", variable=type_of_execution_var, value=2).pack(anchor='w')
        
        tk.Checkbutton(input_frame, text="Thinking model? (default yes)", 
                       variable=thinking_model_var, onvalue='y', offvalue='n').pack(anchor='w')
        
        tk.Label(input_frame, text="Browser tab:").pack(anchor='w')
        tk.Radiobutton(input_frame, text="season", variable=browser_tab_var, value='season').pack(anchor='w')
        tk.Radiobutton(input_frame, text="red", variable=browser_tab_var, value='red').pack(anchor='w')
        
        # Conditional title input
        title_label = tk.Label(input_frame, text="Enter the title (default: copied from clipboard):")
        title_entry = tk.Entry(input_frame, textvariable=title_var)
        
        def toggle_title_input(*args):
            if type_of_execution_var.get() == 1:
                title_label.pack(anchor='w')
                title_entry.pack(anchor='w')
            else:
                title_label.pack_forget()
                title_entry.pack_forget()
        
        type_of_execution_var.trace('w', toggle_title_input)
        toggle_title_input()  # Set initial state
        
        # Add existing inputs (assuming these were part of the original GUI for choice 1)
        tk.Checkbutton(input_frame, text="Download image (default yes)", 
                       variable=download_var, onvalue='y', offvalue='n').pack(anchor='w')
        
        tk.Checkbutton(input_frame, text="Upload to Canva (default yes)", 
                       variable=upload_var, onvalue='y', offvalue='n').pack(anchor='w')
        
        position_label = tk.Label(input_frame, text="Position of the downloaded image (default 0):")
        position_entry = tk.Entry(input_frame, textvariable=position_var)
        
        def toggle_position_input(*args):
            if upload_var.get() == 'y':
                position_label.pack(anchor='w')
                position_entry.pack(anchor='w')
            else:
                position_label.pack_forget()
                position_entry.pack_forget()
        
        upload_var.trace('w', toggle_position_input)
        toggle_position_input()  # Set initial state
    elif choice == 2:
        upload_var = tk.StringVar(value='y')
        position_var = tk.StringVar(value='0')
        input_vars[choice] = {'upload': upload_var, 'position': position_var}

        upload_check = tk.Checkbutton(input_frame, text="Upload to Canva (default yes)", 
                                      variable=upload_var, onvalue='y', offvalue='n')
        upload_check.pack(anchor='w')

        position_label = tk.Label(input_frame, text="Position of the downloaded image (default 0):")
        position_entry = tk.Entry(input_frame, textvariable=position_var)

        def toggle_position_input(*args):
            if upload_var.get() == 'y':
                position_label.pack(anchor='w')
                position_entry.pack(anchor='w')
            else:
                position_label.pack_forget()
                position_entry.pack_forget()

        upload_var.trace('w', toggle_position_input)
        toggle_position_input()  # Set initial state
    elif choice == 3:
        num_of_image_var = tk.StringVar(value=3)
        board_name_var = tk.StringVar(value="")
        board_pos_var = tk.StringVar(value=1)
        
        input_vars[choice] = {
            'num_of_image': num_of_image_var,
            'board_name': board_name_var,
            'board_pos': board_pos_var,
        }

        # Define variables for choice 3
        num_of_image_var = tk.StringVar(value="3")
        board_name_var = tk.StringVar(value="")
        board_pos_var = tk.StringVar(value="1")
        
        # Store variables in input_vars for later retrieval
        input_vars[choice] = {
            'num_of_image': num_of_image_var,
            'board_name': board_name_var,
            'board_pos': board_pos_var,
        }
        
        # Create widgets for the input fields for choice 3
        tk.Label(input_frame, text="Number of Images:").pack(anchor='w')
        tk.Entry(input_frame, textvariable=num_of_image_var).pack(anchor='w')
        
        tk.Label(input_frame, text="Board Name:").pack(anchor='w')
        tk.Entry(input_frame, textvariable=board_name_var).pack(anchor='w')
        
        tk.Label(input_frame, text="Board Position:").pack(anchor='w')
        tk.Entry(input_frame, textvariable=board_pos_var).pack(anchor='w')
    elif choice == 5:
        # Label to instruct the user
        label = tk.Label(input_frame, text="Enter keywords (separated by commas or newlines):")
        label.pack(pady=5)
        
        # Text widget for multi-line input
        text_widget = tk.Text(input_frame)
        text_widget.pack(expand=True, fill='both', pady=5, padx=5)
        
        # Button to process the input
        process_button = tk.Button(
        input_frame,
        text="Process Keywords",
        fg="white",
        bg="green",
        font=("Helvetica", 16, "bold"),
        relief="raised",
        bd=4,
        padx=10, 
        pady=5,
        activebackground="yellow",
        activeforeground="black",
        command=lambda: process_keywords(text_widget.get("1.0", tk.END))
    )
        process_button.pack(pady=5)
    elif choice == 6:
        num_of_process_var = tk.StringVar(value='5')
        input_vars[choice] = {'num_of_process': num_of_process_var}

        tk.Label(input_frame, text="Number of lines to process (default 5):").pack(anchor='w')
        tk.Entry(input_frame, textvariable=num_of_process_var).pack(anchor='w')
    else:
        input_vars[choice] = {}  # No additional inputs for other choices

def process_keywords(keywords_text):
    """Processes the keywords and displays the unique list."""
    unique_keywords = remove_repetitions_app(keywords_text)
    # Display the result in a message box
    if unique_keywords:
        messagebox.showinfo("Unique Keywords", "\n".join(unique_keywords))
    else:
        messagebox.showinfo("Unique Keywords (already copied)", "No keywords entered.")

def execute_task():
    """Execute the selected task based on user inputs."""
    choice = choice_var.get()
    if choice == 7:
        root.destroy()
        return

    if choice in range(1, 7):
        # Mimic terminal output for task execution
        print("\033[32mExecuting task...\033[0m")

    if choice == 1:
        vars = input_vars.get(1, {})
        type_of_execution = vars.get('type_of_execution', tk.IntVar(value=1)).get()
        thinking_model = vars.get('thinking_model', tk.StringVar(value='y')).get()
        browser_tab = vars.get('browser_tab', tk.StringVar(value='season')).get()
        title = vars.get('title', tk.StringVar()).get()
        download_image = vars.get('download', tk.StringVar(value='y')).get()
        confirm_upload_to_canva = vars.get('upload', tk.StringVar(value='y')).get()
        
        try:
            downloaded_image_pos = int(vars.get('position', tk.StringVar(value='0')).get()) if confirm_upload_to_canva == 'y' else 0
        except ValueError:
            messagebox.showerror("Error", "Position must be an integer")
            return
        
        # Execute the task
        play_audio('audio/create_image_start_en.wav')  # Assuming this was part of original flow
        pin_create_app(type_of_execution=type_of_execution, 
                   thinking_model=thinking_model, 
                   browser_tab=browser_tab, 
                   title=title)  # Pass title as-is; pin_create handles empty case
        
        if download_image == 'y':
            ideogram_download(direct=True)
        if confirm_upload_to_canva == 'y':
            upload_to_canva(downloaded_image_pos)
        
        # Indicate task completion (assuming this exists in the original GUI)
        task_executed()
    elif choice == 2:
        vars = input_vars.get(2, {})
        confirm_upload_to_canva = vars.get('upload', tk.StringVar(value='y')).get()
        try:
            downloaded_image_pos = int(vars.get('position', tk.StringVar(value='0')).get()) if confirm_upload_to_canva == 'y' else 0
        except ValueError:
            messagebox.showerror("Error", "Position must be an integer")
            return

        ideogram_download()
        if confirm_upload_to_canva == 'y':
            upload_to_canva(downloaded_image_pos)
        task_executed()

    elif choice == 3:
        vars = input_vars.get(choice, {})
        num_of_image = int(vars.get('num_of_image', tk.StringVar(value=3)).get())
        board_name = vars.get('board_name', tk.StringVar()).get()
        board_pos = int(vars.get('board_pos', tk.StringVar(value=1)).get())
        print("Number of images:", num_of_image)
        print("Board name:", board_name)
        print("Board position:", board_pos)
        pinterest_upload_app(board_name=board_name, board_pos=board_pos, num_of_image=num_of_image)
        task_executed()

    elif choice == 4:
        execute_choice_four()
        task_executed()

    elif choice == 5:
        remove_repetitions_app()

    elif choice == 6:
        vars = input_vars.get(choice, {})
        num_of_line = int(vars.get('num_of_process', tk.StringVar(value=5)).get())
        doc_space_editor_app(num_of_line)
        task_executed()

def execute_choice_four():
    play_audio('audio/tag_pin_options_en.wav')
    try:
        post_amount_str = simpledialog.askstring("Input", "Number of posts to tag:")
        if post_amount_str is None:
            return
        post_amount = int(post_amount_str)
        if post_amount <= 0:
            raise ValueError("Number of posts must be positive")
        pinterest_tag_app(post_amount)
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid positive integer")

def task_executed():
    """Play completion audio."""
    play_audio('audio/task_completed_en.wav', wait=True)
    sys.exit()

# Set up the GUI
if __name__ == "__main__":
    # Play welcome audio at startup
    play_audio('audio/welcome_en.wav')

    # design
    root = tk.Tk()
    root.title("Automation Controller")
    root.geometry("1366x768")
    root.attributes('-alpha', 0.9)
    root.configure(borderwidth=10)

    left_frame = tk.Frame(root)
    right_frame = tk.Frame(root)

    # Place the frames in a grid (left frame in column 0, right frame in column 1)
    left_frame.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)
    right_frame.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)

    # Make the grid expand when the window is resized
    root.grid_columnconfigure(0, weight=1)
    root.grid_columnconfigure(1, weight=5)
    root.grid_rowconfigure(0, weight=1)

    # --- Left Frame: Main Choices ---

    # Welcome message
    welcome_label = tk.Label(left_frame, text="Welcome to the automation controller. What would you like to do?")
    welcome_label.pack(pady=10, anchor='w')

    # Choice selection with radio buttons
    choice_var = tk.IntVar(value=6)  # Default to 6
    choices = [
        ("1) Create a pin from deepseek to ideogram", 1),
        ("2) Download ideogram generated images", 2),
        ("3) Upload pin images", 3),
        ("4) Tag pins and publish them", 4),
        ("5) Remove keywords repetitions", 5),
        ("6) Edit doc space", 6),
        ("7) Exit", 7)
    ]
    for text, value in choices:
        tk.Radiobutton(left_frame, text=text, variable=choice_var, value=value).pack(anchor='w', padx=10)

    # --- Right Frame: Dynamic Input Fields ---
    input_frame = tk.Frame(right_frame, relief=tk.GROOVE, borderwidth=2)
    input_frame.pack(fill='both', expand=True, padx=10, pady=10)

    # Bind choice selection to update input fields
    choice_var.trace('w', update_input_frame)

    # Initialize input frame for default choice
    update_input_frame()

    # Execute button at the bottom (spanning both frames)
    execute_button = tk.Button(
        root,
        text="Execute Task",
        fg="white",          # Text color
        bg="blue",           # Background color
        font=("Helvetica", 16, "bold"),  # Font style and size
        relief="raised",     # Border style
        bd=4,                # Border width
        padx=10,             # Horizontal padding
        pady=5,              # Vertical padding
        activebackground="darkblue",  # Background when button is pressed
        activeforeground="yellow"       # Text color when button is pressed
        , command=execute_task
    )
    execute_button.grid(row=1, column=0, columnspan=2, pady=10)

    root.mainloop()