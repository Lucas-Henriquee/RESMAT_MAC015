from .all_imports import *

class Force:
    def __init__(self, intensity=None, force_type="graus", angle_or_coordinates=None):
        self.type = force_type
        self.intensity = intensity
        self.angle = None
        self.x = None
        self.y = None
        self.original_x = None  
        self.original_y = None  
        self.update_force(intensity, angle_or_coordinates)

    def update_force(self, intensity=None, angle_or_coordinates=None, force_type=None):
        if force_type:
            self.type = force_type

        if self.type == "graus":
            if angle_or_coordinates is None:
                raise ValueError("O ângulo deve ser fornecido para forças do tipo 'graus'.")

            self.angle = angle_or_coordinates
            self.intensity = intensity if intensity is not None else 0
            self.x = cos(radians(self.angle)) * self.intensity
            self.y = sin(radians(self.angle)) * self.intensity

        elif self.type == "coordenadas":
            if angle_or_coordinates is None:
                raise ValueError("As coordenadas X e Y devem ser fornecidas para forças do tipo 'coordenadas'.")

            x, y = angle_or_coordinates
            magnitude = sqrt(x**2 + y**2)

            if intensity is not None:
                if magnitude != 0:
                    scale = intensity / magnitude
                    self.x = x * scale
                    self.y = y * scale
                else:
                    self.x = 0
                    self.y = 0
                self.intensity = intensity
            else:
                self.x = x
                self.y = y
                self.intensity = magnitude

            self.original_x = x
            self.original_y = y
            self.angle = degrees(atan2(self.original_y, self.original_x))

        else:
            raise ValueError("Tipo de força inválido. Use 'graus' ou 'coordenadas'.")

    def __str__(self):
        if self.type == "graus":
            return f"Intensidade: {self.intensity:.2f} N, Ângulo: {self.angle:.2f}°"
        elif self.type == "coordenadas":
            return f"Intensidade: {self.intensity:.2f} N, Coordenadas: ({self.original_x:.2f}, {self.original_y:.2f}), Ângulo: {self.angle:.2f}°"

    def to_dict(self):
        return {
            "type": self.type,
            "intensity": self.intensity,
            "angle": self.angle,
            "x": self.original_x,
            "y": self.original_y,
            "original_x": self.original_x,
            "original_y": self.original_y,
        }
    
def calculate_resultant(forces):

    result_x = sum(force.x for force in forces)
    result_y = sum(force.y for force in forces)

    result_intensity = sqrt(result_x**2 + result_y**2)
    if result_intensity == 0:
        result_angle = None
    else:
        result_angle = degrees(atan2(result_y, result_x))

    return result_intensity, result_angle, result_x, result_y

def draw_resultant(forces, ax):
    result_intensity, result_angle, result_x, result_y = calculate_resultant(forces)

    ax.axhline(0, color='black', linewidth=0.5)
    ax.axvline(0, color='black', linewidth=0.5)
    ax.grid(color='gray', linestyle='--', linewidth=0.5)

    for i, force in enumerate(forces, start=1):
        ax.quiver(0, 0, force.x, force.y, angles='xy', scale_units='xy', scale=1, color='blue', label=f"Força {i}")

    ax.quiver(0, 0, result_x, result_y, angles='xy', scale_units='xy', scale=1, color='red', label='Resultante')

    padding = max(abs(result_x), abs(result_y)) * 0.5
    ax.set_xlim(-abs(result_x) - padding, abs(result_x) + padding)
    ax.set_ylim(-abs(result_y) - padding, abs(result_y) + padding)

    ax.set_title("Plano Cartesiano")
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.legend()
