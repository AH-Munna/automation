import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
import sys
# from functools import partial
import threading
import time
# from PIL import Image, ImageTk

# Import required functions from your modules
from components.ideogram_download import ideogram_download
from components_app.pin_create_app import pin_create_app
from components_app.pinterest_upload_app import pinterest_upload_app
from components_app.pinterest_tag_app import pinterest_tag_app
from components_app.doc_space_editor_app import doc_space_editor_app
from components.upload_to_canva import upload_to_canva
from components_app.remove_repetition_app import remove_repetitions_app
from components_app.wordpress_paste_app import wordpress_paste_app
from helper.play_audio import play_audio

class AutomationControllerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Automation Controller")
        self.root.geometry("1200x700")
        self.setup_theme()
        
        # App state variables
        self.choice_var = tk.IntVar(value=1)
        self.input_vars = {}
        
        # Create and configure main frames
        self.create_main_layout()
        
        # Initialize component-specific input variables
        self.initialize_input_vars()
        
        # Set up the navigation and input areas
        self.setup_navigation()
        self.setup_input_area()
        
        # Setup status bar and footer
        self.setup_status_bar()
        
        # Play welcome audio
        # threading.Thread(target=lambda: play_audio('audio/welcome_en.wav')).start()
    
    def setup_theme(self):
        """Set up the theme and styling for the application"""
        # Configure ttk style
        self.style = ttk.Style()
        self.style.theme_use('clam')  # Use 'clam' theme as base
        
        # Define colors
        self.primary_color = "#4a6fa5"      # Blue
        self.secondary_color = "#6c757d"    # Gray
        self.success_color = "#28a745"      # Green
        self.warning_color = "#ffc107"      # Yellow
        self.danger_color = "#dc3545"       # Red
        self.light_color = "#f8f9fa"        # Light Gray
        self.dark_color = "#343a40"         # Dark Gray
        self.bg_color = "#ffffff"           # White
        
        # Configure styles for various components
        self.style.configure('TFrame', background=self.bg_color)
        self.style.configure('Header.TFrame', background=self.primary_color)
        self.style.configure('Nav.TFrame', background=self.light_color)
        self.style.configure('Content.TFrame', background=self.bg_color)
        self.style.configure('Status.TFrame', background=self.light_color)
        
        self.style.configure('TLabel', background=self.bg_color, font=('Segoe UI', 10))
        self.style.configure('Header.TLabel', background=self.primary_color, foreground='white', font=('Segoe UI', 14, 'bold'))
        self.style.configure('Title.TLabel', font=('Segoe UI', 12, 'bold'))
        self.style.configure('Status.TLabel', background=self.light_color, font=('Segoe UI', 9))
        
        self.style.configure('TButton', font=('Segoe UI', 10))
        self.style.configure('Execute.TButton', background=self.success_color, foreground='white', font=('Segoe UI', 12, 'bold'))
        
        self.style.configure('TRadiobutton', background=self.bg_color, font=('Segoe UI', 10))
        self.style.configure('Nav.TRadiobutton', background=self.light_color, font=('Segoe UI', 11))
        
        self.style.configure('TCheckbutton', background=self.bg_color, font=('Segoe UI', 10))
        self.style.configure('TEntry', font=('Segoe UI', 10))
        
        # Configure the root window
        self.root.configure(bg=self.bg_color)
    
    def create_main_layout(self):
        """Create the main layout frames"""
        # Header frame
        self.header_frame = ttk.Frame(self.root, style='Header.TFrame')
        self.header_frame.pack(fill='x', padx=0, pady=0)
        
        # App title in header
        header_label = ttk.Label(self.header_frame, text="Automation Controller", style='Header.TLabel')
        header_label.pack(pady=15)
        
        # Main content area
        self.main_frame = ttk.Frame(self.root, style='TFrame')
        self.main_frame.pack(fill='both', expand=True, padx=15, pady=15)
        
        # Create a horizontal layout for navigation and content
        self.nav_frame = ttk.Frame(self.main_frame, style='Nav.TFrame', width=250)
        self.nav_frame.pack(side='left', fill='y', padx=0, pady=0)
        
        # Create a separator
        separator = ttk.Separator(self.main_frame, orient='vertical')
        separator.pack(side='left', fill='y', padx=10)
        
        # Content frame for input fields
        self.content_frame = ttk.Frame(self.main_frame, style='Content.TFrame')
        self.content_frame.pack(side='left', fill='both', expand=True, padx=0, pady=0)
        
        # Input frame - will contain dynamic inputs based on selected option
        self.input_frame = ttk.Frame(self.content_frame, style='TFrame')
        self.input_frame.pack(fill='both', expand=True, padx=20, pady=20)
        
        # Footer with execute button
        self.footer_frame = ttk.Frame(self.root, style='TFrame')
        self.footer_frame.pack(fill='x', padx=15, pady=(0, 15))
    
    def initialize_input_vars(self):
        """Initialize all input variables for each component"""
        # Choice 1: Create a pin from deepseek to ideogram
        self.input_vars[1] = {
            'type_of_execution': tk.IntVar(value=1),
            'thinking_model': tk.StringVar(value='y'),
            'browser_tab': tk.StringVar(value='season'),
            'title': tk.StringVar(),
            'download': tk.StringVar(value='y'),
            'upload': tk.StringVar(value='y'),
            'position': tk.StringVar(value='0')
        }
        
        # Choice 2: Download ideogram generated images
        self.input_vars[2] = {
            'upload': tk.StringVar(value='y'),
            'position': tk.StringVar(value='0')
        }
        
        # Choice 3: Upload pin images
        self.input_vars[3] = {
            'num_of_image': tk.StringVar(value='3'),
            'board_name': tk.StringVar(value=""),
            'board_pos': tk.StringVar(value='1')
        }
        
        # Choice 4: Tag pins and publish them
        self.input_vars[4] = {
            'number_of_pins': tk.StringVar(value='9')
        }
        
        # Choice 5: Remove keywords repetitions
        self.input_vars[5] = {
            'keywords_text': tk.StringVar()
        }
        
        # Choice 6: Edit doc space
        self.input_vars[6] = {
            'num_of_process': tk.StringVar(value='5')
        }

        # Choice 7: Paste to WordPress
        self.input_vars[7] = {
            'also_paste_content': tk.StringVar(value='n'),
            'post_title': tk.StringVar(value=''),
            'meta_description': tk.StringVar(value=''),
            'keywords': tk.StringVar(value='')
        }
    
        # Choice 8: upload to canva
        self.input_vars[8] = {
            'num_of_image': tk.StringVar(value='10'),
            'image_start_pos': tk.StringVar(value='0'),
        }

    def setup_navigation(self):
        """Set up the navigation sidebar"""
        # Navigation title
        nav_title = ttk.Label(self.nav_frame, text="Tasks", style='Title.TLabel')
        nav_title.pack(pady=(20, 15), padx=15, anchor='w')
        
        # Tasks menu
        choices = [
            ("Create pin", 1),
            ("Download ideogram images", 2),
            ("Upload pin images", 3),
            ("Tag pins and publish", 4),
            ("Remove keyword repetitions", 5),
            ("Edit doc space", 6),
            ("Paste to WordPress", 7),
            ("Upload to Canva", 8),
            ("Exit", 9)
        ]
        
        # Create a frame for the navigation buttons
        nav_buttons_frame = ttk.Frame(self.nav_frame, style='Nav.TFrame')
        nav_buttons_frame.pack(fill='both', expand=True, padx=0, pady=0)
        
        # Add each option as a radio button
        for text, value in choices:
            # Create a frame for each radio button for better styling
            btn_frame = ttk.Frame(nav_buttons_frame, style='Nav.TFrame')
            btn_frame.pack(fill='x', pady=1)
            
            rb = ttk.Radiobutton(
                btn_frame,
                text=text,
                variable=self.choice_var,
                value=value,
                style='Nav.TRadiobutton',
                command=self.update_input_frame
            )
            rb.pack(fill='x', padx=15, pady=8, anchor='w')
    
    def setup_input_area(self):
        """Initial setup of the input area based on default choice"""
        # Input area title
        self.input_title = ttk.Label(self.content_frame, text="Create Pin Settings", style='Title.TLabel')
        self.input_title.pack(pady=(0, 10), anchor='w')
        
        # Input description
        self.input_description = ttk.Label(
            self.content_frame, 
            text="Configure settings for creating a pin from deepseek to ideogram",
            wraplength=500
        )
        self.input_description.pack(pady=(0, 20), anchor='w')
        
        # Update input frame based on default choice
        self.update_input_frame()
    
    def setup_status_bar(self):
        """Set up the status bar at the bottom"""
        # Status bar
        self.status_frame = ttk.Frame(self.root, style='Status.TFrame')
        self.status_frame.pack(fill='x', side='bottom')
        
        # Status message
        self.status_var = tk.StringVar(value="Ready")
        self.status_label = ttk.Label(self.status_frame, textvariable=self.status_var, style='Status.TLabel')
        self.status_label.pack(side='left', padx=10, pady=5)
        
        # Execute button in footer
        self.execute_button = ttk.Button(
            self.footer_frame,
            text="Execute Task",
            command=self.execute_task,
            style='Execute.TButton'
        )
        self.execute_button.pack(side='right', padx=10, pady=10)
    
    def update_input_frame(self):
        """Update the input frame based on the selected choice."""
        choice = self.choice_var.get()
        
        # Clear the input frame
        for widget in self.input_frame.winfo_children():
            widget.destroy()
        
        # Update title and description based on choice
        titles = {
            1: "Create Pin Settings",
            2: "Download Ideogram Settings",
            3: "Upload Pin Settings",
            4: "Tag Pins Settings",
            5: "Remove Repetitions Tool",
            6: "Doc Space Editor Settings",
            7: "Paste to WordPress Settings",
            8: "Upload to Canva Settings",
            9: "Exit Application"
        }
        
        descriptions = {
            1: "Configure settings for creating a pin from deepseek to ideogram",
            2: "Configure settings for downloading ideogram generated images",
            3: "Configure settings for uploading pin images",
            4: "Configure settings for tagging pins and publishing them",
            5: "Remove repetitions from a list of keywords",
            6: "Configure settings for editing doc space",
            7: "Configure settings for pasting to WordPress",
            8: "Configure settings for uploading to Canva",
            9: "Exit the application"
        }
        
        self.input_title.config(text=titles.get(choice, ""))
        self.input_description.config(text=descriptions.get(choice, ""))
        
        # If exit is selected, update status and disable input
        if choice == 9:
            self.status_var.set("Ready to exit")
            return
        
        # Create the appropriate input widgets based on choice
        method_name = f"create_input_choice_{choice}"
        if hasattr(self, method_name):
            getattr(self, method_name)()
        
    def create_input_choice_1(self):
        """Create input fields for choice 1 - Create pin from deepseek to ideogram"""
        vars = self.input_vars[1]
        
        # Service selection frame
        service_frame = ttk.LabelFrame(self.input_frame, text="Service Selection")
        service_frame.pack(fill='x', padx=10, pady=10, anchor='w')
        
        ttk.Radiobutton(service_frame, text="API Service", variable=vars['type_of_execution'], value=1).pack(anchor='w', padx=20, pady=5)
        ttk.Radiobutton(service_frame, text="Web Service", variable=vars['type_of_execution'], value=2).pack(anchor='w', padx=20, pady=5)
        
        # Browser and model options frame
        options_frame = ttk.LabelFrame(self.input_frame, text="Options")
        options_frame.pack(fill='x', padx=10, pady=10, anchor='w')
        
        # Thinking model checkbox
        ttk.Checkbutton(options_frame, text="Use thinking model", 
                      variable=vars['thinking_model'], onvalue='y', offvalue='n').pack(anchor='w', padx=20, pady=5)
        
        # Browser tab selector
        browser_frame = ttk.Frame(options_frame)
        browser_frame.pack(fill='x', padx=20, pady=5, anchor='w')
        
        ttk.Label(browser_frame, text="Browser tab:").pack(side='left', padx=(0, 10))
        ttk.Radiobutton(browser_frame, text="Season", variable=vars['browser_tab'], value='season').pack(side='left', padx=10)
        ttk.Radiobutton(browser_frame, text="Red", variable=vars['browser_tab'], value='red').pack(side='left', padx=10)
        
        # Title input (only shown for API)
        self.title_frame = ttk.Frame(options_frame)
        self.title_frame.pack(fill='x', padx=20, pady=5, anchor='w')
        
        ttk.Label(self.title_frame, text="Title:").pack(side='left', padx=(0, 10))
        ttk.Entry(self.title_frame, textvariable=vars['title'], width=40).pack(side='left', fill='x', expand=True)
        
        # Processing options frame
        processing_frame = ttk.LabelFrame(self.input_frame, text="Processing Options")
        processing_frame.pack(fill='x', padx=10, pady=10, anchor='w')
        
        # Download checkbox
        ttk.Checkbutton(processing_frame, text="Download image", 
                      variable=vars['download'], onvalue='y', offvalue='n').pack(anchor='w', padx=20, pady=5)
        
        # Upload to Canva checkbox
        upload_check = ttk.Checkbutton(processing_frame, text="Upload to Canva", 
                                     variable=vars['upload'], onvalue='y', offvalue='n',
                                     command=lambda: self.toggle_position_visibility(1))
        upload_check.pack(anchor='w', padx=20, pady=5)
        
        # Position input frame
        self.position_frame_1 = ttk.Frame(processing_frame)
        self.position_frame_1.pack(fill='x', padx=20, pady=5, anchor='w')
        
        ttk.Label(self.position_frame_1, text="Position:").pack(side='left', padx=(0, 10))
        ttk.Entry(self.position_frame_1, textvariable=vars['position'], width=10).pack(side='left')
        
        # Set initial visibility based on checkbox state
        self.toggle_position_visibility(1)
        
        # Toggle title visibility based on type of execution
        vars['type_of_execution'].trace('w', lambda *args: self.toggle_title_visibility())
        self.toggle_title_visibility()
    
    def toggle_title_visibility(self):
        """Toggle visibility of title input based on type of execution"""
        type_of_execution = self.input_vars[1]['type_of_execution'].get()
        if type_of_execution == 1:  # API
            self.title_frame.pack(fill='x', padx=20, pady=5, anchor='w')
        else:
            self.title_frame.pack_forget()
    
    def toggle_position_visibility(self, choice_num):
        """Toggle visibility of position input based on upload checkbox"""
        vars = self.input_vars[choice_num]
        position_frame_attr = f"position_frame_{choice_num}"
        
        if hasattr(self, position_frame_attr):
            position_frame = getattr(self, position_frame_attr)
            if vars['upload'].get() == 'y':
                position_frame.pack(fill='x', padx=20, pady=5, anchor='w')
            else:
                position_frame.pack_forget()
    
    def create_input_choice_2(self):
        """Create input fields for choice 2 - Download ideogram generated images"""
        vars = self.input_vars[2]
        
        # Processing options frame
        processing_frame = ttk.LabelFrame(self.input_frame, text="Processing Options")
        processing_frame.pack(fill='x', padx=10, pady=10, anchor='w')
        
        # Upload to Canva checkbox
        upload_check = ttk.Checkbutton(processing_frame, text="Upload to Canva", 
                                     variable=vars['upload'], onvalue='y', offvalue='n',
                                     command=lambda: self.toggle_position_visibility(2))
        upload_check.pack(anchor='w', padx=20, pady=5)
        
        # Position input frame
        self.position_frame_2 = ttk.Frame(processing_frame)
        self.position_frame_2.pack(fill='x', padx=20, pady=5, anchor='w')
        
        ttk.Label(self.position_frame_2, text="Position:").pack(side='left', padx=(0, 10))
        ttk.Entry(self.position_frame_2, textvariable=vars['position'], width=10).pack(side='left')
        
        # Set initial visibility based on checkbox state
        self.toggle_position_visibility(2)
    
    def create_input_choice_3(self):
        """Create input fields for choice 3 - Upload pin images"""
        vars = self.input_vars[3]
        
        # Upload settings frame
        upload_frame = ttk.LabelFrame(self.input_frame, text="Upload Settings")
        upload_frame.pack(fill='x', padx=10, pady=10, anchor='w')
        
        # Number of images
        num_frame = ttk.Frame(upload_frame)
        num_frame.pack(fill='x', padx=20, pady=5, anchor='w')
        ttk.Label(num_frame, text="Number of Images:").pack(side='left', padx=(0, 10))
        ttk.Entry(num_frame, textvariable=vars['num_of_image'], width=10).pack(side='left')
        
        # Board name
        board_name_frame = ttk.Frame(upload_frame)
        board_name_frame.pack(fill='x', padx=20, pady=5, anchor='w')
        ttk.Label(board_name_frame, text="Board Name:").pack(side='left', padx=(0, 10))
        ttk.Entry(board_name_frame, textvariable=vars['board_name'], width=40).pack(side='left', fill='x', expand=True)
        
        # Board position
        board_pos_frame = ttk.Frame(upload_frame)
        board_pos_frame.pack(fill='x', padx=20, pady=5, anchor='w')
        ttk.Label(board_pos_frame, text="Board Position:").pack(side='left', padx=(0, 10))
        ttk.Entry(board_pos_frame, textvariable=vars['board_pos'], width=10).pack(side='left')
    
    def create_input_choice_4(self):
        """Create input fields for choice 4 - tag pins and publish them"""
        vars = self.input_vars[4]
        
        # pin tag settings frame
        wp_frame = ttk.LabelFrame(self.input_frame, text="pin number Settings")
        wp_frame.pack(fill='x', padx=10, pady=10, anchor='w')
        
        # number of pins input frame
        number_of_pins_var = ttk.Frame(wp_frame)
        number_of_pins_var.pack(fill='x', padx=20, pady=5, anchor='w')
        ttk.Label(number_of_pins_var, text="number of pins:").pack(side='left', padx=(0, 10))
        ttk.Entry(number_of_pins_var, textvariable=vars['number_of_pins'], width=50).pack(side='left', fill='x')
    
    def create_input_choice_5(self):
        """Create input fields for choice 5 - Remove keywords repetitions"""
        # Label to instruct the user
        ttk.Label(self.input_frame, text="Enter keywords (separated by commas or newlines):").pack(pady=10, anchor='w')
        
        # Text widget with scrollbar for multi-line input
        text_frame = ttk.Frame(self.input_frame)
        text_frame.pack(fill='both', expand=True, pady=5)
        
        scrollbar = ttk.Scrollbar(text_frame)
        scrollbar.pack(side='right', fill='y')
        
        self.keywords_text = tk.Text(text_frame, height=10, width=50, yscrollcommand=scrollbar.set)
        self.keywords_text.pack(side='left', fill='both', expand=True)
        scrollbar.config(command=self.keywords_text.yview)
        
        # Process button
        process_button = ttk.Button(
            self.input_frame,
            text="Process Keywords",
            command=lambda: self.process_keywords(self.keywords_text.get("1.0", tk.END))
        )
        process_button.pack(pady=10)
    
    def create_input_choice_6(self):
        """Create input fields for choice 6 - Edit doc space"""
        vars = self.input_vars[6]
        
        # Process settings frame
        process_frame = ttk.LabelFrame(self.input_frame, text="Process Settings")
        process_frame.pack(fill='x', padx=10, pady=10, anchor='w')
        
        # Number of lines
        lines_frame = ttk.Frame(process_frame)
        lines_frame.pack(fill='x', padx=20, pady=5, anchor='w')
        ttk.Label(lines_frame, text="Number of lines to process:").pack(side='left', padx=(0, 10))
        ttk.Entry(lines_frame, textvariable=vars['num_of_process'], width=10).pack(side='left')
    
    def create_input_choice_7(self):
        """Create input fields for choice 7 - Paste to WordPress"""
        vars = self.input_vars[7]
        
        # WordPress settings frame
        wp_frame = ttk.LabelFrame(self.input_frame, text="WordPress Settings")
        wp_frame.pack(fill='x', padx=10, pady=10, anchor='w')
        
        # Also paste content checkbox
        ttk.Checkbutton(wp_frame, text="Also paste post content", 
                    variable=vars['also_paste_content'], onvalue='y', offvalue='n').pack(anchor='w', padx=20, pady=5)
        
        # post title input frame
        post_title_var = ttk.Frame(wp_frame)
        post_title_var.pack(fill='x', padx=20, pady=5, anchor='w')
        ttk.Label(post_title_var, text="Post Title:").pack(side='left', padx=(0, 10))
        ttk.Entry(post_title_var, textvariable=vars['post_title'], width=40).pack(side='left', fill='x', expand=True)

        # meta description input frame
        meta_description_var = ttk.Frame(wp_frame)
        meta_description_var.pack(fill='x', padx=20, pady=5, anchor='w')
        ttk.Label(meta_description_var, text="Meta Description:").pack(side='left', padx=(0, 10))
        ttk.Entry(meta_description_var, textvariable=vars['meta_description'], width=50).pack(side='left', fill='x', expand=True)

        # keywords input frame
        keywords_var = ttk.Frame(wp_frame)
        keywords_var.pack(fill='x', padx=20, pady=5, anchor='w')
        ttk.Label(keywords_var, text="All Keywords:").pack(side='left', padx=(0, 10))
        ttk.Entry(keywords_var, textvariable=vars['keywords'], width=50).pack(side='left', fill='x', expand=True)

    def create_input_choice_8(self):
        """Create input fields for choice 8 - upload to canva"""
        vars = self.input_vars[8]
        
        # canva settings frame
        wp_frame = ttk.LabelFrame(self.input_frame, text="canva Settings")
        wp_frame.pack(fill='x', padx=10, pady=10, anchor='w')
        
        # number of images input frame
        num_of_image_var = ttk.Frame(wp_frame)
        num_of_image_var.pack(fill='x', padx=20, pady=5, anchor='w')
        ttk.Label(num_of_image_var, text="number of images:").pack(side='left', padx=(0, 10))
        ttk.Entry(num_of_image_var, textvariable=vars['num_of_image'], width=50).pack(side='left', fill='x')

        # image position input frame
        image_start_pos_var = ttk.Frame(wp_frame)
        image_start_pos_var.pack(fill='x', padx=20, pady=5, anchor='w')
        ttk.Label(image_start_pos_var, text="number of items before images:").pack(side='left', padx=(0, 10))
        ttk.Entry(image_start_pos_var, textvariable=vars['image_start_pos'], width=40).pack(side='left', fill='x')



    def process_keywords(self, keywords_text):
        """Process keywords and display unique results"""
        self.status_var.set("Processing keywords...")
        try:
            unique_keywords = remove_repetitions_app(keywords_text)
            if unique_keywords:
                messagebox.showinfo("Unique Keywords", "\n".join(unique_keywords))
            else:
                messagebox.showinfo("Unique Keywords", "No keywords entered or no duplicates found.")
            self.status_var.set("Keywords processed successfully")
        except Exception as e:
            messagebox.showerror("Error", f"Error processing keywords: {str(e)}")
            self.status_var.set("Error processing keywords")
    
    def execute_task(self):
        """Execute the selected task based on user inputs"""
        choice = self.choice_var.get()
        
        # If exit is selected, close the application
        if choice == 9:
            self.root.destroy()
            return
        
        # Update status
        self.status_var.set(f"Executing task {choice}...")
        self.root.update()
        
        try:
            # Call the appropriate execution method based on choice
            method_name = f"execute_choice_{choice}"
            if hasattr(self, method_name):
                threading.Thread(target=getattr(self, method_name)).start()
            else:
                self.status_var.set(f"No execution method for choice {choice}")
        except Exception as e:
            messagebox.showerror("Error", f"Error executing task: {str(e)}")
            self.status_var.set("Error executing task")
    
    def execute_choice_1(self):
        """Execute choice 1 - Create pin from deepseek to ideogram"""
        vars = self.input_vars[1]
        type_of_execution = vars['type_of_execution'].get()
        thinking_model = vars['thinking_model'].get()
        browser_tab = vars['browser_tab'].get()
        title = vars['title'].get()
        download_image = vars['download'].get()
        confirm_upload_to_canva = vars['upload'].get()
        
        try:
            downloaded_image_pos = int(vars['position'].get()) if confirm_upload_to_canva == 'y' else 0
        except ValueError:
            self.show_error_and_update_status("Position must be an integer")
            return
        
        # Execute the task
        # play_audio('audio/create_image_start_en.wav')
        pin_create_app(
            type_of_execution=type_of_execution,
            thinking_model=thinking_model,
            browser_tab=browser_tab,
            title=title
        )
        
        if download_image == 'y':
            ideogram_download(direct=True)
        
        if confirm_upload_to_canva == 'y':
            upload_to_canva(downloaded_image_pos=downloaded_image_pos)
        
        self.task_executed()
    
    def execute_choice_2(self):
        """Execute choice 2 - Download ideogram generated images"""
        vars = self.input_vars[2]
        confirm_upload_to_canva = vars['upload'].get()
        
        try:
            downloaded_image_pos = int(vars['position'].get()) if confirm_upload_to_canva == 'y' else 0
        except ValueError:
            self.show_error_and_update_status("Position must be an integer")
            return
        
        ideogram_download()
        
        if confirm_upload_to_canva == 'y':
            upload_to_canva(downloaded_image_pos=downloaded_image_pos)
        
        self.task_executed()
    
    def execute_choice_3(self):
        """Execute choice 3 - Upload pin images"""
        vars = self.input_vars[3]
        
        try:
            num_of_image = int(vars['num_of_image'].get())
            board_name = vars['board_name'].get()
            board_pos = int(vars['board_pos'].get())
        except ValueError:
            self.show_error_and_update_status("Number of images and board position must be integers")
            return
        
        pinterest_upload_app(board_name=board_name, board_pos=board_pos, num_of_image=num_of_image)
        self.task_executed()
    
    def execute_choice_4(self):
        """Execute choice 4 - Tag pins and publish them"""
        # play_audio('audio/tag_pin_options_en.wav')
        vars = self.input_vars[4]
        number_of_pins = vars['number_of_pins'].get()
        
        try:
            # Call your WordPress paste function here
            self.status_var.set("tagging pins...")
            pinterest_tag_app(post_amount=int(number_of_pins))
            
            self.task_executed()
        except Exception as e:
            self.show_error_and_update_status(f"Error pasting to WordPress: {str(e)}")
    
    def execute_choice_5(self):
        """Execute choice 5 - Remove keywords repetitions"""
        if hasattr(self, 'keywords_text'):
            self.process_keywords(self.keywords_text.get("1.0", tk.END))
        else:
            remove_repetitions_app()
    
    def execute_choice_6(self):
        """Execute choice 6 - Edit doc space"""
        vars = self.input_vars[6]
        
        try:
            num_of_line = int(vars['num_of_process'].get())
            doc_space_editor_app(num_of_line)
            self.task_executed()
        except ValueError:
            self.show_error_and_update_status("Number of lines must be an integer")
    
    def execute_choice_7(self):
        """Execute choice 7 - Paste to WordPress"""
        vars = self.input_vars[7]
        also_paste_content = vars['also_paste_content'].get()
        post_title = vars['post_title'].get()
        meta_description = vars['meta_description'].get()
        keywords = vars['keywords'].get()
        
        try:
            # Call your WordPress paste function here
            wordpress_paste_app(post_title=post_title, meta_description=meta_description, keywords=keywords, post_content="", also_paste_content=also_paste_content == 'y')
            # For example: wordpress_paste(also_paste_content=also_paste_content)
            
            # Placeholder for the actual implementation
            self.status_var.set("Pasting to WordPress...")
            
            # You'll need to create or import the actual function
            # For now, just display a message
            # messagebox.showinfo("WordPress", f"Content pasted to WordPress. Also paste content: {also_paste_content == 'y'}")
            
            self.task_executed()
        except Exception as e:
            self.show_error_and_update_status(f"Error pasting to WordPress: {str(e)}")
    
    def execute_choice_8(self):
        """Execute choice 8 - upload to canva"""
        vars = self.input_vars[8]
        num_of_image = vars['num_of_image'].get()
        image_start_pos = vars['image_start_pos'].get()
        
        try:
            # Call your WordPress paste function here
            self.status_var.set("uploading to canva...")
            upload_to_canva(number_of_image=int(num_of_image), downloaded_image_pos=int(image_start_pos))
            
            self.task_executed()
        except Exception as e:
            self.show_error_and_update_status(f"Error pasting to WordPress: {str(e)}")

    def show_error_and_update_status(self, message):
        """Show error message and update status bar"""
        messagebox.showerror("Error", message)
        self.status_var.set(f"Error: {message}")
    
    def task_executed(self):
        """Play completion audio and exit"""
        self.status_var.set("Task completed successfully")
        play_audio('audio/task_completed_en.wav', wait=True)
        sys.exit()