class Support:
    def __init__(self, node, support_type):
        self.node = node
        self.support_type = support_type

    def update(self, node, support_type):
        self.node = node
        self.support_type = support_type

class SupportManager:
    def __init__(self):
        self.supports = []

    def add_support(self, node, support_type):
        self.supports.append(Support(node, support_type))

    def update_support(self, node, support_type):
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

    def list_supports(self):
        return [f"Nó {support.node}: Tipo {support.support_type}" for support in self.supports]