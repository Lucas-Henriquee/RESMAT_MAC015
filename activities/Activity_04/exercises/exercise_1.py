from src.load import Load
from src.all_imports import *
from src.util import clear_frame, confirm_exit_to_main, get_absolute_path
from src.window import create_main_screen_activity_04
from src.section import Section
from src.moment import calculate_moments

def exercise_1_ui(frame, window):

    section = Section()

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

        img_path_1 = get_absolute_path("activities/Activity_01/assets/exercise_2.1.png")
        img_path_2 = get_absolute_path("activities/Activity_01/assets/exercise_2.2.png")
        
        try:
            img1 = Image.open(img_path_1)
            img1 = img1.resize((400, 180), Image.Resampling.LANCZOS)
            img1 = ImageTk.PhotoImage(img1)

            img2 = Image.open(img_path_2)
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
            command=lambda: create_main_screen_activity_04(window, frame),
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
            "3. Definir a função de carregamento, o carregamento pontual ou as cargas momento\n\n"
            "4. Desenhar a area transversal da viga\n\n"
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

        frame_elastic = Frame(frame, bg="#2e3b4e")
        frame_elastic.pack(pady=10)

        explanation_elastic = (
            "Preencha o módulo de elasticidade do material\n\n"
            "Módulo de elasticidade (Pa): "
        )

        Label(
            frame_elastic,
            text=explanation_elastic,
            font=("Arial", 16),
            bg="#2e3b4e",
            fg="#f0f0f0",
            justify="center",
        ).pack(pady=5)

        entry_elastic = Entry(frame_elastic, font=("Arial", 16), width=15, justify="center")
        entry_elastic.pack(pady=5)

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
            command=lambda: info_apoio(entry_lenght.get(), entry_elastic.get(), entry_type.get()),
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

    def info_apoio(length, elastic_module, support_type):
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
        
        try:
            elastic_module = float(elastic_module)
            if elastic_module <= 0:
                start_3()
                messagebox.showerror("Erro", "Insira um valor válido para o módulo de elasticidade")
                return
        except ValueError:
            start_3()
            messagebox.showerror("Erro", "Insira um valor válido para o módulo de elasticidade")
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
            command=lambda: info_forcas(length, support_type, [entry_support.get()] if support_type == "engastada" else [entry_support1.get(), entry_support2.get()], elastic_module),
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

    def info_forcas(length, support_type, supports, elastic_module):
        clear_frame(frame)

        try:
            if(support_type == "engastada"):
                supports[0] = float(supports[0])
                if (supports[0] == 0 or supports[0] == length):
                    pass
                else:
                    info_apoio(length, support_type)
                    messagebox.showerror("Erro", "Apoio engastado deve estar em uma extremidade da viga")
                    return
            else:
                supports[0] = float(supports[0])
                supports[1] = float(supports[1])
                if(supports[0] == supports[1] or supports[0] < 0 or supports[1] > length or supports[0] > length or supports[1] < 0):
                    info_apoio(length, support_type)
                    messagebox.showerror("Erro", "Apoios biapoiados devem estar em pontos diferentes e entre 0 e L")
                    return
        except ValueError:
            info_apoio(length, support_type)
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
            "Insira as informações de carregamento na viga. O carregamento pode ser pontual (força concentrada em uma posição), distribuído (uma função ao longo do comprimento da viga) ou carga momento. \n\n"
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

        pontual_frame = Frame(frame, bg="#2e3b4e")
        pontual_frame.pack(pady=10)

        Label(
            pontual_frame,
            text="Carregamento Pontual (kN): ",
            font=("Arial", 16),
            bg="#2e3b4e",
            fg="#f0f0f0",
            justify="center",
        ).pack(pady=5)

        entry_force_pontual = Entry(pontual_frame, font=("Arial", 16), width=15, justify="center")
        entry_force_pontual.pack(pady=5)

        Label(
            pontual_frame,
            text="Posição do carregamento (m): ",
            font=("Arial", 16),
            bg="#2e3b4e",
            fg="#f0f0f0",
            justify="center",
        ).pack(pady=5)

        entry_position_pontual = Entry(pontual_frame, font=("Arial", 16), width=15, justify="center")
        entry_position_pontual.pack(pady=5)

        def add_force_pontual():
            try:
                force = float(entry_force_pontual.get())
                position = float(entry_position_pontual.get())
                if position < 0 or position > length:
                    messagebox.showerror("Erro", "Posição do carregamento inválida")
                    return
                forces.append(Load(load_type="pontual", value=force, position=position))
                entry_force_pontual.delete(0, "end")
                entry_position_pontual.delete(0, "end")
                messagebox.showinfo("Adicionado", "Carregamento pontual adicionado com sucesso!")
            except ValueError:
                messagebox.showerror("Erro", "Insira valores válidos para o carregamento")
        
        Button(
            pontual_frame,
            text="Adicionar",
            font=("Arial", 16),
            bg="#4caf50",
            fg="white",
            command=lambda: add_force_pontual(),
            cursor="hand2",
        ).pack(pady=10)

        Button(
            pontual_frame,
            text="Proxima etapa",
            font=("Arial", 16),
            bg="#4caf50",
            fg="white",
            command=lambda: info_forca_distribuida(),
        ).pack(pady=10)



        def info_forca_distribuida():
            pontual_frame.pack_forget()
            frame_momento.pack_forget()
            frame_distribuida.pack(pady=10)

        frame_distribuida = Frame(frame, bg="#2e3b4e")

        explanation_forces_distribuida = (
            "Escreva a função que descreve a força em função de x: \n\n"
                "Para funções por partes, use a seguinte notação: {f(x), (a, b); g(x), (c, d); ...}\n\n"
                "Onde f(x) é a função, (a, b) é o intervalo de x onde a função é válida\n\n"
                "Exemplo: {x**2, (0, 2); 2*x, (2, 4)}"
        )

        Label(
            frame_distribuida,
            text=explanation_forces_distribuida,
            font=("Arial", 16),
            bg="#2e3b4e",
            fg="#f0f0f0",
            wraplength=800,
            justify="left",
        ).pack(pady=20)

        Label(
            frame_distribuida,
            text="Carregamento Distribuído (kN/m): ",
            font=("Arial", 16),
            bg="#2e3b4e",
            fg="#f0f0f0",
            justify="center",
        ).pack(pady=5)

        entry_force_function = Entry(frame_distribuida, font=("Arial", 16), width=15, justify="center")
        entry_force_function.pack(pady=5)

        Button(
            frame_distribuida,
            text="Verificar e Adicionar",
            font=("Arial", 16),
            bg="#4caf50",
            fg="white",
            command=lambda: analisar_funcao(),
            cursor="hand2",
        ).pack(pady=10)

        Button(
            frame_distribuida,
            text="Proxima etapa",
            font=("Arial", 16),
            bg="#4caf50",
            fg="white",
            command=lambda: info_momento(),
        ).pack(pady=10)

        Button(
            frame_distribuida,
            text="Voltar",
            font=("Arial", 16),
            bg="#d32f2f",
            fg="white",
            command=lambda: info_pontual(),
        ).pack(pady=10)

        def info_pontual():
            frame_distribuida.pack_forget()
            pontual_frame.pack(pady=10)

        def info_momento():
            frame_distribuida.pack_forget()
            frame_momento.pack(pady=10)

        frame_momento = Frame(frame, bg="#2e3b4e")

        Label(
            frame_momento,
            text="Momento (kNm): ",
            font=("Arial", 16),
            bg="#2e3b4e",
            fg="#f0f0f0",
            justify="center",
        ).pack(pady=5)

        entry_momento = Entry(frame_momento, font=("Arial", 16), width=15, justify="center")
        entry_momento.pack(pady=5)

        Label(
            frame_momento,
            text="Posição do momento (m): ",
            font=("Arial", 16),
            bg="#2e3b4e",
            fg="#f0f0f0",
            justify="center",
        ).pack(pady=5)

        entry_position_momento = Entry(frame_momento, font=("Arial", 16), width=15, justify="center")
        entry_position_momento.pack(pady=5)

        def add_momento():
            try:
                force = float(entry_momento.get())
                position = float(entry_position_momento.get())
                if position < 0 or position > length:
                    messagebox.showerror("Erro", "Posição do momento inválida")
                    return
                forces.append(Load(load_type="momento", value=force, position=position))
                entry_momento.delete(0, "end")
                entry_position_momento.delete(0, "end")
                messagebox.showinfo("Adicionado", "Momento adicionado com sucesso!")
            except ValueError:
                messagebox.showerror("Erro", "Insira valores válidos para o momento")

        Button(
            frame_momento,
            text="Adicionar",
            font=("Arial", 16),
            bg="#4caf50",
            fg="white",
            command=lambda: add_momento(),
            cursor="hand2",
        ).pack(pady=10)

        Button(
            frame_momento,
            text="Voltar",
            font=("Arial", 16),
            bg="#d32f2f",
            fg="white",
            command=lambda: info_forca_distribuida(),
        ).pack(pady=10)
        

        def analisar_funcao_por_partes(func_por_partes):
            forces.clear()
            for funcao, intervalo in func_por_partes:
                load = Load(load_type="function", load_function=funcao, interval=intervalo)
                forces.append(load)
        
        def analisar_funcao_unica(funcao):
            load = Load(load_type="function", load_function=funcao, interval=(0, length))
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
                        if(intervalo[0] < 0 or intervalo[1] > length):
                            messagebox.showerror("Erro", "Intervalo de carregamento inválido")
                            func_por_partes.clear()
                            return
                        func_por_partes.append((funcao, intervalo))
                    entry_force_function.delete(0, "end")
                    messagebox.showinfo("Verificada", f"Função foi verificada e adicionada com sucesso!")
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
            text=("Desenhar seção transversal"),
            font=("Arial", 18, "bold"),
            bg="#4caf50",
            fg="white",
            command=lambda: calculate_results(length, support_type, supports, forces, elastic_module, section), #start_1_second_part(length, support_type, supports, forces, elastic_module, section),
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

    def calculate_efforts(length, support_type, supports, forces, elastic_module, section, results):

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

        results = {
            'V': V,
            'M': M,
        }

        calculate_deflection(length, support_type, supports, forces, elastic_module, section, results)
                
    def calculate_resultant(length, support_type, supports, forces, elastic_module, section):

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

        elif support_type == "biapoiada":
            sum_forces_y = 0
            sum_moments = 0

            for force in forces:
                if(force.load_type == "momento"):
                    moment = force.value
                else:
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
        calculate_efforts(length, support_type, supports, forces, elastic_module, section, results)

    def calculate_deflection(length, support_type, supports, forces, elastic_module, section, results):
        # try:
            # results_inertia = calculate_moments(section)
            results_inertia = {
                "I_x": 0.000005
            }
            x = sp.Symbol('x')
            E = elastic_module
            I = results_inertia["I_x"]
            L = length

            V = results["V"]
            M = results["M"]

            C1 = sp.Symbol('C1')
            C2 = sp.Symbol('C2')

            theta = sp.integrate((M / (E * I)), x) + C1
            print(theta)
            deflection = sp.integrate(theta, x) + C2
            print(deflection)

            if(support_type == "engastada"):
                eq1 = sp.Eq(deflection.subs(x, supports[0]), 0)
                eq2 = sp.Eq(theta.subs(x, supports[0]), 0)
                eq3 = sp.Eq(V.subs(x, abs(supports[0]-L)), 0)
                eq4 = sp.Eq(M.subs(x, abs(supports[0]-L)), 0)
                sol = sp.solve([eq1, eq2, eq3, eq4], (C1, C2))
            elif(support_type == "biapoiada"):
                if supports[0] == 0 or supports[0] == length:
                    eq1 = sp.Eq(M.subs(x, supports[0]), 0)
                    eq2 = sp.Eq(deflection.subs(x, supports[0]), 0)
                else:
                    eq1 = sp.Eq(deflection.subs(x, supports[0]-0.00001), deflection.subs(x, supports[1]+0.00001))
                    eq2 = sp.Eq(theta.subs(x, supports[0]-0.00001), theta.subs(x, supports[1]+0.00001))
                if supports[1] == 0 or supports[1] == length:
                    eq3 = sp.Eq(M.subs(x, supports[1]), 0)
                    eq4 = sp.Eq(deflection.subs(x, supports[1]), 0)
                else:
                    eq3 = sp.Eq(deflection.subs(x, supports[1]-0.00001), deflection.subs(x, supports[1]+0.00001))
                    eq3 = sp.Eq(theta.subs(x, supports[1]-0.00001), theta.subs(x, supports[1]+0.00001))
                sol = sp.solve([eq1, eq2, eq3, eq4], (C1, C2))
            print(sol)
            theta = theta.subs(sol)
            deflection = deflection.subs(sol)

            deflection_func = sp.lambdify(x, deflection, "numpy")
            theta_func = sp.lambdify(x, theta, "numpy")

            results = {
                "deflection": deflection_func,
                "theta": theta_func,
            }

            display_results(results, length)
        # except Exception as e:
        #     print(f"Erro ao calcular a deflexão: {e}")
        #     messagebox.showerror("Erro", f"Erro ao calcular a deflexão: {e}")


    def display_results(solution, length):
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

            x_vals = np.linspace(0, length, 400)
            theta_vals = solution["theta"](x_vals)
            deflection_vals = solution["deflection"](x_vals)

            ax1.plot(x_vals, theta_vals, label="Inclinação (Theta)", color='b')
            ax1.set_title("Diagrama de Inclinação da viga")
            ax1.set_xlabel("Posição (m)")
            ax1.set_ylabel("Inclinação (rad)")
            ax1.grid(True)
            ax1.legend()
            
            ax2.plot(x_vals, deflection_vals, label="Deflexão (v)", color='r')
            ax2.set_title("Diagrama de Deflexão da viga")
            ax2.set_xlabel("Posição (m)")
            ax2.set_ylabel("Y (m)")
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
            command=lambda: confirm_exit_to_main(window, frame, 4),
            cursor="hand2",
            width=20,
            height=2,
        ).pack(side="bottom", padx=20)

    def calculate_support_relations(length, support_type, supports, forces, elastic_module, section):
        # try:
            calculate_resultant(length, support_type, supports, forces, elastic_module, section)
        # except Exception as e:
        #     print(f"Erro em calculate_support_relations: {e}")
        #     messagebox.showerror("Erro", f"Erro ao calcular os apoios: {e}")

    def start_1_second_part(length, support_type, supports, forces, elastic_module, section):
        clear_frame(frame)

        if not forces:
            messagebox.showerror("Erro", "Adicione pelo menos uma força para prosseguir")
            info_forcas(length, support_type, supports, elastic_module)
            return

        Label(
            frame,
            text="Adicionando a seção transversal",
            font=("Arial", 28, "bold"),
            bg="#2e3b4e",
            fg="#f0f0f0"
        ).pack(pady=20)

        explanation1 = (
            "Etapas da inserção:\n"
            "- Definir a forma inicial: retângulo, círculo ou triângulo.\n"
            "- Realizar recortes sucessivos, utilizando as mesmas formas.\n"
            "- Calcular o momento de inércia em relação aos eixos centroidais.\n\n"
            "O cálculo é feito considerando o Teorema dos Eixos Paralelos (Teorema de Steiner) e a distribuição "
            "geométrica das áreas remanescentes após os recortes."
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

        img_path = get_absolute_path("activities/Activity_03/assets/exercise_1.png")
        image_frame = Frame(frame, bg="#2e3b4e")
        image_frame.pack(pady=20)

        try:
            img1 = Image.open(img_path)
            img1 = img1.resize((700, 310), Image.Resampling.LANCZOS)
            img1 = ImageTk.PhotoImage(img1)

            img_label1 = Label(image_frame, image=img1, bg="#2e3b4e")
            img_label1.image = img1
            img_label1.pack(side="left", padx=20)

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
            command=lambda: start_2_second_part(length, support_type, supports, forces, elastic_module, section),
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
            command=lambda: info_forcas(length, support_type, supports, elastic_module),
            cursor="hand2",
            width=15,
            height=2,
        ).pack(side="right", padx=20)

    def start_2_second_part(length, support_type, supports, forces, elastic_module, section):
        clear_frame(frame)

        Label(
            frame,
            text="Criando a Figura Principal",
            font=("Arial", 28, "bold"),
            bg="#2e3b4e",
            fg="#f0f0f0",
        ).pack(pady=20)

        explanation2 = (
        "Atenção! Antes de iniciar, verifique os seguintes pontos:\n\n"
        "Formato das Medidas:\n"
        " - Insira sempre as medidas em metros (m).\n\n"
        "Escolha da Figura Inicial:\n"
        " - Retângulo, Círculo ou Triângulo.\n\n"
        "Orientação dos Eixos:\n"
        " - O ponto de origem (0,0) será considerado no canto inferior esquerdo da figura principal.\n"
        "   - Para retângulos e triângulos, utilize o vértice inferior esquerdo como referência.\n"
        "   - Para círculos, utilize o centro da circunferência como referência.\n\n"
        "Validação das Medidas:\n"
        " - Certifique-se de que as medidas inseridas são válidas e positivas.\n\n"
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
            command=lambda: insert_figure(length, support_type, supports, forces, elastic_module, section),
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
            command=lambda: info_forcas(length, support_type, supports, elastic_module),
            cursor="hand2",
            width=15,
            height=2,
        ).pack(side = "right", padx=20)

    def insert_figure(length, support_type, supports, forces, elastic_module, section):
        clear_frame(frame)

        Label(
            frame,
            text="Criando a Figura Principal",
            font=("Arial", 28, "bold"),
            bg="#2e3b4e",
            fg="#f0f0f0",
        ).pack(pady=20)

        Label(
            frame,
            text="Escolha qual será a figura principal e insira as suas medidas:",
            font=("Arial", 24, "bold"),
            bg="#2e3b4e",
            fg="#f0f0f0",
        ).pack(pady=20)

        frame_figure_type = Frame(frame, bg="#2e3b4e")
        frame_figure_type.pack(pady=10)

        figure_type = StringVar()

        button_rectangle = Radiobutton(frame_figure_type, text="Retângulo", font=("Arial", 20), cursor="hand2", variable=figure_type, value="retangulo",bg="#4caf50", fg="white", selectcolor="#2e3b4e",)
        button_rectangle.pack(side="left", padx=20)
        
        button_triangle = Radiobutton(frame_figure_type, text="Triângulo", font=("Arial", 20), cursor="hand2", variable=figure_type, value="triangulo",bg="#2e3b4e", fg="#f0f0f0", selectcolor="#2e3b4e",)
        button_triangle.pack(side="left", padx=20)

        button_circle = Radiobutton(frame_figure_type, text="Círculo", font=("Arial", 20), cursor="hand2", variable=figure_type, value="circulo",bg="#2e3b4e", fg="#f0f0f0", selectcolor="#2e3b4e",)
        button_circle.pack(side="left", padx=20)

        rectangle_frame = Frame(frame, bg="#2e3b4e")

        Label(rectangle_frame, text="Largura (m):", font=("Arial", 20), bg="#2e3b4e", fg="#f0f0f0").grid(row=0, column=0, padx=10, pady=5, columnspan=2)
        entry_width = Entry(rectangle_frame, font=("Arial", 22), width=10, justify="center")
        entry_width.grid(row=1, column=0, padx=10, pady=5, columnspan=2)

        Label(rectangle_frame, text="Altura (m):", font=("Arial", 20), bg="#2e3b4e", fg="#f0f0f0").grid(row=2, column=0, padx=10, pady=5, columnspan=2)
        entry_height = Entry(rectangle_frame, font=("Arial", 22), width=10, justify="center")
        entry_height.grid(row=3, column=0, padx=10, pady=5, columnspan=2)

        triangle_frame = Frame(frame, bg="#2e3b4e")

        Label(triangle_frame, text="Base (m):", font=("Arial", 20), bg="#2e3b4e", fg="#f0f0f0").grid(row=0, column=0, padx=10, pady=5, columnspan=2)
        entry_base = Entry(triangle_frame, font=("Arial", 22), width=12, justify="center")
        entry_base.grid(row=1, column=0, padx=10, pady=5, columnspan=2)

        Label(triangle_frame, text="Altura (m):", font=("Arial", 20), bg="#2e3b4e", fg="#f0f0f0").grid(row=2, column=0, padx=10, pady=5, columnspan=2)
        entry_height_2 = Entry(triangle_frame, font=("Arial", 22), width=12, justify="center")
        entry_height_2.grid(row=3, column=0, padx=10, pady=5, columnspan=2)

        circle_frame = Frame(frame, bg="#2e3b4e")

        Label(circle_frame, text="Raio (m)", font=("Arial", 20), bg="#2e3b4e", fg="#f0f0f0").grid(row=0, column=0, padx=10, pady=5)
        entry_radius = Entry(circle_frame, font=("Arial", 22), width=15, justify="center")
        entry_radius.grid(row=1, column=0, padx=10, pady=5)

        def update_input_fields(*args):
            rectangle_frame.pack_forget()
            triangle_frame.pack_forget()
            circle_frame.pack_forget()
            if figure_type.get() == "retangulo":
                rectangle_frame.pack(pady=10)
                button_rectangle.config(bg="#ffa500", fg="white")
                button_triangle.config(bg="#2e3b4e", fg="#f0f0f0")
                button_circle.config(bg="#2e3b4e", fg="#f0f0f0")
            elif figure_type.get() == "triangulo":
                triangle_frame.pack(pady=10)
                button_rectangle.config(bg="#2e3b4e", fg="#f0f0f0")
                button_triangle.config(bg="#ffa500", fg="white")
                button_circle.config(bg="#2e3b4e", fg="#f0f0f0")
            elif figure_type.get() == "circulo":
                circle_frame.pack(pady=10)
                button_rectangle.config(bg="#2e3b4e", fg="#f0f0f0")
                button_triangle.config(bg="#2e3b4e", fg="#f0f0f0")
                button_circle.config(bg="#ffa500", fg="white")
            else:  
                button_rectangle.config(bg="#2e3b4e", fg="#f0f0f0")
                button_triangle.config(bg="#2e3b4e", fg="#f0f0f0")
                button_circle.config(bg="#2e3b4e", fg="#f0f0f0")

        figure_type.trace_add("write", update_input_fields)
        update_input_fields()

        button_frame = Frame(frame, bg="#2e3b4e")
        button_frame.pack(side="bottom", pady=20)

        Button(button_frame, text="Avancar",font=("Arial", 20, "bold"), cursor="hand2", bg="#4caf50", fg="white", command=lambda: check_figure(length, support_type, supports, forces, elastic_module, section), width=20, height=2).pack(side="left", padx=10)
        Button(button_frame, text="Voltar", font=("Arial", 20, "bold"), bg="#d32f2f", fg="white", cursor="hand2", command=start_2, width=20, height=2).pack(side="left", padx=10)

        def check_figure(length, support_type, supports, forces, elastic_module, section):
            figure = figure_type.get()

            if figure == "retangulo":
                try:
                    width = float(entry_width.get())
                    height = float(entry_height.get())

                    if width <= 0 or height <= 0:
                        messagebox.showerror("Erro", "As dimensões devem ser maiores que zero.")
                        return

                    messagebox.showinfo("Verificação", "Foi inserido um Retângulo como Figura Principal.")
                    
                    section.create_main_figure("retangulo", (width, height))
                    insert_cut_figure(length, support_type, supports, forces, elastic_module, section)

                except ValueError:
                    messagebox.showerror("Erro", "Por favor, insira valores numéricos válidos.")

            elif figure == "triangulo":
                try:
                    base = float(entry_base.get())
                    height = float(entry_height_2.get())
                    section.create_main_figure("triangulo", (base, height))
                    messagebox.showinfo("Verificação", "Foi inserido um Triângulo como Figura Principal.")
                    insert_cut_figure(length, support_type, supports, forces, elastic_module, section)

                except ValueError:
                    messagebox.showerror("Erro", "Por favor, insira valores numéricos válidos.")

            elif figure == "circulo":
                try:
                    radius = float(entry_radius.get())

                    if radius <= 0:
                        messagebox.showerror("Erro", "O raio deve ser um valor maior que zero.")
                        return

                    messagebox.showinfo("Verificação", "Foi inserido um Círculo como Figura Principal.")
                    
                    section.create_main_figure("circulo", radius)
                    insert_cut_figure(length, support_type, supports, forces, elastic_module, section)

                except ValueError:
                    messagebox.showerror("Erro", "Por favor, insira um valor numérico válido para o raio.")

            else:
                messagebox.showerror("Erro", "Selecione uma figura válida antes de prosseguir.")

    def insert_cut_figure(length, support_type, supports, forces, elastic_module, section):
        clear_frame(frame)

        Label(frame, text="Agora vc vai pode escolher as figuras de corte", font=("Arial", 28), bg="#2e3b4e", fg="#f0f0f0").pack(pady=20)

        frame_visualizar = Frame(frame, bg="#2e3b4e")
        frame_visualizar.pack(padx=20, pady=20)

        Label(
            frame_visualizar,
            text="Caso queira visualizar a estrutura até o momento.",
            font=("Arial", 14),
            bg="#2e3b4e",
            fg="#f0f0f0",
            wraplength=750,
            justify="left"
        ).pack(side="left", padx=(0, 20))

        Button(
            frame_visualizar,
            text="Visualizar Estrutura",
            font=("Arial", 16),
            bg="#4caf50",
            fg="white",
            cursor="hand2",
            command=lambda: render_drawing()
        ).pack(side="left")

        Label(frame, text="Escolha a figura de corte que deseja adicionar e insira os dados corretamente:", font=("Arial", 24), bg="#2e3b4e", fg="#f0f0f0").pack(pady=20)

        frame_figure_type = Frame(frame, bg="#2e3b4e")
        frame_figure_type.pack(pady=10)
        figure_type = StringVar()

        button_rectangle = Radiobutton(frame_figure_type, text="Retângulo", font=("Arial", 20), cursor="hand2", variable=figure_type, value="retangulo",bg="#4caf50", fg="white", selectcolor="#2e3b4e",)
        button_rectangle.pack(side="left", padx=20)
        
        button_triangle = Radiobutton(frame_figure_type, text="Triângulo", font=("Arial", 20), cursor="hand2", variable=figure_type, value="triangulo",bg="#2e3b4e", fg="#f0f0f0", selectcolor="#2e3b4e",)
        button_triangle.pack(side="left", padx=20)

        button_circle = Radiobutton(frame_figure_type, text="Círculo", font=("Arial", 20), cursor="hand2", variable=figure_type, value="circulo",bg="#2e3b4e", fg="#f0f0f0", selectcolor="#2e3b4e",)
        button_circle.pack(side="left", padx=20)

        rectangle_frame = Frame(frame, bg="#2e3b4e")

        Label(rectangle_frame, text="Coordenadas do Retângulo:", font=("Arial", 20, "bold"), bg="#2e3b4e", fg="#f0f0f0").pack(pady=5)

        coord_labels = ["(x1, y1)", "(x2, y2)", "(x3, y3)", "(x4, y4)"]
        entries_rectangle = []

        for i in range(4):
            row_frame = Frame(rectangle_frame, bg="#2e3b4e")
            row_frame.pack(pady=2)
            
            Label(row_frame, text=coord_labels[i], font=("Arial", 18), bg="#2e3b4e", fg="#f0f0f0").pack(side="left", padx=5)
            
            entry_x = Entry(row_frame, font=("Arial", 18), width=5, justify="center")
            entry_x.pack(side="left", padx=5)
            entry_y = Entry(row_frame, font=("Arial", 18), width=5, justify="center")
            entry_y.pack(side="left", padx=5)
            
            entries_rectangle.append(entry_x)
            entries_rectangle.append(entry_y)

        triangle_frame = Frame(frame, bg="#2e3b4e")

        Label(triangle_frame, text="Coordenadas do Triângulo:", font=("Arial", 20, "bold"), bg="#2e3b4e", fg="#f0f0f0").pack(pady=5)

        coord_labels_tri = ["(x1, y1)", "(x2, y2)", "(x3, y3)"]
        entries_triangle = []

        for i in range(3):
            row_frame = Frame(triangle_frame, bg="#2e3b4e")
            row_frame.pack(pady=2)
            
            Label(row_frame, text=coord_labels_tri[i], font=("Arial", 18), bg="#2e3b4e", fg="#f0f0f0").pack(side="left", padx=5)
            
            entry_x = Entry(row_frame, font=("Arial", 18), width=5, justify="center")
            entry_x.pack(side="left", padx=5)
            entry_y = Entry(row_frame, font=("Arial", 18), width=5, justify="center")
            entry_y.pack(side="left", padx=5)
            
            entries_triangle.append(entry_x)
            entries_triangle.append(entry_y)

        circle_frame = Frame(frame, bg="#2e3b4e")

        Label(circle_frame, text="Centro do Círculo (cx, cy):", font=("Arial", 20, "bold"), bg="#2e3b4e", fg="#f0f0f0").pack(pady=5)
        circle_coord_frame = Frame(circle_frame, bg="#2e3b4e")
        circle_coord_frame.pack(pady=2)

        entry_circle_x = Entry(circle_coord_frame, font=("Arial", 18), width=5, justify="center")
        entry_circle_x.pack(side="left", padx=5)
        entry_circle_y = Entry(circle_coord_frame, font=("Arial", 18), width=5, justify="center")
        entry_circle_y.pack(side="left", padx=5)

        Label(circle_frame, text="Raio (m):", font=("Arial", 20, "bold"), bg="#2e3b4e", fg="#f0f0f0").pack(pady=5)
        entry_radius = Entry(circle_frame, font=("Arial", 18), width=10, justify="center")
        entry_radius.pack(pady=5)

        def update_input_fields(*args):
            rectangle_frame.pack_forget()
            triangle_frame.pack_forget()
            circle_frame.pack_forget()
            if figure_type.get() == "retangulo":
                rectangle_frame.pack(pady=10)
                button_rectangle.config(bg="#ffa500", fg="white")
                button_triangle.config(bg="#2e3b4e", fg="#f0f0f0")
                button_circle.config(bg="#2e3b4e", fg="#f0f0f0")
            elif figure_type.get() == "triangulo":
                triangle_frame.pack(pady=10)
                button_rectangle.config(bg="#2e3b4e", fg="#f0f0f0")
                button_triangle.config(bg="#ffa500", fg="white")
                button_circle.config(bg="#2e3b4e", fg="#f0f0f0")
            elif figure_type.get() == "circulo":
                circle_frame.pack(pady=10)
                button_rectangle.config(bg="#2e3b4e", fg="#f0f0f0")
                button_triangle.config(bg="#2e3b4e", fg="#f0f0f0")
                button_circle.config(bg="#ffa500", fg="white")
            else:  
                button_rectangle.config(bg="#2e3b4e", fg="#f0f0f0")
                button_triangle.config(bg="#2e3b4e", fg="#f0f0f0")
                button_circle.config(bg="#2e3b4e", fg="#f0f0f0")

        figure_type.trace_add("write", update_input_fields)
        update_input_fields()

        frame_navigation = Frame(frame, bg="#2e3b4e")
        frame_navigation.pack(side="bottom", pady=10)

        Button(
            frame_navigation,
            text="Adicionar Figura de Corte", 
            font=("Arial", 18, "bold"),
            bg="#4caf50",
            fg="white",
            cursor="hand2",
            command=lambda: check_figure(),
            width=22, height=2 
        ).pack(side="left", padx=10, pady=5)

        Button(
            frame_navigation,
            text="Avançar para os cálculos",
            font=("Arial", 18, "bold"),
            bg="#4caf50",
            fg="white",
            cursor="hand2",
            command=lambda: calculate_results(length, support_type, supports, forces, elastic_module, section),
            width=22, height=2 
        ).pack(side="left", padx=10, pady=5)

        Button(
            frame_navigation,
            text="Voltar",
            font=("Arial", 18, "bold"),
            bg="#d32f2f",
            fg="white",
            cursor="hand2",
            command=lambda: start_2(),
            width=22, height=2 
        ).pack(side="left", padx=10, pady=5)
      

        def check_figure():
            figure = figure_type.get()
            try: 
                if figure == "retangulo":
                    coords = []
                    for entry in entries_rectangle:
                        coords.append(float(entry.get().strip()))
                    
                    cut_coords = [(coords[i], coords[i + 1]) for i in range(0, 8, 2)]

                    section.add_cut_figure("retangulo", cut_coords)
                    messagebox.showinfo("Verificação", "Foi inserido um Retângulo como Figura de Corte.")

                elif figure == "triangulo":
                    coords = []
                    for entry in entries_triangle:
                        coords.append(float(entry.get().strip()))

                    cut_coords = [(coords[i], coords[i + 1]) for i in range(0, 6, 2)]

                    section.add_cut_figure("triangulo", cut_coords)
                    messagebox.showinfo("Verificação", "Foi inserido um Triângulo como Figura de Corte.")

                elif figure == "circulo":
                    cx = float(entry_circle_x.get().strip())
                    cy = float(entry_circle_y.get().strip())
                    radius = float(entry_radius.get().strip())

                    if radius <= 0:
                        messagebox.showerror("Erro", "O raio deve ser um valor maior que zero.")
                        return

                    section.add_cut_figure("circulo", (cx, cy, radius))
                    messagebox.showinfo("Verificação", "Foi inserido um Círculo como Figura de Corte.")

                else:
                    messagebox.showerror("Erro", "Selecione uma figura válida antes de prosseguir.")

            except ValueError as e:
                messagebox.showerror("Erro", "Por favor, insira apenas números válidos para as coordenadas.")

    def render_drawing():
        clear_frame(frame)

        Label(frame, text="Estrutura Atual", font=("Arial", 28, "bold"), bg="#2e3b4e", fg="#f0f0f0").pack(pady=20)

        fig, ax = plt.subplots(figsize=(6, 6))
        
        try:
            section.draw_section(ax)
        except ValueError as e:
            messagebox.showerror("Erro", str(e))
            return

        canvas = FigureCanvasTkAgg(fig, frame)
        canvas_widget = canvas.get_tk_widget()
        canvas_widget.pack(fill='both', expand=True)
        canvas.draw()

        button_frame = Frame(frame, bg="#2e3b4e")
        button_frame.pack(side="bottom", pady=20)

        Button(button_frame, text="Voltar", font=("Arial", 20, "bold"), bg="#d32f2f", fg="white", 
            cursor="hand2", command=insert_cut_figure, width=20, height=2).pack(side="left", padx=10)
        
    def calculate_results(length, support_type, supports, forces, elastic_module, section):
        calculate_support_relations(length, support_type, supports, forces, elastic_module, section)

    start_1()