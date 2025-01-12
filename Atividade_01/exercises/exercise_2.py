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

        if support_type != "engastada" and support_type != "biapoiada":
            start_3()
            messagebox.showerror("Erro", "Selecione um tipo de apoio válido")
            return

        try:
            length = float(length)
        except ValueError:
            start_3()
            messagebox.showerror("Erro", "Insira um valor válido para o comprimento da viga")

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
            Label(frame, text="Posição do apoio de segundo gênero (m): ", font=("Arial", 16), bg="#2e3b4e", fg="#f0f0f0").pack(pady=20)
            entry_support1 = Entry(frame, font=("Arial", 16), width=15)
            entry_support1.pack(pady=20)

            Label(frame, text="Posição do apoio de primeiro gênero (m): ", font=("Arial", 16), bg="#2e3b4e", fg="#f0f0f0").pack(pady=20)
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
            command=lambda: info_forcas(length, support_type, [entry_support.get()] if support_type == "engastada" else [entry_support1.get(), entry_support2.get()]),
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

        try:
            if(support_type == "engastada"):
                supports[0] = float(supports[0])
                if (supports[0] == 0 or supports[0] == lenght):
                    pass
                else:
                    info_apoio(lenght, support_type)
                    messagebox.showerror("Erro", "Apoio engastado deve estar em uma extremidade da viga")
                    return
            else:
                supports[0] = float(supports[0])
                supports[1] = float(supports[1])
                if(supports[0] == supports[1] or supports[0] < 0 or supports[1] > lenght or supports[0] > lenght or supports[1] < 0):
                    info_apoio(lenght, support_type)
                    messagebox.showerror("Erro", "Apoios biapoiados devem estar em pontos diferentes e entre 0 e L")
                    return
        except ValueError:
            info_apoio(lenght, support_type)
            messagebox.showerror("Erro", "Insira valores válidos para os apoios")

        forces = []

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
            add_button = Button(
                frame_forca_pontual,
                text="Adicionar Força",
                font=("Arial", 18, "bold"),
                bg="#4caf50",
                fg="white",
                command = lambda: clean_entrys_and_add_force(),
                cursor="hand2",
                width=15,
                height=2,
            )
            add_button.pack(pady=20)

            def clean_entrys_and_add_force(*args):
                try:
                    intensity = float(entry_force.get())
                    position = float(entry_position.get())
                    entry_force.delete(0, 'end')
                    entry_position.delete(0, 'end')
                    forces.append((intensity, position))
                except ValueError:
                    messagebox.showerror("Erro", "Insira valores válidos para a força e a posição")  

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
            verify_button = Button(
                frame_forca_funcao,
                text="Analisar Função",
                font=("Arial", 18, "bold"),
                bg="#4caf50",
                fg="white",
                command = lambda: analisar_funcao(),
                cursor="hand2",
                width=15,
                height=2,
            )
            verify_button.pack(side="bottom",pady=20)
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
            calcular_x_barra = 0
            for funcao, intervalo in func_por_partes:
                forca = sp.integrate(funcao, (x, intervalo[0], intervalo[1]))
                informacao = sp.integrate(funcao * x, (x, intervalo[0], intervalo[1]))
                soma_forcas += forca
                calcular_x_barra += informacao
            x_barra = calcular_x_barra / soma_forcas
            forces.append((soma_forcas, x_barra))
        
        def analisar_funcao_unica(funcao, var):
            x = sp.Symbol(var)
            forca = sp.integrate(funcao, x)
            informacao = sp.integrate(funcao * x, x)
            x_barra = informacao / forca
            forces.append((forca, x_barra))

        def analisar_funcao(event=None):
            entrada = entry_force_function.get().strip()  # Obter texto do Entry
            try:
                # Processar a entrada com sympy
                #{100*x, (0,3); 300, (3,5); 400, (5,10)}
                #{x**2, (-oo, 0; x, (0, oo)}
                if "{" in entrada and "}" in entrada:
                    # Função por partes (usando uma notação específica)
                    partes = entrada[1:-1].split(";")
                    func_por_partes = []
                    for parte in partes:
                        funcao, intervalo = parte.split(",", 1)
                        funcao = sp.sympify(funcao.strip())
                        intervalo = intervalo.strip()
                        intervalo = eval(intervalo)  # Convertendo para tuple
                        func_por_partes.append((funcao, intervalo))
                    analisar_funcao_por_partes(func_por_partes, 'x')
                else:
                    # Função única
                    funcao = sp.sympify(entrada)
                    analisar_funcao_unica(funcao, 'x')
            except Exception as e:
                messagebox.showerror("Erro", f"Erro ao processar a função:\n{e}")

        button_frame = Frame(frame, bg="#2e3b4e")
        button_frame.pack(side="bottom",pady=20)

        Button(
            button_frame,
            text=("Calculos de apoio"),
            font=("Arial", 18, "bold"),
            bg="#4caf50",
            fg="white",
            command=lambda: calculate_support_relations(lenght, support_type, supports, forces),
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

    def calculate_resultant(lenght, support_type, supports, forces):
        if(support_type == "engastada"):
            sum_forces_x = 0
            sum_forces_y = 0
            sum_moments = 0
            for force in forces:
                # Calculo do momento
                moment = force[0] * (supports[0] - force[1]) #Positivo se antihorário
                sum_moments += moment
                sum_forces_y += force[0]
            messagebox.showinfo("Resultados", f"Reações de apoio: F1_x = 0, F1_y = {sum_forces_y}, momento = {sum_moments}")
        else:
            sum_forces_y = 0
            sum_moments = 0
            for force in forces:
                # Calculo do momento
                moment = force[0] * (supports[0] - force[1]) #Positivo se antihorário
                sum_moments += moment
                sum_forces_y += force[0]
            F1_x = sp.Symbol('F1_x')
            F1_y = sp.Symbol('F1_y')
            F2 = sp.Symbol('F2')
            system = [F2 * (supports[1] - supports[0]) + sum_moments, F1_y + F2 - sum_forces_y, F1_x]
            solution = sp.solve(system, (F1_x, F1_y, F2))
            print(solution)
            messagebox.showinfo("Resultados", f"Reações de apoio: \nF1_x = {solution.get(F1_x)}, \nF1_y = {solution.get(F1_y)}, \nF2 = {solution.get(F2)}")                 
    
    def calculate_support_relations(lenght, support_type, supports, forces):
                calculate_resultant(lenght, support_type, supports, forces)            

    start_1()