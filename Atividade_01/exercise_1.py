import sys
from tkinter import Label, Entry, Button, StringVar, Radiobutton, Frame
from util import clear_frame
from window import create_main_screen
from force_operations import calcular_resultante, desenhar_resultante
from force import Force
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def exercise_1_ui(frame, window):
    clear_frame(frame)
    Label(frame, text="Exercício 1: Forças Concorrentes", font=("Arial", 28, "bold"), bg="#2e3b4e", fg="#f0f0f0").pack(pady=20)

    Label(frame, text="Quantas forças você deseja inserir?", font=("Arial", 20), bg="#2e3b4e", fg="#f0f0f0").pack(pady=10)
    entry_num_forces = Entry(frame, font=("Arial", 22), width=15)
    entry_num_forces.pack(pady=15)

    forces = [] 

    def reset_state():
        forces.clear()
        clear_frame(frame)
        exercise_1_ui(frame, window)

    def close_program():
        window.destroy()
        sys.exit()

    def get_forces():
        try:
            num_forces = int(entry_num_forces.get())
            if num_forces <= 0:
                raise ValueError("O número de forças deve ser maior que zero.")

            def create_force_frame(force_count):
                clear_frame(frame)
                Label(frame, text=f"Força {force_count}", font=("Arial", 24, "bold"), bg="#2e3b4e", fg="#f0f0f0").pack(pady=20)

                entry_type = StringVar(value="graus")
                frame_entry_type = Frame(frame, bg="#2e3b4e")
                frame_entry_type.pack(pady=15)

                Radiobutton(frame_entry_type, text="Ângulo (graus)", font=("Arial", 20), variable=entry_type, value="graus", bg="#2e3b4e", fg="#f0f0f0").pack(side="left", padx=20)
                Radiobutton(frame_entry_type, text="Coordenadas (X, Y)", font=("Arial", 20), variable=entry_type, value="coordenadas", bg="#2e3b4e", fg="#f0f0f0").pack(side="left", padx=20)

                Label(frame, text="Intensidade (opcional para coordenadas):", font=("Arial", 20), bg="#2e3b4e", fg="#f0f0f0").pack(pady=10)
                entry_intensity = Entry(frame, font=("Arial", 22), width=15)
                entry_intensity.pack(pady=10)

                angle_frame, coord_frame, entry_angle, entry_x, entry_y = create_angle_and_coord_frames()

                def save_and_next(force_count):
                    try:
                        intensity = float(entry_intensity.get()) if entry_intensity.get() else None
                        if entry_type.get() == "graus":
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
                        Label(frame, text=f"Erro: {str(e)}", font=("Arial", 16), bg="#2e3b4e", fg="red").pack(pady=10)

                def update_input_fields(*args):
                    angle_frame.pack_forget()
                    coord_frame.pack_forget()
                    if entry_type.get() == "graus":
                        angle_frame.pack(pady=10)
                    else:
                        coord_frame.pack(pady=10)

                entry_type.trace_add("write", update_input_fields)
                angle_frame.pack(pady=10)

                button_frame = Frame(frame, bg="#2e3b4e")
                button_frame.pack(side="bottom", pady=20)

                Button(button_frame, text="Salvar e Próxima", font=("Arial", 20, "bold"), bg="#4caf50", fg="white", command=lambda: save_and_next(force_count), width=20, height=2).pack(side="left", padx=10)
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
                Label(frame, text="Lista de Forças", font=("Arial", 24, "bold"), bg="#2e3b4e", fg="#f0f0f0").pack(pady=20)

                for i, force in enumerate(forces, start=1):
                    Label(frame, text=f"Força {i}: {force}", font=("Arial", 20), bg="#2e3b4e", fg="#f0f0f0").pack(pady=5)
                    Button(frame, text=f"Editar Força {i}", font=("Arial", 16), bg="#1976d2", fg="white", command=lambda idx=i-1: edit_force(idx)).pack(pady=5)

                result_intensity, result_angle, result_x, result_y = calcular_resultante(forces)
                result_display = (f"Resultante: Intensidade = {result_intensity:.2f} N, "
                                  f"Ângulo = {result_angle:.2f}°, "
                                  f"Coordenadas (X, Y) = ({result_x:.2f}, {result_y:.2f})")
                Label(frame, text=result_display, font=("Arial", 20), bg="#2e3b4e", fg="#f0f0f0").pack(pady=20)

                button_frame = Frame(frame, bg="#2e3b4e")
                button_frame.pack(side="bottom", pady=20)

                Button(button_frame, text="Visualizar Resultante", font=("Arial", 20, "bold"), bg="#4caf50", fg="white", command=result_canvas, width=20, height=2).pack(side="left", padx=10)
                Button(button_frame, text="Menu Principal", font=("Arial", 20, "bold"), bg="#d32f2f", fg="white", command=lambda: create_main_screen(window, frame), width=20, height=2).pack(side="left", padx=10)

            def edit_force(index):
                def save_changes():
                    try:
                        new_intensity = float(entry_intensity.get()) if entry_intensity.get() else None
                        if force.type == "graus":
                            new_angle = float(entry_angle.get())
                            forces[index].update_force(intensity=new_intensity, angle_or_coordinates=new_angle)
                        else:
                            new_x = float(entry_x.get())
                            new_y = float(entry_y.get())
                            forces[index].update_force(intensity=new_intensity, angle_or_coordinates=(new_x, new_y))
                        display_forces()
                    except ValueError:
                        Label(edit_frame, text="Erro! Insira valores válidos.", font=("Arial", 16), bg="#2e3b4e", fg="red").pack(pady=10)

                force = forces[index]
                clear_frame(frame)
                edit_frame = Frame(frame, bg="#2e3b4e")
                edit_frame.pack(pady=20)

                Label(edit_frame, text=f"Editando Força {index + 1}", font=("Arial", 24, "bold"), bg="#2e3b4e", fg="#f0f0f0").pack(pady=20)
                entry_intensity = Entry(edit_frame, font=("Arial", 22), width=15)
                entry_intensity.insert(0, str(force.intensity) if force.intensity else "")
                Label(edit_frame, text="Nova Intensidade:", font=("Arial", 20), bg="#2e3b4e", fg="#f0f0f0").pack()
                entry_intensity.pack()

                if force.type == "graus":
                    entry_angle = Entry(edit_frame, font=("Arial", 22), width=15)
                    entry_angle.insert(0, str(force.angle))
                    Label(edit_frame, text="Novo Ângulo:", font=("Arial", 20), bg="#2e3b4e", fg="#f0f0f0").pack()
                    entry_angle.pack()
                else:
                    entry_x = Entry(edit_frame, font=("Arial", 22), width=15)
                    entry_x.insert(0, str(force.x))
                    Label(edit_frame, text="Novo X:", font=("Arial", 20), bg="#2e3b4e", fg="#f0f0f0").pack()
                    entry_x.pack()
                    entry_y = Entry(edit_frame, font=("Arial", 22), width=15)
                    entry_y.insert(0, str(force.y))
                    Label(edit_frame, text="Novo Y:", font=("Arial", 20), bg="#2e3b4e", fg="#f0f0f0").pack()
                    entry_y.pack()

                Button(edit_frame, text="Salvar", font=("Arial", 20, "bold"), bg="#4caf50", fg="white", command=save_changes).pack(pady=20)
                Button(edit_frame, text="Cancelar", font=("Arial", 20, "bold"), bg="#d32f2f", fg="white", command=display_forces).pack(pady=20)

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
                Button(button_frame, text="Menu Principal", font=("Arial", 20, "bold"), bg="#d32f2f", fg="white", command=lambda: create_main_screen(window, frame), width=20, height=2).pack(side="left", padx=10)

            create_force_frame(1)

        except ValueError:
            Label(frame, text="Erro: Insira um número válido!", font=("Arial", 20), bg="#2e3b4e", fg="red").pack(pady=10)

    Button(frame, text="Iniciar", font=("Arial", 20, "bold"), bg="#4caf50", fg="white", command=get_forces, width=20, height=2).pack(pady=20)
    Button(frame, text="Sair", font=("Arial", 20, "bold"), bg="#d32f2f", fg="white", command=close_program, width=20, height=2).pack(pady=10)