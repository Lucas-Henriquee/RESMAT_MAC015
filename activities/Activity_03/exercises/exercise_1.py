from src.all_imports import *
from src.window import create_main_screen_activity_03
from src.util import clear_frame, confirm_exit_to_main, get_absolute_path
from src.section import Section
from src.moment import calculate_moments

def exercise_1_ui(frame, window):

    section = Section()

    def start_1():
        clear_frame(frame)

        Label(
            frame,
            text="Exercício 1: Cálculo do Momento de Inércia de Seções",
            font=("Arial", 28, "bold"),
            bg="#2e3b4e",
            fg="#f0f0f0"
        ).pack(pady=20)

        explanation1 = (
            "Este exercício tem como objetivo determinar o momento de inércia e o produto de inércia de seções "
            "compostas por figuras geométricas básicas, como retângulos, círculos e triângulos.\n\n"
            "Etapas do exercício:\n"
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
            command=lambda: insert_figure(),
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

    def insert_figure():
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

        Button(button_frame, text="Avancar",font=("Arial", 20, "bold"), cursor="hand2", bg="#4caf50", fg="white", command=lambda: check_figure(), width=20, height=2).pack(side="left", padx=10)
        Button(button_frame, text="Voltar", font=("Arial", 20, "bold"), bg="#d32f2f", fg="white", cursor="hand2", command=start_2, width=20, height=2).pack(side="left", padx=10)

        def check_figure():
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
                    insert_cut_figure()

                except ValueError:
                    messagebox.showerror("Erro", "Por favor, insira valores numéricos válidos.")

            elif figure == "triangulo":
                try:
                    base = float(entry_base.get())
                    height = float(entry_height_2.get())
                    section.create_main_figure("triangulo", (base, height))
                    messagebox.showinfo("Verificação", "Foi inserido um Triângulo como Figura Principal.")
                    insert_cut_figure()

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
                    insert_cut_figure()

                except ValueError:
                    messagebox.showerror("Erro", "Por favor, insira um valor numérico válido para o raio.")

            else:
                messagebox.showerror("Erro", "Selecione uma figura válida antes de prosseguir.")

    def insert_cut_figure():
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
            command=lambda: show_results(section),
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
        
    def show_results(section):
        clear_frame(frame)

        Label(
            frame,
            text="Resultados dos Cálculos",
            font=("Arial", 28, "bold"),
            bg="#2e3b4e",
            fg="#f0f0f0",
        ).pack(pady=20)

        results = calculate_moments(section)
        results_text = "\n".join(results)
        
        result_label = Label(
            frame,
            text=results_text,
            font=("Courier", 16),
            bg="#2e3b4e",
            fg="#f0f0f0",
            justify="left",
            anchor="w",
        )
        result_label.pack(pady=20)
        
        button_frame = Frame(frame, bg="#2e3b4e")
        button_frame.pack(pady=20)
        
        Button(
            button_frame,
            text="Menu Principal",
            font=("Arial", 18, "bold"),
            bg="#d32f2f",
            fg="white",
            cursor="hand2",
            command=lambda: confirm_exit_to_main(window, frame, 3),
            width=15,
            height=2,
        ).pack(side="left", padx=20)

    start_1()