def iguales(num1, num2):
    return num1 == num2


def sumar(num1, num2):
    return num1 + num2


def restar(num1, num2):
    return num1 - num2


def multiplicar(num1, num2):
    return num1 * num2


def dividir(num1, num2):
    try:
        return num1 / num2
    except ZeroDivisionError:
        return -1


def potencia(num1, num2):
    return num1 ** num2


def factorial(num):
    try:
        if num < 0 or not(isinstance(num, int)):
            raise ValueError
        if num == 0:
            return 1

        fact = 1
        for i in range(2, num + 1):
            fact *= i

        return fact

    except ValueError:
        return -1
