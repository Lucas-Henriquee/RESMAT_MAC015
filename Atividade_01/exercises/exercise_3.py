from imports.all_imports import *
from src.util import clear_frame
from src.window import create_main_screen
from src.node import NodeManager
from src.support import SupportManager
from src.bar import BarManager

def exercise_3_ui(frame, window):

    node_manager = NodeManager()
    bar_manager = BarManager(node_manager)
    support_manager = SupportManager()

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
            img = Image.open("assets/exercise_3.png") 
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
        reset_state()

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
            text="Exercício 3: Análise de Treliças Planas Isostáticas",
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
        entry_x = Entry(coord_frame, font=("Arial", 22), width=15)
        entry_x.pack()
        Label(coord_frame, text="Componente Y:", font=("Arial", 20), bg="#2e3b4e", fg="#f0f0f0").pack()
        entry_y = Entry(coord_frame, font=("Arial", 22), width=15)
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
        entry_start = Entry(coord_frame_start, font=("Arial", 22), width=15)
        entry_start.pack()

        coord_frame_end = Frame(frame, bg="#2e3b4e")
        coord_frame_end.pack(pady=10)
        Label(coord_frame_end, text="Nó de Fim:", font=("Arial", 20), bg="#2e3b4e", fg="#f0f0f0").pack()
        entry_end = Entry(coord_frame_end, font=("Arial", 22), width=15)
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

            if bar_count == num_bar:
                add_supports()
            else:
                create_bar_frame(bar_count + 1, num_bar)

        except ValueError as e:
            messagebox.showerror("Erro", str(e))

    def render_drawing():
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
            padding = max(max(all_x) - min(all_x), max(all_y) - min(all_y)) * 0.1
            ax.set_xlim(min(all_x) - padding, max(all_x) + padding)
            ax.set_ylim(min(all_y) - padding, max(all_y) + padding)

        ax.set_xlabel("Coordenada X")
        ax.set_ylabel("Coordenada Y")

        legend_elements = [
            Line2D([0], [0], marker='o', color='w', markerfacecolor='blue', markersize=10, label='Nós'),
            Line2D([0], [0], color='black', linewidth=4.5, label='Barras'),
            Polygon([[0, 0]], closed=True, color='red', label='Apoio de 1º gênero'),
            Polygon([[0, 0]], closed=True, color='green', label='Apoio de 2º gênero')
            ]

        ax.legend(handles=legend_elements, loc='upper right', fontsize=8)

        canvas = FigureCanvasTkAgg(fig, frame)
        canvas_widget = canvas.get_tk_widget()
        canvas_widget.pack(fill='both', expand=True)
        canvas.draw()

        button_frame = Frame(frame, bg="#2e3b4e")
        button_frame.pack(side="bottom", pady=20)
        Button(button_frame, text="Voltar", font=("Arial", 20, "bold"), bg="#d32f2f", fg="white", 
           cursor="hand2", command=add_supports, width=20, height=2).pack(side="left", padx=10)

    def add_supports():
        clear_frame(frame)

        Label(frame, text="Insira os dados dos apoios da treliça", font=("Arial", 28), bg="#2e3b4e", fg="#f0f0f0").pack(pady=20)

        Label(
            frame,
            text="Como estamos trabalhando em treliças planas, você pode escolher entre:\n"
             "- 3 apoios de 1º Gênero\n"
             "- 1 apoio de 1º Gênero e 1 apoio de 2º Gênero\n"
             "Evite sobrepor apoios no mesmo nó.",
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
            command=lambda: render_drawing()
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
        frame_navigation.pack(pady=10)

        Button(
            frame_navigation,
            text="Finalizar",
            font=("Arial", 16),
            bg="#4caf50",
            fg="white",
            cursor="hand2",
            command=lambda: start_1()
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

    def save_support(node, entry_type):
        try:
            support_type = int(entry_type)
            if support_type not in [1, 2]:
                raise ValueError("Tipo inválido.")
            support_manager.add_support(node, support_type)
            messagebox.showerror("Adicionado!", "Apoio adicionado ao problema!")
            add_supports()
        except ValueError:
            messagebox.showerror("Erro", "Por favor, insira um tipo válido (1 ou 2).")

    start_1()