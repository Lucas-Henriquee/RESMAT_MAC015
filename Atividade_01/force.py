import math

class Force:
    def __init__(self, intensity=None, force_type="graus", angle_or_coordinates=None):
        self.intensity = intensity
        self.type = force_type
        if force_type == "graus":
            self.angle = angle_or_coordinates
            self.x = math.cos(math.radians(self.angle)) * (self.intensity if self.intensity else 0)
            self.y = math.sin(math.radians(self.angle)) * (self.intensity if self.intensity else 0)
        elif force_type == "coordenadas":
            self.x, self.y = angle_or_coordinates
            self.intensity = intensity if intensity else math.sqrt(self.x**2 + self.y**2)

    def update_force(self, intensity=None, angle_or_coordinates=None):
        self.intensity = intensity
        if self.type == "graus":
            self.angle = angle_or_coordinates
            self.x = math.cos(math.radians(self.angle)) * (self.intensity if self.intensity else 0)
            self.y = math.sin(math.radians(self.angle)) * (self.intensity if self.intensity else 0)
        elif self.type == "coordenadas":
            self.x, self.y = angle_or_coordinates
            self.intensity = intensity if intensity else math.sqrt(self.x**2 + self.y**2)

    def __str__(self):
        if self.type == "graus":
            return f"Intensidade: {self.intensity:.2f} N, Ângulo: {self.angle:.2f}°"
        elif self.type == "coordenadas":
            return f"Intensidade: {self.intensity:.2f} N, Coordenadas: ({self.x:.2f}, {self.y:.2f})"
