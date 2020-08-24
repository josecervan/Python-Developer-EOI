lista = [1, 2, 3, 4, 5]

try:
    print(lista[10])
except IndexError as exception:
    print(f'IndexError: {exception.args}')
