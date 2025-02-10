from src.all_imports import *
from src.util import clear_frame, confirm_exit_to_main
from src.window import create_main_screen_activity_03
from src.node import NodeManager
from src.support import SupportManager
from src.bar import BarManager
from src.force import Force

def exercise_2_ui(frame, window):

    node_manager = NodeManager()
    bar_manager = BarManager(node_manager)
    support_manager = SupportManager()

    def start_0():
        clear_frame(frame)

        Label(
            frame,
            text="Exercício 2: Deformacões em Treliças Planas Isostáticas",
            font=("Arial", 28, "bold"),
            bg="#2e3b4e",
            fg="#f0f0f0",
        ).pack(pady=20)

        explanation0 = (
            "Neste exercício, você realizará a Análise de Deformações em Treliças Planas Isostáticas. "
            "A base do exercício é dada pelo exercício 3 da Atividade 01. "
            "Logo você deve configurar a treliça isostática e no final será abordado a questão da deformação.\n\n") 
        
        Label(
            frame,
            text=explanation0,
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
            command=lambda: start_1(),
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
            command=lambda: create_main_screen_activity_03(window, frame),
            cursor="hand2",
            width=15,
            height=2,
        ).pack(side = "right", padx=20)


    def start_1():
        clear_frame(frame)

        Label(
            frame,
            text="Exercício 2: Deformacões em Treliças Planas Isostáticas",
            font=("Arial", 28, "bold"),
            bg="#2e3b4e",
            fg="#f0f0f0",
        ).pack(pady=20)

        explanation1 = (
            "Neste exercício, você realizará a Análise e o Cálculo de Treliças Planas Isostáticas e no final a análise da deformação da treliça. "
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
            img = Image.open("activities/Activity_02/assets/exercise_2.png") 
            img = img.resize((600, 300), Image.Resampling.LANCZOS) 
            img = ImageTk.PhotoImage(img)

            img_label = Label(frame, image=img, bg="#2e3b4e")
            img_label.image = img  
            img_label.pack(pady=20)
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
            command=lambda: start_0(),
            cursor="hand2",
            width=15,
            height=2,
        ).pack(side = "right", padx=20)

    def start_2():
        reset_state()

        Label(
            frame,
            text="Exercício 2: Deformacões em Treliças Planas Isostáticas",
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
            "3. Inserir os apoios: Informe o nó onde cada apoio estará localizado e o tipo de apoio que será usado: \n"
            "   - Apoio móvel (Apoio de 1º Gênero):  Permite deslocamento em uma direção e bloqueia na perpendicular.\n"
            "   - Apoio fixo (Apoio de 2º Gênero): Bloqueia movimentos em todas as direções, mas permite rotações.\n"
            "   - Engaste (Apoio de 3º Gênero): Restringe totalmente movimentos e rotações.\n\n"
            "4. Definir os carregamentos: Para cada carregamento, especifique o nó onde ele será aplicado e a intensidade\n\n"
            "5. Calcular a deformação: Após configurar a treliça, você poderá visualizar a estrutura e calcular a deformação das barras."
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
            command=lambda: add_num_nodes(),
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

    def reset_state():
        node_manager.clear_nodes()
        bar_manager.clear_bars()
        support_manager.clear_supports()
        clear_frame(frame)

    def add_num_nodes():

        clear_frame(frame)

        Label(
            frame,
            text="Exercício 2: Deformacões em Treliças Planas Isostáticas",
            font=("Arial", 28, "bold"),
            bg="#2e3b4e",
            fg="#f0f0f0",
        ).pack(pady=20)

        Label(
            frame,
            text="Insira a quantidade de nós que a treliça terá:",
            font=("Arial", 20),
            bg="#2e3b4e",
            fg="#f0f0f0",
        ).pack(pady=10)

        entry_num_nodes = Entry(frame, font=("Arial", 18), width=10, justify="center")
        entry_num_nodes.pack(pady=15)

        button_frame_1 = Frame(frame, bg="#2e3b4e")
        button_frame_1.pack(padx=20)

        Button(button_frame_1, text="Iniciar", font=("Arial", 18, "bold"), bg="#4caf50", fg="white", command=lambda: get_nodes(entry_num_nodes) , cursor="hand2", width=15, height=1).pack(side="left", padx=20)
        Button(button_frame_1, text="Voltar", font=("Arial", 18, "bold"), bg="#d32f2f", fg="white", command=lambda: start_2, cursor="hand2", width=15, height=1).pack(side="left", padx=20)

    def save_and_next_nodes(x, y, nodes_count, num_nodes):
        try:
            if not x or not y:
                raise ValueError("Coordenadas X e Y não podem estar vazias.")
            x, y = float(x), float(y)
            node_manager.add_node(x, y)
            messagebox.showinfo("Adiconado!", f"Nó {chr(64 + nodes_count)} adicionado com sucesso!")
            if nodes_count == num_nodes:
                add_bars()
            else:
                create_nodes_frame(nodes_count + 1, num_nodes)
        except ValueError as e:
            messagebox.showerror("Erro", str(e))

    def display_nodes():
        Label(frame, text="Lista de Nós", font=("Arial", 24, "bold"), bg="#2e3b4e", fg="#f0f0f0").pack(pady=20)

        nodes = node_manager.list_nodes()
        if not nodes:
            Label(frame, text="Não há Nó adicionado", font=("Arial", 20, "bold"), bg="#2e3b4e", fg="#f0f0f0").pack(pady=20)
            return

        max_columns = 3  
        nodes_frame = Frame(frame, bg="#2e3b4e")
        nodes_frame.pack(pady=10)

        for i, node in enumerate(nodes):
            row = i // max_columns
            col = i % max_columns
            Label(nodes_frame, text=f"Nó {node}\t", font=("Arial", 20), bg="#2e3b4e", fg="#f0f0f0").grid(row=row, column=col, padx=10, pady=5)

    def create_nodes_frame(nodes_count, num_nodes):

        clear_frame(frame)

        Label(frame, text=f"Insira os dados do Nó {chr(64 + nodes_count)}", font=("Arial", 24, "bold"), bg="#2e3b4e", fg="#f0f0f0",).pack(pady=20)

        coord_frame = Frame(frame, bg="#2e3b4e")
        coord_frame.pack(pady=20)
        Label(coord_frame, text="Componente X:", font=("Arial", 20), bg="#2e3b4e", fg="#f0f0f0").pack()
        entry_x = Entry(coord_frame, font=("Arial", 22), width=15, justify="center")
        entry_x.pack()
        Label(coord_frame, text="Componente Y:", font=("Arial", 20), bg="#2e3b4e", fg="#f0f0f0").pack()
        entry_y = Entry(coord_frame, font=("Arial", 22), width=15, justify="center")
        entry_y.pack()

        button_frame_2 = Frame(frame, bg="#2e3b4e")
        button_frame_2.pack(side="bottom", pady=20)

        display_nodes()

        Button(
            button_frame_2, 
            text="Avançar para barras" if nodes_count == num_nodes else "Salvar e Próxima",
            font=("Arial", 20, "bold"), 
            cursor="hand2", 
            bg="#4caf50", 
            fg="white", 
            command= lambda: save_and_next_nodes(entry_x.get(), entry_y.get(), nodes_count, num_nodes), 
            width=20, 
            height=2).pack(side="left", padx=10)
        
        Button(
            button_frame_2, 
            text="Voltar", 
            font=("Arial", 20, "bold"), 
            bg="#d32f2f", 
            fg="white", 
            cursor="hand2", 
            command=start_2, 
            width=20, 
            height=2).pack(side="left", padx=10)

    def get_nodes(entry_num_nodes):
        try:
            num_nodes = int(entry_num_nodes.get())
            if num_nodes <= 2:
                raise ValueError("O número de nós deve ser no mínimo 3 para ser considerad uma treliça.")
            create_nodes_frame(1, num_nodes)
        except ValueError as e:
            messagebox.showerror("Erro", str(e))

    def add_bars():

        clear_frame(frame)

        max_bars = 2*len(node_manager.nodes)-3

        Label(frame, text=f"Adicionando as barras a treliça", font=("Arial", 24, "bold"), bg="#2e3b4e", fg="#f0f0f0",).pack(pady=20)

        Label(
            frame,
            text="Para considerarmos uma treliça isostática será considerado um número fixo de barras a serem adicionadas no problema:",
            font=("Arial", 18),
            bg="#2e3b4e",
            fg="#f0f0f0",
            wraplength=750,  
            justify="left"
        ).pack(pady=(35, 20))  

        Label(
            frame,
            text="Número de Barras: 2N - 3, onde N é o número de nós.",
            font=("Arial", 18),
            bg="#2e3b4e",
            fg="#f0f0f0",
        ).pack(pady=5)

        Label(
            frame,
            text=f"O número de barras nesse caso é: {max_bars}",
            font=("Arial", 18),
            bg="#2e3b4e",
            fg="#f0f0f0",
        ).pack(pady=12)

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
            command=lambda: render_drawing("bar")
        ).pack(side="left")

        button_frame_1 = Frame(frame, bg="#2e3b4e")
        button_frame_1.pack(pady=50)

        Button(button_frame_1, text="Iniciar", font=("Arial", 18, "bold"), bg="#4caf50", fg="white", command=lambda: get_bar(max_bars) , cursor="hand2", width=15, height=1).pack(side="left", padx=20)
        Button(button_frame_1, text="Voltar", font=("Arial", 18, "bold"), bg="#d32f2f", fg="white", command=lambda: start_2(), cursor="hand2", width=15, height=1).pack(side="left", padx=20)

    def create_bar_frame(bars_count, num_bars):
        clear_frame(frame)

        Label(frame, text=f"Insira os dados da Barra {bars_count}", font=("Arial", 24, "bold"), bg="#2e3b4e", fg="#f0f0f0").pack(pady=20)

        coord_frame_start = Frame(frame, bg="#2e3b4e")
        coord_frame_start.pack(pady=10)
        Label(coord_frame_start, text="Nó de Início:", font=("Arial", 20), bg="#2e3b4e", fg="#f0f0f0").pack()
        entry_start = Entry(coord_frame_start, font=("Arial", 22), width=15, justify="center")
        entry_start.pack()

        coord_frame_end = Frame(frame, bg="#2e3b4e")
        coord_frame_end.pack(pady=10)
        Label(coord_frame_end, text="Nó de Fim:", font=("Arial", 20), bg="#2e3b4e", fg="#f0f0f0").pack()
        entry_end = Entry(coord_frame_end, font=("Arial", 22), width=15, justify="center")
        entry_end.pack()

        button_frame_2 = Frame(frame, bg="#2e3b4e")
        button_frame_2.pack(side="bottom", pady=20)

        display_nodes()

        Button(
            button_frame_2,
            text="Avançar para apoios" if bars_count == num_bars else "Salvar e Próxima",
            font=("Arial", 20, "bold"),
            cursor="hand2",
            bg="#4caf50",
            fg="white",
            command=lambda: save_bar(bars_count, entry_start.get(), entry_end.get()),
            width=20,
            height=2
        ).pack(side="left", padx=10)

        Button(
            button_frame_2,
            text="Voltar",
            font=("Arial", 20, "bold"),
            bg="#d32f2f",
            fg="white",
            cursor="hand2",
            command=start_2,
            width=20,
            height=2
        ).pack(side="left", padx=10)

    def get_bar(max_bars):
        try:
            create_bar_frame(1, max_bars)
        except ValueError as e:
            messagebox.showerror("Erro", str(e))

    def save_bar(bar_count, start_node, end_node):
        try:
            if start_node not in [node.name for node in node_manager.nodes] or \
           end_node not in [node.name for node in node_manager.nodes]:
                raise ValueError("Os nós especificados não existem. Verifique a lista de nós adicionados.")

            if not bar_manager.validate_bar(start_node, end_node):
                raise ValueError("Barra inválida.")

            bar_manager.add_bar(start_node, end_node)
            num_bar = 2 * len(node_manager.nodes) - 3

            messagebox.showinfo("Adicionado!", f"Barra {bar_count} adicionada com sucesso!")

            if bar_count == num_bar:
                add_supports()
            else:
                create_bar_frame(bar_count + 1, num_bar)

        except ValueError as e:
            messagebox.showerror("Erro", str(e))

    def render_drawing(type):
        clear_frame(frame)

        Label(frame, text="Estrutura Atual", font=("Arial", 28, "bold"), bg="#2e3b4e", fg="#f0f0f0").pack(pady=20)

        fig, ax = plt.subplots(figsize=(6, 6))
        ax.axhline(0, color='gray', linewidth=0.5, linestyle='--')
        ax.axvline(0, color='gray', linewidth=0.5, linestyle='--')
        ax.grid(color='lightgray', linestyle='--', linewidth=0.5, alpha=0.7)

        support_manager.draw_supports(ax, node_manager)
        node_x, node_y = node_manager.draw_nodes(ax)
        bar_x, bar_y = bar_manager.draw_bars(ax)

        all_x = node_x + bar_x
        all_y = node_y + bar_y
        if all_x and all_y:
            max_range = max(max(all_x) - min(all_x), max(all_y) - min(all_y))
            padding = max_range * 0.1
            ax.set_xlim(min(all_x) - padding, max(all_x) + padding)
            ax.set_ylim(min(all_y) - padding, max(all_y) + padding)
            ax.set_aspect('equal')

        ax.set_xlabel("Coordenada X")
        ax.set_ylabel("Coordenada Y")

        legend_elements = [
            Line2D([0], [0], marker='o', color='w', markerfacecolor='blue', markersize=10, label='Nós'),
            Line2D([0], [0], color='black', linewidth=4.5, label='Barras'),
            Polygon([[0, 0]], closed=True, color='red', label='Apoio de 2º gênero'),
            Polygon([[0, 0]], closed=True, color='green', label='Apoio de 1º gênero'),
            Line2D([0], [0], color='orange', lw=2, label='Forças Aplicadas')
        ]

        deformation_threshold = 1e-6

        for bar in bar_manager.bars:
            start_node = node_manager.get_node(bar.start_node)
            end_node = node_manager.get_node(bar.end_node)

            if start_node is None or end_node is None:
                continue  

            x_orig = [start_node.x, end_node.x]
            y_orig = [start_node.y, end_node.y]

            x_deformed = [start_node.x_deformed, end_node.x_deformed]
            y_deformed = [start_node.y_deformed, end_node.y_deformed]

            deformation = max(
                abs(x_deformed[0] - x_orig[0]), abs(x_deformed[1] - x_orig[1]),
                abs(y_deformed[0] - y_orig[0]), abs(y_deformed[1] - y_orig[1])
            )

            if deformation > deformation_threshold:
                scale_factor = 250
                x_deformed_scaled = [
                    orig + (deformed - orig) * scale_factor 
                    for orig, deformed in zip(x_orig, x_deformed)
                ]
                y_deformed_scaled = [
                    orig + (deformed - orig) * scale_factor 
                    for orig, deformed in zip(y_orig, y_deformed)
                ]

                ax.plot(
                    x_deformed_scaled, y_deformed_scaled, color='red', linestyle='--', linewidth=1.5,
                    label='Barra Deformada' if 'Barra Deformada' not in [el.get_label() for el in legend_elements] else ""
                )


                if 'Barra Deformada' not in [el.get_label() for el in legend_elements]:
                    legend_elements.append(Line2D([0], [0], color='red', linestyle='--', linewidth=1.5, label='Barra Deformada'))

        ax.legend(handles=legend_elements, loc='upper right', fontsize=8)

        canvas = FigureCanvasTkAgg(fig, frame)
        canvas_widget = canvas.get_tk_widget()
        canvas_widget.pack(fill='both', expand=True)
        canvas.draw()

        button_frame = Frame(frame, bg="#2e3b4e")
        button_frame.pack(side="bottom", pady=20)

        if type == "support":
            Button(button_frame, text="Voltar", font=("Arial", 20, "bold"), bg="#d32f2f", fg="white", 
           cursor="hand2", command=add_supports, width=20, height=2).pack(side="left", padx=10)
        elif type == "force":
            Button(button_frame, text="Voltar", font=("Arial", 20, "bold"), bg="#d32f2f", fg="white", 
           cursor="hand2", command=add_force, width=20, height=2).pack(side="left", padx=10)
        elif type == "bar":
            Button(button_frame, text="Voltar", font=("Arial", 20, "bold"), bg="#d32f2f", fg="white", 
           cursor="hand2", command=add_bars, width=20, height=2).pack(side="left", padx=10)
        elif type == "final":
            Button(button_frame, text="Voltar", font=("Arial", 20, "bold"), bg="#d32f2f", fg="white", 
           cursor="hand2", command=calculate_results, width=20, height=2).pack(side="left", padx=10)
        elif type == "bar_deformed":
            Button(button_frame, text="Voltar", font=("Arial", 20, "bold"), bg="#d32f2f", fg="white", 
           cursor="hand2", command=calculate_deformed, width=20, height=2).pack(side="left", padx=10)
        else: 
            Button(button_frame, text="Voltar", font=("Arial", 20, "bold"), bg="#d32f2f", fg="white", 
           cursor="hand2", command=start_2, width=20, height=2).pack(side="left", padx=10)

    def add_supports():
        clear_frame(frame)

        Label(frame, text="Insira os dados dos apoios da treliça", font=("Arial", 28), bg="#2e3b4e", fg="#f0f0f0").pack(pady=20)

        Label(
            frame,
            text="Como estamos trabalhando em treliças planas isostáticas, você pode escolher entre:\n"
             "- 3 apoios de 1º Gênero\n"
             "- 1 apoio de 1º Gênero e 1 apoio de 2º Gênero",
            font=("Arial", 18),
            bg="#2e3b4e",
            fg="#f0f0f0",
            wraplength=750,
            justify="left"
        ).pack(pady=(35, 20))

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
            command=lambda: render_drawing("support")
        ).pack(side="left")

        Label(frame, text="Digite o nó para o apoio:", font=("Arial", 20), bg="#2e3b4e", fg="#f0f0f0").pack(pady=(10, 5))
        node_entry = Entry(frame, font=("Arial", 16), bg="#f0f0f0", fg="#2e3b4e", justify="center")
        node_entry.pack(pady=5)

        Label(frame, text="Selecione o tipo de apoio:", font=("Arial", 20), bg="#2e3b4e", fg="#f0f0f0").pack(pady=(20, 5))

        entry_type = StringVar(value="")  

        def update_support_type(support_type):
            entry_type.set(support_type)
            if support_type == "1":
                button_1.config(bg="#ffa500", fg="white")
                button_2.config(bg="#2e3b4e", fg="#f0f0f0")
            elif support_type == "2":
                button_2.config(bg="#ffa500", fg="white")
                button_1.config(bg="#2e3b4e", fg="#f0f0f0")
            else:
                button_1.config(bg="#2e3b4e", fg="#f0f0f0")
                button_2.config(bg="#2e3b4e", fg="#f0f0f0")

        frame_buttons_support = Frame(frame, bg="#2e3b4e")
        frame_buttons_support.pack(pady=15)

        button_1 = Button(
            frame_buttons_support,
            text="1º Gênero",
            font=("Arial", 18),
            bg="#2e3b4e",
            fg="#f0f0f0",
            cursor="hand2",
            activebackground="#ffa500",
            activeforeground="white",
            command=lambda: update_support_type("1")
        )
        button_1.pack(side="left", padx=20)

        button_2 = Button(
            frame_buttons_support,
            text="2º Gênero",
            font=("Arial", 18),
            bg="#2e3b4e",
            fg="#f0f0f0",
            cursor="hand2",
            activebackground="#ffa500",
            activeforeground="white",
            command=lambda: update_support_type("2")
        )
        button_2.pack(side="left", padx=20)

        frame_buttons = Frame(frame, bg="#2e3b4e")
        frame_buttons.pack(pady=30)

        Button(
            frame_buttons,
            text="Adicionar Apoio",
            font=("Arial", 16),
            bg="#4caf50",
            fg="white",
            cursor="hand2",
            command=lambda: save_support(node_entry.get(), entry_type.get())
        ).pack(side="left", padx=20)

        frame_navigation = Frame(frame, bg="#2e3b4e")
        frame_navigation.pack(pady=20)

        Button(
            frame_navigation,
            text="Avançar para o carregamento", 
            font=("Arial", 16),
            bg="#4caf50",
            fg="white",
            cursor="hand2",
            command=lambda: check_supports()
        ).pack(side="left", padx=10)

        Button(
            frame_navigation,
            text="Voltar",
            font=("Arial", 16),
            bg="#d32f2f",
            fg="white",
            cursor="hand2",
            command=lambda: start_2()
        ).pack(side="left", padx=10)

    def check_supports():
        support_counts = {1: 0, 2: 0}

        for support in support_manager.supports:
            support_counts[support.support_type] += 1

        if support_counts[1] == 3 or (support_counts[1] == 1 and support_counts[2] == 1):
            add_force()
        else:
            messagebox.showerror("Erro", "Você precisa inserir 3 apoios de 1º gênero ou 1 de 1º gênero e 1 de 2º gênero antes de avançar.")

    def save_support(node, entry_type):
        try:
            support_type = int(entry_type)
            if support_type not in [1, 2]:
                raise ValueError("Tipo inválido! Escolha 1 (1º gênero) ou 2 (2º gênero).")

            support_manager.add_support(node, support_type)
            messagebox.showinfo("Sucesso!", f"Apoio do tipo {support_type} adicionado no nó {node}!")
            add_supports()

        except ValueError as e:
            messagebox.showerror("Erro ao adicionar apoio", str(e))

    def add_force():

        clear_frame(frame)

        Label(
            frame,
            text="Adicionando carregamento à treliça",
            font=("Arial", 20),
            bg="#2e3b4e",
            fg="#f0f0f0",
        ).pack(pady=20)

        Label(
            frame,
            text=(
                "Você está prestes a adicionar forças à treliça.\n"
                "Lembre-se: o carregamento se refere a uma força vertical com sentido para baixo.\n"
                "Insira o valor da força em módulo."
            ),
            font=("Arial", 18),
            bg="#2e3b4e",
            fg="#f0f0f0",
            wraplength=750,
            justify="left",
        ).pack(pady=(10, 20))

        Label(
            frame,
            text="Quantos carregamentos você deseja inserir?",
            font=("Arial", 20),
            bg="#2e3b4e",
            fg="#f0f0f0",
        ).pack(pady=10)

        entry_num_forces = Entry(frame, font=("Arial", 20), width=10, justify="center")
        entry_num_forces.pack(pady=15)

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
            command=lambda: render_drawing("force")
        ).pack(side="left")

        button_frame_1 = Frame(frame, bg="#2e3b4e")
        button_frame_1.pack(pady=20)

        Button(button_frame_1, text="Iniciar", font=("Arial", 18, "bold"), bg="#4caf50", fg="white", command=lambda: get_forces(entry_num_forces) , cursor="hand2", width=15, height=1).pack(side="left", padx=20)
        Button(button_frame_1, text="Voltar", font=("Arial", 18, "bold"), bg="#d32f2f", fg="white", command=lambda: start_2(), cursor="hand2", width=15, height=1).pack(side="left", padx=20)

    def get_forces(entry_num_forces):
        try:
            num_forces = int(entry_num_forces.get())
            if num_forces <= 0:
                raise ValueError("O número de carregamentos deve ser maior que 0.")
            create_force_frame(1, num_forces)
        except ValueError as e:
            messagebox.showerror("Erro", str(e))

    def create_force_frame(forces_count, num_forces):
        clear_frame(frame)

        Label(frame, text=f"Insira os dados do Carregamento {forces_count}", font=("Arial", 24, "bold"), bg="#2e3b4e", fg="#f0f0f0").pack(pady=20)

        node_frame = Frame(frame, bg="#2e3b4e")
        node_frame.pack(pady=10)
        Label(node_frame, text="Nó de Aplicação:", font=("Arial", 20), bg="#2e3b4e", fg="#f0f0f0").pack()
        entry_start = Entry(node_frame, font=("Arial", 22), width=15, justify="center")
        entry_start.pack()

        intensity_frame = Frame(frame, bg="#2e3b4e")
        intensity_frame.pack(pady=10)
        Label(intensity_frame, text="Intensidade (em N):", font=("Arial", 20), bg="#2e3b4e", fg="#f0f0f0").pack()
        entry_end = Entry(intensity_frame, font=("Arial", 22), width=15, justify="center")
        entry_end.pack()

        display_nodes()

        button_frame_2 = Frame(frame, bg="#2e3b4e")
        button_frame_2.pack(side="bottom", pady=20)     

        Button(
            button_frame_2,
            text="Avançar para resultados" if forces_count == num_forces else "Salvar e Próxima",
            font=("Arial", 20, "bold"),
            cursor="hand2",
            bg="#4caf50",
            fg="white",
            command=lambda: save_force(num_forces, forces_count, entry_start.get(), entry_end.get()),
            width=20,
            height=2
        ).pack(side="left", padx=10)

        Button(
            button_frame_2,
            text="Voltar",
            font=("Arial", 20, "bold"),
            bg="#d32f2f",
            fg="white",
            cursor="hand2",
            command=start_2,
            width=20,
            height=2
        ).pack(side="left", padx=10)

    def save_force(num_forces, force_count, node_name, intensity):
        try:
            target_node = node_manager.get_node(node_name)
            if not target_node:
                raise ValueError("O nó especificado não existe. Verifique a lista de nós adicionados.")
            if not intensity:
                raise ValueError("A intensidade do carregamento não pode estar vazia.")
            intensity = float(intensity)
            force = Force(intensity=abs(intensity), force_type="graus", angle_or_coordinates=270)
            target_node.add_force(force)

            messagebox.showinfo("Adicionado!", f"Carregamento {force_count} adicionado com sucesso!")

            if force_count == num_forces:
                info()
            else:
                create_force_frame(force_count + 1, num_forces)
        except ValueError as e:
            messagebox.showerror("Erro", str(e))
    
    def info():

        clear_frame(frame)

        Label(frame, text=f"Você terminou de preencher os dados corretamente para a criação de uma treliça plana isostática", font=("Arial", 24, "bold"), bg="#2e3b4e", fg="#f0f0f0",wraplength=800,
            justify="left").pack(pady=20)

        Label(frame, text="Atenção! Não há uma forma de garantir que a treliça será isostática com as condições aplicadas nesse programa. A restrição feita aqui contempla:\n", font=("Arial", 16), bg="#2e3b4e", fg="#f0f0f0", wraplength=800,
            justify="left").pack(pady=20)

        Label(
            frame,
            text=(
            "- Número mínimo de nós que uma treliça deve conter\n"
            "- Condição do número exato de barras : B = 2N - 3\n"
            "- Não pode haver cruzamento de barras no plano xy\n"
            ),
            font=("Arial", 16),
            bg="#2e3b4e",
            fg="#f0f0f0",
            wraplength=800,
            justify="left"  
        )  .pack(pady=10)
        
        Label(frame, text="Agora você pode calcular os resultados da treliça.", font=("Arial", 20), bg="#2e3b4e", fg="#f0f0f0").pack(pady=20)

        button_frame_2 = Frame(frame, bg="#2e3b4e")
        button_frame_2.pack(side="bottom", pady=20)     

        Button(
            button_frame_2,
            text="Calcular resultados",
            font=("Arial", 20, "bold"),
            cursor="hand2",
            bg="#4caf50",
            fg="white",
            command=lambda: calculate_results(),
            width=20,
            height=2
        ).pack(side="left", padx=10)

        Button(
            button_frame_2,
            text="Voltar",
            font=("Arial", 20, "bold"),
            bg="#d32f2f",
            fg="white",
            cursor="hand2",
            command=start_2,
            width=20,
            height=2
        ).pack(side="left", padx=10)

    def deformed_truss():
        clear_frame(frame)

        Label(
            frame,
            text="Deformação de uma Treliça Plana Isostática",
            font=("Arial", 24, "bold"),
            bg="#2e3b4e",
            fg="#f0f0f0",
            wraplength=800,
            justify="left"
        ).pack(pady=20)

        Label(
            frame,
            text="Escolha na tabela abaixo o valor do módulo de elasticidade E e a área da seção transversal A:",
            font=("Arial", 16),
            bg="#2e3b4e",
            fg="#f0f0f0",
            wraplength=800,
            justify="left"
        ).pack(pady=20)

        materials = [
            ("Material", "Módulo de Elasticidade (GPa)", "Área (m²)"),
            ("Aço Estrutural", "200", "5.0e-4"),
            ("Alumínio", "69", "4.0e-4"),
            ("Madeira (Pinus)", "10", "1.0e-3"),
            ("Madeira (Carvalho)", "12", "1.2e-3"),
            ("Concreto Armado", "30", "8.0e-4"),
            ("Titânio", "116", "3.5e-4")
        ]

        material_text = f"{materials[0][0]:<22}{materials[0][1]:<30}{materials[0][2]:<20}\n"
        material_text += "-" * 70 + "\n"

        for material, modulus, area in materials[1:]:
            material_text += f"{material:<32}{modulus:<20}{area:<20}\n"
        
        material_text += "-" * 70 + "\n"

        material_label = Label(
            frame,
            text=material_text,
            font=("Courier", 16),
            bg="#2e3b4e",
            fg="#f0f0f0",
            justify="left",
            anchor="w",
        )
        material_label.pack(pady=20)

        Label(
            frame,
            text="Digite o valor do módulo de elasticidade (GPa):",
            font=("Arial", 16),
            bg="#2e3b4e",
            fg="#f0f0f0"
        ).pack(pady=10)

        entry_E = Entry(frame, font=("Arial", 18), width=10, justify="center")
        entry_E.insert(0,"")  
        entry_E.pack(pady=5)

        Label(
            frame,
            text="Digite o valor da área da seção transversal no formato científico (ex: 5.01e-4):",
            font=("Arial", 16),
            bg="#2e3b4e",
            fg="#f0f0f0"
        ).pack(pady=10)

        entry_A = Entry(frame, font=("Arial", 18), width=10, justify="center")
        entry_A.insert(0, "") 
        entry_A.pack(pady=5)

        def apply_EA():
            try:
                E_value = float(entry_E.get()) * 1e9 
                A_value = float(eval(entry_A.get())) 
                
                if E_value <= 0 or A_value <= 0:
                    raise ValueError("Os valores de E e A devem ser positivos.")
                
                bar_manager.set_elasticity_modulus(E_value)
                bar_manager.set_cross_sectional_area(float(A_value))
                
                messagebox.showinfo("Sucesso!", f"E = {E_value / 1e9:.2f} GPa, A = {A_value:.2e} m² definidos.")
                calculate_deformed()
            
            except ValueError:
                messagebox.showerror("Erro", "Digite valores válidos para E e A.")

        button_frame = Frame(frame, bg="#2e3b4e")
        button_frame.pack(pady=20)

        Button(
            button_frame,
            text="Aplicar",
            font=("Arial", 18, "bold"),
            bg="#4caf50",
            fg="white",
            command=apply_EA,
            cursor="hand2",
            width=15,
            height=1,
        ).pack(side="left", padx=15)

        Button(
            button_frame,
            text="Voltar",
            font=("Arial", 18, "bold"),
            bg="#d32f2f",
            fg="white",
            command=lambda: start_2(),
            cursor="hand2",
            width=15,
            height=1,
        ).pack(side="left", padx=15)

    def calculate_results():
        clear_frame(frame)
        from src.truss import solve_truss

        try:
            nodes = node_manager.nodes
            bars = bar_manager.bars
            supports = support_manager.supports

            #results = solve_truss(nodes, bars, supports)

            #results = solve_truss_by_nodes(nodes, bars, supports)

            results = solve_truss(nodes, bars, supports)

            results_text = "Barra\tTração/Compressão\t+-(N)\n"
            for bar_name, status, force in results:
                results_text += f"{bar_name}\t{status}\t{force:.2f}\n"

            results_text = "Barra       T/C/N    +-(N)\n"
            results_text += "-" * 30 + "\n"

            for bar_name, status, force in results:
                force_value = force[0] if isinstance(force, tuple) else force

                results_text += f"{bar_name:<14}{status:<7}{f"+{force_value:.2f}" if force_value > 0 else f"{force_value:.2f}" if force_value < 0 else "0.00"}\n"

            results_text += "-" * 30 + "\n"

            Label(
                frame,
                text="Resultados do Cálculo",
                font=("Arial", 26),
                bg="#2e3b4e",
                fg="#f0f0f0",
            ).pack(pady=20)

            result_label = Label(
                frame,
                text=results_text,
                font=("Courier", 22),
                bg="#2e3b4e",
                fg="#f0f0f0",
                justify="left",
                anchor="w",
            )
            result_label.pack(pady=20)

            button_frame_2 = Frame(frame, bg="#2e3b4e")
            button_frame_2.pack(side="bottom", pady=20)     

            Button(
                button_frame_2,
                text="Deformação na Treliça", 
                font=("Arial", 20, "bold"),
                cursor="hand2",
                bg="#4caf50",
                fg="white",
                command=lambda: deformed_truss(),
                width=20,
                height=2
            ).pack(side="left", padx=10)

            Button(
                button_frame_2,
                text="Menu Principal",
                font=("Arial", 20, "bold"),
                bg="#d32f2f",
                fg="white",
                cursor="hand2",
                command= lambda:confirm_exit_to_main(window, frame, 2),
                width=20,
                height=2
            ).pack(side="left", padx=10)

        except Exception as e:
            messagebox.showerror("Erro", f"Ocorreu um erro ao calcular os resultados: {e}")

    def calculate_deformed():
        clear_frame(frame)

        from src.truss import solve_truss_by_global_stiffness

        nodes = node_manager.nodes
        bars = bar_manager.bars
        supports = support_manager.supports

        if bar_manager.E is None:
            messagebox.showerror("Erro", "Defina um valor para o módulo de elasticidade (E) antes de calcular a deformação.")
            return

        results, displacements = solve_truss_by_global_stiffness(nodes, bars, supports, bar_manager.E, bar_manager.A)
        node_manager.apply_displacements(displacements)

        Label(
            frame,
            text = f"Análise da Deformação na Treliça (E = {bar_manager.E / 1e9:.0f} GPa)",
            font=("Arial", 26),
            bg="#2e3b4e",
            fg="#f0f0f0",
        ).pack(pady=20)

        results_text = "Nó       X Inicial   Y Inicial   X Deformado   Y Deformado\n"
        results_text += "-" * 70 + "\n"

        for node in nodes:
            results_text += f"{node.name:^9}{node.x:^13.3f}{node.y:^12.3f}{node.x_deformed:^15.6f}{node.y_deformed:^12.6f}\n"

        results_text += "-" * 70 + "\n"
        results_text += "\nVariação no Comprimento das Barras:\n"
        results_text += "Barra       L (m)      T/C\n"
        results_text += "-" * 40 + "\n"

        for bar, (bar_name, status, force) in zip(bars, results):
            start_node = node_manager.get_node(bar.start_node)
            end_node = node_manager.get_node(bar.end_node)

            L_original = np.sqrt((start_node.x - end_node.x) ** 2 + (start_node.y - end_node.y) ** 2)
            L_deformed = np.sqrt((start_node.x_deformed - end_node.x_deformed) ** 2 + (start_node.y_deformed - end_node.y_deformed) ** 2)
            delta_L = L_deformed - L_original

            results_text += f"{bar_name:<10}{delta_L:^12.6f}{status:^5}\n"
        
        results_text += "-" * 40 + "\n"

        result_label = Label(
            frame,
            text=results_text,
            font=("Courier", 16),
            bg="#2e3b4e",
            fg="#f0f0f0",
            justify="center",
            anchor="center",
        )

        result_label.pack(pady=20)

        Label(
            frame,
            text=(
                "Foi utilizada uma escala de 250x no plot da treliça deformada para facilitar a visualização da deformação\n"
            ),
            font=("Arial", 16),
            bg="#2e3b4e",
            fg="#f0f0f0",
        ).pack(pady=20)

        button_frame = Frame(frame, bg="#2e3b4e")
        button_frame.pack(pady=20)

        Button(
            button_frame,
            text="Alterar E e A",
            font=("Arial", 18, "bold"),
            bg="#4caf50",
            fg="white",
            cursor="hand2",
            command=lambda: deformed_truss(),
            width=15,
            height=1,
        ).pack(side="left", padx=20)

        Button(
            button_frame,
            text="Visualizar Treliça",
            font=("Arial", 18, "bold"),
            bg="#4caf50",
            fg="white",
            cursor="hand2",
            command= lambda:render_drawing("bar_deformed"),
            width=15,
            height=1,
        ).pack(side="left", padx=20)

        Button(
            button_frame,
            text="Menu Principal",
            font=("Arial", 18, "bold"),
            bg="#d32f2f",
            fg="white",
            command=lambda: confirm_exit_to_main(window, frame, 2),
            cursor="hand2",
            width=15,
            height=1,
        ).pack(side="left", padx=20)

    start_0()