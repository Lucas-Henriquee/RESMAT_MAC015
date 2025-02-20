from .all_imports import *
from .force import Force

class Node:
    def __init__(self, name, x, y, radius=None):
        self.name = name
        self.x = x
        self.y = y
        self.radius = radius
        self.x_deformed = x  
        self.y_deformed = y  
        self.forces = []

    def update(self, x, y):
        self.x = x
        self.y = y
        self.x_deformed = x  
        self.y_deformed = y

    def apply_displacement(self, dx, dy):
        self.x_deformed = self.x + dx
        self.y_deformed = self.y + dy

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

    def draw_node_label(self, ax):
        offset_x = 0.18
        offset_y = 0.18
        label_x = self.x + offset_x
        label_y = self.y + offset_y

        ax.text(
            label_x, label_y, self.name,
            fontsize=12, color='black', weight='bold',
            ha='center', va='center', zorder=7
        )

class NodeManager:
    def __init__(self):
        self.nodes = []
        self.counter = 0

    def generate_node_name(self):
        return chr(65 + self.counter)

    def add_node(self, x, y, radius=None):
        for node in self.nodes:
            if node.x == x and node.y == y:
                raise ValueError(f"Nó com coordenadas ({x}, {y}) já existe.")
        
        name = self.generate_node_name()
        self.nodes.append(Node(name, x, y, radius))
        self.counter += 1
        return name

    def get_node(self, name):
        for node in self.nodes:
            if node.name == name:
                return node
        return None

    def apply_displacements(self, displacements):
        for i, node in enumerate(self.nodes):
            dx = displacements[2 * i]
            dy = displacements[2 * i + 1]
            node.apply_displacement(dx, dy)

    def list_nodes(self):
        return [f"{node.name}: ({node.x}, {node.y})" for node in self.nodes]

    def draw_nodes(self, ax, deformed=False):
        x_coords = []
        y_coords = []

        for node in self.nodes:
            if deformed:
                x, y = node.x_deformed, node.y_deformed
                color = 'red'
            else:
                x, y = node.x, node.y
                color = 'blue'

            x_coords.append(x)
            y_coords.append(y)
            ax.plot(x, y, 'o', markersize=10, markeredgecolor='black', markerfacecolor=color, zorder=3)
            node.draw_forces(ax, scale_proportional=False, fixed_size=0.5)
            node.draw_node_label(ax)  

        return x_coords, y_coords

    def clear_nodes(self):
        self.nodes.clear()
        self.counter = 0

    def get_node_by_coordinates(self, x, y):
        for node in self.nodes:
            if node.x == x and node.y == y:
                return node
        return None