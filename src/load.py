from .all_imports import *

class Load:
    def __init__(self, load_type, load_function=None, interval=None, value = None, position = None):
        self.load_type = load_type
        self.load_function = load_function
        self.interval = interval
        self.value = value
        self.position = position
        self.calculate_value_and_position()

    @property
    def get_load_type(self):
        return self.load_type
    
    @property
    def get_load_function(self):
        return self.load_function
    
    @property
    def get_interval(self):
        return self.interval
    
    @property
    def get_value(self):
        return self.value
    
    @property
    def get_position(self):
        return self.position
    
    def calculate_value_and_position(self):
        x = sp.Symbol('x')
        if self.load_type == 'function':
            forca = sp.integrate(self.load_function, x)
            informacao = sp.integrate(self.load_function * x, x)
            x_barra = informacao / forca
            self.value = forca
            self.position = x_barra
