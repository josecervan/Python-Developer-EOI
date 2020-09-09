import sys

args = sys.argv

if len(args) != 3:
    print('Debe tomar 2 argumentos (números enteros del 0 al 9)')
    raise Exception

filas = int(args[1])
columnas = int(args[2])

if (filas not in range(9)) or (columnas not in range(9)):
    print('Los argumentos no están en el rango 0 - 9')
    raise Exception

for f in range(filas):
    for c in range(columnas):
        print(" * ", end='')
    print('\n')

