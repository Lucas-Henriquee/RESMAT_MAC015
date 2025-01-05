from tkinter import Label, Entry, Button, StringVar, Radiobutton, Frame, messagebox, ttk
from src.util import clear_frame
from src.window import create_main_screen
from src.force_operations import calcular_resultante, desenhar_resultante
from src.force import Force
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def exercise_1_ui(frame, window):
    clear_frame(frame)

    Label(
        frame,
        text="Exercício 1: Forças Concorrentes",
        font=("Arial", 28, "bold"),
        bg="#2e3b4e",
        fg="#f0f0f0",
    ).pack(pady=20)

    explanation = (
        "Este exercício permite calcular a intensidade e a direção resultante de **N** forças coplanares "
        "concorrentes em um nó.\n\n"
        "Existem dois tipos de força que você pode inserir:\n"
        "- Força por Ângulo e Intensidade: Indique a intensidade (N) e o ângulo (em graus).\n"
        "- Força por Coordenadas Cartesianas (X, Y): Informe as componentes da força no plano e a intensidade (em N), se necessário.\n\n"
        "Escolha o tipo de força desejado e insira os valores correspondentes."
    )

    Label(
        frame,
        text=explanation,
        font=("Arial", 16),
        bg="#2e3b4e",
        fg="#f0f0f0",
        wraplength=800,
        justify="left",
    ).pack(pady=20)

    Label(
        frame,
        text="Quantas forças você deseja inserir?",
        font=("Arial", 20),
        bg="#2e3b4e",
        fg="#f0f0f0",
    ).pack(pady=10)

    entry_num_forces = Entry(frame, font=("Arial", 20), width=10, justify="center")
    entry_num_forces.pack(pady=15)

    button_frame = Frame(frame, bg="#2e3b4e")
    button_frame.pack(pady=20)

    forces = [] 

    def reset_state():
        forces.clear()
        clear_frame(frame)
        exercise_1_ui(frame, window)

    def confirm_exit_to_main():
        if messagebox.askyesno("Confirmação", "Deseja voltar ao menu principal? Todas as alterações serão perdidas."):
            create_main_screen(window, frame)

    def get_forces():
        try:
            num_forces = int(entry_num_forces.get())
            if num_forces <= 0:
                raise ValueError("O número de forças deve ser maior que zero.")

            def create_force_frame(force_count):
                clear_frame(frame)
                Label(frame, text=f"Insira os dados da Força {force_count}", font=("Arial", 24, "bold"), bg="#2e3b4e", fg="#f0f0f0",).pack(pady=20)

                entry_type = StringVar()

                Label(frame,text="Escolha o tipo de força:", font=("Arial", 18), bg="#2e3b4e", fg="#f0f0f0",).pack(pady=10)
                frame_entry_type = Frame(frame, bg="#2e3b4e")
                frame_entry_type.pack(pady=10)

                button_angle = Radiobutton(frame_entry_type, text="Ângulo (graus)", font=("Arial", 20), variable=entry_type, value="graus",bg="#4caf50", fg="white", selectcolor="#2e3b4e",)
                button_angle.pack(side="left", padx=20)
                button_coord = Radiobutton(frame_entry_type, text="Coordenadas (X, Y)", font=("Arial", 20), variable=entry_type, value="coordenadas",bg="#2e3b4e", fg="#f0f0f0", selectcolor="#2e3b4e",)
                button_coord.pack(side="left", padx=20)

                Label(frame, text="Intensidade (obrigatório para graus):", font=("Arial", 20), bg="#2e3b4e", fg="#f0f0f0").pack(pady=10)
                entry_intensity = Entry(frame, font=("Arial", 22), width=15)
                entry_intensity.pack(pady=10)

                angle_frame, coord_frame, entry_angle, entry_x, entry_y = create_angle_and_coord_frames()

                def save_and_next(force_count):
                    try:
                        intensity = float(entry_intensity.get()) if entry_intensity.get() else None
                        if entry_type.get() == "graus":
                            if intensity is None:
                                raise ValueError("A intensidade é obrigatória para ângulo em graus.")
                            angle = float(entry_angle.get())
                            forces.append(Force(intensity, "graus", angle))
                        else:
                            x = float(entry_x.get())
                            y = float(entry_y.get())
                            forces.append(Force(intensity, "coordenadas", (x, y)))

                        if force_count < num_forces:
                            create_force_frame(force_count + 1)
                        else:
                            display_forces()
                    except ValueError as e:
                        messagebox.showerror("Erro", str(e))

                def update_input_fields(*args):
                    angle_frame.pack_forget()
                    coord_frame.pack_forget()
                    if entry_type.get() == "graus":
                        angle_frame.pack(pady=10)
                        button_angle.config(bg="#ffa500", fg="white")
                        button_coord.config(bg="#2e3b4e", fg="#f0f0f0")
                    elif entry_type.get() == "coordenadas":
                        coord_frame.pack(pady=10)
                        button_coord.config(bg="#ffa500", fg="white")
                        button_angle.config(bg="#2e3b4e", fg="#f0f0f0")
                    else:  
                        button_angle.config(bg="#2e3b4e", fg="#f0f0f0")
                        button_coord.config(bg="#2e3b4e", fg="#f0f0f0")

                entry_type.trace_add("write", update_input_fields)
                update_input_fields()
                button_frame = Frame(frame, bg="#2e3b4e")
                button_frame.pack(side="bottom", pady=20)

                Button(button_frame, text="Calcular Resultante" if force_count == num_forces else "Salvar e Próxima",font=("Arial", 20, "bold"), bg="#4caf50", fg="white", command=lambda: save_and_next(force_count), width=20, height=2).pack(side="left", padx=10)
                Button(button_frame, text="Voltar", font=("Arial", 20, "bold"), bg="#d32f2f", fg="white", command=reset_state, width=20, height=2).pack(side="left", padx=10)

            def create_angle_and_coord_frames():
                angle_frame = Frame(frame, bg="#2e3b4e")
                Label(angle_frame, text="Ângulo (graus):", font=("Arial", 20), bg="#2e3b4e", fg="#f0f0f0").pack()
                entry_angle = Entry(angle_frame, font=("Arial", 22), width=15)
                entry_angle.pack()

                coord_frame = Frame(frame, bg="#2e3b4e")
                Label(coord_frame, text="Componente X:", font=("Arial", 20), bg="#2e3b4e", fg="#f0f0f0").pack()
                entry_x = Entry(coord_frame, font=("Arial", 22), width=15)
                entry_x.pack()
                Label(coord_frame, text="Componente Y:", font=("Arial", 20), bg="#2e3b4e", fg="#f0f0f0").pack()
                entry_y = Entry(coord_frame, font=("Arial", 22), width=15)
                entry_y.pack()

                return angle_frame, coord_frame, entry_angle, entry_x, entry_y

            def display_forces():
                clear_frame(frame)
                if not forces:
                    Label(frame, text="Sem nenhuma força registrada", font=("Arial", 24, "bold"), bg="#2e3b4e", fg="#f0f0f0").pack(pady=20)
                    Button(frame, text="Voltar", font=("Arial", 20, "bold"), bg="#4caf50", fg="white", command=reset_state, width=20, height=2).pack(pady=10)
                    Button(frame, text="Menu Principal", font=("Arial", 20, "bold"), bg="#d32f2f", fg="white", command=lambda: create_main_screen(window, frame), width=20, height=2).pack(pady=10)
                    return

                Label(frame, text="Lista de Forças", font=("Arial", 24, "bold"), bg="#2e3b4e", fg="#f0f0f0").pack(pady=20)

                for i, force in enumerate(forces, start=1):
                    Label(frame, text=f"Força {i}: {force}", font=("Arial", 20), bg="#2e3b4e", fg="#f0f0f0").pack(pady=5)
                    button_frame = Frame(frame, bg="#2e3b4e")
                    button_frame.pack(pady=5)

                    Button(button_frame, text="Editar", font=("Arial", 16), bg="#1976d2", fg="white", command=lambda idx=i-1: edit_force(idx)).pack(side="left", padx=10)
                    Button(button_frame, text="Excluir", font=("Arial", 16), bg="#d32f2f", fg="white", command=lambda idx=i-1: delete_force(idx)).pack(side="left", padx=10)

                result_intensity, result_angle, result_x, result_y = calcular_resultante(forces)
                result_display = (f"Resultante: Intensidade = {result_intensity:.2f} N, "
                      f"Ângulo = {result_angle:.2f}°, "
                      f"Coordenadas (X, Y) = ({result_x:.2f}, {result_y:.2f})")
                Label(frame, text=result_display, font=("Arial", 20), bg="#2e3b4e", fg="#f0f0f0").pack(pady=20)

                button_frame = Frame(frame, bg="#2e3b4e")
                button_frame.pack(side="bottom", pady=20)

                Button(button_frame, text="Visualizar Resultante", font=("Arial", 20, "bold"), bg="#4caf50", fg="white", command=result_canvas, width=20, height=2).pack(side="left", padx=10)
                Button(button_frame, text="Menu Principal", font=("Arial", 20, "bold"), bg="#d32f2f", fg="white", command=lambda: confirm_exit_to_main(), width=20, height=2).pack(side="left", padx=10)

            def edit_force(index):
                def save_changes():
                    try:
                        new_intensity = float(entry_intensity.get()) if entry_intensity.get() else None
                        new_type = entry_type.get()

                        if new_type == "graus":
                            if not entry_angle.get():
                                raise ValueError("O ângulo deve ser fornecido para forças do tipo 'graus'.")
                            new_angle = float(entry_angle.get())
                            forces[index].update_force(intensity=new_intensity, angle_or_coordinates=new_angle, force_type=new_type)

                        elif new_type == "coordenadas":
                            if not entry_x.get() or not entry_y.get():
                                raise ValueError("As coordenadas X e Y devem ser fornecidas para forças do tipo 'coordenadas'.")
                            new_x = float(entry_x.get())
                            new_y = float(entry_y.get())

                            if new_intensity is None:
                                new_intensity = (new_x**2 + new_y**2) ** 0.5

                            forces[index].update_force(intensity=new_intensity, angle_or_coordinates=(new_x, new_y), force_type=new_type)

                        display_forces()

                    except ValueError as e:
                        messagebox.showerror("Erro", str(e))

                force = forces[index]
                clear_frame(frame)

                Label(frame, text=f"Editando Força {index + 1}", font=("Arial", 24, "bold"), bg="#2e3b4e", fg="#f0f0f0").pack(pady=20)

                entry_type = StringVar()
                frame_entry_type = Frame(frame, bg="#2e3b4e")
                frame_entry_type.pack(pady=15)

                button_angle = Radiobutton(frame_entry_type, text="Ângulo (graus)", font=("Arial", 20), variable=entry_type, value="graus",bg="#2e3b4e", fg="white", selectcolor="#2e3b4e",)
                button_angle.pack(side="left", padx=20)
                button_coord = Radiobutton(frame_entry_type, text="Coordenadas (X, Y)", font=("Arial", 20), variable=entry_type, value="coordenadas",bg="#2e3b4e", fg="#f0f0f0", selectcolor="#2e3b4e",)
                button_coord.pack(side="left", padx=20)

                Label(frame, text="Nova Intensidade:", font=("Arial", 20), bg="#2e3b4e", fg="#f0f0f0").pack()
                entry_intensity = Entry(frame, font=("Arial", 22), width=15)
                entry_intensity.insert(0, str(force.intensity) if force.intensity else "")
                entry_intensity.pack()


                angle_frame, coord_frame, entry_angle, entry_x, entry_y = create_angle_and_coord_frames()

                if force.type == "graus":
                    angle_frame.pack(pady=10)
                    button_angle.config(bg="#ffa500") 
                    entry_intensity.delete(0, 'end')
                    entry_intensity.insert(0, str(force.intensity) if force.intensity else "")

                    entry_angle.insert(0, str(force.angle))
                else:
                    coord_frame.pack(pady=10)
                    entry_intensity.delete(0, 'end')
                    button_coord.config(bg="#ffa500") 
                    entry_intensity.insert(0, str(force.intensity) if force.intensity else "")
                    entry_x.insert(0, str(force.original_x))
                    entry_y.insert(0, str(force.original_y))

                def update_input_fields(*args):
                    angle_frame.pack_forget()
                    coord_frame.pack_forget()
                    if entry_type.get() == "graus":
                        angle_frame.pack(pady=10)
                        button_angle.config(bg="#ffa500", fg="white")
                        button_coord.config(bg="#2e3b4e", fg="#f0f0f0")

                    elif entry_type.get() == "coordenadas":
                        coord_frame.pack(pady=10)
                        button_coord.config(bg="#ffa500", fg="white")
                        button_angle.config(bg="#2e3b4e", fg="#f0f0f0")
                    else:  
                        button_angle.config(bg="#2e3b4e", fg="#f0f0f0")
                        button_coord.config(bg="#2e3b4e", fg="#f0f0f0")

                entry_type.trace_add("write", update_input_fields)

                button_frame = Frame(frame, bg="#2e3b4e")
                button_frame.pack(side="bottom", pady=20)

                Button(button_frame, text="Salvar", font=("Arial", 20, "bold"), bg="#4caf50", fg="white", command=save_changes).pack(side="left", padx=20)
                Button(button_frame, text="Cancelar", font=("Arial", 20, "bold"), bg="#d32f2f", fg="white", command=display_forces).pack(side="left", padx=20)


            def delete_force(index):
                forces.pop(index)
                display_forces()

            def result_canvas():
                clear_frame(frame)

                Label(frame, text="Força Resultante", font=("Arial", 28, "bold"), bg="#2e3b4e", fg="#f0f0f0").pack(pady=20)

                result_intensity, result_angle, result_x, result_y = calcular_resultante(forces)

                fig, ax = plt.subplots(figsize=(6, 6))
                desenhar_resultante(forces, ax)

                canvas = FigureCanvasTkAgg(fig, master=frame)
                canvas.draw()
                canvas.get_tk_widget().pack(fill='both', expand=True)

                button_frame = Frame(frame, bg="#2e3b4e")
                button_frame.pack(side="bottom", pady=20)
                Button(button_frame, text="Voltar", font=("Arial", 20, "bold"), bg="#4caf50", fg="white", command=display_forces, width=20, height=2).pack(side="left", padx=10)
                Button(button_frame, text="Menu Principal", font=("Arial", 20, "bold"), bg="#d32f2f", fg="white", command=lambda: confirm_exit_to_main(), width=20, height=2).pack(side="left", padx=10)

            create_force_frame(1)

        except ValueError:
            messagebox.showerror("Erro", "Insira um número válido!")
    
    Button(button_frame, text="Iniciar", font=("Arial", 18, "bold"), bg="#4caf50", fg="white", command=get_forces, width=15, height=2).pack(side="left", padx=20)
    Button(button_frame, text="Voltar", font=("Arial", 18, "bold"), bg="#d32f2f", fg="white", command=lambda: create_main_screen(window, frame), width=15, height=2).pack(side="left", padx=20)