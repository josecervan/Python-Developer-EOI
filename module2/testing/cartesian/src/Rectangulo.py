import sys
sys.path.append(".")
import Punto

class Rectangulo:
    def __init__(self, p1=Punto.Punto(0, 0), p2=Punto.Punto(0, 0)):
        self.P1 = p1
        self.P2 = p2

    def base(self):
        if self.P1.X == self.P2.X:
            print("No se puede formar un rectangulo.")
            return
        P3 = Punto.Punto(self.P2.X, self.P1.Y)
        base = self.P1.distancia(P3)
        print(f"La base mide {base}")
        return base

    def altura(self):
        if self.P1.X == self.P2.X:
            print("No se puede formar un rectangulo.")
            return
        P3 = Punto.Punto(self.P2.X, self.P1.Y)
        altura = self.P2.distancia(P3)
        print(f"La altura mide {altura}")
        return altura

    def area(self):
        if self.P1.X == self.P2.X or self.P1.Y == self.P2.Y:
            print("No se puede formar un rectangulo.")
            return
        area = self.base() * self.altura()
        print(f"El área mide {area}.")
        return area

