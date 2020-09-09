import unittest
import sys
sys.path.append("src")
import Punto
import Rectangulo
from math import sqrt


A = Punto.Punto(2, 3)
B = Punto.Punto(-5, 5)
C = Punto.Punto(-3, -1)
D = Punto.Punto(1, -1)
E = Punto.Punto(0, 0)


class TestPunto(unittest.TestCase):
    def test_cuadrante(self):
        self.assertEqual(E.cuadrante(), "Origen de coordenadas.")
        self.assertEqual(A.cuadrante(), "Primer cuadrante.")
        self.assertEqual(B.cuadrante(), "Segundo cuadrante.")
        self.assertEqual(C.cuadrante(), "Tercer cuadrante.")
        self.assertEqual(D.cuadrante(), "Cuarto cuadrante.")

    def test_distancia(self):
        self.assertAlmostEqual(A.distancia(B), sqrt(53))

    def test_mas_lejos(self):
        mas_alejado = max([A, B, C, D], key=lambda p: p.distancia(E))
        self.assertIs(mas_alejado, B)
        self.assertEqual(mas_alejado.distancia(D), B.distancia(D))


class TestRectangulo(unittest.TestCase):

    def test_base(self):
        self.assertIsNone(Rectangulo.Rectangulo(E, E).base())
        self.assertEqual(Rectangulo.Rectangulo(A, B).base(), 7)

    def test_altura(self):
        self.assertIsNone(Rectangulo.Rectangulo(E, E).altura())
        self.assertEqual(Rectangulo.Rectangulo(A, B).altura(), 2)

    def test_area(self):
        self.assertIsNone(Rectangulo.Rectangulo(E, E).area())
        self.assertEqual(Rectangulo.Rectangulo(A, B).area(), 14)


if __name__ == '__main__':
    unittest.main()
