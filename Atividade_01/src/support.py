from imports.all_imports import *

class Support:
    def __init__(self, node, support_type):
        self.node = node
        self.support_type = support_type

    def update(self, node, support_type):
        self.node = node
        self.support_type = support_type

    def __str__(self):
        return f"Nó {self.node}: Tipo {self.support_type}"

class SupportManager:
    def __init__(self):
        self.supports = []

    def add_support(self, node, support_type):
        if any(support.node == node for support in self.supports):
            raise ValueError(f"Já existe um apoio no nó {node}!")
        
        if not self.validate_support_type(support_type):
            raise ValueError("Tipo de suporte inválido!")

        if not self.check_support_restrictions(support_type):
            raise ValueError("As restrições de configuração de apoios foram violadas!")

        self.supports.append(Support(node, support_type))

    def clear_supports(self):
        self.supports.clear()

    def update_support(self, node, support_type):
        if not self.validate_support_type(support_type):
            raise ValueError("Tipo de suporte inválido!")
        for support in self.supports:
            if support.node == node:
                support.update(node, support_type)
                return True
        return False

    def remove_support(self, node):
        for support in self.supports:
            if support.node == node:
                self.supports.remove(support)
                return True
        return False
    
    def check_support_restrictions(self, support_type):
   
        support_counts = {1: 0, 2: 0}  
        for support in self.supports:
            support_counts[support.support_type] += 1

        if support_type == 1: 
            if support_counts[1] >= 3: 
                return False
            if support_counts[1] == 1 and support_counts[2] == 1: 
                return False

        elif support_type == 2:  
            if support_counts[2] >= 1: 
                return False
            if support_counts[1] != 1:  
                return False

        return True

    def validate_support_type(self, support_type):
        return support_type in [1, 2] 

    def list_supports(self):
        return [str(support) for support in self.supports]

    def draw_supports(self, ax, node_manager):
        for support in self.supports:
            node = node_manager.get_node(support.node)

            if abs(node.x) < 1:
                label_offset_x = -0.5 if node.x >= 0 else 0.5
            if abs(node.y) < 1:
                label_offset_y = -0.5

            if support.support_type == 1: 
                fixed_patch = Polygon(
                    [[node.x - 0.15, node.y - 0.2], [node.x + 0.15, node.y - 0.2], [node.x, node.y]], 
                    closed=True, color='red', zorder=3
                )
                ax.add_patch(fixed_patch)
        
            elif support.support_type == 2: 
                roller_patch = Polygon(
                    [[node.x - 0.15, node.y - 0.2], [node.x + 0.15, node.y - 0.2], [node.x, node.y]], 
                    closed=True, color='green', zorder=3
                )
                ax.add_patch(roller_patch)

                wheel_radius = 0.04
                wheel_positions = [node.x - 0.1, node.x, node.x + 0.1]
                for wx in wheel_positions:
                    ax.add_patch(Circle((wx, node.y - 0.25), wheel_radius, color='green', zorder=4))