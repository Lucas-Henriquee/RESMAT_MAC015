from .all_imports import * 
from .util import clear_frame, center_window, exit_program, create_label, create_button
from .credits import credits_ui, information_1_ui, information_2_ui, information_3_ui

def configure_window(window):
    window.title("Resistência dos Materiais (MAC-015)")
    center_window(window)  
    window.configure(bg="#2e3b4e")

def create_main_screen(window, frame):

    clear_frame(frame)

    create_label(frame, "Resistência dos Materiais\n\n2024/3 - Turma X", 
                 ("Arial", 24, "bold"), "#2e3b4e", "#f0f0f0", pady=30)
    
    create_label(frame, "Selecione uma atividade", 
                 ("Arial", 18), "#2e3b4e", "#f0f0f0", pady=20)
    
    button_width = 35  
    button_spacing = 15 

    create_button(
        frame, "Atividade 01", 
        ("Arial", 16, "bold"), "#4caf50", "white", lambda: create_main_screen_activity_01(window, frame),
        button_width, 2, pady=button_spacing
    )

    create_button(
        frame, "Atividade 02", 
        ("Arial", 16, "bold"), "#2196f3", "white", lambda: create_main_screen_activity_02(window, frame),
        button_width, 2, pady=button_spacing
    )

    create_button(
        frame, "Atividade 03", 
        ("Arial", 16, "bold"), "#ff9800", "white", lambda: create_main_screen_activity_03(window, frame),
        button_width, 2, pady=button_spacing
    )

    create_button(
        frame, "Créditos", 
        ("Arial", 16, "bold"), "#616161", "white", lambda: credits_ui(frame, window),
        button_width, 2, pady=button_spacing
    )

    create_button(
        frame, "Sair", 
        ("Arial", 16, "bold"), "#d32f2f", "white", exit_program,
        button_width, 2, pady=button_spacing
    )

def create_main_screen_activity_01(window, frame):

    clear_frame(frame)

    from activities.Activity_01.exercises.exercise_1 import exercise_1_ui
    from activities.Activity_01.exercises.exercise_2 import exercise_2_ui
    from activities.Activity_01.exercises.exercise_3 import exercise_3_ui
    
    create_label(frame, "Resistência dos Materiais\n\nAtividade 01", 
                 ("Arial", 24, "bold"), "#2e3b4e", "#f0f0f0", pady=30)

    create_label(frame, "Selecione um exercício", 
                 ("Arial", 18), "#2e3b4e", "#f0f0f0", pady=20)

    button_width = 35  
    button_spacing = 15  

    create_button(
        frame, "Exercício 1 - Forças Concorrentes", 
        ("Arial", 16, "bold"), "#4caf50", "white", lambda: exercise_1_ui(frame, window),
        button_width, 2, pady=button_spacing
    )

    create_button(
        frame, "Exercício 2 - Apoio em Vigas", 
        ("Arial", 16, "bold"), "#2196f3", "white", lambda: exercise_2_ui(frame, window),
        button_width, 2, pady=button_spacing
    )

    create_button(
        frame, "Exercício 3 - Treliças Planas", 
        ("Arial", 16, "bold"), "#ff9800", "white", lambda: exercise_3_ui(frame, window),
        button_width, 2, pady=button_spacing
    )

    create_button(
        frame, "Informações", 
        ("Arial", 16, "bold"), "#616161", "white", lambda: information_1_ui(frame, window),
        button_width, 2, pady=button_spacing
    )

    create_button(
        frame, "Menu Principal", 
        ("Arial", 16, "bold"), "#d32f2f", "white", lambda: create_main_screen(window, frame),
        button_width, 2, pady=button_spacing
    )

def create_main_screen_activity_02(window, frame):

    clear_frame(frame)

    from activities.Activity_02.exercises.exercise_1 import exercise_1_ui
    from activities.Activity_02.exercises.exercise_2 import exercise_2_ui
    
    create_label(frame, "Resistência dos Materiais\n\nAtividade 02", 
                 ("Arial", 24, "bold"), "#2e3b4e", "#f0f0f0", pady=30)

    create_label(frame, "Selecione um exercício", 
                 ("Arial", 18), "#2e3b4e", "#f0f0f0", pady=20)

    button_width = 35  
    button_spacing = 15  

    create_button(
        frame, "Exercício 1 - Esforços em vigas", 
        ("Arial", 16, "bold"), "#4caf50", "white", lambda: exercise_1_ui(frame, window),
        button_width, 2, pady=button_spacing
    )

    create_button(
        frame, "Exercício 2 - Deformação em treliças", 
        ("Arial", 16, "bold"), "#2196f3", "white", lambda: exercise_2_ui(frame, window),
        button_width, 2, pady=button_spacing
    )

    create_button(
        frame, "Informações", 
        ("Arial", 16, "bold"), "#616161", "white", lambda: information_2_ui(frame, window),
        button_width, 2, pady=button_spacing
    )

    create_button(
        frame, "Menu Principal", 
        ("Arial", 16, "bold"), "#d32f2f", "white", lambda: create_main_screen(window, frame),
        button_width, 2, pady=button_spacing
    )

def create_main_screen_activity_03(window, frame):

    clear_frame(frame)

    from activities.Activity_03.exercises.exercise_1 import exercise_1_ui
    from activities.Activity_03.exercises.exercise_2 import exercise_2_ui
    from activities.Activity_03.exercises.exercise_3 import exercise_3_ui
    
    create_label(frame, "Resistência dos Materiais\n\nAtividade 03", 
                 ("Arial", 24, "bold"), "#2e3b4e", "#f0f0f0", pady=30)

    create_label(frame, "Selecione um exercício", 
                 ("Arial", 18), "#2e3b4e", "#f0f0f0", pady=20)

    button_width = 35  
    button_spacing = 15  

    create_button(
        frame, "Exercício 1 - Momento de Inércia", 
        ("Arial", 16, "bold"), "#4caf50", "white", lambda: exercise_1_ui(frame, window),
        button_width, 2, pady=button_spacing
    )

    create_button(
        frame, "Exercício 2 - Tensões máximas de tração e compressão", #TODO: Rever nomes
        ("Arial", 16, "bold"), "#2196f3", "white", lambda: exercise_2_ui(frame, window),
        button_width, 2, pady=button_spacing
    )

    create_button(
        frame, "Exercício 3 - Tensões máximas de cisalhamento", #TODO: Rever nomes
        ("Arial", 16, "bold"), "#ff9800", "white", lambda: exercise_3_ui(frame, window),
        button_width, 2, pady=button_spacing
    )

    create_button(
        frame, "Informações", 
        ("Arial", 16, "bold"), "#616161", "white", lambda: information_1_ui(frame, window),
        button_width, 2, pady=button_spacing
    )

    create_button(
        frame, "Menu Principal", 
        ("Arial", 16, "bold"), "#d32f2f", "white", lambda: create_main_screen(window, frame),
        button_width, 2, pady=button_spacing
    )