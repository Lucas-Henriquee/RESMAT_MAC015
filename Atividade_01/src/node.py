from imports.all_imports import *
from src.force import Force

class Node:
    def __init__(self, name, x, y):
        self.name = name
        self.x = x
        self.y = y
        self.forces = []

    def update(self, x, y):
        self.x = x
        self.y = y

    def add_force(self, force):
        if isinstance(force, Force):
            force.angle = 270
            force.x = 0
            force.y = -force.intensity  
            self.forces.append(force)
        else:
            raise ValueError("O objeto adicionado deve ser uma instância da classe Force.")

    def list_forces(self):
        return [str(force) for force in self.forces]

    def clear_forces(self):
        self.forces.clear()

    def calculate_resultant_force(self):
        total_x = sum(force.x for force in self.forces)
        total_y = sum(force.y for force in self.forces)
        intensity = (total_x**2 + total_y**2) ** 0.5
        angle = degrees(atan2(total_y, total_x))
        return intensity, angle
    
    def draw_forces(self, ax, scale_proportional=False, fixed_size=0.5):
        if not self.forces:
            return

        for i, force in enumerate(self.forces, start=1):
            intensity = (force.x**2 + force.y**2)**0.5
            if scale_proportional:
                scaled_x = force.x
                scaled_y = force.y
            else:
                factor = fixed_size / intensity if intensity != 0 else 0
                scaled_x = force.x * factor
                scaled_y = force.y * factor

            ax.quiver(
                self.x, self.y, scaled_x, scaled_y,
                angles='xy', scale_units='xy', scale=1,
                color='orange',
                label=f"Força {i}" if i == 1 else "",
                zorder=5, width=0.005, headwidth=4
            )
            margin = 0.2  
            text_x = self.x + scaled_x
            text_y = self.y + scaled_y - margin  

            ax.text(
                text_x, text_y, f"{intensity:.2f} N",
                color='orange', fontsize=9, ha='center', va='center', zorder=6
            )


class NodeManager:
    def __init__(self):
        self.nodes = []
        self.counter = 0

    def generate_node_name(self):
        return chr(65 + self.counter)

    def add_node(self, x, y):
        for node in self.nodes:
            if node.x == x and node.y == y:
                raise ValueError(f"Nó com coordenadas ({x}, {y}) já existe.")
        
        name = self.generate_node_name()
        self.nodes.append(Node(name, x, y))
        self.counter += 1
        return name

    def get_node(self, name):
        for node in self.nodes:
            if node.name == name:
                return node
        return None

    def list_nodes(self):
        return [f"{node.name}: ({node.x}, {node.y})" for node in self.nodes]

    def draw_nodes(self, ax):
        x_coords = []
        y_coords = []

        for node in self.nodes:
            x_coords.append(node.x)
            y_coords.append(node.y)
            ax.plot(node.x, node.y, 'o', markersize=10, markeredgecolor='black', markerfacecolor='blue', zorder=3)
            
            node.draw_forces(ax, scale_proportional=False, fixed_size=0.5)


        return x_coords, y_coords

    def clear_nodes(self):
        self.nodes.clear()
        self.counter = 0