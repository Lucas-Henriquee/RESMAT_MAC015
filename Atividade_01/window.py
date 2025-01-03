from tkinter import Label, Button
from util import clear_frame, center_window

def configure_window(window):
    window.title("RESMAT - Atividade 01")
    center_window(window, 1200, 800)  
    window.configure(bg="#2e3b4e")

def create_main_screen(window, frame):
    clear_frame(frame)

    from exercise_1 import exercise_1_ui
    from exercise_2 import exercise_2_ui
    from exercise_3 import exercise_3_ui

    def create_label(frame, text, font, bg, fg, side=None, pady=None):
        label = Label(frame, text=text, font=font, bg=bg, fg=fg)
        label.pack(side=side, pady=pady)
        return label

    def create_button(frame, text, font, bg, fg, command, width, height, side=None, pady=None):
        button = Button(
            frame, text=text, font=font, bg=bg, fg=fg, command=command, 
            cursor="hand2", relief="raised", width=width, height=height
        )
        button.pack(side=side, pady=pady)
        return button

    create_label(frame, "Resistência dos Materiais - 2024/3\n\nAtividade 01", 
                 ("Arial", 24, "bold"), "#2e3b4e", "#f0f0f0", pady=30)

    create_label(frame, "Selecione um exercício", 
                 ("Arial", 18), "#2e3b4e", "#f0f0f0", pady=20)

    button_width = 35  

    create_button(
        frame, "Exercício 1 - Forças Concorrentes", 
        ("Arial", 16, "bold"), "#4caf50", "white", lambda: exercise_1_ui(frame, window),
        button_width, 2, pady=20
    )

    create_button(
        frame, "Exercício 2 - Apoio em Vigas", 
        ("Arial", 16, "bold"), "#2196f3", "white", lambda: exercise_2_ui(frame, window),
        button_width, 2, pady=20
    )

    create_button(
        frame, "Exercício 3 - Treliças Planas", 
        ("Arial", 16, "bold"), "#ff9800", "white", lambda: exercise_3_ui(frame, window),
        button_width, 2, pady=20
    )

    create_label(frame, "Feito por: Breno Montanha e Lucas Henrique\nProf: Artur Hallack", 
                 ("Arial", 14, "italic"), "#2e3b4e", "#f0f0f0", side="bottom", pady=15)
    
    create_button(
        frame, "Sair", 
        ("Arial", 16, "bold"), "#d32f2f", "white", window.destroy,
        button_width, 2, side="bottom", pady=20
    )
