from src.eixo import Eixo
from src.all_imports import *
from src.window import create_main_screen_activity_03
from src.util import clear_frame, confirm_exit_to_main, get_absolute_path
from src.load import Load

def exercise_3_ui(frame, window):

    def start_1():
        clear_frame(frame)

        Label(
            frame,
            text="Exercício 3: Análise de Tensão de Cisalhamento",
            font=("Arial", 28, "bold"),
            bg="#2e3b4e",
            fg="#f0f0f0",
        ).pack(pady=20)

        explanation1 = (
            "Este exercício aborda a análise de tensão de Cisalhamento e ângulo de torção \n"
            "de um eixo, seja ele:\n\n"
            "- Prismático\n"
            "- Composto por partes\n"
            "- Com seção transversal circular variável\n\n"
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
            img1_path = get_absolute_path("activities/Activity_03/assets/exercise_3.1.png")
            img2_path = get_absolute_path("activities/Activity_03/assets/exercise_3.2.png")
            img3_path = get_absolute_path("activities/Activity_03/assets/exercise_3.3.png")

            #TODO: colocar legendas

            img1 = Image.open(img1_path)
            img1 = img1.resize((300, 180), Image.Resampling.LANCZOS)
            img1 = ImageTk.PhotoImage(img1)

            img2 = Image.open(img2_path)
            img2 = img2.resize((300, 180), Image.Resampling.LANCZOS)
            img2 = ImageTk.PhotoImage(img2)

            img3 = Image.open(img3_path)
            img3 = img3.resize((300, 180), Image.Resampling.LANCZOS)
            img3 = ImageTk.PhotoImage(img3)

            img_label1 = Label(image_frame, image=img1, bg="#2e3b4e")
            img_label1.image = img1
            img_label1.pack(side="left", padx=20)

            img_label2 = Label(image_frame, image=img2, bg="#2e3b4e")
            img_label2.image = img2
            img_label2.pack(side="left", padx=20) 

            img_label3 = Label(image_frame, image=img3, bg="#2e3b4e")
            img_label3.image = img3
            img_label3.pack(side="left", padx=20) 

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
        button_frame.pack(pady=20, side="bottom")

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
            text="Exercício 3: Análise de Tensão de Cisalhamento",
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
            "1. Preencha quantas partes o eixo terá\n"
            "  - Se um eixo tiver parte cheia e parte oca, considere cada parte como um eixo separado\n\n"
            "2. Para cada eixo:\n"
            "  - Definir o comprimento do eixo\n"
            "  - Definir o diametro externo ou função do diametro externo\n"
            "  - Definir o diametro interno ou função do diametro interno(0 se for cheio)\n"
            "  - Definir o torque na extremidade direita do eixo\n"
            "  - Selecionar o material do eixo\n\n"
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
        button_frame.pack(pady=20, side="bottom")

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
            text="Exercício 3: Análise de Tensão de Cisalhamento",
            font=("Arial", 28, "bold"),
            bg="#2e3b4e",
            fg="#f0f0f0",
        ).pack(pady=20)

        Label(
            frame,
            text="Configuração do Eixo",
            font=("Arial", 24, "bold"),
            bg="#2e3b4e",
            fg="#f0f0f0",
        ).pack(pady=20)

        frame_eixos = Frame(frame, bg="#2e3b4e")
        frame_eixos.pack(pady=10)

        explanation_eixos = (
            "Preencha quantos eixos terão\n\n"
            "Eixos: "
        )

        Label(
            frame_eixos,
            text=explanation_eixos,
            font=("Arial", 16),
            bg="#2e3b4e",
            fg="#f0f0f0",
            justify="center",
        ).pack(pady=5)

        entry_eixos = Entry(frame_eixos, font=("Arial", 16), width=15, justify="center")
        entry_eixos.pack(pady=5)

        explanation_info_eixos = (
            "A ordem de inserção dos eixos é importante para que o exercício fique correto\n"
            "Devido a isso, escolhemos que o eixo 1 seja o da extremidade livre e o último o da extremidade engastada\n\n"
        )

        Label(
            frame,
            text=explanation_info_eixos,
            font=("Arial", 16),
            bg="#2e3b4e",
            fg="#f0f0f0",
            justify="left",
        ).pack(pady=20)

        button_frame = Frame(frame, bg="#2e3b4e")
        button_frame.pack(pady=20, side="bottom")

        eixos = []

        Button(
            button_frame,
            text="Próximo",
            font=("Arial", 18, "bold"),
            bg="#4caf50",
            fg="white",
            command=lambda: info_eixos(entry_eixos.get(), 0, eixos),
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

    def info_eixos(num_eixos, done, eixos):
        clear_frame(frame)

        try:
            num_eixos = int(num_eixos)
            if num_eixos <= 0:
                start_3()
                messagebox.showerror("Erro", "Insira um valor válido para a quantidade de eixos")
                return
        except ValueError:
            start_3()
            messagebox.showerror("Erro", "Insira um valor válido para a quantidade de eixos")
            return

        Label(
            frame,
            text="Exercício 3: Análise de Tensão de Cisalhamento",
            font=("Arial", 28, "bold"),
            bg="#2e3b4e",
            fg="#f0f0f0",
        ).pack(pady=20)

        explanation_lenght = (
            f"Insira o comprimento do eixo {done+1}"
        )

        Label(
            frame,
            text=explanation_lenght,
            font=("Arial", 18),
            bg="#2e3b4e",
            fg="#f0f0f0",
            wraplength=800,
            justify="left",
        ).pack(pady=20)

        entry_lenght = Entry(frame, font=("Arial", 16), width=15, justify="center")
        entry_lenght.pack(pady=5)

        explanation_eradius = (
            f"Insira o raio externo do eixo {done+1}"
        )

        Label(
            frame,
            text=explanation_eradius,
            font=("Arial", 18),
            bg="#2e3b4e",
            fg="#f0f0f0",
            wraplength=800,
            justify="left",
        ).pack(pady=20)

        entry_eradius = Entry(frame, font=("Arial", 16), width=15, justify="center")
        entry_eradius.pack(pady=5)

        explanation_iradius = (
            f"Insira o raio interno do eixo {done+1}"
        )

        Label(
            frame,
            text=explanation_iradius,
            font=("Arial", 18),
            bg="#2e3b4e",
            fg="#f0f0f0",
            wraplength=800,
            justify="left",
        ).pack(pady=20)

        entry_iradius = Entry(frame, font=("Arial", 16), width=15, justify="center")
        entry_iradius.pack(pady=5)

        explanation_torcao = (
            f"Insira a torção na extremidade do eixo {done+1}"
        )

        Label(
            frame,
            text=explanation_torcao,
            font=("Arial", 18),
            bg="#2e3b4e",
            fg="#f0f0f0",
            wraplength=800,
            justify="left",
        ).pack(pady=20)

        entry_torcao = Entry(frame, font=("Arial", 16), width=15, justify="center")
        entry_torcao.pack(pady=5)

        explanation_G = (
            f"Insira o módulo de cisalhamento do eixo {done+1}"
        )

        Label(
            frame,
            text=explanation_G,
            font=("Arial", 18),
            bg="#2e3b4e",
            fg="#f0f0f0",
            wraplength=800,
            justify="left",
        ).pack(pady=20)

        entry_G = Entry(frame, font=("Arial", 16), width=15, justify="center")
        entry_G.pack(pady=5)

        button_frame = Frame(frame, bg="#2e3b4e")
        button_frame.pack(pady=20, side="bottom")

        Button(
            button_frame,
            text="Próximo" if done < num_eixos - 1 else "Finalizar",
            font=("Arial", 18, "bold"),
            bg="#4caf50",
            fg="white",
            command=lambda: save_and_next(eixos, done, entry_lenght.get(), entry_eradius.get(), entry_iradius.get(), entry_G.get(), entry_torcao.get(), num_eixos),
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

    def save_and_next(eixos, done, lenght, extern_radius, intern_radius, G, Torcao, num_eixos):
        try:
            lenght = float(lenght)
            extern_radius = float(extern_radius)
            intern_radius = float(intern_radius)
            G = float(G)
            Torcao = float(Torcao)
        except ValueError:
            info_eixos(num_eixos, done, eixos)
            messagebox.showerror("Erro", "Os valores devem ser numéricos")
            return

        if lenght <= 0:
            info_eixos(eixos, done)
            messagebox.showerror("Erro", "O comprimento deve ser maior que zero")
            return
        if extern_radius <= 0:
            info_eixos(eixos, done)
            messagebox.showerror("Erro", "O raio externo deve ser maior que zero")
            return
        if intern_radius < 0:
            info_eixos(eixos, done)
            messagebox.showerror("Erro", "O raio interno deve ser maior que zero")
            return
        if G <= 0:
            info_eixos(eixos, done)
            messagebox.showerror("Erro", "O módulo de elasticidade deve ser maior que zero")
            return
        torcao = Torcao
        if len(eixos) > 0:
            for eixo in eixos:
                torcao += eixo.Torcao

        eixos.append(Eixo(lenght, extern_radius, intern_radius, G, torcao))

        if done < num_eixos - 1:
            info_eixos(num_eixos, done + 1, eixos)
        else:
            display_results(eixos)


    def display_results(eixos):
        clear_frame(frame)

        Label(
            frame,
            text="Resultados do Cálculo",
            font=("Arial", 26, "bold"),
            bg="#2e3b4e",
            fg="#f0f0f0",
        ).pack(pady=20, side="top")

        angulo_total = 0
        for i, eixo in enumerate(eixos):
            angulo_total += eixo.angle
            Label(
                frame,
                text=f"Eixo {i+1}",
                font=("Arial", 24, "bold"),
                bg="#2e3b4e",
                fg="#f0f0f0",
            ).pack(pady=20, side="top")

            Label(
                frame,
                text=f"Torque Máximo: {eixo.t_max:.2f} Nm",
                font=("Arial", 20),
                bg="#2e3b4e",
                fg="#f0f0f0",
            ).pack(pady=10, side="top")

            Label(
                frame,
                text=f"Ângulo de Torção: {eixo.angle:.4f} rad",
                font=("Arial", 20),
                bg="#2e3b4e",
                fg="#f0f0f0",
            ).pack(pady=10, side="top")
        Label(
            frame,
            text=f"Ângulo de Torção Total: {angulo_total:.4f} rad",
            font=("Arial", 24, "bold"),
            bg="#2e3b4e",
            fg="#f0f0f0",
        ).pack(pady=20, side="top")
        

        button_frame = Frame(frame, bg="#2e3b4e")
        button_frame.pack(pady=20, side="bottom")

        Button(
            button_frame,
            text="Menu Principal",
            font=("Arial", 20, "bold"),
            bg="#d32f2f",
            fg="white",
            command=lambda: confirm_exit_to_main(window, frame, 3),
            cursor="hand2",
            width=20,
            height=2,
        ).pack(side="bottom", padx=20)

    start_1()