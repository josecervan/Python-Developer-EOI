"""
Source: https://en.wikipedia.org/wiki/Minkowski_inequality
"""
import random


def minkowski_inequality(a, b, c):
    return a + b > c and b + c > a and a + c > b


def minkowski_ineq_instead(a, b, c):
    if minkowski_inequality(a, b, c):
        return True, [a, b, c]
    else:
        new_c = 0
        while not(minkowski_inequality(a, b, new_c)):
            new_c += round(random.random(), ndigits=1)

        return False, [a, b, new_c]


if __name__ == '__main__':

    # Primera versión
    lado1, lado2, lado3 = 5, 8, 3

    if minkowski_inequality(lado1, lado2, lado3):
        print(f'La terna ({lado1}, {lado2}, {lado3}) SÍ forma un triángulo')
    else:
        print(f'La terna ({lado1}, {lado2}, {lado3}) NO forma un triángulo')

    lado1, lado2, lado3 = 7, 10, 5

    if minkowski_inequality(lado1, lado2, lado3):
        print(f'La terna ({lado1}, {lado2}, {lado3}) SÍ forma un triángulo')
    else:
        print(f'La terna ({lado1}, {lado2}, {lado3}) NO forma un triángulo')

    # Segunda versión
    lado1, lado2, lado3 = 5, 8, 3

    ineq, lados = minkowski_ineq_instead(lado1, lado2, lado3)
    if ineq:
        print(f'La terna ({lado1}, {lado2}, {lado3}) SÍ forma un triángulo')
    else:
        print(f'La terna ({lado1}, {lado2}, {lado3}) NO forma un triángulo')
        print(f'Terna alternativa: ({lados[0]}, {lados[1]}, {round(lados[2], ndigits=1)})')
