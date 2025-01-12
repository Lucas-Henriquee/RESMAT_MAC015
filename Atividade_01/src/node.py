from imports.all_imports import *

class Node:
    def __init__(self, name, x, y):
        self.name = name
        self.x = x
        self.y = y

    def update(self, x, y):

        self.x = x
        self.y = y

class NodeManager:

    def __init__(self):
        self.nodes = []
        self.counter = 0

    def generate_node_name(self):

        if self.counter < 26:
            return chr(65 + self.counter)  

    def add_node(self, x, y):

        for node in self.nodes:
            if node.x == x and node.y == y:
                raise ValueError(f"Nó com coordenadas ({x}, {y}) já existe.")
            
        name = self.generate_node_name()
        self.nodes.append(Node(name, x, y))
        self.counter += 1
        return name

    def update_node(self, name, x, y):

        for node in self.nodes:
            if node.name == name:
                node.update(x, y)
                return True
        return False

    def clear_nodes(self):
        self.nodes.clear()
        self.counter = 0

    def remove_nodes(self):

        for node in self.nodes:
                self.nodes.remove(node)

    def list_nodes(self):
        return [f"{node.name}: ({node.x}, {node.y})" for node in self.nodes]
    
    def get_node(self, name):
        name = name.split(":")[0].strip()
        for node in self.nodes:
            if node.name == name:
                return node
        return None

    def draw_nodes(self, ax):
        x_coords = []
        y_coords = []

        for node in self.nodes:
            x_coords.append(node.x)
            y_coords.append(node.y)
            ax.plot(node.x, node.y, 'o', markersize=10, markeredgecolor='black', markerfacecolor='blue', zorder=3)

        return x_coords, y_coords