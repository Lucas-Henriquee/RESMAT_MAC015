from tkinter import Label, Button, Entry, Frame, Radiobutton, StringVar
from src.window import create_main_screen
from src.force_operations import calculate_resultant
from src.util import clear_frame


def exercise_2_ui(frame, window):

    clear_frame(frame)

    Label(frame, text="Exercício 2: Apoio em Vigas", font=("Arial", 28, "bold"), bg="#2e3b4e", fg="#f0f0f0").pack(pady=20)

    Label(frame, text="Digite o comprimento da barra(em metros):", font=("Arial", 16), bg="#2e3b4e", fg="#f0f0f0").pack(pady=20)
    entry_lenght = Entry(frame, font=("Arial", 16), width=10, justify="center")
    entry_lenght.pack(pady=15)

    button_frame_1 = Frame(frame, bg="#2e3b4e")
    button_frame_1.pack(pady=20)

    Button(button_frame_1, text="Iniciar", font=("Arial", 18, "bold"), bg="#4caf50", fg="white", command=lambda: get_lenght(entry_lenght) , cursor="hand2", width=15, height=2).pack(side="left", padx=20)
    Button(button_frame_1, text="Voltar", font=("Arial", 18, "bold"), bg="#d32f2f", fg="white", command=lambda: go_back_to_menu(frame, window), cursor="hand2", width=15, height=2).pack(side="left", padx=20)

    def get_lenght(entry_lenght):

        lenght = entry_lenght.get()

        if lenght == "":
            return

        try:
            lenght = float(lenght)
            create_supports_relation_frame(lenght)

            def create_supports_relation_frame(lenght):
                clear_frame(frame)

                entry_type = StringVar()

                Label(frame,text="Escolha o tipo de apoios:", font=("Arial", 18), bg="#2e3b4e", fg="#f0f0f0",).pack(pady=10)
                frame_entry_type = Frame(frame, bg="#2e3b4e")
                frame_entry_type.pack(pady=10)

                button_angle = Radiobutton(frame_entry_type, text="Engaste", font=("Arial", 20), cursor="hand2", variable=entry_type, value="graus",bg="#4caf50", fg="white", selectcolor="#2e3b4e",)
                button_angle.pack(side="left", padx=20)
                button_coord = Radiobutton(frame_entry_type, text="Apoio de segundo gênero e apoio de primeiro gênero", font=("Arial", 20), cursor="hand2", variable=entry_type, value="coordenadas",bg="#2e3b4e", fg="#f0f0f0", selectcolor="#2e3b4e",)
                button_coord.pack(side="left", padx=20)
                button_coord = Radiobutton(frame_entry_type, text="Três apoios de primeiro gênero", font=("Arial", 20), cursor="hand2", variable=entry_type, value="coordenadas",bg="#2e3b4e", fg="#f0f0f0", selectcolor="#2e3b4e",)
                button_coord.pack(side="left", padx=20)
                
                
        except Exception as e:
            print(f"Erro ao converter o comprimento para float: {e}")


def go_back_to_menu(window, frame):

    create_main_screen(window, frame)
