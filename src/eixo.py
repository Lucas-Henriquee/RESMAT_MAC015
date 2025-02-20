import numpy as np

class Eixo:
    def __init__(self, lenght, extern_radius, intern_radius, G, Torcao):
        lenght = float(lenght)
        extern_radius = float(extern_radius)
        intern_radius = float(intern_radius)
        G = float(G)
        Torcao = float(Torcao)
        self.lenght = lenght
        self.extern_radius = extern_radius
        self.intern_radius = intern_radius
        self.G = G
        self.Torcao = Torcao
        self.t_max = Torcao * extern_radius / (np.pi * (extern_radius**4 - intern_radius**4) / 2)
        self.angle = Torcao * lenght / (G * (np.pi * (extern_radius**4 - intern_radius**4) / 2))