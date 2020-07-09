import numpy as np
import matplotlib.pyplot as plt
from drawnow import drawnow


def estimate_x_0(N):

    D = 0       # Número de dígitos a la izquierda del punto decimal de N
    aux = N     # Variable auxiliar

    while aux >= 1:
        aux = aux / 10
        D += 1

    if D % 2 == 0:
        return D,  int((D - 2) / 2), 6 * 10 ** ((D - 2) / 2)
    else:
        return D, int((D - 1) / 2), 2 * 10 ** ((D - 1) / 2)


def bab_sqrt(N, x_0, epsilon):

    i = 0
    x_n = x_0

    print('Proceso iterativo')
    print('\tx' + str(i) + ' = ' + str(x_n))

    aux = x_n
    x_n1 = (x_n + N / x_n) / 2  # x_{n+1}
    ordinate.append(x_0)
    x_n = x_n1
    i += 1
    abscissa.append(i)

    plt.ion()                   # Enable interactivity
    plt.figure()          # Make a figure
    plt.pause(5)

    drawnow(make_fig)
    plt.pause(0.001)

    while(abs(x_n1 - aux) >= epsilon):

        aux = x_n
        x_n1 = (x_n + N / x_n) / 2  # x_{n+1}
        ordinate.append(x_n1)
        x_n = x_n1
        print('\tx' + str(i) + ' = ' + str(x_n))

        i += 1
        abscissa.append(i)
        drawnow(make_fig)
        plt.pause(0.001)

    print('Iteraciones: i =', i)

    return x_n1


def make_fig():
    clmap = ['b'] * (len(abscissa) - 1)
    clmap.append('r')

    plt.title('$Babylonian$ $method$ $ (N = %i)$' %N)
    plt.scatter(abscissa, ordinate, c=clmap)
    plt.plot(abscissa, ordinate, 'k-.', alpha=0.3)
    plt.grid()

    plt.xlabel('$Iteration$')
    plt.ylabel('$x_{n + 1}$')

    plt.xticks(abscissa, range(len(abscissa) + 1))

    for index in range(len(abscissa)):
        plt.annotate(str(round(ordinate[index], 5)), (abscissa[index], ordinate[index]))


if __name__ == '__main__':
    abscissa = list()
    ordinate = list()

    print('--------------------------------------')
    print('Algoritmo babilónico (método de Herón)')
    print('--------------------------------------')
    print('Descripción: calcula la raíz cuadrada de un número real N >= 1')

    N = float(input('--> Introduzca un número real: N = '))

    epsilon = 1e-6

    D, z, x_0 = estimate_x_0(N)

    print('N =', N)
    print('Número de dígitos: D =', D)
    print('Exponente: z =', z)
    print('Valor inicial: x_0 =', x_0)
    print('Error de precisión: epsilon =', epsilon)
    print('')

    square_root = bab_sqrt(N, x_0, epsilon)

    print('')
    print('np.sqrt(' + str(N) + ') = ' + str(np.sqrt(N)))
    print('sqrt(' + str(N) + ') = ' + str(square_root))
    print('')
    print('Error cometido: e =', abs(np.sqrt(N) - square_root))
    print('Cierre el gráfico para finalizar el programa')

    plt.show(block=True)

    print('')
    print('Programa finalizado')

