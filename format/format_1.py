#### Ejercicio 1: Formatea los siguientes valores para mostrar el resultado indicado:

# * "Hola Mundo" → Alineado a la derecha en 20 caracteres
s = 'Hola, Mundo'
print('{0:>20}'.format(s))

# * "Hola Mundo" → Truncamiento en el cuarto carácter (índice 3)
print('{0}'.format(s[:4]))

# * "Hola Mundo" → Alineamiento al centro en 20 caracteres con truncamiento en el segundo carácter (índice 1)
print('{0:^20}'.format(s[:2]))

# * 150 → Formateo a 5 números enteros rellenados con ceros
print(format(150, '05d'))

# * 7887 → Formateo a 7 números enteros rellenados con espacios
print(format(7887, '7d'))

# * 20.02 → Formateo a 3 números enteros y 3 números decimales
print('{0:07.3f}'.format(20.02))
