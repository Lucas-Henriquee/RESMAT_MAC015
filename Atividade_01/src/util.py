import sys
from tkinter import messagebox

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

def confirm_exit_to_main(window, frame):

    from .window import create_main_screen
    
    if messagebox.askyesno("Confirmação", "Deseja voltar ao menu principal? Todas as alterações serão perdidas."):
            create_main_screen(window, frame)