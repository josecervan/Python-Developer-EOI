import random


def insertion_sort(source_lst):

    lst = source_lst.copy()

    for i in range(1, len(lst)):

        token = lst[i]
        j = i - 1

        while j >= 0 and token < lst[j]:
            lst[j + 1] = lst[j]
            j -= 1
            print(lst)

        lst[j + 1] = token
    return lst


if __name__ == '__main__':

    # A = list(range(1, 6 + 1))
    # A = list(range(6, 0, -1))
    A = random.sample(range(1, 6 + 1), 6)
    print(A)
    print('--')
    ordenada = insertion_sort(A)
    print('--')
    print(ordenada)

    # n_numeros = random.sample(range(10), 1)
    # print('n_numeros', n_numeros)
    # A = random.sample(range(100), n_numeros[0])
    #
    # for i in range(1, 100 + 1):
    #     if sorted(A) == insertion_sort(A):
    #         print(str(i) + ') Ordenación correcta')
    #     else:
    #         print('sorted(lst):\n', sorted(lst))
    #         print('insertion_sort(lst):\n', insertion_sort(A))
    #         print(str(i) + ') ¡Ordenación incorrecta!')
    #         raise Exception
    #
    # print('--')
    # print('Yiiiiiiiiiiiha!')