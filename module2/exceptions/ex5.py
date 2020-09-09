def agregar_una_vez(lista, elemento):
    try:
        if elemento in lista:
            raise ValueError
    except ValueError:
        print(f'Error: Imposible añadir elementos duplicados => [{elemento}]')
    else:
        lista.append(elemento)


if __name__ == '__main__':
    elementos = [1, 5, -2]
    print(elementos)

    agregar_una_vez(elementos, 10)
    print(elementos)

    agregar_una_vez(elementos, -2)
    print(elementos)

    agregar_una_vez(elementos, 'Hola')
    print(elementos)
