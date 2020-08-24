# Lee una línea de elementos y la separa por cada espacio
lst = input('Números: ').split(' ')

# Se ejecuta si no es una línea en blanco
while any('' != item for item in lst):

    # Variable que guarda el resultado final, inicializada a cero en cada iteración
    result = 0

    # Se comprueban los elementos de la línea uno a uno
    for item in lst:
        try:
            # Casting a float
            num = float(item)
        except ValueError:
            print(f'Entrada no válida: {item}')
        else:
            # Casting a int si, siendo float, también es int
            if num.is_integer():
                num = int(num)

            # Se actualiza la suma y se imprime el resultado
            result += num
            print(f'Result: {result}')

    # Lee una línea de elementos y la separa por cada espacio
    lst = input('Números: ').split(' ')
