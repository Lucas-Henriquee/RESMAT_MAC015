from .all_imports import *

class Bar:
    def __init__(self, name, start_node, end_node):
        self.name = name
        self.start_node = start_node
        self.end_node = end_node

    def update(self, start_node, end_node):
        self.start_node = start_node
        self.end_node = end_node

class BarManager:
    def __init__(self, node_manager):
        self.bars = []
        self.counter = 0
        self.node_manager = node_manager
        self.E = None
        self.A = None

    def generate_bar_name(self):
        return f"B{self.counter + 1}"
    
    def clear_bars(self):
        self.bars.clear()
        self.counter = 0
        self.E = None
        self.A = None

    def add_bar(self, start_node, end_node):
        if not self.node_manager.get_node(start_node):
            return
        if not self.node_manager.get_node(end_node):
            return

        self.validate_bar(start_node, end_node)  
        name = self.generate_bar_name()
        self.bars.append(Bar(name, start_node, end_node))
        self.counter += 1

    def update_bar(self, name, start_node, end_node):
        for bar in self.bars:
            if bar.name == name:
                bar.update(start_node, end_node)
                return True
        return False

    def remove_bar(self, name):
        for bar in self.bars:
            if bar.name == name:
                self.bars.remove(bar)
                return True
        return False
    
    def validate_bar(self, start_node, end_node):

        if start_node == end_node:
            raise ValueError("O nó inicial e o nó final não podem ser iguais.")

        for bar in self.bars:
            if ((bar.start_node == start_node and bar.end_node == end_node) or
                (bar.start_node == end_node and bar.end_node == start_node)):
                raise ValueError("Já existe uma barra entre esses nós.")

        start_node_obj = self.node_manager.get_node(start_node)
        end_node_obj = self.node_manager.get_node(end_node)

        if not start_node_obj or not end_node_obj:
            raise ValueError("Os nós especificados não existem.")

        for bar in self.bars:
            bar_start_coords = self.node_manager.get_node(bar.start_node)
            bar_end_coords = self.node_manager.get_node(bar.end_node)

            if (bar.start_node == start_node or bar.end_node == start_node or bar.start_node == end_node or bar.end_node == end_node):
                continue

            if self.check_crossing(
                (start_node_obj.x, start_node_obj.y),
                (end_node_obj.x, end_node_obj.y),
                (bar_start_coords.x, bar_start_coords.y),
                (bar_end_coords.x, bar_end_coords.y)
            ):
                raise ValueError("Essa barra cruza com outra já existente.")

        return True

    def list_bars(self):
        return [f"{bar.name}: {bar.start_node} -> {bar.end_node}" for bar in self.bars]
    
    def get_bar_count(self):
        return len(self.bars)

    def check_crossing(self, line1_start, line1_end, line2_start, line2_end):
        def ccw(A, B, C):
            return (C[1] - A[1]) * (B[0] - A[0]) > (B[1] - A[1]) * (C[0] - A[0])

        return (
            ccw(line1_start, line2_start, line2_end) != ccw(line1_end, line2_start, line2_end) and
            ccw(line1_start, line1_end, line2_start) != ccw(line1_start, line1_end, line2_end)
        )

    def set_elasticity_modulus(self, E):
        if E <= 0:
            raise ValueError("O módulo de elasticidade deve ser maior que zero.")
        
        self.E = E

    def set_cross_sectional_area(self, A):
        if A <= 0:
            raise ValueError("A área da seção transversal deve ser maior que zero.")
        
        self.A = A

    def draw_bars(self, ax):
        x_coords = []
        y_coords = []

        for bar in self.bars:
            start_node = self.node_manager.get_node(bar.start_node)
            end_node = self.node_manager.get_node(bar.end_node)

            if start_node and end_node:
                x_coords.extend([start_node.x, end_node.x])
                y_coords.extend([start_node.y, end_node.y])

                ax.plot(
                [start_node.x, end_node.x],
                [start_node.y, end_node.y],
                color='white', linewidth=6, zorder=1
                )

                ax.plot(
                [start_node.x, end_node.x],
                [start_node.y, end_node.y],
                color='black', zorder=2
                )


        return x_coords, y_coords