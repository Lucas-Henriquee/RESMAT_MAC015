def clear_frame(frame):

    for widget in frame.winfo_children():
        widget.destroy()

def center_window(window, width=1200, height=800):
    
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width // 2) - (width // 2)
    y = (screen_height // 2) - (height // 2)
    window.geometry(f"{width}x{height}+{x}+{y}")