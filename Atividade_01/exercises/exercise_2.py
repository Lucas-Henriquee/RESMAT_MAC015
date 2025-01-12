from tkinter import Label, Button, Entry, Frame, Radiobutton, StringVar, messagebox
from src.window import create_main_screen
from src.force_operations import calculate_resultant
from src.util import clear_frame
import sympy as sp


def exercise_2_ui(frame, window):

    def start_1():
        clear_frame(frame)

        Label(
            frame,
            text="Exercício 2: Análise de Carregamento em Viga",
            font=("Arial", 28, "bold"),
            bg="#2e3b4e",
            fg="#f0f0f0",
        ).pack(pady=20)

        explanation1 = (
            "A "
            "B\n\n"
            "C\n"
            "D\n"
            "E\n"
            "F\n\n"
            "G"
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
            text="Exercício 2: Análise de Carregamento em Viga",
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
            "1. Preencha o tamanho da viga\n\n"
            "2. Escolha o tipo de apoio na viga: Biapoiada ou Engastada\n\n"
            "3. Definir a função de carregamento ou o carregamento pontual\n\n"
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
            text="Iniciar",
            font=("Arial", 18, "bold"),
            bg="#4caf50",
            fg="white",
            command=lambda: start_3(),
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

    def start_3():
        clear_frame(frame)

        Label(
            frame,
            text="Exercício 2: Análise de Carregamento em Viga",
            font=("Arial", 28, "bold"),
            bg="#2e3b4e",
            fg="#f0f0f0",
        ).pack(pady=20)

        Label(
            frame,
            text="Configuração da Viga",
            font=("Arial", 24, "bold"),
            bg="#2e3b4e",
            fg="#f0f0f0",
        ).pack(pady=20)

        explanation_lenght = (
            "Preencha o tamanho da viga em metros.\n\n"
            "Largura (m): \n\n"
        )
        
        Label(
            frame,
            text=explanation_lenght,
            font=("Arial", 16),
            bg="#2e3b4e",
            fg="#f0f0f0",
            justify="center",
        ).pack(pady=20)
        entry_lenght = Entry(frame, font=("Arial", 16), width=15)
        entry_lenght.pack(pady=20)

        explanation_support_type = (
            "Tipo de Apoio:\n\n"
        )
        Label(
            frame,
            text=explanation_support_type,
            font=("Arial", 16),
            bg="#2e3b4e",
            fg="#f0f0f0",
            justify="center",
        ).pack(pady=20)

        entry_type = StringVar()

        frame_entry_type = Frame(frame, bg="#2e3b4e")
        frame_entry_type.pack(pady=10)

        button_angle = Radiobutton(frame_entry_type, text="engastada", font=("Arial", 20), cursor="hand2", variable=entry_type, value="engastada",bg="#4caf50", fg="white", selectcolor="#2e3b4e",)
        button_angle.pack(side="left", padx=20)
        button_coord = Radiobutton(frame_entry_type, text="biapoiada", font=("Arial", 20), cursor="hand2", variable=entry_type, value="biapoiada",bg="#2e3b4e", fg="#f0f0f0", selectcolor="#2e3b4e",)
        button_coord.pack(side="left", padx=20)

        button_frame = Frame(frame, bg="#2e3b4e")
        button_frame.pack(pady=20)

        Button(button_frame,
            text="Próximo",
            font=("Arial", 18, "bold"),
            bg="#4caf50",
            fg="white",
            command=lambda: info_apoio(entry_lenght.get(), entry_type.get()),
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
            command=lambda: start_2(),
            cursor="hand2",
            width=15,
            height=2,
        ).pack(side = "right", padx=20)

    def info_apoio(length, support_type):
        clear_frame(frame)

        Label(
            frame,
            text="Exercício 2: Análise de Carregamento em Viga",
            font=("Arial", 28, "bold"),
            bg="#2e3b4e",
            fg="#f0f0f0",
        ).pack(pady=20)

        explanation_position = (
            "Para esse exercício, a viga inicia no ponto 0 do eixo x\n\n"
            "Sabendo disso, preencha as informações dos apoios\n\n"
        )

        Label(
            frame,
            text=explanation_position,
            font=("Arial", 16),
            bg="#2e3b4e",
            fg="#f0f0f0",
            wraplength=800,
            justify="left",
        ).pack(pady=20)

        if(support_type == "engastada"):
            explanation_support = (
                "O engaste da viga deve estar em uma extremidade, então insira ou 0 "
                "ou o valor de L para o apoio\n\n"
            )
        else:
            explanation_support = (
                "A viga é biapoiada, então insira valores entre 0 e L para os apoios\n\n"
                "Lembre-se que os apoios devem estar em pontos diferentes\n\n"
            )
        
        Label(
            frame,
            text=explanation_support,
            font=("Arial", 16),
            bg="#2e3b4e",
            fg="#f0f0f0",
            wraplength=800,
            justify="left",
        ).pack(pady=20)

        if(support_type == "engastada"):
            Label(frame, text="Posição do apoio (m): ", font=("Arial", 16), bg="#2e3b4e", fg="#f0f0f0").pack(pady=20)
            entry_support = Entry(frame, font=("Arial", 16), width=15)
            entry_support.pack(pady=20)
        else:
            Label(frame, text="Posição do apoio 1 (m): ", font=("Arial", 16), bg="#2e3b4e", fg="#f0f0f0").pack(pady=20)
            entry_support1 = Entry(frame, font=("Arial", 16), width=15)
            entry_support1.pack(pady=20)

            Label(frame, text="Posição do apoio 2 (m): ", font=("Arial", 16), bg="#2e3b4e", fg="#f0f0f0").pack(pady=20)
            entry_support2 = Entry(frame, font=("Arial", 16), width=15)
            entry_support2.pack(pady=20)
        

        button_frame = Frame(frame, bg="#2e3b4e")
        button_frame.pack(pady=20)

        Button(
            button_frame,
            text="Iniciar",
            font=("Arial", 18, "bold"),
            bg="#4caf50",
            fg="white",
            command=lambda: info_forcas(length, support_type, entry_support.get() if support_type == "engastada" else [entry_support1.get(), entry_support2.get()]),
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
            command=lambda: start_3(),
            cursor="hand2",
            width=15,
            height=2,
        ).pack(side = "right", padx=20)

    def info_forcas(lenght, support_type, supports):
        clear_frame(frame)

        Label(
            frame,
            text="Exercício 2: Análise de Carregamento em Viga",
            font=("Arial", 28, "bold"),
            bg="#2e3b4e",
            fg="#f0f0f0",
        ).pack(pady=20)

        explanation_forces = (
            "Insira as informações de carregamento na viga\n\n"
        )

        Label(
            frame,
            text=explanation_forces,
            font=("Arial", 16),
            bg="#2e3b4e",
            fg="#f0f0f0",
            wraplength=800,
            justify="left",
        ).pack(pady=20)

        entry_type = StringVar()

        def update_input_fields(*args):
            frame_forca_pontual.pack_forget()
            frame_forca_funcao.pack_forget()
            print(entry_type.get())
            if(entry_type.get() == "pontual"):
                frame_forca_pontual.pack(pady=20)
            elif(entry_type.get() == "funcao"):
                frame_forca_funcao.pack(pady=20)
            else:
                pass
        def create_func_and_pontual_frames():
            frame_forca_pontual = Frame(frame, bg="#2e3b4e")
            explanation_force = (
                    "Força Pontual (N): \n\n"
            )
            Label(
                frame_forca_pontual,
                text=explanation_force,
                font=("Arial", 16),
                bg="#2e3b4e",
                fg="#f0f0f0",
                justify="center",
            ).pack(pady=20)
            entry_force = Entry(frame_forca_pontual, font=("Arial", 16), width=15)
            entry_force.pack(pady=20)

            explanation_position = (
                "Posição da força (m): \n\n"
            )
            Label(
                frame_forca_pontual,
                text=explanation_position,
                font=("Arial", 16),
                bg="#2e3b4e",
                fg="#f0f0f0",
                justify="center",
            ).pack(pady=20)
            entry_position = Entry(frame_forca_pontual, font=("Arial", 16), width=15)
            entry_position.pack(pady=20)
            frame_forca_funcao = Frame(frame, bg="#2e3b4e")
            explanation_force = (
                "Escreva a função que descreve a força em função de x: \n\n"
                "Para funções por partes, use a seguinte notação: {f(x), (a, b); g(x), (c, d); ...}\n\n"
                "Onde f(x) é a função, (a, b) é o intervalo de x onde a função é válida\n\n"
                "Exemplo: {x**2, (0, 2); 2*x, (2, 4)}\n\n"
            )
            Label(
                frame_forca_funcao,
                text=explanation_force,
                font=("Arial", 16),
                bg="#2e3b4e",
                fg="#f0f0f0",
                justify="center",
            ).pack(pady=20)
            entry_force_function = Entry(frame_forca_funcao, font=("Arial", 16), width=15)
            entry_force_function.pack(pady=20)
            return frame_forca_pontual, frame_forca_funcao, entry_force, entry_position, entry_force_function

        frame_forca_pontual, frame_forca_funcao, entry_force, entry_position, entry_force_function = create_func_and_pontual_frames()
        frame_entry_type = Frame(frame, bg="#2e3b4e")
        frame_entry_type.pack(pady=10)

        button_angle = Radiobutton(frame_entry_type, text="pontual", font=("Arial", 20), cursor="hand2", variable=entry_type, value="pontual",bg="#4caf50", fg="white", selectcolor="#2e3b4e",)
        button_angle.pack(side="left", padx=20)
        button_coord = Radiobutton(frame_entry_type, text="função", font=("Arial", 20), cursor="hand2", variable=entry_type, value="funcao",bg="#2e3b4e", fg="#f0f0f0", selectcolor="#2e3b4e",)
        button_coord.pack(side="left", padx=20)

        entry_type.trace_add("write", update_input_fields)
        update_input_fields()

        def analisar_funcao_por_partes(func_por_partes, var):
            x = sp.Symbol(var)
            soma_forcas = 0
            soma_momentos = 0
            for funcao, intervalo in func_por_partes:
                forca = sp.integrate(funcao, (x, intervalo[0], intervalo[1]))
                momento = sp.integrate(funcao * x, (x, intervalo[0], intervalo[1]))/sp.integrate(funcao, (x, intervalo[0], intervalo[1]))
                soma_forcas += forca
                soma_momentos += momento
        

        def analisar_funcao(event=None):
            entrada = entry_force.get().strip()  # Obter texto do Entry
            try:
                # Processar a entrada com sympy
                if "{" in entrada and "}" in entrada:
                    # Função por partes (usando uma notação específica)
                    partes = entrada[1:-1].split(";")
                    func_por_partes = []
                    for parte in partes:
                        funcao, intervalo = parte.split(",")
                        funcao = sp.sympify(funcao.strip())
                        intervalo = intervalo.strip()
                        intervalo = eval(intervalo)  # Convertendo para tuple
                        func_por_partes.append((funcao, intervalo))

                    resultados = analisar_funcao_por_partes(func_por_partes, 'x')

                    # Mostrar os resultados
                    texto_resultados = "Análise de Funções Definidas por Partes:\n"
                    for resultado in resultados:
                        texto_resultados += f"\nFunção no intervalo {resultado['Intervalo']}:\n"
                        for chave, valor in resultado.items():
                            if chave != "Intervalo":
                                texto_resultados += f"  {chave}: {valor}\n"

                else:
                    # Função única
                    funcao = sp.sympify(entrada)
                    resultados = analisar_funcao_unica(funcao, 'x')
                    texto_resultados = "Análise da Função:\n"
                    for chave, valor in resultados.items():
                        texto_resultados += f"{chave}: {valor}\n"

                # Mostrar os resultados em uma MessageBox
                messagebox.showinfo("Resultados", texto_resultados)

            except Exception as e:
                messagebox.showerror("Erro", f"Erro ao processar a função:\n{e}")

        button_frame = Frame(frame, bg="#2e3b4e")
        button_frame.pack(side="bottom",pady=20)

        Button(
            button_frame,
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
            command=lambda: info_apoio(lenght, support_type),
            cursor="hand2",
            width=15,
            height=2,
        ).pack(side = "right", padx=20)

    start_1()