from .all_imports import *
from .util import clear_frame

def go_back(frame, window, type):
    
    from .window import create_main_screen, create_main_screen_activity_01, create_main_screen_activity_02, create_main_screen_activity_03

    cases = {
        0: create_main_screen,
        1: create_main_screen_activity_01,
        2: create_main_screen_activity_02,
        3: create_main_screen_activity_03,
    }

    case_function = cases.get(type)
    case_function(window, frame)  

def credits_ui(frame, window, type):
    clear_frame(frame)

    if type == 1:
        information_1_ui(frame, window)
    
    elif type == 2:
        information_2_ui(frame, window)
    
    elif type == 3:
        information_3_ui(frame, window)
    
    else:
        credits_ui(frame, window)

def credits_ui(frame, window):

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
            "Esse programa foi desenvolvido pelos alunos Lucas Henrique e Breno Montanha como proposta de avaliação da disciplina de Resistência dos Materiais (Turma X) "
            "oferecida pela UFJF no segundo período letivo de 2024, sob a orientação do professor Artur Hallack.\n\n"
            "O programa foi desenvolvido em Python, utilizando a biblioteca Tkinter para a interface gráfica e os módulos Math, Numpy, Sympy para cálculos matemáticos."
        ),
        font=("Arial", 16),
        bg="#2e3b4e",
        fg="#f0f0f0",
        wraplength=800,
        justify="left"
    ).pack(pady=10)

    Label(
        frame,
        text="Atividades do Programa",
        font=("Arial", 24, "bold"),
        bg="#2e3b4e",
        fg="#f0f0f0"
    ).pack(pady=20)

    Label(
        frame,
        text=(
            "As atividades do programa consistem no desenvolvimento de rotinas computacionais para resolver problemas práticos de engenharia.\n\n"
            
            "Atividade 01: Forças concorrentes, reações em vigas apoiadas e análise de treliças planas isostáticas.\n\n"
            
            "Atividade 02: Cálculo dos esforços internos (M(x) e V(x)) e representação dos diagramas em vigas isostáticas, além da plotagem e do cálculo da configuração deformada de treliças planas isostáticas com fator de escala adequado."
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
        command= lambda: go_back(frame, window, 0),
        cursor="hand2",
        relief="raised",
        width=15,
        height=2
        ).pack(pady=45)

def information_1_ui(frame, window):

    clear_frame(frame)

    Label(
        frame,
        text="Atividades Desenvolvidas",
        font=("Arial", 18, "bold"),
        bg="#2e3b4e",
        fg="#f0f0f0",
    ).pack(pady=(30, 5))

    Label(
        frame,
        text=(
            "- Exercício 1: Cálculo da intensidade e direção da força resultante de sistemas de forças coplanares concorrentes, com visualização gráfica dos vetores.\n"
            "- Exercício 2: Determinação das reações de apoio em vigas submetidas a carregamentos pontuais e distribuídos, utilizando equações de equilíbrio.\n"
            "- Exercício 3: Análise de treliças planas isostáticas, incluindo a definição de nós, barras e apoios, além do cálculo dos esforços internos nas barras, classificando-os como tração ou compressão."
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
        command= lambda: go_back(frame, window, 1),
        cursor="hand2",
        relief="raised",
        width=15,
        height=2
        ).pack(pady=20)


def information_2_ui(frame, window):
    clear_frame(frame)

    Label(
        frame,
        text="Atividades Desenvolvidas",
        font=("Arial", 18, "bold"),
        bg="#2e3b4e",
        fg="#f0f0f0",
    ).pack(pady=(30, 5))

    Label(
        frame,
        text=(
            "- Exercício 1: O Cálculo dos esforços internos em vigas isostáticas, "
            "com geração das equações M(x) e V(x), além da representação gráfica dos respectivos diagramas.\n"
            "- Exercício 2: O plote e o cálculo da configuração deformada de treliças planas isostáticas, "
            "incluindo a aplicação de fator de escala adequado para visualização clara da deformação."
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
            "Todos os exercícios desenvolvidos (1, 2) foram baseados nos problemas apresentados pelo professor, utilizando o material de apoio disponibilizado como base."
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
            "- Imagem 1 (Exercício 1): Retiradas da Internet.\n"
            "- Imagem 2 (Exercício 2): Retirada da Internet.\n"
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
        command= lambda: go_back(frame, window, 2),
        cursor="hand2",
        relief="raised",
        width=15,
        height=2
        ).pack(pady=20)

def information_3_ui(frame, window):
    pass