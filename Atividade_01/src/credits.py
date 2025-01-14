from imports.all_imports import *
from .util import clear_frame

def credits_ui(frame, window):

    def go_back():
        from .window import create_main_screen
        create_main_screen(window, frame)

    clear_frame(frame)

    Label(
        frame,
        text="Créditos",
        font=("Arial", 24, "bold"),
        bg="#2e3b4e",
        fg="#f0f0f0"
    ).pack(pady=20)

    Label(
        frame,
        text=(
            "Esse programa foi desenvolvido pelos alunos Lucas Henrique e Breno Montanha como parte da Atividade 01 da disciplina de Resistência dos Materiais (Turma X) oferecida pela UFJF no segundo período letivo de 2024, sob a orientação do professor Artur Hallack.\n\n"
            "A Atividade 01 consiste no desenvolvimento de rotinas computacionais para resolver problemas práticos de Engenharia relacionados a forças concorrentes, reações em vigas apoiadas e análise de treliças planas isostáticas. O objetivo principal é aplicar conceitos teóricos à prática por meio da programação, promovendo o entendimento aprofundado das estruturas estudadas."
        ),
        font=("Arial", 16),
        bg="#2e3b4e",
        fg="#f0f0f0",
        wraplength=800,
        justify="left"  
    ).pack(pady=10)

    Label(
        frame,
        text="Fontes Bibliográficas",
        font=("Arial", 18, "bold"),
        bg="#2e3b4e",
        fg="#f0f0f0",
    ).pack(pady=(30, 5))

    Label(
        frame,
        text=(
            "Todos os exercícios desenvolvidos (1, 2, 3) foram baseados nos problemas apresentados pelo professor, utilizando o material de apoio disponibilizado."
        ),
        font=("Arial", 16),
        bg="#2e3b4e",
        fg="#f0f0f0",
        wraplength=800,
        justify="left"  
    ).pack(pady=10)

    Label(
        frame,
        text="Imagens",
        font=("Arial", 18, "bold"),
        bg="#2e3b4e",
        fg="#f0f0f0",
    ).pack(pady=(30, 5))

    Label(
        frame,
        text=(
            "- Imagem 1 (Exercício 1): Retirada do enunciado fornecido pelo professor.\n"
            "- Imagem 2 (Exercício 2): Retiradas da Internet.\n"
            "- Imagem 3 (Exercício 3): Extraída do livro Mecânica e Resistência dos Materiais de Hibbeler."
        ),
        font=("Arial", 16),
        bg="#2e3b4e",
        fg="#f0f0f0",
        wraplength=800,
        justify="left"  
    ).pack(pady=10)

    Button(
        frame,
        text="Voltar",
        font=("Arial", 16, "bold"),
        bg="#d32f2f",
        fg="white",
        command=go_back,
        cursor="hand2",
        relief="raised",
        width=15,
        height=2
    ).pack(pady=20)