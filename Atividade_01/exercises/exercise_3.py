from tkinter import Label, Entry, Button, Frame, messagebox
from src.util import clear_frame
from src.window import create_main_screen
from PIL import Image, ImageTk

def exercise_3_ui(frame, window):

    def start_1():
        clear_frame(frame)

        Label(
            frame,
            text="Exercício 3: Análise de Treliças Planas Isostáticas",
            font=("Arial", 28, "bold"),
            bg="#2e3b4e",
            fg="#f0f0f0",
        ).pack(pady=20)


        explanation1 = (
            "Neste exercício, você realizará a Análise e o Cálculo de Treliças Planas Isostáticas. "
            "O objetivo é configurar corretamente os parâmetros de uma treliça isostática, fornecendo informações como:\n\n"
            "- Nós: Os pontos que compõem a estrutura.\n"
            "- Barras: Os elementos conectando os nós.\n"
            "- Carregamentos: As forças aplicadas nos nós.\n"
            "- Apoios: Os tipos e localizações de restrições na estrutura.\n\n"
            "A análise correta dos dados permitirá determinar os esforços internos das barras e a estabilidade da treliça."
        )


        Label(
            frame,
            text=explanation1,
            font=("Arial", 16),
            bg="#2e3b4e",
            fg="#f0f0f0",
            wraplength=800,
            justify="left",
        ).pack(pady=20)

        try:
            img = Image.open("assets/exercise_2.png") 
            img = img.resize((600, 300), Image.Resampling.LANCZOS) 
            img = ImageTk.PhotoImage(img)

            img_label = Label(frame, image=img, bg="#2e3b4e")
            img_label.image = img  
            img_label.pack(pady=20)
        except Exception as e:
            print(f"Erro ao carregar a imagem: {e}")


        button_frame = Frame(frame, bg="#2e3b4e")
        button_frame.pack(pady=20)

        Button(button_frame,
            text="Próximo",
            font=("Arial", 18, "bold"),
            bg="#4caf50",
            fg="white",
            command=lambda: start_2(),
            cursor="hand2",
            width=15,
            height=2,
        ).pack(side = "left", padx=20)

        Button(
            button_frame,
            text="Voltar",
            font=("Arial", 18, "bold"),
            bg="#d32f2f",
            fg="white",
            command=lambda: create_main_screen(window, frame),
            cursor="hand2",
            width=15,
            height=2,
        ).pack(side = "right", padx=20)


    def start_2():
        clear_frame(frame)

        Label(
            frame,
            text="Exercício 3: Análise de Treliças Planas Isostáticas",
            font=("Arial", 28, "bold"),
            bg="#2e3b4e",
            fg="#f0f0f0",
        ).pack(pady=20)

        Label(
            frame,
            text="Orientações para Configuração",
            font=("Arial", 24, "bold"),
            bg="#2e3b4e",
            fg="#f0f0f0",
        ).pack(pady=20)

        explanation2 = (
            "Para configurar o problema, siga estas etapas:\n\n"
            "1. Adicionar os nós: Insira a localização de cada nó da treliça, especificando suas coordenadas X e Y.\n\n"
            "2. Definir as barras: Indique as conexões entre os nós que formarão as barras da treliça, especificando os nós "
            "de início e fim de cada barra.\n\n"
            "3. Definir os carregamentos: Para cada carregamento, especifique o nó onde ele será aplicado e forneça o vetor "
            "do peso (intensidade e direção).\n\n"
            "4. Inserir os apoios: Informe o nó onde cada apoio estará localizado e o tipo de apoio que será usado: \n"
            "   - Apoio fixo (Apoio de 1º Gênero): Bloqueia deslocamentos em todas as direções.\n"
            "   - Apoio móvel (Apoio de 2º Gênero): Permite deslocamento em uma direção e bloqueia na perpendicular.\n"
            "   - Engaste (Apoio de 3º Gênero): Restringe deslocamentos e rotações, fixando o corpo.\n\n"
            )

        Label(
            frame,
            text=explanation2,
            font=("Arial", 16),
            bg="#2e3b4e",
            fg="#f0f0f0",
            wraplength=800,
            justify="left",
        ).pack(pady=20)

        button_frame = Frame(frame, bg="#2e3b4e")
        button_frame.pack(pady=20)

        Button(button_frame,
            text="Próximo",
            font=("Arial", 18, "bold"),
            bg="#4caf50",
            fg="white",
            command=lambda: None,
            cursor="hand2",
            width=15,
            height=2,
        ).pack(side = "left", padx=20)

        Button(
            button_frame,
            text="Voltar",
            font=("Arial", 18, "bold"),
            bg="#d32f2f",
            fg="white",
            command=lambda: start_1(),
            cursor="hand2",
            width=15,
            height=2,
        ).pack(side = "right", padx=20)

    start_1()