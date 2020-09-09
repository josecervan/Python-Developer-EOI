class Punto:

    def __init__(self, x=0, y=0):
        self.X = x  # Por qué la 1ª en mayus??
        self.Y = y

    def __str__(self):
        return f"({self.X},{self.Y})"

    def cuadrante(self):
        if self.X == 0 and self.Y == 0:
            return "Origen de coordenadas."
        elif self.X < 0 and self.Y < 0:
            return "Tercer cuadrante."
        elif self.X < 0 and self.Y > 0:
            return "Segundo cuadrante."
        elif self.X > 0 and self.Y < 0:
            return "Cuarto cuadrante."
        elif self.X > 0 and self.Y > 0:
            return "Primer cuadrante."
        else:
            return "Eje de coordenadas."

    def vector(self, p2):
        x1 = p2.X - self.X
        y1 = p2.Y - self.Y
        print(f"El vector resultante es ({x1},{y1})")
        return (x1, y1)

    def distancia(self, p2):
        d = ((p2.X - self.X) ** 2 + (p2.Y - self.Y) ** 2) ** 0.5
        print(f"La distancia entre los puntos es {d}")
        return d

