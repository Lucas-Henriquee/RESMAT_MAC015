from tkinter import Label, Button
from src.window import create_main_screen
from src.force_operations import calculate_resultant

def exercise_3_ui(frame, window):

    for widget in frame.winfo_children():
        widget.destroy()

def go_back_to_menu(window, frame):

    from Atividade_01.src.window import create_main_screen
    create_main_screen(window, frame)
