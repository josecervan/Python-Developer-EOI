class Shape:
    def __init__(self, line_color, line_thickness, fill, lado):
        self.line_color = line_color
        self.line_thickness = line_thickness
        self.fill = fill
        self.lado = lado
        
    def calcular_area(self):
        return self.lado ** 2