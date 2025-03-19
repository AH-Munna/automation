import tkinter as tk
from tkinter import messagebox, simpledialog
from ideogram_download import ideogram_download
from components_app.pin_create_app import pin_create_app
from components_app.pinterest_upload_app import pinterest_upload_app
from components_app.pinterest_tag_app import pinterest_tag_app
from upload_to_canva import upload_to_canva
from doc_space_editor import doc_space_editor
from repeatation_remover import remove_repetitions
from helper.play_audio import play_audio
import sys

# Dictionary to store input variables for each choice
input_vars = {}

def update_input_frame(*args):
    """Update the input frame based on the selected choice."""
    choice = choice_var.get()
    # Clear existing widgets in input_frame
    for widget in input_frame.winfo_children():
        widget.destroy()

    if choice == 1:
        # Define variables for pin_create inputs
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
    else:
        input_vars[choice] = {}  # No additional inputs for other choices

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
        remove_repetitions()

    elif choice == 6:
        doc_space_editor()

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
    """Play completion audio, matching original script behavior."""
    play_audio('audio/task_completed_en.wav', wait=True)
    sys.exit()

# Set up the GUI
if __name__ == "__main__":
    # Play welcome audio at startup
    play_audio('audio/welcome_en.wav')

    root = tk.Tk()
    root.title("Automation Controller")

    # Welcome message
    welcome_label = tk.Label(root, text="Welcome to the automation controller. What would you like to do?")
    welcome_label.pack(pady=10)

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
        tk.Radiobutton(root, text=text, variable=choice_var, value=value).pack(anchor='w', padx=10)

    # Frame for dynamic input fields
    input_frame = tk.Frame(root)
    input_frame.pack(pady=10)

    # Bind choice selection to update input fields
    choice_var.trace('w', update_input_frame)

    # Execute button
    execute_button = tk.Button(root, text="Execute", command=execute_task)
    execute_button.pack(pady=10)

    # Initialize input frame for default choice
    update_input_frame()

    # tk.Radiobutton(root, text="4) Tag pins and publish them", variable=choice_var, value=4).pack(anchor="w")
    # tk.Button(root, text="Execute", command=execute_task).pack()

    root.mainloop()