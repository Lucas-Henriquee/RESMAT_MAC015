import math
import matplotlib.pyplot as plt

def calcular_resultante(forces):

    result_x = sum(force.x for force in forces)
    result_y = sum(force.y for force in forces)
    result_intensity = math.sqrt(result_x**2 + result_y**2)

    if result_intensity == 0:
        result_angle = None 
    else:
        result_angle = math.degrees(math.atan2(result_y, result_x))

    return result_intensity, result_angle, result_x, result_y

def desenhar_resultante(forces, ax):

    result_intensity, result_angle, result_x, result_y = calcular_resultante(forces)

    ax.axhline(0, color='black', linewidth=0.5)
    ax.axvline(0, color='black', linewidth=0.5)
    ax.grid(color='gray', linestyle='--', linewidth=0.5)

    for i, force in enumerate(forces, start=1):
        ax.quiver(0, 0, force.x, force.y, angles='xy', scale_units='xy', scale=1, color='blue', label=f"Força {i}")

    ax.quiver(0, 0, result_x, result_y, angles='xy', scale_units='xy', scale=1, color='red', label='Resultante')
    ax.set_xlim(-abs(result_x) * 1.5, abs(result_x) * 1.5)
    ax.set_ylim(-abs(result_y) * 1.5, abs(result_y) * 1.5)
    ax.set_title("Plano Cartesiano")
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.legend()
