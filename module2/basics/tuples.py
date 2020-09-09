mytuple = (99.9, "una tupla en", "Python", 345, 56)

print('¿Qué tipo de dato es mytuple?')
print(type(mytuple))

print('¿Cómo puedes determinar que tipo de dato es cada elemento de la lista?')
for i in range(len(mytuple)):
    print(type(mytuple[i]))

print('Hay dos elementos que son de tipo cadena de texto. Escribe el código Python que determina si la palabra "tupla" está incluida en alguno de los dos.')

for i in range(len(mytuple)):
    if mytuple is str and 'tupla' in mytuple[i]:
        print('tupla está en el elemento', i)


print('Escribe el código Python que determina si el número 345 está incluido en mytuple')

print(345 in mytuple)
