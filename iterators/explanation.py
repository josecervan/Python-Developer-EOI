def is_iterable(object):
    # Función que comprueba si 'object' iterable
    try:
        next(object)
        return True
    except StopIteration:
        return False

# Se crea una lista de diez elementos: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
lst = list(range(10))

# 1.- Se imprime la lista anterior recorriendo el iterable 'lst' a partir de la llamada a 'iter()' de la sentencia 'for'
print('Bucle 1')
for num in lst:
    print(num, end=' ')

# Se crea un iterador a partir de la lista anteriormente creada
it = iter(lst)
print('')

# 2.- Se imprime la lista anterior a partir del iterador creado, no a partir de la lista creada
# print('Bucle 2')
# for num in it:
#     print(num, end=' ')

# 3.- Se imprime la lista cada dos elementos (la sentencia 'for' invoca a 'iter()' en cada iteración)
# print('\nBucle 3')
# for num in it:
#     print(num, end=' ')     # Se imprime el valor de índice correspondiente
#     next(it)                # Se avanza una posición

# 4.- Se imprime la lista cada tres elementos (la sentencia 'for' invoca a 'iter()' en cada iteración) y sale del rango
#     iterable, por lo que salta una excepción
print('\nBucle 4')
for num in it:
    print(num, end=' ')     # Se imprime el valor de índice correspondiente
    next(it)                # Se avanza una posición
    next(it)  # Se avanza una posición

