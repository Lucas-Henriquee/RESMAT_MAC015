from tkinter import Label, Button
from window import create_main_screen
from force_operations import calcular_resultante

def exercise_3_ui(frame, window):

    for widget in frame.winfo_children():
        widget.destroy()

def go_back_to_menu(window, frame):

    from window import create_main_screen
    create_main_screen(window, frame)
