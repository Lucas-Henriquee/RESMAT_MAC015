from .all_imports import *

def clear_frame(frame):
    for widget in frame.winfo_children():
        widget.destroy()

def center_window(window):
    width, height = 1300, 850  
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width // 2) - (width // 2)
    y = (screen_height // 2) - (height // 2)
    window.geometry(f"{width}x{height}+{x}+{y}")

def exit_program():
    sys.exit(0)

def confirm_exit_to_main(window, frame, screen):

    from .window import create_main_screen_activity_01
    from .window import create_main_screen_activity_02
    from .window import create_main_screen_activity_03
    
    messagebox.askyesno("Confirmação", "Deseja voltar ao Menu? Todas as alterações serão perdidas.")

    if(messagebox.askyesno):
        if screen == 1:
            create_main_screen_activity_01(window, frame)
        
        elif screen == 2:
            create_main_screen_activity_02(window, frame)

        elif screen == 3:
            create_main_screen_activity_03(window, frame)

def configure_close_behavior(window):
    def on_close():
        window.destroy()

    window.protocol("WM_DELETE_WINDOW", on_close)

def create_label(frame, text, font, bg, fg, pady=None):
    label = Label(frame, text=text, font=font, bg=bg, fg=fg)
    label.pack(pady=pady)
    return label

def create_button(frame, text, font, bg, fg, command, width, height, pady=None):
    button = Button(
        frame, text=text, font=font, bg=bg, fg=fg, command=command,
        cursor="hand2", relief="raised", width=width, height=height
    )
    button.pack(pady=pady)
    return button

def get_absolute_path(relative_path):
    if getattr(sys, "frozen", False):  
        base_dir = sys._MEIPASS      # PyInstaller
    else: 
        base_dir = os.path.dirname(os.path.abspath(sys.argv[0]))  #Python

    return os.path.join(base_dir, relative_path)