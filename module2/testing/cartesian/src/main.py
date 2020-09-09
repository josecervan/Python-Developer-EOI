import sys
sys.path.append(".")

import Punto
import Rectangulo

a = Punto.Punto(2, 3)
b = Punto.Punto(5, 5)
c = Punto.Punto(-3, -1)
d = Punto.Punto(0, 0)

print(a.cuadrante())
print(c.cuadrante())
print(d.cuadrante())

a.vector(b)
b.vector(a)

a.distancia(b)
b.distancia(a)

a.distancia(d)
b.distancia(d)
c.distancia(d)

rectAB = Rectangulo.Rectangulo(a, b)

rectAB.base()
rectAB.altura()
rectAB.area()
