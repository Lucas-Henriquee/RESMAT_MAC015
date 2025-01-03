import sys

def clear_frame(frame):

    for widget in frame.winfo_children():
        widget.destroy()

def center_window(window, width=1300, height=900):
    
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width // 2) - (width // 2)
    y = (screen_height // 2) - (height // 2)
    window.geometry(f"{width}x{height}+{x}+{y}")

def exit_program():
    sys.exit(0)