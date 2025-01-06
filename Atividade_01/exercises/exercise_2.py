from tkinter import Label, Button
from src.window import create_main_screen
from src.force_operations import calculate_resultant


def exercise_2_ui(frame, window):

    for widget in frame.winfo_children():
        widget.destroy()

    Label(frame, text="Exercício 2: Apoio em Vigas", font=("Arial", 28, "bold"), bg="#2e3b4e", fg="#f0f0f0").pack(pady=20)

    Button(frame, text="Voltar ao Menu Principal", font=("Arial", 20, "bold"), bg="#d32f2f", fg="white", command=lambda: go_back_to_menu(window, frame), width=20, height=2).pack(pady=20)

def go_back_to_menu(window, frame):

    from Atividade_01.src.window import create_main_screen
    create_main_screen(window, frame)
