from src.all_imports import *
from src.window import create_main_screen_activity_03
from src.util import clear_frame, confirm_exit_to_main
from src.load import Load

def exercise_3_ui(frame, window):

    def start_1():
        clear_frame(frame)

        Label(
            frame,
            text="Exercício 1: Análise de Esforços em uma Viga",
            font=("Arial", 28, "bold"),
            bg="#2e3b4e",
            fg="#f0f0f0",
        ).pack(pady=20)

        explanation1 = (
            "Este exercício aborda a análise de vigas apoiadas. Existem dois tipos principais de vigas que você pode "
            "encontrar:\n\n"
            "Vigas Biapoiadas:\n"
            "- Contêm dois apoios: um apoio fixo (de primeiro gênero) e um apoio móvel (de segundo gênero).\n\n"
            "Vigas Engastadas:\n"
            "- Possuem um engaste em uma extremidade, que restringe todas as translações e rotações.\n\n"
        )

        Label(
            frame,
            text=explanation1,
            font=("Arial", 16),
            bg="#2e3b4e",
            fg="#f0f0f0",
            wraplength=800,
            justify="left",
        ).pack(pady=16)

        image_frame = Frame(frame, bg="#2e3b4e")
        image_frame.pack(pady=20)

        try:
            img1 = Image.open("activities/Activity_01/assets/exercise_2.1.png")
            img1 = img1.resize((400, 180), Image.Resampling.LANCZOS)
            img1 = ImageTk.PhotoImage(img1)

            img2 = Image.open("activities/Activity_01/assets/exercise_2.2.png")
            img2 = img2.resize((400, 180), Image.Resampling.LANCZOS)
            img2 = ImageTk.PhotoImage(img2)

            img_label1 = Label(image_frame, image=img1, bg="#2e3b4e")
            img_label1.image = img1
            img_label1.pack(side="left", padx=20)

            img_label2 = Label(image_frame, image=img2, bg="#2e3b4e")
            img_label2.image = img2
            img_label2.pack(side="left", padx=20) 

        except Exception as e:
            print(f"Erro ao carregar a imagem: {e}")
            Label(
                frame,
                text="Erro ao carregar as imagens. Verifique os arquivos!",
                font=("Arial", 16),
                bg="#2e3b4e",
                fg="red",
            ).pack(pady=20)

        button_frame = Frame(frame, bg="#2e3b4e")
        button_frame.pack(pady=20)

        Button(
            button_frame,
            text="Próximo",
            font=("Arial", 18, "bold"),
            bg="#4caf50",
            fg="white",
            command=lambda: start_2(),
            cursor="hand2",
            width=15,
            height=2,
        ).pack(side="left", padx=20)

        Button(
            button_frame,
            text="Voltar",
            font=("Arial", 18, "bold"),
            bg="#d32f2f",
            fg="white",
            command=lambda: create_main_screen_activity_03(window, frame),
            cursor="hand2",
            width=15,
            height=2,
        ).pack(side="right", padx=20)

    def reset_all():
        global forces  
        forces = []  

    def start_2():
        reset_all()
        clear_frame(frame)

        Label(
            frame,
            text="Exercício 1: Análise de Esforços em uma Viga",
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
            text="Exercício 1: Análise de Esforços em uma Viga",
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

        frame_lenght = Frame(frame, bg="#2e3b4e")
        frame_lenght.pack(pady=10)

        explanation_lenght = (
            "Preencha o tamanho da viga em metros.\n\n"
            "Largura (m): "
        )

        Label(
            frame_lenght,
            text=explanation_lenght,
            font=("Arial", 16),
            bg="#2e3b4e",
            fg="#f0f0f0",
            justify="center",
        ).pack(pady=5)

        entry_lenght = Entry(frame_lenght, font=("Arial", 16), width=15, justify="center")
        entry_lenght.pack(pady=5)

        explanation_support_type = "\n\nTipo de Apoio:"
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

        button_angle = Radiobutton(
            frame_entry_type, 
            text="engastada", 
            font=("Arial", 20), 
            cursor="hand2", 
            variable=entry_type, 
            value="engastada",
            bg="#2e3b4e", 
            fg="white", 
            selectcolor="#2e3b4e", 
            command=lambda: update_support_type("engastada")
        )
        button_angle.pack(side="left", padx=20)

        button_coord = Radiobutton(
            frame_entry_type, 
            text="biapoiada", 
            font=("Arial", 20), 
            cursor="hand2", 
            variable=entry_type, 
            value="biapoiada",
            bg="#2e3b4e", 
            fg="#f0f0f0", 
            selectcolor="#2e3b4e", 
            command=lambda: update_support_type("biapoiada")
        )
        button_coord.pack(side="left", padx=20)

        def update_support_type(support_type):
            entry_type.set(support_type)
            if support_type == "engastada":
                button_angle.config(bg="#ffa500", fg="white")
                button_coord.config(bg="#2e3b4e", fg="#f0f0f0")
            elif support_type == "biapoiada":
                button_coord.config(bg="#ffa500", fg="white")
                button_angle.config(bg="#2e3b4e", fg="#f0f0f0")
            else:
                button_angle.config(bg="#2e3b4e", fg="#f0f0f0")
                button_coord.config(bg="#2e3b4e", fg="#f0f0f0")
        
        frame_gap = Frame(frame, bg="#2e3b4e")
        frame_gap.pack(pady=20)

        button_frame = Frame(frame, bg="#2e3b4e")
        button_frame.pack(pady=20)

        Button(
            button_frame,
            text="Próximo",
            font=("Arial", 18, "bold"),
            bg="#4caf50",
            fg="white",
            command=lambda: info_apoio(entry_lenght.get(), entry_type.get()),
            cursor="hand2",
            width=15,
            height=2,
        ).pack(side="left", padx=20)

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
        ).pack(side="right", padx=20)

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
            return

        Label(
            frame,
            text="Exercício 1: Análise de Esforços em uma Viga",
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
            font=("Arial", 18),
            bg="#2e3b4e",
            fg="#f0f0f0",
            wraplength=800,
            justify="left",
        ).pack(pady=20)

        if(support_type == "engastada"):
            explanation_support = (
                "O engaste da viga deve estar em uma extremidade, então insira ou 0\n "
                "ou o valor de L para o apoio\n\n"
            )
        else:
            explanation_support = (
                "A viga é biapoiada, então insira valores entre 0 e L para os apoios\n"
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
            entry_support = Entry(frame, font=("Arial", 16), width=15, justify="center")
            entry_support.pack(pady=5)
        else:
            Label(frame, text="Posição do apoio de segundo gênero (m): ", font=("Arial", 16), bg="#2e3b4e", fg="#f0f0f0").pack(pady=20)
            entry_support1 = Entry(frame, font=("Arial", 16), width=15, justify="center")
            entry_support1.pack(pady=5)

            Label(frame, text="Posição do apoio de primeiro gênero (m): ", font=("Arial", 16), bg="#2e3b4e", fg="#f0f0f0").pack(pady=20)
            entry_support2 = Entry(frame, font=("Arial", 16), width=15, justify="center")
            entry_support2.pack(pady=5)
        

        frame_gap = Frame(frame, bg="#2e3b4e")
        frame_gap.pack(pady=25)

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
            command=lambda: start_2(),
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
            text="Exercício 1: Análise de Esforços em uma Viga",
            font=("Arial", 28, "bold"),
            bg="#2e3b4e",
            fg="#f0f0f0",
        ).pack(pady=20)

        explanation_forces = (
            "Insira as informações de carregamento na viga. O carregamento pode ser pontual (força concentrada em uma posição) ou distribuído (uma função ao longo do comprimento da viga). \n\n"
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
                button_angle.config(bg="#ffa500", fg="white")
                button_coord.config(bg="#2e3b4e", fg="#f0f0f0")
            elif(entry_type.get() == "funcao"):
                frame_forca_funcao.pack(pady=20)
                button_angle.config(bg="#2e3b4e", fg="white")
                button_coord.config(bg="#ffa500", fg="#f0f0f0")
            else:
                button_angle.config(bg="#2e3b4e", fg="#f0f0f0")
                button_coord.config(bg="#2e3b4e", fg="#f0f0f0")

        def create_func_and_pontual_frames():
            frame_forca_pontual = Frame(frame, bg="#2e3b4e")
            explanation_force = (
                    "Força Pontual (N):"
            )
            Label(
                frame_forca_pontual,
                text=explanation_force,
                font=("Arial", 16),
                bg="#2e3b4e",
                fg="#f0f0f0",
                justify="center",
            ).pack(pady=20)
            entry_force = Entry(frame_forca_pontual, font=("Arial", 16), width=15, justify="center")
            entry_force.pack(pady=20)

            explanation_position = (
                "Posição da força (m):"
            )
            Label(
                frame_forca_pontual,
                text=explanation_position,
                font=("Arial", 16),
                bg="#2e3b4e",
                fg="#f0f0f0",
                justify="center",
            ).pack(pady=20)
            entry_position = Entry(frame_forca_pontual, font=("Arial", 16), width=15, justify="center")
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
                    if position < 0 or position > lenght:
                        messagebox.showerror("Erro", "Posição da força deve estar entre 0 e L")
                        return
                    load = Load("pontual", value=intensity, position=position)
                    entry_force.delete(0, 'end')
                    entry_position.delete(0, 'end')
                    forces.append(load)
                    messagebox.showinfo("Força Adicionada", f"Força de {intensity} N na posição {position} m foi adicionada com sucesso!")
                except ValueError:
                    messagebox.showerror("Erro", "Insira valores válidos para a força e a posição")  

            frame_forca_funcao = Frame(frame, bg="#2e3b4e")
            explanation_force = (
                "Escreva a função que descreve a força em função de x: \n\n"
                "Para funções por partes, use a seguinte notação: {f(x), (a, b); g(x), (c, d); ...}\n\n"
                "Onde f(x) é a função, (a, b) é o intervalo de x onde a função é válida\n\n"
                "Exemplo: {x**2, (0, 2); 2*x, (2, 4)}"
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
            verify_button.pack(side="bottom",pady=5)
            entry_force_function = Entry(frame_forca_funcao, font=("Arial", 16), width=15, justify="center")
            entry_force_function.pack(pady=20)
            return frame_forca_pontual, frame_forca_funcao, entry_force, entry_position, entry_force_function

        frame_forca_pontual, frame_forca_funcao, entry_force, entry_position, entry_force_function = create_func_and_pontual_frames()
        frame_entry_type = Frame(frame, bg="#2e3b4e")
        frame_entry_type.pack(pady=10)

        button_angle = Radiobutton(frame_entry_type, text="Pontual", font=("Arial", 20), cursor="hand2", variable=entry_type, value="pontual",bg="#4caf50", fg="white", selectcolor="#2e3b4e",)
        button_angle.pack(side="left", padx=20)
        button_coord = Radiobutton(frame_entry_type, text="Função", font=("Arial", 20), cursor="hand2", variable=entry_type, value="funcao",bg="#2e3b4e", fg="#f0f0f0", selectcolor="#2e3b4e",)
        button_coord.pack(side="left", padx=20)

        entry_type.trace_add("write", update_input_fields)
        update_input_fields()

        def analisar_funcao_por_partes(func_por_partes):
            forces.clear()
            for funcao, intervalo in func_por_partes:
                load = Load(load_type="function", load_function=funcao, interval=intervalo)
                forces.append(load)
        
        def analisar_funcao_unica(funcao):
            load = Load(load_type="function", load_function=funcao, interval=(0, lenght))
            forces.clear()
            forces.append(load)

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
                    messagebox.showinfo("Verificada", f"Função foi verificada com sucesso!")
                    analisar_funcao_por_partes(func_por_partes)
                    
                else:
                    # Função única
                    funcao = sp.sympify(entrada)
                    analisar_funcao_unica(funcao)
            except Exception as e:
                messagebox.showerror("Erro", f"Erro ao processar a função:\n{e}")

        button_frame = Frame(frame, bg="#2e3b4e")
        button_frame.pack(side="bottom",pady=20)

        Button(
            button_frame,
            text=("Calcular Resultado"),
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
            command=lambda: start_2(),
            cursor="hand2",
            width=15,
            height=2,
        ).pack(side = "right", padx=20)

    def calculate_efforts(length, support_type, supports, forces, results):
        x = sp.Symbol('x')
        # {100, (0, 1.5); 200, (1.5, 3)}
        V = results["F1_y"]
        if forces[0].load_type == "pontual":
            for force in forces:
                V -= sp.Piecewise((force.value, x >= force.position), (0, True))
        elif forces[0].load_type == "function":
            for force in forces:
                V -= sp.Piecewise((sp.integrate(force.load_function, x), (x >= force.interval[0]) & (x <= force.interval[1])), (0, True))
        
        V = sp.sympify(V)

        M = results["M_A"] - sp.integrate(V, x)
        M = sp.sympify(M)

        V_func = sp.lambdify(x, sp.simplify(V), "numpy")
        M_func = sp.lambdify(x, sp.simplify(M), "numpy")

        results = {
            'V': V_func,
            'M': M_func,
        }

        display_results(results, length)
                

    def calculate_resultant(length, support_type, supports, forces):

        if support_type == "engastada":
            sum_forces_x = 0  
            sum_forces_y = 0
            sum_moments = 0

            for force in forces:
                moment = force.value * (supports[0] - force.position) 
                sum_moments += moment
                sum_forces_y += force.value

            results = {
                'F1_x': 0.0, 
                'F1_y': sum_forces_y, 
                'M_A': sum_moments,  
                "F2": 0.0,
            }

        else:
            sum_forces_y = 0
            sum_moments = 0

            for force in forces:
                moment = force.value * (force.position - supports[0])  
                sum_moments += moment
                sum_forces_y += force.value

            F1_x = sp.Symbol('F1_x')
            F1_y = sp.Symbol('F1_y')
            F2 = sp.Symbol('F2')

            system = [
                F2 * (supports[1] - supports[0]) - sum_moments,  
                F1_y + F2 - sum_forces_y,  
                F1_x,  
            ]

            try:
                solution = sp.solve(system, (F1_x, F1_y, F2))
            except Exception as e:
                print(f"Erro ao resolver o sistema: {e}")
                raise e

            results = {
                'F1_x': float(solution.get(F1_x, 0)),
                'F1_y': float(solution.get(F1_y, 0)),
                'F2': float(solution.get(F2, 0)),
                "M_A": 0.0,
            }
        calculate_efforts(length, support_type, supports, forces, results)


    def display_results(solution, lenght):
        clear_frame(frame)

        Label(
            frame,
            text="Resultados do Cálculo",
            font=("Arial", 26, "bold"),
            bg="#2e3b4e",
            fg="#f0f0f0",
        ).pack(pady=20, side="top")
        try:
            solution = {str(key): value for key, value in solution.items()}

            fig, (ax1, ax2) = plt.subplots(1, 2)

            canvas = FigureCanvasTkAgg(fig, master=frame)
            canvas_widget = canvas.get_tk_widget()
            canvas_widget.pack(fill=tk.BOTH, expand=True)

            x_vals = np.linspace(0, lenght, 400)
            V_vals = solution["V"](x_vals)
            M_vals = solution["M"](x_vals)

            ax1.plot(x_vals, V_vals, label="Esforço Cortante (V)", color='b')
            ax1.set_title("Diagrama de Esforço Cortante")
            ax1.set_xlabel("Posição (m)")
            ax1.set_ylabel("Cortante (kN)")
            ax1.grid(True)
            ax1.legend()
            
            # Segundo gráfico: Momento Fletor
            ax2.plot(x_vals, M_vals, label="Momento Fletor (M)", color='r')
            ax2.set_title("Diagrama de Momento Fletor")
            ax2.set_xlabel("Posição (m)")
            ax2.set_ylabel("Momento (kNm)")
            ax2.grid(True)
            ax2.legend()

            canvas.draw()
        except Exception as e:
            print(f"Erro em display_results: {e}")
            messagebox.showerror("Erro", f"Erro ao exibir os resultados: {e}")
        

        button_frame = Frame(frame, bg="#2e3b4e")
        button_frame.pack(pady=20)

        Button(
            button_frame,
            text="Menu Principal",
            font=("Arial", 20, "bold"),
            bg="#d32f2f",
            fg="white",
            command=lambda: confirm_exit_to_main(window, frame, 2),
            cursor="hand2",
            width=20,
            height=2,
        ).pack(side="bottom", padx=20)


    def calculate_support_relations(lenght, support_type, supports, forces):
        try:
            calculate_resultant(lenght, support_type, supports, forces)
        except Exception as e:
            print(f"Erro em calculate_support_relations: {e}")
            messagebox.showerror("Erro", f"Erro ao calcular os apoios: {e}")

    start_1()