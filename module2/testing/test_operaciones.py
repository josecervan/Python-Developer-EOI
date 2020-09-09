import operations
import unittest


class Test(unittest.TestCase):

    def test_sonIguales(self):
        self.assertEqual(operations.iguales(3, 3), True)
        self.assertEqual(operations.iguales(3, 4), False)

    def test_sumar(self):
        self.assertEqual(operations.sumar(5, 3), 8)

    def test_restar(self):
        self.assertEqual(operations.restar(5, 3), 2)

    def test_multiplicar(self):
        self.assertEqual(operations.multiplicar(4, 5), 20)

    def test_dividir(self):
        self.assertEqual(operations.dividir(5, 0), -1)
        self.assertEqual(operations.dividir(4, 2), 2)

    def test_potencia(self):
        self.assertEqual(operations.potencia(2, 5), 32)
        self.assertEqual(operations.potencia(5, 2), 25)

    def test_factorial(self):
        self.assertEqual(operations.factorial(-5), -1)
        self.assertEqual(operations.factorial(3.4), -1)
        self.assertEqual(operations.factorial(0), 1)
        self.assertEqual(operations.factorial(0), 1)
        self.assertEqual(operations.factorial(5), 120)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
